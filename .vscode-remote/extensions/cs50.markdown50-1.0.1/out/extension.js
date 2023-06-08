"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = void 0;
const vscode = require("vscode");
const path = require("path");
const engine_1 = require("./engine");
const html_entities_1 = require("html-entities");
const node_html_parser_1 = require("node-html-parser");
const MarkdownIt = require("markdown-it");
const markdownItAttrs = require("markdown-it-attrs");
const LAB_WEBVIEW_SCRIPT = 'markdown50.js'; // Script
const LAB_WEBVIEW_STYLESHEET = 'markdown50.css'; // Styleshet
const STATIC_FOLDER = 'static'; // Statics
let currentSource;
let currentMarkdownEditor;
let vscodeContext;
let watchEvents = [];
let webViewGlobal;
async function activate(context) {
    init(context);
}
exports.activate = activate;
async function init(context) {
    vscodeContext = context;
    context.subscriptions.push(vscode.commands.registerCommand('markdown50.showSource', showSource));
    context.subscriptions.push(vscode.commands.registerCommand('markdown50.openPreviewToTheSide', openPreview));
    await vscode.commands.executeCommand("setContext", "hasCustomMarkdownPreview", true);
}
function showSource() {
    vscode.window.visibleTextEditors.forEach((each) => {
        if (each.document.uri === currentSource) {
            vscode.window.showTextDocument(each.document, vscode.ViewColumn.One);
            return;
        }
    });
    vscode.window.showTextDocument(currentSource);
}
function openPreview() {
    if (webViewGlobal !== undefined) {
        webViewGlobal.dispose();
    }
    currentMarkdownEditor = vscode.window.activeTextEditor;
    const activeTextDocument = currentMarkdownEditor.document;
    currentSource = currentMarkdownEditor.document.uri;
    createWebviewPanel(activeTextDocument.fileName);
    renderWebview(activeTextDocument.fileName, activeTextDocument.getText());
    startWebviewUpdate();
    syncWebviewScroll(currentMarkdownEditor);
}
function createWebviewPanel(fileName) {
    const workspaceFolder = vscode.workspace.workspaceFolders[0];
    const showOptions = {
        "viewColumn": vscode.ViewColumn.Two
    };
    const viewOptions = {
        enableCommandUris: true,
        enableScripts: true,
        localResourceRoots: [vscodeContext.extension.extensionUri, workspaceFolder.uri]
    };
    webViewGlobal = vscode.window.createWebviewPanel("markdown50.preview", `Preview ${path.basename(fileName)}`, showOptions, viewOptions);
    webViewGlobal.iconPath = {
        light: vscode.Uri.file(path.join(vscodeContext.extensionPath, "static/images", "codicon_preview_inverse.svg")),
        dark: vscode.Uri.file(path.join(vscodeContext.extensionPath, "static/images", "codicon_preview.svg"))
    };
    webViewGlobal.webview.onDidReceiveMessage(message => {
        switch (message.command) {
            case "scrollSync":
                syncTextEditorScroll(message.percentage);
                break;
        }
    }, undefined, vscodeContext.subscriptions);
    webViewGlobal.onDidDispose(() => { stopWebviewUpdate(); });
}
function startWebviewUpdate() {
    watchEvents.push(vscode.workspace.onDidChangeTextDocument((document) => {
        if (document === undefined) {
            return;
        }
        if (document.document.languageId === "markdown") {
            const activeTextDocument = vscode.window.activeTextEditor.document;
            renderWebview(activeTextDocument.fileName, activeTextDocument.getText());
        }
    }));
    watchEvents.push(vscode.window.onDidChangeActiveTextEditor((textEditor) => {
        if (textEditor === undefined) {
            return;
        }
        if (textEditor.document.languageId === "markdown") {
            currentSource = textEditor.document.uri;
            currentMarkdownEditor = textEditor;
            const activeTextDocument = vscode.window.activeTextEditor.document;
            renderWebview(activeTextDocument.fileName, activeTextDocument.getText());
        }
    }));
    watchEvents.push(vscode.window.onDidChangeTextEditorVisibleRanges((event) => {
        if (event.textEditor.document === undefined) {
            return;
        }
        if (event.textEditor.document.languageId === "markdown") {
            syncWebviewScroll(event.textEditor);
        }
    }));
}
function syncWebviewScroll(activeTextEditor) {
    const lineCount = activeTextEditor.document.lineCount;
    const visibleRange = activeTextEditor.visibleRanges;
    const visibleStart = visibleRange[0].start.line;
    webViewGlobal.webview.postMessage({ command: 'scrollSync', percentage: visibleStart / lineCount, timestamp: Date.now() });
}
function syncTextEditorScroll(percentage) {
    const lineCount = currentMarkdownEditor.document.lineCount;
    const topLine = Math.floor(lineCount * percentage);
    const range = new vscode.Range(new vscode.Position(topLine, 0), new vscode.Position(topLine + 1, 0));
    currentMarkdownEditor.revealRange(range);
}
function stopWebviewUpdate() {
    watchEvents.forEach((each) => {
        each.dispose();
    });
    watchEvents = [];
    currentSource = undefined;
}
async function renderWebview(fileName, markdownString) {
    const markdownHtml = renderMarkdown(markdownString);
    const liquidHtml = await renderLiquid(markdownHtml);
    const parsedHtml = renderCustom(liquidHtml);
    try {
        webViewGlobal.webview.html = getWebviewHtml(fileName, parsedHtml);
    }
    catch (error) { }
}
function renderMarkdown(markdown) {
    // Instantiate and configure Markdown-It instance
    const md = new MarkdownIt({
        html: true
    });
    md.use(markdownItAttrs, {
        leftDelimiter: "{:",
        rightDelimiter: "}"
    });
    // Syntax highlight
    const hightlightOpts = { inline: false, auto: false };
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    md.use(require('markdown-it-highlightjs'), hightlightOpts);
    // Parse markdown file into HTML
    let markdownHtml = md.render(markdown);
    // Restore any Liquid.js tag
    markdownHtml = (0, node_html_parser_1.parse)(markdownHtml);
    markdownHtml.querySelectorAll('p').forEach((each) => {
        // Does the trick for now, need to replace it with regex
        if (each.innerHTML.includes(`{%`) && each.innerHTML.includes(`%}`)) {
            each.replaceWith((0, html_entities_1.decode)(each.innerHTML));
        }
    });
    return markdownHtml.toString();
}
async function renderLiquid(markdownHtml) {
    const engine = (0, engine_1.liquidEngine)();
    return await engine.parseAndRender(markdownHtml).then(async (liquidHtml) => {
        return liquidHtml;
    });
}
function renderCustom(liquidHtml) {
    // handle Kramdown {: start="3"}
    try {
        const root = (0, node_html_parser_1.parse)(liquidHtml);
        root.querySelectorAll('p').forEach((each) => {
            if (each.getAttribute('start') !== null) {
                const start = each.getAttribute('start');
                if (each.nextElementSibling === null) {
                    return;
                }
                if (each.nextElementSibling.tagName === 'OL') {
                    each.nextElementSibling.setAttribute('start', start);
                    each.remove();
                }
            }
        });
        liquidHtml = root.toString();
    }
    catch (error) {
        console.log(error);
    }
    return liquidHtml;
}
function getWebviewHtml(fileName, html) {
    const scriptUri = webViewGlobal.webview.asWebviewUri(vscode.Uri.joinPath(vscodeContext.extension.extensionUri, STATIC_FOLDER, LAB_WEBVIEW_SCRIPT));
    const styleUri = webViewGlobal.webview.asWebviewUri(vscode.Uri.joinPath(vscodeContext.extension.extensionUri, STATIC_FOLDER, LAB_WEBVIEW_STYLESHEET));
    const base = webViewGlobal.webview.asWebviewUri(vscode.Uri.file(fileName));
    const fontawesomeUri = webViewGlobal.webview.asWebviewUri(vscode.Uri.joinPath(vscodeContext.extension.extensionUri, `${STATIC_FOLDER}/vendor/fontawesome/css/all.min.css`));
    const mathjaxUri = webViewGlobal.webview.asWebviewUri(vscode.Uri.joinPath(vscodeContext.extension.extensionUri, `${STATIC_FOLDER}/vendor/mathjax/js/tex-chtml.js`));
    const highlightjsUri = webViewGlobal.webview.asWebviewUri(vscode.Uri.joinPath(vscodeContext.extension.extensionUri, `${STATIC_FOLDER}/vendor/highlightjs/js/11.6.0/highlight.min.js`));
    const highlightStyleUri = webViewGlobal.webview.asWebviewUri(vscode.Uri.joinPath(vscodeContext.extension.extensionUri, `${STATIC_FOLDER}/vendor/highlightjs/css/11.6.0/styles/github-dark.min.css`));
    const htmlString = `<!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <base href="${base}">
            <link href="${fontawesomeUri}" rel="stylesheet">
            <link href="${styleUri}" rel="stylesheet">
            <link href="${highlightStyleUri}" rel="stylesheet">
        </head>
        <body>
            ${html}
        </body>
        <script>
            MathJax = {
            chtml: {
                    displayAlign: "left"
                }
            };
        </script>
        <script crossorign="anonymous" src="${mathjaxUri}"></script>
        <script src="${highlightjsUri}"></script>
        <script src="${scriptUri}"></script>
    </html>`.trim();
    return htmlString;
}
//# sourceMappingURL=extension.js.map
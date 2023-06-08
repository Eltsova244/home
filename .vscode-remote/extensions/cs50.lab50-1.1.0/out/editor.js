"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.LabEditorProvider = void 0;
const vscode = require("vscode");
const fs = require("fs");
class LabMarkdown {
    constructor(uri) {
        this.uri = uri;
    }
    dispose() {
        return;
    }
}
class LabEditorProvider {
    constructor(labViewHandler) {
        this.labViewHandler = labViewHandler;
    }
    static register(labViewHandler) {
        const provider = new LabEditorProvider(labViewHandler);
        const providerRegistration = vscode.window.registerCustomEditorProvider(LabEditorProvider.viewType, provider);
        return providerRegistration;
    }
    openCustomDocument(uri, openContext, token) {
        if (!fs.existsSync(uri['fsPath'])) {
            fs.writeFileSync(uri['fsPath'], '');
        }
        return new LabMarkdown(uri);
    }
    resolveCustomEditor(document, webviewPanel, token) {
        const header = "CS50 Lab";
        const options = { detail: 'Open README.md in CS50 Lab?', modal: true };
        vscode.window.showInformationMessage(header, options, ...["Yes"]).then(async (item) => {
            if (item === 'Yes') {
                this.labViewHandler({ path: document['uri']['path'] });
            }
            else {
                try {
                    await vscode.commands.executeCommand('workbench.action.closeActiveEditor');
                    vscode.window.showTextDocument(document['uri']);
                }
                catch (error) {
                    console.error(error);
                }
            }
        });
    }
    saveCustomDocument(document, cancellation) {
        throw new Error('Method not implemented.');
    }
    saveCustomDocumentAs(document, destination, cancellation) {
        throw new Error('Method not implemented.');
    }
    revertCustomDocument(document, cancellation) {
        throw new Error('Method not implemented.');
    }
    backupCustomDocument(document, context, cancellation) {
        throw new Error('Method not implemented.');
    }
}
exports.LabEditorProvider = LabEditorProvider;
LabEditorProvider.viewType = 'lab50.editor';
//# sourceMappingURL=editor.js.map
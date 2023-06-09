"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.detectInsiderVersion = exports.checkForUpdates = void 0;
const vscode = require("vscode");
const child_process_1 = require("child_process");
// eslint-disable-next-line @typescript-eslint/no-var-requires
const axios = require('axios').default;
function checkForUpdates() {
    (0, child_process_1.exec)(`tail -1 /etc/issue`, (error, stdout, stderr) => {
        const currentVersion = stdout.trim();
        const url = 'https://api.github.com/repos/cs50/codespace/git/matching-refs/tags/latest';
        const headers = {
            'Authorization': `token ${process.env['GITHUB_TOKEN']}`,
            'Accept': 'application/vnd.github.v3+json'
        };
        axios.get(url, { headers: headers }).then((response) => {
            const latestVersion = response.data[0]['object']['sha'].trim();
            if (currentVersion != latestVersion) {
                promptUpdate();
            }
        }).catch((error) => {
            console.log(error);
        });
    });
}
exports.checkForUpdates = checkForUpdates;
function promptUpdate() {
    const message = `Updates Available`;
    vscode.window.showInformationMessage(message, ...['Update Now', 'Remind Me Later']).then((selection) => {
        if (selection === 'Update Now') {
            (0, child_process_1.exec)('/opt/cs50/bin/update50', (stdin, stdout, stderr) => {
                console.log(stderr);
            });
        }
    });
}
function detectInsiderVersion() {
    try {
        if (process.env['VSCODE_CWD'].includes('insider')) {
            const message = 'You seem to be running the Insiders version of VS Code, which might not be compatible with some of CS50\'s own features. Best to switch back to the Stable version of VS Code, as via "Switch to Stable Version..." under VS Code\'s gear icon.';
            vscode.window.showWarningMessage(message);
        }
    }
    catch (error) {
        console.log(error);
    }
}
exports.detectInsiderVersion = detectInsiderVersion;
//# sourceMappingURL=updates.js.map
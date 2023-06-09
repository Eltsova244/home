"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.registerCommand = void 0;
const child_process_1 = require("child_process");
const vscode = require("vscode");
const vnc_1 = require("./vnc");
function registerCommand(context) {
    // Command: Launch VNC
    let command = 'cs50.launchGUI';
    let commandHandler = () => {
        (0, vnc_1.startVNC)();
    };
    context.subscriptions.push(vscode.commands.registerCommand(command, commandHandler));
    // Command: Update Codespace
    command = 'cs50.updateCodespace';
    commandHandler = () => {
        (0, child_process_1.exec)(`/opt/cs50/bin/update50 --force`, {
            'env': process.env
        }, (error, stdout, stderr) => {
            console.log(error, stdout, stderr);
        });
    };
    context.subscriptions.push(vscode.commands.registerCommand(command, commandHandler));
    // Command: Sync Changes
    command = "cs50.syncChanges";
    commandHandler = () => {
        (0, child_process_1.exec)('cd /workspaces/$RepositoryName && git add . && git commit -m "commit changes" && git push --force', {
            'env': process.env
        }, (error, stdout, stderr) => {
            console.log(error, stdout, stderr);
            if (error !== null) {
                vscode.window.showErrorMessage(`${stdout}`);
            }
            else {
                vscode.window.showInformationMessage(`Successfully synced changes to backing repository. ${stdout}`);
            }
        });
    };
    context.subscriptions.push(vscode.commands.registerCommand(command, commandHandler));
    // Command: Cleanup Workspace Repository
    command = 'cs50.cleanupRepository';
    commandHandler = () => {
        vscode.commands.executeCommand('workbench.action.terminal.focus');
        vscode.window.activeTerminal.sendText('cd $CODESPACE_VSCODE_FOLDER && clean50');
    };
    context.subscriptions.push(vscode.commands.registerCommand(command, commandHandler));
    // Command: Reset Terminal
    command = 'cs50.resetTerminal';
    commandHandler = async () => {
        vscode.window.terminals.forEach((terminal) => {
            terminal.dispose();
        });
        vscode.window.createTerminal('bash', 'bash', ['--login']).show();
    };
    context.subscriptions.push(vscode.commands.registerCommand(command, commandHandler));
    // Command: Return to workspace home
    command = 'cs50.returnHome';
    commandHandler = async () => {
        if (process.env['CODESPACE_NAME'] !== undefined) {
            const homeDir = `/workspaces/${process.env['RepositoryName']}`;
            if (vscode.workspace.workspaceFolders[0]['uri']['path'] !== homeDir) {
                const uri = vscode.Uri.file(homeDir);
                await vscode.commands.executeCommand('vscode.openFolder', uri, false);
            }
            else {
                const message = 'Currently at workspace home directory.';
                vscode.window.showInformationMessage(message);
            }
        }
    };
    context.subscriptions.push(vscode.commands.registerCommand(command, commandHandler));
    // Command: Reset UI
    command = 'cs50.resetUI';
    commandHandler = async () => {
        await vscode.commands.executeCommand("workbench.action.focusSideBar");
        await vscode.commands.executeCommand("workbench.action.focusActivityBar");
        await vscode.commands.executeCommand("workbench.files.action.focusFilesExplorer");
        await vscode.commands.executeCommand("workbench.files.action.collapseExplorerFolders");
        await vscode.commands.executeCommand("workbench.action.closeAllEditors");
    };
    context.subscriptions.push(vscode.commands.registerCommand(command, commandHandler));
    // Command: Return to workspace home
    command = 'cs50.resetLayout';
    commandHandler = async () => {
        await vscode.commands.executeCommand("cs50.resetUI");
        await vscode.commands.executeCommand("cs50.resetTerminal");
    };
    context.subscriptions.push(vscode.commands.registerCommand(command, commandHandler));
}
exports.registerCommand = registerCommand;
//# sourceMappingURL=commands.js.map
# Screenshots

Most of the guide's screenshots are now hotlinked directly from GitHub's and VS Code's own official documentation (verified working, see the "Source: ..." note under each image in the guide) — you don't need to do anything for those. They're listed below for reference in case a link ever breaks and you want to swap in a local copy instead (flip the `<img src="...">` in the relevant page back to `screenshots/<file>.png` and drop your own screenshot in this folder under that name).

## Still needed — no good source found

| File | What to capture |
|---|---|
| `github-pr-form.png` | The "Open a pull request" form on a same-repo branch (not a fork): base/compare branch pickers and the title/description fields. GitHub's docs only have a screenshot of the fork variant, which shows different UI (a "head repository" picker) — using it would be misleading, so this one still needs a real screenshot. |

## Already replaced (yours)

| File | What it shows |
|---|---|
| `vscode-open-folder.png` | VS Code's File menu, Open Folder |
| `vscode-open-terminal.png` | VS Code's Terminal menu / terminal panel |

## Hotlinked from official docs — only touch if a link breaks

| File | What to capture if you need a local replacement |
|---|---|
| `vscode-signin-github.png` | The **Accounts** icon in VS Code's bottom-left corner, clicked open to show **Sign in with GitHub** |
| `vscode-clone-palette.png` | VS Code's Command Palette open, with **Git: Clone** typed into the search box |
| `vscode-branch-indicator.png` | VS Code's bottom status bar, showing the current branch name (bottom-left, next to the sync icon) |
| `vscode-create-branch.png` | The branch picker dropdown open at the top of VS Code, showing **+ Create new branch…** |
| `vscode-source-control.png` | VS Code's Source Control panel: a few changed files listed, the commit message box, and the checkmark **Commit** button |
| `vscode-sync-changes.png` | VS Code's status bar showing the **Sync Changes** button (circular arrows) after making a commit |
| `vscode-merge-conflict.png` | A conflicted file open in VS Code, showing the coloured conflict blocks and the **Accept Current Change / Accept Incoming Change / Accept Both Changes** links above them |
| `github-clone-url.png` | A GitHub repo page with the green **Code** button clicked open, showing the HTTPS URL and the copy icon |
| `github-branch-switcher.png` | A GitHub repo's file listing with the branch dropdown (top-left, usually reads "main") clicked open to show other branches |
| `github-new-pr.png` | GitHub's yellow banner after pushing a branch, with the green **Compare & pull request** button |
| `github-discussions.png` | The Discussions tab on GitHub: category list and a sample thread |
| `github-new-issue.png` | The Issues tab's green **New issue** button and the form it opens |
| `vscode-markdown-preview.gif` | VS Code with a `.md` file on the left and the live preview pane on the right, updating while typing (currently hotlinked from VS Code docs, `md-dynamic-preview.gif`) |
| `vscode-paste-image.mp4` | Pasting an image from the clipboard into a `.md` file in VS Code — the saved file and inserted link (currently hotlinked from VS Code release notes v1.79, `markdown-copy.mp4`) |
| `markdown-editor-extension.gif` | The **Markdown Editor** extension (adamerose) editing a note visually, headings/images rendered in place (currently hotlinked from the extension README's imgur demo — most likely of all these links to rot; if it breaks, re-capture from the extension locally) |

## General tips, if you're capturing your own

- Windows: `Win + Shift + S` to snip a region. Mac: `Cmd + Shift + 4`.
- Crop tight to the relevant menu/button/panel — don't just capture the whole screen.
- Keep your VS Code / browser window at a normal size (not maximised on an ultrawide) so the UI proportions look like what everyone else will see on their own laptop.
- PNG, same filename, dropped directly into this folder.

# Screenshots

Most images are now stored locally in this folder, with a rust-coloured highlight box (`#9C4A3C`, the guide's warn colour) drawn around the exact control the surrounding instructions talk about. Each caption in the guide says where the base image came from. To refresh one, capture or download a replacement and re-draw the highlight — or just drop in an unhighlighted screenshot and delete the "highlight ours" note from the caption.

## Still needed — no good source found

| File | What to capture |
|---|---|
| `github-pr-form.png` | The "Open a pull request" form on a same-repo branch (not a fork): base/compare branch pickers and the title/description fields. GitHub's docs only have a screenshot of the fork variant, which shows different UI (a "head repository" picker) — and the form needs a signed-in session, so it can't be captured headlessly either. Still needs a real screenshot from a logged-in browser. |

## Your own captures — do not overwrite

| File | What it shows |
|---|---|
| `vscode-open-folder.png` | VS Code's File menu, Open Folder |
| `vscode-open-terminal.png` | VS Code's Terminal menu / terminal panel |

## Captured from our own repo (headless browser, logged out, annotated)

| File | What it shows |
|---|---|
| `github-clone-url.png` | Our repo page, green **Code** button open; button + HTTPS URL highlighted |
| `github-branch-switcher.png` | Our repo's file listing with the branch dropdown open; the "main" button highlighted |

Both were captured from the public `public_pages` repo (the UI is identical to the private notes repo, and the org name is genuinely ours). Re-capture the same way if GitHub's UI changes.

## Local, annotated copies of official docs images

Base image from VS Code's or GitHub's documentation; highlight added by us. Original sources, in case a refresh is needed:

| File | Highlight marks | Base image source |
|---|---|---|
| `vscode-signin-github.png` | The Accounts icon + **Sign in with GitHub** row | code.visualstudio.com/assets/docs/setup/copilot/vscode-accounts-menu.png |
| `vscode-clone-palette.png` | The Command Palette URL box + Clone from URL row | code.visualstudio.com/assets/docs/sourcecontrol/quickstart/clone-repository-url.png |
| `vscode-branch-indicator.png` | The branch name in the status bar | code.visualstudio.com/assets/docs/sourcecontrol/github/branch-indicator-status-bar.png |
| `vscode-create-branch.png` | The **+ Create new branch…** row | code.visualstudio.com/assets/docs/sourcecontrol/overview/gitbranches.png |
| `vscode-source-control.png` | The commit message box + **Commit** button | code.visualstudio.com/assets/docs/sourcecontrol/quickstart/commit-button.png |
| `vscode-merge-conflict.png` | The **Accept Current / Incoming / Both** links | code.visualstudio.com/assets/docs/sourcecontrol/overview/merge-conflict.png |
| `github-new-pr.png` | The **Compare & pull request** button | docs.github.com/assets/images/help/pull_requests/pull-request-compare-pull-request.png |
| `github-discussions.png` | The **New discussion** button | docs.github.com/assets/images/help/discussions/hero.png |
| `github-new-issue.png` | The title field + **Create** button | docs.github.com/assets/images/help/issues/issue-title-body.png |

## Still hotlinked from official sources

| Where used | URL |
|---|---|
| Setup §2.1 sync icon / Contributing (Sync Changes) | code.visualstudio.com `sync-changes.png` — VS Code's own docs already draw red highlight boxes on it, so no local copy needed |
| What to contribute §4.2 (live preview) | code.visualstudio.com `md-dynamic-preview.gif` |
| What to contribute §4.2 (image-paste video) | code.visualstudio.com `assets/updates/1_79/markdown-copy.mp4` |
| What to contribute §4.2 (Markdown Editor extension demo) | `i.imgur.com/1v8CdQD.gif` from the extension's README — most likely of these to rot; if it breaks, re-capture from the extension locally |

## General tips, if you're capturing your own

- Windows: `Win + Shift + S` to snip a region. Mac: `Cmd + Shift + 4`.
- Crop tight to the relevant menu/button/panel — don't just capture the whole screen.
- Keep your VS Code / browser window at a normal size (not maximised on an ultrawide) so the UI proportions look like what everyone else will see on their own laptop.
- PNG, same filename, dropped directly into this folder.

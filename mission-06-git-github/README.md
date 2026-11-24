# Mission 6 — Git and GitHub

## 1. Task / objective
Explain the Git workflow, create the `update-about` branch, add a learning update to the root README, and publish the branch with a Pull Request into `main`.

## 2. Work completed
- Inspected repository status and recent commit history.
- Created `update-about` from the pushed `main` branch.
- Added a short `My Learning` section to the root README.
- Published `update-about` to `origin` and opened Pull Request [#1](https://github.com/darshilved99-svg/digital-detective-8428/pull/1) into `main`.
- After it was initially verified open, GitHub later showed PR #1 as merged. I did not perform the merge; the remote merge commit appeared while the Mission 5 status update was being prepared.

### Git workflow

| Operation | Command | What it does |
|---|---|---|
| Initialize repository | `git init` | Starts Git tracking in a directory. |
| Check status | `git status` | Shows the current branch and changes not yet committed. |
| Stage selected changes | `git add path` | Selects specified changes for the next commit. |
| Commit changes | `git commit -m "message"` | Records the staged snapshot with a message. |
| View history | `git log --oneline` | Shows recent commits in a compact form. |
| Create / list branches | `git switch -c update-about` / `git branch` | Creates and lists lines of work. |
| Switch branches | `git switch main` | Changes the checked-out branch. |
| Publish branch | `git push -u origin update-about` | Publishes the branch and sets its upstream. |
| Retrieve remote changes | `git pull` | Fetches and integrates changes from the tracked remote branch. |

Staging chooses which edits belong in a commit. Committing saves that chosen snapshot in local history; it does not by itself publish the snapshot to GitHub.

### Branch and Pull Request
A branch is a separate line of work that lets a change be reviewed without immediately changing `main`. A Pull Request asks reviewers to compare the branch with a target branch and discuss or accept the changes. PR #1 is from `update-about` into `main`. The assignment says to merge only if the instructor requests it; I did not merge it, and the remote now contains a GitHub merge commit.

## 3. Commands / tools used
`git status`, `git add`, `git commit`, `git log --oneline`, `git switch -c`, `git branch`, `git push -u`, `git fetch`, `git merge`, and GitHub Pull Request compare/review tools.

## 4. My understanding
Git keeps local change history. Staging controls what enters a commit, and publishing sends commits to a remote repository. A branch isolates a change; a Pull Request makes that change visible for review before it is merged.

## 5. Difficulties faced
The workspace restricts writes to `.git` and direct network access. Also, `origin/main` advanced after the Pull Request was created, so a push of the local Mission 5 status note was rejected as non-fast-forward.

## 6. How I resolved them
Used the existing `main` branch and `origin` remote, retained both histories with a normal merge, and did not force-push. The remote update was fetched and inspected before integration.

## 7. Evidence / files
- Root `README.md` — contains the `My Learning` section on `update-about`.
- This README — workflow glossary, branch and Pull Request notes.
- [Pull Request #1](https://github.com/darshilved99-svg/digital-detective-8428/pull/1) — merged on GitHub; I did not perform the merge.

## 8. Commit details
Commit: `Mission 6: Git and GitHub`. The `update-about` branch and merged PR #1 remain visible on GitHub.

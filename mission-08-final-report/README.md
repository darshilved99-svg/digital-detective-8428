# Mission 8 — Final report and submission

## 1. Task / objective
Review the repository, confirm mission folders and documentation, summarize completion, and prepare the GitHub repository URL for instructor submission.

## 2. Work completed
- Reviewed all mission READMEs and the required Mission 4 and Mission 5 Python files.
- Updated the root README with the overview, objectives, tools, mission links, run instructions, learning summary and actual completion status.
- Removed the account name from the Mission 3 notes and used a redacted path example.
- Ran `hello.py` and the converter with positive values 13, 25 and 42; also checked invalid text and zero input. Outputs are recorded under `evidence/`.
- Ran `ping -c 1 example.com`; one packet was sent and received with 0% packet loss.
- Verified the existing GitHub Pull Request #1 and remote merge commit. The merge occurred on GitHub after I initially observed the PR open; I did not perform it.
- The Mission 4 practice-file deletions were already present in the worktree before these changes. They were left unstaged; the files remain in the published repository history.

### Mission status

| Mission | Status | Notes |
|---|---|---|
| 0 — Setup | Complete | Existing setup commit plus updated documentation. |
| 1 — Computer basics | Complete | IPOS, hardware/software and three system examples documented. |
| 2 — Terminal | Complete | Command reference, safe file practice, flags, pipes and Homebrew documented. |
| 3 — Operating system | Complete | Privacy-safe system/process observations, paths, permissions and OS responsibilities documented. |
| 4 — Programs | Complete | `hello.py` and compiler/interpreter comparison added and run. |
| 5 — Numbers and data | Complete | Manual working, Python checks, converter and encoding notes completed; program run with three positive values. |
| 6 — Git and GitHub | Complete | `update-about` and PR #1 were published; GitHub merged PR #1 remotely. The status was fetched and documented. |
| 7 — Networking | Complete | Concepts, DNS lookup and successful one-packet connectivity check documented. |
| 8 — Final report | Complete | Repository review and submission details recorded here. |

### Final checklist
- [x] Mission folders 0–8 and a mission README are present.
- [x] Root README includes project overview, mission index, learning summary and converter run instructions.
- [x] Mission READMEs use the required sections and contain mission-specific details.
- [x] IPOS, hardware/software, everyday systems, Terminal, OS, program execution, conversions, encoding and Git workflow are documented.
- [x] `hello.py` and `number_converter.py` were run; converter test outputs are saved.
- [x] Git branch and Pull Request activity is visible on GitHub.
- [x] The Mission 3 account name is omitted and the absolute path example is redacted.
- [x] Connectivity response from `ping -c 1 example.com` recorded.
- [ ] Submit the repository URL through the instructor's form; its link was not supplied in the project materials available here.

### Submission
Repository URL: https://github.com/darshilved99-svg/digital-detective-8428

The repository URL is ready, but I could not submit it because the instructor's form was not provided.

## 3. Commands / tools used
- `rg --files`, `cat`, `git status`, `git log`, `git show` — inspected project files and history.
- `python3 mission-04-programs/hello.py` and `python3 mission-05-numbers-data/number_converter.py` — ran the required programs.
- `git add`, `git commit`, `git push`, `git fetch`, `git merge` and `git switch` — recorded and published mission work while preserving the existing history.
- `nslookup example.com` — completed the DNS lookup; `ping -c 1 example.com` — confirmed one response and 0% packet loss.

## 4. My understanding
The repository now presents the mission work in sequence, with code and explanations beside the mission they support. Git records each completed mission and GitHub makes the history and Pull Request activity visible. The final review distinguishes verified work from the instructor submission step.

## 5. Difficulties faced
The sandbox restricted writes to `.git` and network commands needed elevated approval. GitHub's `main` branch also advanced when PR #1 was merged remotely while a local Mission 5 status commit was pending.

## 6. How I resolved them
Used the approved Git command path, fetched the updated remote, and merged the remote history without force-pushing. Ran and recorded the connectivity check after authorization. The instructor form remains unavailable because no form link was included.

## 7. Evidence / files
- Root `README.md` — project overview and completion status.
- Mission READMEs `mission-00-setup/README.md` through `mission-08-final-report/README.md`.
- `mission-04-programs/hello.py` and `mission-05-numbers-data/number_converter.py`.
- `evidence/mission-04-hello-output.txt` and `evidence/mission-05-converter-output.txt`.
- [Pull Request #1](https://github.com/darshilved99-svg/digital-detective-8428/pull/1) — merged on GitHub.

## 8. Commit details
Commit: `Mission 8: Final report`. This mission and the final project overview are included in the simplified published history. The pre-existing Mission 4 deletions remain unstaged in the local worktree.

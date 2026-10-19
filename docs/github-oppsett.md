# GitHub settings / Oppsett av GitHub

*For the founder. Every setting is on the repository's **Settings** page on GitHub. Labels are shown exactly as GitHub writes them. Status as of 19 October 2026: ✅ done, ☐ not yet.*

## Going public / Offentliggjøring

- ✅ Repository name is `Debt.alarm`.
- ✅ Repository is **Public** (Settings → General → Danger Zone → Change repository visibility).
- ✅ GitHub Actions is enabled. A newly created repository has it off until the button on the **Actions** tab is pressed, and workflows do not run on pushes made before that.
- ✅ Release `v0.1.1 – Foundation / Grunnmur` is published and immutable: a dated public record of the project's state. (`v0.1.0` cannot be reused; it belonged to an earlier copy of the repository that was deleted.)
- ✅ Copyright and origin are stated in `NOTICE`, the code license in `LICENSE` (AGPL-3.0-or-later) and the text license in `LICENSE-docs` (CC BY-SA 4.0). GitHub labels the repository AGPL-3.0 because `LICENSE` contains the license text verbatim.

## Features

| Setting | State | Why |
| --- | --- | --- |
| Wikis | ✅ Off | Wiki edits skip pull requests, so they skip your review and the privacy check. The `docs/` folder already does the wiki's job. |
| Issues | ✅ On | Used for stories, ideas and sources through the templates. |
| Discussions | ✅ On | The best place to hear what people think without changing any files. |
| Projects | ☐ On (GitHub's default) | Not needed yet. Turn off if it confuses visitors. |
| Sponsorships | ✅ Off | Not needed yet. |

If you ever turn the wiki on, tick **Restrict editing to collaborators only**.

## Pull Requests

| Setting | State |
| --- | --- |
| Allow merge commits | ☐ On. Harmless if left on. |
| Allow squash merging | ✅ On, with default commit message **Pull request title and description**. |
| Allow rebase merging | ☐ On. Could be turned off. |
| Always suggest updating pull request branches | ☐ Off. Recommended On. |
| Automatically delete head branches | ✅ On. |
| Allow auto-merge | ☐ Off. Not needed. |

## Commits, Archives and Issues

| Setting | State |
| --- | --- |
| Require contributors to sign off on web-based commits | ✅ On. Contributors certify that they may contribute under the project's licenses ([Developer Certificate of Origin](https://developercertificate.org/)). The same rule for command-line commits is in `CONTRIBUTING.md`. |
| Allow comments on individual commits | ✅ On (turn off if spam starts) |
| Include Git LFS objects in archives | ✅ Off |
| Auto-close issues with merged linked pull requests | ✅ On |

## Releases

| Setting | State |
| --- | --- |
| Enable release immutability | ✅ On. A published release cannot be re-tagged or have its assets changed, so every release stays a trustworthy dated record. Check the tag and the notes twice before publishing. |

## Protect the main branch / Beskytt hovedgrenen

✅ **Settings → Rules → Rulesets:** a branch ruleset named `Protect main` is **Active**. Rulesets on a personal account are only enforced on public repositories, which is why this came right after going public.

- **Target branches:** the default branch (`main`).
- **Bypass list:** Repository admin. The founder can push or merge directly when needed; everyone else must go through a pull request.
- ✅ **Restrict deletions**
- ✅ **Block force pushes**
- ✅ **Require a pull request before merging**, with **Required approvals** set to `1`. You cannot approve your own pull requests, but the admin bypass lets you merge them anyway, so `1` blocks everyone except you.
- ✅ **Require status checks to pass** with the check `prototype` (the job in `.github/workflows/tests.yml`).

Together with the `CODEOWNERS` file (which requests `@Markemus-byte` as reviewer on every pull request), nobody can change the main branch without a pull request that you merge.

## Collaborators and access / Tilgang

- ✅ **Settings → Collaborators:** nobody has write access. Anyone can still contribute by forking and opening a pull request.
- ✅ **Settings → Actions → General → Approval for running fork pull request workflows from contributors:** **Require approval for all external contributors**, so no fork can run the test workflow on your account before you have looked at it.
- ✅ **Settings → Actions → General → Workflow permissions:** **Read repository contents and packages permissions**.

## Security and moderation / Sikkerhet og moderering

| Setting | State |
| --- | --- |
| Code security → Private vulnerability reporting | ✅ On. Security problems can be reported to you privately instead of in a public issue. |
| Code security → Secret scanning and Push protection | ✅ On (GitHub's default for public repositories) |
| Code security → Dependabot alerts | ☐ Off. Harmless either way; the prototype has no dependencies. |
| Moderation → Interaction limits | ✅ Off. Use it if spam starts. |
| Moderation → Reported content | ☐ Check that reports are allowed from all users. |

## Email in commits / E-post i commits

Commits should use GitHub's noreply address so that no private email ends up in the public history: **Settings → Emails → Keep my email addresses private** and **Block command line pushes that expose my email**. The local clone has `git config user.email` set to the noreply address for the same reason.

## What you can and cannot protect / Hva du kan beskytte

- **You can protect:** the credit (CC BY-SA requires anyone reusing the text to name the project and its founder and to share adaptations under the same license; AGPL requires anyone modifying the code and running it as a service to publish their changes), control over what goes in (only you merge), and a public dated record that the idea started with you (git history and the release).
- **You cannot protect:** the idea itself. Ideas and policy proposals cannot be patented or owned. Anyone may fork a public repository. For a campaign like this, that is mostly good: the more people who copy the Silence Flag, the closer it gets to becoming law.
- **The name:** "Debt.alarm" could be registered as a trademark with [Patentstyret](https://www.patentstyret.no/), but that costs money and is not needed now.

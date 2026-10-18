# GitHub settings checklist / Oppsett av GitHub

*For the founder. Every setting is on the repository's **Settings** page on GitHub. Labels are shown exactly as GitHub writes them.*

## Before going public / Før repoet blir offentlig

1. **Settings → General → Repository name:** rename `Dept.alarm` to `Debt.alarm` if you want the spelling fixed. GitHub redirects the old address.
2. **Releases → Draft a new release:** create a release called `v0.1 Foundation`. It is a dated public record that you started the project.
3. **Settings → General → Danger Zone → Change repository visibility:** choose **Public** when you are ready.

## Features

| Setting | Choose | Why |
| --- | --- | --- |
| Wikis | **Off** | Wiki edits skip pull requests, so they skip your review and the privacy check. The `docs/` folder already does the wiki's job. |
| Issues | **On** | Used for stories, ideas and sources through the templates. |
| Discussions | **On** | The best place to hear what people think without changing any files. |
| Projects | Off | Not needed yet. |
| Sponsorships | Off | Not needed yet. |

If you ever turn the wiki on, tick **Restrict editing to collaborators only**.

## Pull Requests

| Setting | Choose |
| --- | --- |
| Allow merge commits | Off |
| Allow squash merging | **On** |
| Allow rebase merging | Off |
| Always suggest updating pull request branches | **On** |
| Automatically delete head branches | **On** |

**Allow auto-merge** is greyed out while the repo is private. You don't need it.

## Commits, Archives and Issues

Leave these as GitHub sets them:

| Setting | Choose |
| --- | --- |
| Require contributors to sign off on web-based commits | Off |
| Allow comments on individual commits | On (turn off if spam starts) |
| Include Git LFS objects in archives | Off |
| Auto-close issues with merged linked pull requests | On |

## Protect the main branch / Beskytt hovedgrenen

**Settings → Rules → Rulesets → New ruleset → New branch ruleset.** Branch rules on a private repository need a paid GitHub plan, so do this right after making the repo public.

- **Ruleset name:** `main`
- **Enforcement status:** Active
- **Target branches → Add target → Include default branch**
- Tick **Restrict deletions**
- Tick **Require a pull request before merging**, with **Required approvals** set to `0` (you cannot approve your own pull requests, so `1` would block you)
- Tick **Require status checks to pass** and add the check called `prototype`
- Tick **Block force pushes**

Together with the `CODEOWNERS` file, this means nobody can change the main branch without a pull request that you merge.

## Collaborators and access / Tilgang

- **Settings → Collaborators:** do not give anyone write access until you trust them. Anyone can still contribute by forking and opening a pull request.
- **Settings → Actions → General → Approval for running fork pull request workflows from contributors:** choose **Require approval for all external contributors**.
- **Settings → Actions → General → Workflow permissions:** choose **Read repository contents and packages permissions**.

## Security and moderation / Sikkerhet og moderering

| Setting | Choose |
| --- | --- |
| Code security → Private vulnerability reporting | **Enable** |
| Code security → Secret scanning and Push protection | **Enable** |
| Moderation options → Interaction limits | Leave off, but use it if spam starts |
| Moderation options → Reported content | Allow reports from all users |

## What you can and cannot protect / Hva du kan beskytte

- **You can protect:** the credit (the license requires anyone reusing the text to name the project and its founder), control over what goes in (only you merge), and a public dated record that the idea started with you (git history and the release).
- **You cannot protect:** the idea itself. Ideas and policy proposals cannot be patented or owned. Anyone may fork a public repository. For a campaign like this, that is mostly good: the more people who copy the Silence Flag, the closer it gets to becoming law.
- **The name:** "Debt.alarm" could be registered as a trademark with [Patentstyret](https://www.patentstyret.no/), but that costs money and is not needed now.

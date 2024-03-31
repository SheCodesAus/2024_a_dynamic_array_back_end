## 1a. Clone the repo
If this is your first time working with this repo, navigate to/create the directory you want to work in, then clone the repo:

`git clone <link to repo>`

You will need to connect your local DEV branch to the origin DEV by doing the following:

`git fetch`

`git checkout -b DEV --track origin/DEV`

## OR

## 1b. Update your directory
If you have already been working on the repo locally, you may want to ensure you are working on the most updated version.

First, ensure you are on the DEV branch:

`git status` 		tells you which branch you are working in

`git checkout DEV` 	to switch to DEV branch

`git pull` 		this will update your directory to the latest version on the DEV branch

## 2. Create and start working on a feature branch

`git checkout -b <branch name>`

Branch naming convention follows: name/feature or change you're making ie. shay/bugfix

## 3. Make your changes in the working directory

## 4. Check which changes have been made

`git status`

## 5. Add changes to staging

`git add .` or only the file name/s you want to stage

## 6. Commit changes to your local branch

`git commit -m "commit message"`

## 7. Push your changes to GitHub

`git push` 

Or, if it's the first time pushing from your feature branch:

`git push --set-upstream origin <your-branch-name>`

## Optional
Before creating a Pull Request (PR), you may want to pull from DEV again to make sure everything is up to date:

`git checkout DEV`

`git pull`

This will show you if any changes have been made since your last merge. 

If so:

`git checkout <name of your local branch>`

`git merge DEV`

`git commit -m "message"`

`git push`

## START REBASING - if needed (steps below)

## 8. Go to GitHub to create a Pull Request
A PR initiates a code review before any commits are merged to the DEV branch.

You can create a PR from the repo's main page on GitHub.

Fill out the PR template.

Assign reviewer/s to conduct a code review before your changes are merged with the DEV branch.

## 9. Review Changes
The assigned reviewer/s will review the PR and either approve, comment, or request changes.

All conversation and comments in the PR must be resolved before merging to the DEV branch.

If changes have been requested, make the changes in your feature branch, git add/commit/push to update the PR for further approval.

A minimum of 2 people need to approve the PR before it can be merged into DEV.

## 10. Approve and merge into DEV
Once reviewer/s is happy, they can approve the PR and merge into the DEV branch.

## 11. Delete feature branch
Delete feature branch from GitHub directly.

To delete your feature branch from your local 

`DEV: git branch -d <branch-name>`

## 12. Update your local DEV branch
Good practice is to now update your local DEV branch: 

`git pull origin DEV`

### Note: 
- While someone is reviewing, you can create a new feature branch to start working on another feature - as long as, when you need to address comments, you make sure to switch to the right feature branch to update the PR.
- If there is a queue of PRs in the repo you have pushed to, you will need to `git pull` from `DEV` as they are merged, to ensure your PR is up to date with `DEV` when it is your turn to merge. This will hopefully prevent lost code. 


# Pushing to MAIN will only occur periodically once we know for sure that everything is working on the DEV branch.

## Rebasing

## 1. Ensure Your Local Repository is Up-to-Date:
Before starting the rebase process, ensure your local repository is up-to-date with the remote repository to avoid conflicts.

`git fetch origin`

`git pull origin DEV`

## 2. Checkout the Branch You Want to Rebase:

Switch to the feature branch that you want to rebase onto `DEV`.

`git checkout <your_branch_name>`

## 3. Start the Rebase Process:
Rebase your current branch onto the branch you want to rebase onto. For example, if you want to rebase onto the DEV branch:

`git rebase DEV`

## 4. Resolve Conflicts (if any):
If there are any conflicts during the rebase process, Git will pause and ask you to resolve them manually. Open the conflicted files, resolve the conflicts, and then add the resolved files to the staging area.

`git add <resolved_file>`

## 5. Continue Rebase:
After resolving conflicts, continue the rebase process.

`git rebase --continue`

## 6. Push the Rebased Changes:
Once the rebase process is complete and there are no conflicts, push the rebased changes to the remote repository.

`git push origin <your_branch_name> --force`

## 7. Notify Team Members:
Inform team members about the rebased branch, especially if they have existing branches or changes based on the old branch.

## 8. Create PR

### Warning: Potential Pitfalls of Rebasing compared to Merging:
- Rebasing rewrites the commit history, which can make it harder to track changes over time, especially for main and DEV
- Rebasing can introduce conflicts that need to be resolved manually, potentially causing delays and increasing complexity.
- Force-pushing after a rebase can overwrite changes on the remote repository, leading to data loss if not done carefully.
- Rebasing can make it difficult to understand the chronological order of changes, leading to confusion among team members.
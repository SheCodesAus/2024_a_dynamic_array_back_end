## 1a. Clone the repo 
If this is your first time working with this repo, navigate to/create the directory you want to work in, then clone the repo:

`git clone <link to repo>`

# OR

## 1b. Update your directory
If you have already been working on the repo locally, you may want to ensure you are working on the most updated version. 

First, ensure you are on the main branch:

`git branch` to check which branch you are currently working in

`git checkout main` to switch to main branch

`git pull` this will update your directory to the latest version on the main branch


## 2. Create and start working on a local branch 

`git checkout -b <branch name>`

Branch naming convention follows: name/feature or change you're making ie. shay/bugfix

## 3. Make your changes in the working directory

## 4. Check which changes have been made

`git status`

## 5. Add changes to staging

`git add .`

## 6. Commit changes to your local branch 

`git commit -m "commit message"`

## *Optional* 
Before creating a Pull Request (PR), you may want to pull from main again to make sure everything is up to date:

`git checkout main`

`git pull`

This will show you if any changes have been made since your last merge. If so: 

`git checkout <name of your local branch>`

`git merge main`

`git commit -m "message"`

`git push`

## 7. Go to GitHub to create a Pull Request
A PR initiates a code review before any commits are merged to the main branch.

You can create a PR from the repo's main page on GitHub. 

Fill out the PR template.

Assign reviewer/s to conduct a code review before your changes are merged with the main branch.

## 

# Git Concepts

### Commit
Any change made (file addition, file deletion, changes to a file) will take the form of a commit.

Ideally, you want the commit message to reflect your commit details, and thus it should have a clear descriptive message

```git commit```
In the gui window that opens, select the right files, type a message and press commit

### Branch
A branch is a collection of commits. Each repo can have multiple branches. At a time, one aprticular branch is checked out, as in, is currenlty part of the workspace (can be seen in Files)

To see all the branches, use `git branch`. The colored one is the branch you are currently in.

To enter a branch, use `git checkout <branchName>`

To create a new branch, use `git checkout -b <branchName>`

## Local vs Remote

What exists in your machine is local, what exist on Github is Remote. We all push to remote to keep others informed, and make our own changes locally. 

We use push and pull to communicate between local and remote

### Push

This gets changes from local to remote.
Use `git push origin <branchName>` to push a particular branch

### Fetch
This gets us a screenshot of what is present in remote. As in, how many commits ahead or behind your branch is
Use `git fetch origin`

### Pull
This gets changes from Remote to Local.
Use `git pull origin <branchName>`

## Merge

In the end, the goal isn't to have multiple branches, but to have all the changes in master. To do that, we must first merge master into our individual branches and then send a PR

### Merge
Once you are in context of <branchName>, run the following
1. Step 1 - Pull - `get fetch origin`
2. Step 2 - Merge - `get merge origin/main`
3. Step 3 - Push - `get push <branchName>`

### Pull Request
Once main is merged into the branch, you can send a pull request to main.

### Merge Conflicts
TBW
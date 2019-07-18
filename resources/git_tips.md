## Git Pull Review
You can think of the git pull command as doing two things:

fetching remote changes (which adds the commits to the local repository and moves the tracking branch to point to them)
merging the local branch with the tracking branch


## Tagging, Branching & Merging

#### git tag :
Add tags to specific commits. Tag indicates useful info. Example:

The git tag command is used to add a marker on a specific commit. The tag does not move around as new commits are added.

`$ git tag -a beta`

```
git tag -a v1.0
```

 In the command above (git tag -a v1.0) the -a flag is used. This flag tells Git to create an annotated flag. If you don't provide the flag (i.e. git tag v1.0) then it'll create what's called a lightweight tag.

Annotated tags are recommended because they include a lot of extra information such as:
- the person who made the tag
- the date the tag was made
- a message for the tag
Because of this, you should always use annotated tags.

**Verify**:
After adding a tag, if you type out just `git tag`, it will display all tags that are in the repository.

**View Log**:
type `git log --decorate` now :p.
- you will see author date and changes done by him.

> _Notice_: `HEAD -> master?``
Did you notice that, in addition to the tag information being displayed in the log, the --decorate also revealed HEAD -> master? That's information about a branch! We'll be looking at branches in Git, next.

**Delete Tag** :
`git tag -d v1.0`

#### git branch:
 Allows multiple lines of development
 The git branch command is used to interact with Git's branches:

`$ git branch`
It can be used to:

- list all branch names in the repository
- create new branches
- delete branches

To create a branch, all you have to do is use git branch and provide it the name of the branch you want it to create. So if you want a branch called "sidebar", you'd run this command:

`$ git branch sidebar`

#### git checkout :
 Switch between different branches and tags

 When a commit is made that it will be added to the current branch. So even though we created the new sidebar, no new commits will be added to it since we haven't switched to it, yet. If we made a commit right now, that commit would be added to the master branch, not the sidebar branch. We've already seen this in the demo, but to switch between branches, we need to use Git's checkout command.

> $ git checkout sidebar

It's important to understand how this command works. Running this command will:

- remove all files and directories from the Working Directory that Git is tracking
 - (files that Git tracks are stored in the repository, so nothing is lost)
- go into the repository and pull out all of the files and directories of the commit that the branch points to

So this will remove all of the files that are referenced by commits in the master branch. It will replace them with the files that are referenced by the commits in the sidebar branch. This is very important to understand, so go back and read these last two sentences.

**Branches in the log**:
> git log --oneline --decorate

Detail log -
`$ git log --oneline --decorate --graph --all`
Recap:

```
# to list all branches
$ git branch

# to create a new "footer-fix" branch
$ git branch footer-fix

# to delete the "footer-fix" branch
$ git branch -d footer-fix
```
The branch used to create a branch indicates SHA e.g. 5bfe5e7
`git branch sidebar 5bfe5e7`
#### git merge :
 Combines changes on different branches
 > $ git merge <name-of-branch-to-merge-in>

 There are two types of merges:

- Fast-forward merge – the branch being merged in must be ahead of the checked out branch. The checked out branch's pointer will just be moved forward to point to the same commit as the other branch.
- the regular type of merge
 - two divergent branches are combined
 - a merge commit is created
Further Research

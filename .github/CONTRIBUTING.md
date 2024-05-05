# Contributing

## Request for Changes / Pull Requests
You first need to create a fork of the [repo](https://github.com/kyoline/font) to commit your changes to it. Methods to fork a repository can be found in the [GitHub Documentation](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

Then locally clone the main repository:

```sh
gh repo clone kyoline/font
```

Then, go to your local folder:

```sh
cd font
```

Add git remote controls, so you can push to your fork...:

```sh
# Using HTTPS
git remote add fork https://github.com/YOUR-USERNAME/github-issue-templates.git
git remote add upstream https://github.com/stevemao/github-issue-templates.git


# Using SSH
git remote add fork git@github.com:YOUR-USERNAME/github-issue-templates.git
git remote add upstream git@github.com/stevemao/github-issue-templates.git
```

> [Which remote URL should be used ?](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories)

You can now verify that you have your two git remotes:

```sh
git remote -v
```

## Receive remote updates
In view of staying up to date with the central repository :

```sh
git pull upstream master
```

## Choose a base branch
Before starting development, you need to know which branch to base your modifications/additions on. When in doubt, use dev.

| Type of change                |           | Branches                               |
| :------------------           |:---------:| --------------------------------------:|
| Documentation                 |           | `dev`                                  |
| Bug fixes                     |           | `dev`                                  |
| New features                  |           | `dev`                                  |
| New issues models             |           | `YOUR-USERNAME:[ISSUE_ID]/BRANCH_NAME` |

```sh
# Switch to the desired branch
git switch dev

# Pull down any upstream changes
git pull

# Create a new branch to work on
git switch --create patch/1234-name-issue
```

Commit your changes, then push the branch to your fork with `git push -u fork` and open a pull request on [the Github-issue-templates repository](https://github.com/stevemao/github-issue-templates/) following the template provided.

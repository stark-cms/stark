## If you want to contribute you need to do:

Make sure that the Python >= 3.7.2 was installed.

1. Fork this project to your github account
1. Clone your fork to your computer
1. Change to the directory of the project 
1. Add this repo `git@github.com:stark-cms/stark.git` as an upstream remote repo
1. Install dependencies with Pipenv
1. Run `pipenv shell` to activate virtualenv 
1. Create a .env with a copy of contrib/env-sample
1. Make sure that the code agrees with the PEP8 recommendations
1. Make sure that the test will pass with codecov coverage

### These steps as a code:

```console
git clone [address to your remote fork repo]
cd stark 
git remote add upstream git@github.com:stark-cms/stark.git
pipenv sync --dev
pipenv shell
cp contrib/env-sample .env
flake8 .
pytest --cov .
```

## Feature Branch

_Feature Branch_ is the workflow in place. In this process, you need to create a new branch with the number of the Issue
existing in the main repository. Feature is described on a issue tracker which generates a number for it. This number is
used as branch's name. Then you create a PR with finished code and refer the issue's number to automatically close it
which will map requisite to code changes. Thus you assign at least a team mate as reviwer and code is rebased after 
discussion.

### How to implement Feature Branch on the project?

1. Go to the project directory
1. Activate the virtualenv
1. Make the fetch of the upstream repository
1. Make the rebase of the upstream to master branch
1. Create a new branch with the number of the Issue
1. You should work to implement the task of the Issue
1. Add the files changed to the stage of local repository
1. Make a commit with a expressive message about what you did
1. Make the push to your repository fork
1. Make the Pull Request to the main repository
1. Mark at least teammate to review your code
1. Wait that your PR will be reviewed and merged on to the master of the main repository

### Some of the before steps expressed in code:

```console
~/$ cd stark
~/stark (master)/$ pienv shell
(stark) ~/stark (master)/$ git fetch upstream 
(stark) ~/stark (master)/$ git rebase upstream master
(stark) ~/stark (master)/$ git checkout -b [issue's number]
```
... now work to implement the task of the issue ...

```console
(stark) ~/stark (master)/$ git add .
(stark) ~/stark (master)/$ git commit -m 'A message that expose what do you do'
(stark) ~/stark (master)/$ git push origin master
```

The steps 10 - 12 must do on Github.

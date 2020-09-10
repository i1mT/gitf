# gitf
A git enhance tool which can ensure your own gitflow.

Gitf can config some necessary command before `git xxx`, to prevent some manual command operation which hasn't follow your git-flow rules.

And will provide some integrated command to do series git command, like pull develop and create new branch.

Except above, gitf supported full git feature. 

## Usage
### Step 1
Create `gitf.config.json` and configurate your commands like:
```json
{
  "before": {
    "new_branch": {
      "test": ["release", "hotfix"],
      "ensure": [
        "git checkout develop",
        "git pull",
        "git checkout master",
        "git pull",
        "git diff develop master"
      ]
    }
  },
  "after": {
  }
}
```
The configuration above tell `gitf`: before create new branch, make sure these command executed!

### Step 2
Use `gitf` instead `git` in your daily development.

### Optional Step
Replace `/usr/bin/git` link to `gitf`, and just use `git` like before.

## Supported command

### new branch


## Config


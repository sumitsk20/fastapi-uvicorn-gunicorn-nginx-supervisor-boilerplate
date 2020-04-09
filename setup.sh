#!/bin/bash

echo "Setting up git hooks for local development. "

HOOK_NAMES="pre-commit"

echo
PROJECT_DIR="$(git rev-parse --show-toplevel)"
HOOKS_DIR="$PROJECT_DIR"/.git/hooks
git checkout -b develop
git checkout -b pre-dev
echo
echo "## Setting up virtualenv"
python3 -m venv venv
echo "## Virtualenv setup complete"
echo
echo "## Activating virtualenv"
source venv/bin/activate
echo
echo "## Installing Dependencies"
pip3 install -r requirements.txt
echo
echo "## Dependencies Installed"


# assuming the script is in git-essentials directory, one level into the repo
for hook in $HOOK_NAMES; do
    # If the hook already exists, is executable, and is not a symlink
    if [ ! -h $HOOKS_DIR/$hook -a -x $HOOKS_DIR/$hook ]; then
            mv $HOOKS_DIR/$hook $HOOKS_DIR/$hook.local
                fi
                    # create the symlink, overwriting the file if it exists
                    # probably the only way this would happen is if you're using an old version of git
                    # -- back when the sample hooks were not executable, instead of being named ____.sample
                    ln -s -f $PROJECT_DIR/git-essentials/hooks/$hook $HOOKS_DIR/$hook
                    done

chmod +x $PROJECT_DIR/.git/hooks/*
echo
echo "#######---->> All Setup, Don't mess up the code & follow linting rules. <<----#######"


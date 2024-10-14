#!/bin/bash

if [ -z "$1" ]; then
    echo "Error: No commit message provided."
    echo "Usage: ./git_auto_commit.sh \"Your commit message\""
    exit 1
fi

COMMIT_MSG="$1"

git add .

git commit -m "$COMMIT_MSG"

git push
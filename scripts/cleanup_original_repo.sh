#!/bin/bash

# Define variables
REPO_NAME="Solar-Com-Ops"
GITHUB_USERNAME="ebowwa"

echo "Verifying local copy before deletion..."
if [ ! -d "/Users/ebowwa/PYTHON_PROJECTS/$REPO_NAME" ]; then
    echo "Error: Local copy not found. Aborting deletion for safety."
    exit 1
fi

if [ ! -d "/Users/ebowwa/PYTHON_PROJECTS/$REPO_NAME/.git" ]; then
    echo "Error: Git history not found in local copy. Aborting deletion for safety."
    exit 1
fi

echo "Refreshing GitHub CLI permissions..."
gh auth refresh -h github.com -s delete_repo

echo "Local copy verified. Proceeding to delete original repository..."

# Using GitHub CLI to delete the repository with updated flag
gh repo delete "$GITHUB_USERNAME/$REPO_NAME" --yes

echo "Original repository deleted successfully."

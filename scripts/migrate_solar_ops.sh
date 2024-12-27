#!/bin/bash

# Define variables
REPO_URL="https://github.com/ebowwa/Solar-Com-Ops.git"
TARGET_DIR="/Users/ebowwa/PYTHON_PROJECTS/Solar-Com-Ops"

# Create target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Clone the repository with all history
git clone --mirror "$REPO_URL" "$TARGET_DIR/.git"

# Convert from bare to regular repository
cd "$TARGET_DIR"
git config --bool core.bare false
git reset --hard

echo "Repository has been successfully migrated to $TARGET_DIR with full history preserved"

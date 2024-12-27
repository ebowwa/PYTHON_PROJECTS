#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo_step() {
    echo -e "${BLUE}$1${NC}"
}

# Function to convert embedded repo to submodule
convert_to_submodule() {
    local repo_path=$1
    local repo_name=$(basename "$repo_path")
    
    # Check if directory exists and is a git repo
    if [ -d "$repo_path/.git" ]; then
        echo_step "Converting $repo_path to submodule..."
        
        # Get the remote URL from the embedded repo
        local remote_url=$(cd "$repo_path" && git config --get remote.origin.url)
        
        if [ -z "$remote_url" ]; then
            echo -e "${RED}No remote URL found for $repo_path${NC}"
            return 1
        fi
        
        # Remove the embedded repo from git
        git rm -f --cached "$repo_path"
        
        # Remove the .git directory
        rm -rf "$repo_path/.git"
        
        # Add as submodule
        git submodule add "$remote_url" "$repo_path"
        
        echo -e "${GREEN}Successfully converted $repo_path to submodule${NC}"
    fi
}

# Main script
echo_step "Converting embedded repositories to submodules..."

# Convert public repositories
for repo in public/*/.git; do
    repo_path=$(dirname "$repo")
    convert_to_submodule "$repo_path"
done

# Convert private repositories (if any exist)
for repo in private/*/.git; do
    repo_path=$(dirname "$repo")
    convert_to_submodule "$repo_path"
done

echo_step "Committing changes..."
git add .
git commit -m "refactor: convert embedded repositories to submodules"

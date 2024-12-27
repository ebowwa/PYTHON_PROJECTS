#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo_step() {
    echo -e "${BLUE}$1${NC}"
}

# Function to handle a repository
handle_repo() {
    local repo_path=$1
    local repo_name=$(basename "$repo_path")
    
    if [ -d "$repo_path" ]; then
        echo_step "Processing $repo_path..."
        
        # Check if it's a git repository
        if [ -d "$repo_path/.git" ]; then
            # Get remote URL
            local remote_url=$(cd "$repo_path" && git config --get remote.origin.url)
            
            if [ ! -z "$remote_url" ]; then
                echo_step "Found remote URL: $remote_url"
                
                # Remove from git tracking
                git rm -rf --cached "$repo_path"
                rm -rf "$repo_path"
                
                # Add as submodule
                git submodule add "$remote_url" "$repo_path"
                echo -e "${GREEN}Successfully added $repo_path as submodule${NC}"
            else
                echo -e "${RED}No remote URL found for $repo_path${NC}"
            fi
        else
            echo -e "${RED}$repo_path is not a git repository${NC}"
        fi
    fi
}

# Main script
echo_step "Setting up monorepo..."

# Initialize git if needed
if [ ! -d ".git" ]; then
    git init
fi

# Create .gitmodules if it doesn't exist
if [ ! -f ".gitmodules" ]; then
    touch .gitmodules
fi

# Process public repositories
for repo in public/*; do
    if [ -d "$repo" ]; then
        handle_repo "$repo"
    fi
done

# Process private repositories
for repo in private/*; do
    if [ -d "$repo" ]; then
        handle_repo "$repo"
    fi
done

echo_step "Committing changes..."
git add .
git commit -m "refactor: set up monorepo with submodules"

echo -e "${GREEN}Monorepo setup complete!${NC}"

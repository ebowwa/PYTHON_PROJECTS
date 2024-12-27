#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo_step() {
    echo -e "${BLUE}$1${NC}"
}

# Function to initialize a repository
init_repo() {
    local repo_path=$1
    local repo_name=$(basename "$repo_path")
    
    if [ -d "$repo_path" ]; then
        echo_step "Initializing $repo_path..."
        
        # Navigate to repository
        cd "$repo_path"
        
        # Initialize git if not already initialized
        if [ ! -d ".git" ]; then
            git init
            
            # Add all files
            git add .
            
            # Initial commit
            git commit -m "Initial commit for $repo_name"
            
            # Create GitHub repository
            gh repo create "ebowwa/$repo_name" --public --source=. --remote=origin --push
            
            echo -e "${GREEN}Successfully initialized $repo_path${NC}"
        else
            echo -e "${RED}$repo_path is already a git repository${NC}"
        fi
        
        # Return to original directory
        cd - > /dev/null
    fi
}

# Main script
echo_step "Initializing repositories..."

# Process public repositories
for repo in public/*; do
    if [ -d "$repo" ]; then
        init_repo "$repo"
    fi
done

# Process private repositories
for repo in private/*; do
    if [ -d "$repo" ]; then
        init_repo "$repo"
    fi
done

echo -e "${GREEN}Repository initialization complete!${NC}"

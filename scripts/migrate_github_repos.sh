#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Base directory for repositories
BASE_DIR="/Users/ebowwa/PYTHON_PROJECTS"
PUBLIC_DIR="$BASE_DIR/public"
PRIVATE_DIR="$BASE_DIR/private"

# Function to check requirements
check_requirements() {
    echo -e "${BLUE}Checking requirements...${NC}"
    
    # Check for gh CLI
    if ! command -v gh &> /dev/null; then
        echo -e "${YELLOW}GitHub CLI not found. Installing...${NC}"
        brew install gh
    fi
    
    # Check for jq
    if ! command -v jq &> /dev/null; then
        echo -e "${YELLOW}jq not found. Installing...${NC}"
        brew install jq
    fi
    
    # Check GitHub authentication
    if ! gh auth status &> /dev/null; then
        echo -e "${RED}Please authenticate with GitHub first:${NC}"
        gh auth login
    fi
}

# Function to create directory structure
create_directories() {
    echo -e "${BLUE}Creating directory structure...${NC}"
    mkdir -p "$PUBLIC_DIR"
    mkdir -p "$PRIVATE_DIR"
}

# Function to detect Python repository
is_python_repo() {
    local repo_url=$1
    local temp_dir=$(mktemp -d)
    
    git clone --quiet "$repo_url" "$temp_dir" 2>/dev/null
    
    # Check for Python files or indicators
    if [ -f "$temp_dir/requirements.txt" ] || \
       [ -f "$temp_dir/setup.py" ] || \
       [ -f "$temp_dir/Pipfile" ] || \
       [ -f "$temp_dir/pyproject.toml" ] || \
       [ $(find "$temp_dir" -name "*.py" | wc -l) -gt 0 ]; then
        rm -rf "$temp_dir"
        return 0
    fi
    
    rm -rf "$temp_dir"
    return 1
}

# Function to migrate a repository
migrate_repository() {
    local repo_name=$1
    local is_private=$2
    local target_dir
    
    if [ "$is_private" = "true" ]; then
        target_dir="$PRIVATE_DIR/$repo_name"
    else
        target_dir="$PUBLIC_DIR/$repo_name"
    fi
    
    echo -e "${BLUE}Migrating repository: $repo_name${NC}"
    
    # Clone repository with all history
    if [ -d "$target_dir" ]; then
        echo -e "${YELLOW}Repository already exists in $target_dir, updating...${NC}"
        cd "$target_dir"
        git pull
    else
        echo -e "${GREEN}Cloning $repo_name...${NC}"
        git clone "https://github.com/ebowwa/$repo_name.git" "$target_dir"
    fi
    
    # Set up GPG encryption for private repositories
    if [ "$is_private" = "true" ]; then
        cd "$target_dir"
        echo -e "${BLUE}Setting up GPG encryption for $repo_name...${NC}"
        
        # Create .gitattributes if it doesn't exist
        if [ ! -f .gitattributes ]; then
            echo "*.secret filter=git-crypt diff=git-crypt" > .gitattributes
            echo "*.env filter=git-crypt diff=git-crypt" >> .gitattributes
            echo "*.key filter=git-crypt diff=git-crypt" >> .gitattributes
            git add .gitattributes
            git commit -m "Add .gitattributes for encryption"
        fi
    fi
}

# Function to fetch and migrate all Python repositories
fetch_and_migrate_repos() {
    echo -e "${BLUE}Fetching repositories...${NC}"
    
    # Get all repositories
    gh repo list ebowwa --json name,isPrivate,url -L 1000 | \
    jq -c '.[]' | while read -r repo; do
        name=$(echo $repo | jq -r '.name')
        is_private=$(echo $repo | jq -r '.isPrivate')
        url=$(echo $repo | jq -r '.url')
        
        # Check if it's a Python repository
        if is_python_repo "$url"; then
            migrate_repository "$name" "$is_private"
        fi
    done
}

# Function to generate repository report
generate_report() {
    echo -e "${BLUE}Generating repository report...${NC}"
    echo -e "${GREEN}Public Python repositories:${NC}"
    ls -1 "$PUBLIC_DIR"
    echo -e "\n${YELLOW}Private Python repositories:${NC}"
    ls -1 "$PRIVATE_DIR"
}

# Main execution
echo -e "${BLUE}Starting GitHub Python repositories migration...${NC}"

check_requirements
create_directories
fetch_and_migrate_repos
generate_report

echo -e "${GREEN}Migration complete!${NC}"

#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get user email from git config
EMAIL=$(git config user.email)
NAME=$(git config user.name)

if [ -z "$EMAIL" ] || [ -z "$NAME" ]; then
    echo -e "${RED}Error: Git user email or name not configured${NC}"
    exit 1
fi

# Create GPG key generation configuration
cat > /tmp/gpg-gen-key << EOF
%echo Generating GPG key
Key-Type: RSA
Key-Length: 4096
Name-Real: $NAME
Name-Email: $EMAIL
Expire-Date: 0
%no-protection
%commit
%echo Done
EOF

# Generate GPG key
echo -e "${BLUE}Generating GPG key for $EMAIL...${NC}"
gpg --batch --generate-key /tmp/gpg-gen-key

# Clean up
rm /tmp/gpg-gen-key

# List the generated key
echo -e "${GREEN}Generated GPG key:${NC}"
gpg --list-secret-keys --keyid-format LONG

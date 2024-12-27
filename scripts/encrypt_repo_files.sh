#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to check if GPG is installed
check_gpg() {
    if ! command -v gpg &> /dev/null; then
        echo -e "${RED}GPG is not installed. Installing via Homebrew...${NC}"
        brew install gnupg
    else
        echo -e "${GREEN}GPG is already installed${NC}"
    fi
}

# Function to check for existing GPG keys
check_gpg_keys() {
    if ! gpg --list-secret-keys --keyid-format LONG | grep -q "sec"; then
        echo -e "${BLUE}No GPG keys found. Generating new key...${NC}"
        generate_gpg_key
    else
        echo -e "${GREEN}GPG keys found${NC}"
        gpg --list-secret-keys --keyid-format LONG
    fi
}

# Function to generate GPG key
generate_gpg_key() {
    echo -e "${BLUE}Generating GPG key...${NC}"
    gpg --full-generate-key
}

# Function to encrypt a file
encrypt_file() {
    local file=$1
    local recipient=$2
    
    if [ ! -f "$file" ]; then
        echo -e "${RED}File not found: $file${NC}"
        return 1
    fi
    
    echo -e "${BLUE}Encrypting $file...${NC}"
    gpg --output "${file}.gpg" --encrypt --recipient "$recipient" "$file"
    echo -e "${GREEN}Encrypted $file to ${file}.gpg${NC}"
}

# Function to decrypt a file
decrypt_file() {
    local encrypted_file=$1
    
    if [ ! -f "$encrypted_file" ]; then
        echo -e "${RED}Encrypted file not found: $encrypted_file${NC}"
        return 1
    fi
    
    local output_file=${encrypted_file%.gpg}
    echo -e "${BLUE}Decrypting $encrypted_file...${NC}"
    gpg --output "$output_file" --decrypt "$encrypted_file"
    echo -e "${GREEN}Decrypted $encrypted_file to $output_file${NC}"
}

# Function to encrypt all files in a directory matching pattern
encrypt_directory() {
    local dir=$1
    local pattern=$2
    local recipient=$3
    
    echo -e "${BLUE}Encrypting files in $dir matching pattern $pattern${NC}"
    find "$dir" -type f -name "$pattern" -not -name "*.gpg" | while read -r file; do
        encrypt_file "$file" "$recipient"
    done
}

# Main script
case "$1" in
    "check")
        check_gpg
        check_gpg_keys
        ;;
    "encrypt")
        if [ "$#" -lt 3 ]; then
            echo "Usage: $0 encrypt <file/directory> <recipient> [pattern]"
            exit 1
        fi
        if [ -f "$2" ]; then
            encrypt_file "$2" "$3"
        elif [ -d "$2" ]; then
            pattern=${4:-"*"}  # Use provided pattern or default to all files
            encrypt_directory "$2" "$pattern" "$3"
        else
            echo -e "${RED}Invalid file or directory: $2${NC}"
        fi
        ;;
    "decrypt")
        if [ "$#" -ne 2 ]; then
            echo "Usage: $0 decrypt <encrypted_file>"
            exit 1
        fi
        decrypt_file "$2"
        ;;
    *)
        echo "Usage: $0 {check|encrypt|decrypt} [file/directory] [recipient] [pattern]"
        echo "Commands:"
        echo "  check                     - Check GPG installation and keys"
        echo "  encrypt <file> <recipient> - Encrypt a single file"
        echo "  encrypt <dir> <recipient> [pattern] - Encrypt files in directory matching pattern"
        echo "  decrypt <file>            - Decrypt an encrypted file"
        exit 1
        ;;
esac

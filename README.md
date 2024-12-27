# PYTHON_PROJECTS

A consolidated monorepo containing my development history and projects, organized and cleaned up for better maintainability.

## Repository Structure

- `private/`: Private repositories and sensitive data (encrypted)
- `public/`: Public repositories and open-source projects
- `scripts/`: Utility scripts for repository management
  - `encrypt_repo_files.sh`: Handles encryption of sensitive files
  - `git_smart.sh`: Smart git operations with automated commit messages
  - `setup_gpg.sh`: Sets up GPG keys for secure operations
  - `setup_submodules.sh`: Converts embedded repositories to git submodules

## Security

This repository uses GPG encryption for sensitive files. All files in the `private/` directory are automatically encrypted before being committed.

## Getting Started

1. Clone the repository
2. Run `./scripts/setup_gpg.sh` to set up GPG keys
3. Run `./scripts/setup_submodules.sh` to initialize submodules

## Contributing

This is a personal monorepo for tracking development history. Pull requests are not accepted.

## License

All rights reserved unless otherwise specified in individual project directories.

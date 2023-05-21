# CodebaseCraft.ai

CodebaseCraft.ai is an autonomous codebase Command-Line Interface (CLI) tool designed to simplify and automate your codebase management tasks. With this tool, you can easily handle codebase templating, setup, workflow management, autonomous codebase enhancement, and codebase contextualization.

## What I've Learned (so far)
1. Creating python CLI tools
2. Extensive logging and terminal ux using Rich and Typer
3. GPT-4 API integration for generating directory templates from scanned directory structure
4. Codebase scanning to extract metadata, codebase metrics, and directory structure using python
5. Codebase setup automation for the following tasks:
   - Setting up a codebase directory structure
   - Setting up environment: 
      - Checking system-level dependencies, like versions of programming languages and package managers, etc
      - Setting up virtual environment (python)
   - Installing dependencies using pip, npm, and yarn
   - Setting up configuration files: 
      - Setting up linting and formatting
      - Configuring setup files: setup.py and package.json
      - Automating PostgreSQL relational and Milvus vector database setups using NexusDb.
   - Setting Up Version Control
      - Remote and Local Git Repo Initialization
      - Initial Commit
      - Setting up branch structure
   - Running initial builds
   - Setting up and running the initial test suite
   - Setting up CI/CD pipelines


   

## Features

### MVP Features
1. **Codebase Templating**: 
   - Codebase Scanning: Scan your existing codebase to understand its structure and dependencies.
   - Template Management: Manage and apply templates to automate codebase creation and modifications.

2. **Codebase Setup**: 
   - Directory Setup: Easily set up your project directory structure.
   - Repo Setup: Initialize and manage your Git repositories.
   - Dependency Management: Handle your project dependencies in a systematic way.
   - Project Configuration: Manage your project configuration settings.
   - Boilerplate Management: Manage and apply boilerplate code to speed up development.
   - Deployment Scripts: Generate and manage deployment scripts to streamline your deployment process.

3. **Workflow Management**:
   - Version Control Management: Automate version control tasks with Git.
   - Testing Suite Management: Manage your testing suites and automate testing tasks.

### Codebase Enhancement
- **Modification Suggestions**: Suggest modifications to improve your codebase.

### Codebase Contextualization
1. **AST Management**: Create and use Abstract Syntax Trees (ASTs) for codebase analysis.
2. **Directory Contextualization**: Use ASTs and codebase scanning to simplify the directory structure to its essentials and contextualize the directory tree in relation to the project setup.
3. **File Contextualization**: Use ASTs and their nearest neighbor in terms of imports to contextualize files and store the context in a summary.
4. **Directory-File Contextualization**: Use directory and file contextualization AST summaries to relate directories and files across the entire codebase and summarize the context to an input.

## Tools
CodebaseCraft.ai uses various technologies including Python, Typer, Rich, GPT API, and possibly Langchain.

## How to Use
Instructions on how to use this tool will be added as the project develops.

## Contributing
If you're interested in contributing, please follow the guidelines provided in the CONTRIBUTING.md file.

## License
This project is licensed under the terms of the MIT License. Please see the LICENSE file for details.


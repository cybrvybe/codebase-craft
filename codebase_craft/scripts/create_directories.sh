#!/bin/bash

# Get the project name from the command line arguments
project_name=$1

# Create the directories
mkdir -p ../${project_name}/src/components
mkdir -p ../${project_name}/src/utils
mkdir -p ../${project_name}/public
mkdir -p ../${project_name}/tests

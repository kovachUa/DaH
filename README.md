# Docker Project for Storing and Loading Git and Websites

This repository contains a Docker project designed for convenient storage and loading of Git repositories and websites. Utilizing Docker enables easy identification and isolation of all necessary dependencies, making the workflow more predictable and simplifying deployment.

## Repository Structure

The repository includes the following files and directories:

- `./data/mirror{git/site}`: Directories for storing mirrors of Git repositories and websites.
- `./data/json{git/site}`: JSON files containing links to Git repositories and websites in JSON format.

## Link Format

The following formats are used for entering links:

- For organization Git repositories: `https://github.com/repos`
- For websites: `https://site.si`

## Usage Instructions

1. Install Docker on your computer if it's not already installed.
2. Clone this repository to your computer.
3. In the terminal, navigate to the repository directory.
4. Launch the Docker container using the `docker-compose up` command.
5. After launching, the web server will be accessible at `http://127.0.0.1:9000`.

## Limitations

Currently, the project only supports working with websites through the Firefox browser.

This project enhances the process of storing and loading Git repositories and websites, making it more convenient and predictable by leveraging Docker containers.

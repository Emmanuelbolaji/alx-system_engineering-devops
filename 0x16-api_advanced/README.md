# 0x16. API Advanced

This directory contains Python scripts that demonstrate advanced API handling, including fetching data from APIs, sorting data, and handling paginated responses.

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Libraries imported in your Python files must be organized in alphabetical order
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (e.g., `python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use the Requests module for sending HTTP requests to the Reddit API

## Files
- `0-subs.py`: Contains the function to fetch the number of subscribers for a given subreddit.
- `0-main.py`: Script to test the function via command line arguments.
- `1-top_ten.py`: Contains the function to fetch and print the titles of the first 10 hot posts for a given subreddit.
- `1-main.py`: Script to test the function via command line arguments.

## Usage
Make sure the script is executable and run it as follows:

```sh
./0-subs.py
./0-main.py <subreddit>
./1-top_ten.py
./1-main.py <subreddit>

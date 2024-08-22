# Web Stack Debugging #4

## Overview
This project is part of the Web Stack Debugging series, focusing on optimizing and fixing web server configurations under high load conditions. In this specific task, we address issues with an Nginx web server that's failing to handle a large number of requests efficiently.

## Files
- `0-the_sky_is_the_limit_not.pp`: Puppet manifest to fix the Nginx configuration and improve its performance under high load.

## Task 0: Sky is the limit, let's bring that limit higher

### Problem
The Nginx web server is failing to handle a high number of requests, resulting in numerous failed requests during a benchmarking test using ApacheBench (ab).

### Solution
We use Puppet to automate the fix for this issue. The manifest file `0-the_sky_is_the_limit_not.pp` includes the necessary configuration changes to optimize Nginx for handling a higher number of concurrent requests.

### Before Fix
- Failed requests: 943 out of 2000
- Requests per second: 5664.01

### After Fix
- Failed requests: 0 out of 2000
- Requests per second: 6650.99

## Usage
To apply the fix:

1. Ensure Puppet is installed on your system.
2. Run the following command:

## Testing
You can test the server's performance using ApacheBench:

## Note
Always test configuration changes in a safe, non-production environment before applying them to live servers.

## Repository
- GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- Directory: 0x1B-web_stack_debugging_4

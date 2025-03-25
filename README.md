# go2web: Command-Line Web Fetching and Search Tool

## Overview
`go2web` is a powerful command-line tool for making HTTP requests, searching the web, and fetching web content with advanced features like caching and content negotiation.

## Features
- HTTP requests to specified URLs
- Web search using DuckDuckGo
- Content negotiation (JSON/HTML)
- HTTP caching mechanism
- Redirect handling
- Clean, human-readable output

## Requirements
- Python 3.7+
- Standard Python libraries (no external HTTP libraries)

## Installation
1. Clone the repository
2. Ensure you have Python 3.7+ installed
3. Make the script executable:
   ```bash
   chmod +x go2web.py
   ```

## Usage
### Fetch URL Content
    python go2web.py -u https://example.com
- Retrieves and displays human-readable content from the specified URL
- Removes HTML tags and formatting

### Web Search
    python go2web.py -s "python programming"
- Searches DuckDuckGo for the given term
- Displays top 10 search results with titles and URLs

### Open Search Result
    python go2web.py -o 1
- Opens the first result from the previous search
- Fetches and displays the content of the selected URL

### Help
    python go2web.py -h
- Displays help and available options

## Advanced Options
- `--json`: Request JSON content
- `--html`: Request HTML content
- `no-cache`: Disable response caching

## Caching
- Responses are automatically cached for 1 hour
- Cached responses speed up repeated requests
- Cache can be disabled with `--no-cache`

## Content Negotiation
- Supports both JSON and HTML content types
- Use `--json` or `--html` to specify preferred format

## Technical Details
- Uses raw socket programming
- Implements custom HTTP client
- No third-party HTTP request libraries
- Handles redirects and content extraction

## Limitations
- Works best with text-based content
- Limited support for complex web pages
- Relies on HTML parsing heuristics

## Demo
![Demo](DemoGif5.gif)
#!/usr/bin/env python
import argparse
import sys
import os


def create_parser():
    """Create command line argument parser"""
    parser = argparse.ArgumentParser(prog='go2web', description='Web request and search tool')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u', '--url', help='Make an HTTP request to the specified URL')
    group.add_argument('-s', '--search', help='Search the term using DuckDuckGo and print top 10 results')
    group.add_argument('-o', '--open', type=int, help='Open the specified search result')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    # Store last search results for -o option
    last_search_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.last_search')

    if args.url:
        print("URL functionality not implemented yet.")
    elif args.search:
        print("Search functionality not implemented yet.")
    elif args.open is not None:
        print("Open functionality not implemented yet.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
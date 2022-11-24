#!/usr/bin/python

import argparse


parser = argparse.ArgumentParser(description="Generate usernames using python")
parser.add_argument(
    '-w', '--wordlist', help="Specify wordlist with first and last name")   

args = parser.parse_args()

wordlist_name = args.wordlist

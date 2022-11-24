#!/usr/bin/python

import argparse


parser = argparse.ArgumentParser(description="Generate usernames using python")
parser.add_argument(
    '-w', '--wordlist', help="Specify wordlist with first and last name")

args = parser.parse_args()

wordlist_name = args.wordlist

names = []

with open(f"{wordlist_name}") as file:
    for line in file.readlines():
        names.append(line.rstrip("\n"))


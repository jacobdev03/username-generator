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

def generate_usernames():
    first_last = []
    first_last_upper = []
    for n in names:
        first_last.append(n.lower().split())
        first_last_upper.append(n.upper().split())
        

    for name in first_last:
        print(name[0])
        print(name[1])
        print(f"{name[0]}{name[1]}")
        print(f"{name[1]}{name[0]}")
        print(f"{name[0]}-{name[1]}")
        print(f"{name[0]}.{name[1]}")
        print(f"{name[0]}_{name[1]}")
        print(f"{name[0]}+{name[1]}")
        print(f"{name[0][0]}{name[1]}")
        print(f"{name[0][0]}-{name[1]}")
        print(f"{name[0][0]}.{name[1]}")
        print(f"{name[0][0]}_{name[1]}")
        print(f"{name[0][0]}+{name[1]}")


    print("---------UPPERCASE-----------")    


    for name in first_last_upper:
        print(name[0])
        print(name[1])
        print(f"{name[0]}{name[1]}")
        print(f"{name[1]}{name[0]}")
        print(f"{name[0]}-{name[1]}")
        print(f"{name[0]}.{name[1]}")
        print(f"{name[0]}_{name[1]}")
        print(f"{name[0]}+{name[1]}")
        print(f"{name[0][0]}{name[1]}")
        print(f"{name[0][0]}-{name[1]}")
        print(f"{name[0][0]}.{name[1]}")
        print(f"{name[0][0]}_{name[1]}")
        print(f"{name[0][0]}+{name[1]}")


generate_usernames()
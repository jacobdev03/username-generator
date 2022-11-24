# username-generator
Username generator script written in python

# Usage
```
python generate.py -w [your wordlist here]
python3 generate.py -w [your wordlist here]

usage: generate.py [-h] [-w WORDLIST]

Generate usernames using python

options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Specify wordlist with first and last name
```

# Example 

```
python generate.py -w test_wordlist.txt

john
doe
johndoe
doejohn
john-doe
john.doe
john_doe
john+doe
jdoe
j-doe
j.doe
j_doe
j+doe
---------UPPERCASE-----------
JOHN
DOE
JOHNDOE
DOEJOHN
JOHN-DOE
JOHN.DOE
JOHN_DOE
JOHN+DOE
JDOE
J-DOE
J.DOE
J_DOE
J+DOE

```

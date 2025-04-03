import webbrowser
from pathlib import Path
import random

"""
This Python Script contains a database of links for all completed LeetCode Questions so far on 
the AlgoMap.io List.

The purpose of this script is to be run everyday in order to practice random problems that I have
already completed for the sake of revision.
"""

# Python Dictionary of All Completed Problems:
LinkDict = {}

# Iterate through all Files in the current directory:
base_dir = Path(__file__).parent
current_file = Path(__file__).resolve()

# Recursively go through all files under that directory
for file in base_dir.rglob('*.py'):
    if file.is_file() and file.resolve() != current_file:
        try:
            with file.open('r', encoding='utf-8') as f:
                lines = f.readlines()
                if len(lines) >= 4:
                    LinkDict[file.name] = lines[3].strip()
        except Exception as e:
            print(f"{file.name} → Error reading file: {e}")



while True:
    user_input = input("Press 'Enter' for Random Problem, or 'q' to quit: ")
    if user_input.lower() == 'q':
        print("Quitting!")
        exit()
    else:
        key = random.choice(list(LinkDict.keys()))
        url = LinkDict[key]
        print("Solving Problem: ", key)
        webbrowser.open(url)




import webbrowser
from pathlib import Path

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

# Recursively go through all files under that directory
for file in base_dir.rglob('*.py'):
    if file.is_file():
        try:
            with file.open('r', encoding='utf-8') as f:
                lines = f.readlines()
                if len(lines) >= 4:
                    LinkDict[file.name] = lines[3].strip()
        except Exception as e:
            print(f"{file.name} → Error reading file: {e}")


print(LinkDict)





# url = "https://leetcode.com/problems/roman-to-integer/"
# webbrowser.open(url)
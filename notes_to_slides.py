#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1], 'r') as notes_file:
    notes = notes_file.readlines()

mode = []
section = None
for line in notes:
    line = line.rstrip()
    if len(mode) > 0 and mode[-1][0] == "*" and (line.strip().startswith(mode[-1]) or line.strip() == ""):
        mode.pop()
    if line.startswith('## '):
        if len(mode) > 0:
            mode.pop()
        if "Announcements" in line:
            section = "Announcements"
            mode.append("all")
            print(line)
        elif "Outline" in line:
            section = "Outline"
            mode.append("all")
            print(line)
        elif "Warm-up" in line:
            section = "Warm-up"
            mode.append("questions")
            print(line)
        else:
            section = line.strip('# ')
            mode.append("questions")
            print('\n<div style="page-break-after: always;"></div>\n')
            print(line)
    elif len(mode) > 0 and mode[-1] == "all":
        print(line)
    elif len(mode) > 0 and mode[-1] == "questions":
        match = re.search("\* Q\d+:", line)
        if match:
            print('\n<div style="page-break-after: always;"></div>\n')
            print(match.group(0).replace('*', '##'))
            level = line.strip()
            level = level[:level.index(' ')+1]
            mode.append(level)
    elif len(mode) > 0 and mode[-1][0] == "*":
        print(line)

        

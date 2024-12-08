import re

file = open("input.txt")

parse_re = r'mul\((\d{1,3}),(\d{1,3})\)'

computers_mem = file.readlines()

total = 0
for line in computers_mem:
    all_matches = re.finditer(parse_re, line)

    for match in all_matches:
        x1 = int(match.group(1))
        x2 = int(match.group(2))
        total += x1 * x2
            
print(total)
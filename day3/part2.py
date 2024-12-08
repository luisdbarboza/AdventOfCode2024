import re

file = open("input.txt")

mul_re = r'mul\((\d{1,3}),(\d{1,3})\)'
do_re = r'do\(\)'
dont_re = r'don\'t\(\)'

file_content = file.readlines()

file_content = ''.join(file_content)
file_content = file_content.replace("\n", "")

total = 0

next_do_match = re.search(do_re, file_content)
next_dont_match = re.search(dont_re, file_content)

current_state = "DO"

def perform_code_operations():
    global file_content
    global total
    global current_state

    if current_state == "DO":
        next_dont_match = re.search(dont_re, file_content)

        if next_dont_match:
            stop_index = next_dont_match.span()[0]
            matches = list(re.finditer(mul_re, file_content[0:stop_index]))
            file_content = file_content[stop_index:]
        else:
            matches = list(re.finditer(mul_re, file_content[0:]))
            file_content = ""

        for match in matches:
            x1 = int(match.group(1))
            x2 = int(match.group(2))
            total += x1 * x2

        current_state = "DONT"
    else:
        next_do_match = re.search(do_re, file_content)
        
        if next_do_match:
            stop_index = next_do_match.span()[0]
            file_content = file_content[stop_index:]
            current_state = "DO"
        else:
            file_content = ""
        
while len(file_content) > 0:
    perform_code_operations()
            
print(total)
import re

file = open("input.txt", "r")

file_lines = file.readlines()

number_of_lines = len(file_lines)

top_row_regex = r'(?=(?:(M.M)|(M.S)|(S.S)|(S.M)))'

counter = 0

for line_index in range(number_of_lines):
    line = file_lines[line_index]

    if line_index <= (number_of_lines - 3):
        matches = list(re.finditer(top_row_regex, line))

        parsed_matches = []
        for match in matches:
            obj = {"match": line[match.span()[0]:match.span()[0] + 3], "indexes": [match.span()[0], match.span()[0] + 3]}
            parsed_matches.append(obj)

        for match in parsed_matches:
            if (line_index) <= ((number_of_lines - 1) - 2):
                bottom_line = file_lines[line_index + 2]

                top_line_match = match["match"]
                middle_point = file_lines[line_index + 1][match["indexes"][0] + 1]
                bottom_line_match = bottom_line[match["indexes"][0]:match["indexes"][1]]

                first_requirement = (top_line_match[0] == "M" and bottom_line_match[2] == "S") or (top_line_match[0] == "S" and bottom_line_match[2] == "M")
                second_requirement = middle_point == "A"
                third_requirement = (bottom_line_match[0] == "M" and top_line_match[2] == "S") or (bottom_line_match[0] == "S" and top_line_match[2] == "M")
                
                if first_requirement and second_requirement and third_requirement:
                    # print(f"line: {line_index + 1}\n{top_line_match}\n {middle_point} \n{bottom_line_match}")
                    counter += 1

print(counter)
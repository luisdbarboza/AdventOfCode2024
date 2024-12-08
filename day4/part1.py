import re

file = open("input.txt", "r")

counter = 0

xmas_regex = r'XMAS'

lines_matrix = []
diagonal_matrix = []
diagonal_matrix_backwards = []

for line in file.readlines():
    lineRow = []
    for letter in line:
        lineRow.append(letter)

    lines_matrix.append(lineRow)

def get_horizontal_count(lines_matrix):
    global counter

    for row in lines_matrix:
        line = "".join(row)

        backwards = line[::-1]

        matches = list(re.findall(xmas_regex, line))

        counter += len(matches)

        matches = list(re.findall(xmas_regex, backwards))

        counter += len(matches)

def get_vertical_count(lines_matrix):
    global counter

    matrix_columns = len(lines_matrix[0]) - 1
    matrix_rows = len(lines_matrix)

    for column in range(matrix_columns):
        line = ""
        for row in range(matrix_rows):
            line += lines_matrix[row][column]
        
        matches = list(re.findall(xmas_regex, line))

        counter += len(matches)

    for column in range(matrix_columns):
        line = ""
        
        for row in range(matrix_rows - 1, -1, -1):
            line += lines_matrix[row][column]

        matches = list(re.findall(xmas_regex, line))

        counter += len(matches)

def diagonal_traversal():
    global diagonal_matrix
    
    matrix_columns = len(lines_matrix[0]) - 1
    matrix_rows = len(lines_matrix)

    #Traverse first half of the matrix
    for row_index in range(matrix_rows):
        line = ""

        accum = 0
        for rows_left in range(row_index, -1 ,-1):
            line += lines_matrix[row_index - accum][accum]
            accum += 1

        diagonal_matrix.append(line)
        
    #Traverse second half of the matrix
    for column_index in range(1, matrix_columns):
        line = ""

        accum = 0
        for rows_left in range(matrix_rows - 1, -1 ,-1):
            if (column_index + accum) < matrix_columns:
                line += lines_matrix[rows_left][column_index + accum]
                accum += 1

        diagonal_matrix.append(line)

def diagonal_traversal_backwards():
    global diagonal_matrix_backwards

    matrix_columns = len(lines_matrix[0]) - 1
    matrix_rows = len(lines_matrix)

    #Traverse first half of the matrix
    for row_index in range(matrix_rows):
        line = ""

        accum = 0
        for rows_left in range(row_index, -1 ,-1):
            line += lines_matrix[row_index - accum][(matrix_columns - 1) - accum]
            accum += 1

        diagonal_matrix_backwards.append(line)
        

    #Traverse second half of the matrix
    for column_index in range(matrix_columns - 2, -1, -1):
        line = ""

        accum = 0
        for rows_left in range(matrix_rows - 1, -1 ,-1):
            if (column_index - accum) > -1:
                line += lines_matrix[rows_left][column_index - accum]
                accum += 1

        diagonal_matrix_backwards.append(line)

diagonal_traversal()
diagonal_traversal_backwards()

get_horizontal_count(lines_matrix)
get_vertical_count(lines_matrix)
get_horizontal_count(diagonal_matrix)
get_horizontal_count(diagonal_matrix_backwards)

print(counter)
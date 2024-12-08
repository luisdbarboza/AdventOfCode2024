file = open("input.txt", "r")

safe_reports_counter = 0

for report in file.readlines():
    levels = report.split(" ")

    unsafe = False
    order = None

    max_differ_length = 3
    min_differ_length = 1

    previous_level = None

    for level in levels:
        level = int(level)

        if previous_level == None:
            previous_level = level
            continue

        if previous_level != None and order == None:
            diff = level - previous_level

            if abs(diff) > max_differ_length or abs(diff) < min_differ_length:
                unsafe = True
                break

            if diff > 0:
                order = "ASC"
            else:
                order = "DESC"


        if previous_level != None and order != None:
            diff = level - previous_level

            if abs(diff) > max_differ_length or abs(diff) < min_differ_length:
                unsafe = True
                break
            
            if order == "ASC" and diff < 0:
                unsafe = True
                break
            elif order == "DESC" and diff > 0:
                unsafe = True
                break

            previous_level = level


    if unsafe == True:
        order = None
        previous_level = None
        unsafe = False
        continue
    else:
        safe_reports_counter+= 1

file.close()

print(safe_reports_counter)
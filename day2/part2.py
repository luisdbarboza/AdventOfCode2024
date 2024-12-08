file = open("input.txt", "r")

safe_reports_counter = 0

def is_full_sequence_safe(levels):
    order = None
    safe_report = False
    report_length = len(levels)

    for index in range(report_length - 1):
        level = int(levels[index])
        next_level = int(levels[index + 1])

        diff = abs(level - next_level)
        signed_diff = level - next_level

        #Check if neighbor is in range
        if diff <= 3 and diff >= 1:
            #Check if sequence order is correct
            if order == None:
                if signed_diff > 0:
                    order = "DESC"
                elif signed_diff < 0:
                    order = "ASC"
                else:
                    safe_report = False
                    break
            else:
                if (order == "ASC" and signed_diff > 0) or (order == "DESC" and signed_diff < 0) or signed_diff == 0:
                    safe_report = False
                    break

            
            safe_report = True
        else:
            safe_report = False
            break

    return safe_report


for report in file.readlines():
    levels = report.split(" ")
    report_length = len(levels)
    safe_report = False

    #Full pass through
    safe_report = is_full_sequence_safe(levels)

    #Partial pass through
    if safe_report == False:
        for index in range(report_length):
            filtered_levels = [levels[index2] for index2 in range(report_length) if index2 != index]

            if is_full_sequence_safe(filtered_levels):
                safe_report = True
                break
    
    if safe_report == True:
        safe_reports_counter += 1

file.close()

print(safe_reports_counter)
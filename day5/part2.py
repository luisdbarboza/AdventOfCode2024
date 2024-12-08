import re

file = open("input.txt", "r")

scanning_ordering_rules = True
page_order_hash = {}

#75: {47: BEFORE, 61: BEFORE, 53: BEFORE, 29: BEFORE}
#47: {75: AFTER, 61: BEFORE, 53: BEFORE, 29: BEFORE}

order_rule_regex = r'(\d+)\|(\d+)'

correct_print_sum = 0

incorrect_updates = []

line_index = 0
for line in file.readlines():
    if len(line.strip()) == 0:
        scanning_ordering_rules = False
        continue

    if scanning_ordering_rules == True:
        match = re.search(order_rule_regex, line)

        first_page = match.group(1)
        second_page = match.group(2)

        if not(first_page in page_order_hash):
            page_order_hash[first_page] = {}

        page_order_hash[first_page][second_page] = "BEFORE"
        
        if not(second_page in page_order_hash):
            page_order_hash[second_page] = {}
        
        page_order_hash[second_page][first_page] = "AFTER"
    else:
        pages = line.split(",")
        pages[-1] = pages[-1][:-1] if pages[-1][-1] == "\n" else pages[-1]

        should_print_update = True

        pages_ordered_by_number_of_updated_pages_after_it = {"length": len(pages)}

        for page1_index in range(len(pages)):
            is_page_in_correct_order = True
            page1 = pages[page1_index]

            page1_after_counter = 0

            for page2_index in range(len(pages)):
                page2 = pages[page2_index]

                if page1_index == page2_index:
                    continue

                if page_order_hash[page1][page2] == "BEFORE":
                    page1_after_counter += 1

                if should_print_update:
                    if (page1_index < page2_index and page_order_hash[page1][page2] == "BEFORE") or (page1_index > page2_index and page_order_hash[page1][page2] == "AFTER"):
                        continue
                    else:
                        should_print_update = False
            
            pages_ordered_by_number_of_updated_pages_after_it[page1_after_counter] = page1

        if should_print_update == False:
            incorrect_updates.append(pages_ordered_by_number_of_updated_pages_after_it)

        line_index += 1
    

for pages in incorrect_updates:
    ordered_pages = []

    for page_index in range(pages["length"]):
        ordered_pages.append(pages[page_index])

    middle_point = len(ordered_pages) // 2

    correct_print_sum += int(ordered_pages[middle_point])

print(correct_print_sum)
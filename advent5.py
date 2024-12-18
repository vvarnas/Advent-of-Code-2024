import numpy as np
with open(r"/Users/varnas/Desktop/vscode/input5") as file:
    data_something = file.read()


sample_rules_and_pages = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

#Part 1
def seperate_rules_pages(data):
    parts = data.split('\n\n')
    rules_dat = parts[0]       
    pages_dat = parts[1]
    return rules_dat, pages_dat

rules, pages = seperate_rules_pages(data_something)

#Sequentialise rules
def number_rule(numx):
    first_page = []
    following_page = []
    rules_data = rules.split('\n')
    for rule_x in rules_data:
        a, b = rule_x.split('|')
        if a == str(numx):
            first_page.append(a)
            following_page.append(b)
    return first_page, following_page

#Pass row through rules
def row_rules_checker(a_row):
    row_len = len(a_row)
    passed_nums = 0
    for i in range(0, row_len):
        number = a_row[i]
        rest_row = a_row[i+1:]
        valid_next_pages = number_rule(number)[1]
        #check_commons
        if len(rest_row) !=0:
            rest_row = a_row[i+1:]
            # Check for intersections between the rest_row and valid_next_pages
            if all(page in valid_next_pages for page in rest_row):
                passed_nums +=1
            else:
                break
    if row_len-1 == passed_nums:
        return a_row

#Sequentialise pages rows
pages_data = pages.split('\n')
correct_rows = []
for page in pages_data:
    nums_row = (page.split(','))
    passed_row = row_rules_checker(nums_row)
    if passed_row:
        correct_rows.append(passed_row)

middle_sum = 0
for correct_row in correct_rows:
    row_size = len(correct_row)
    if row_size != 0:
        ind = int((row_size-1)/2)
        if ind != 0:
            middle_number = (correct_row[ind])
            middle_sum += int(middle_number)

print(f"Middle numbers sum: {middle_sum}")

#Part 2:
incorrect_rows = []
for page_x in pages_data:
    if page_x.split(',') not in correct_rows:
        incorrect_rows.append(page_x)

def row_rules_fixer(a_row):
    row_len = len(a_row)
    for i in range(0, (row_len)-1):
        a, b = a_row[i], a_row[i+1]
        following_pages = number_rule(a)[1]
        if str(b) not in following_pages:
            a_row[i], a_row[i+1] = a_row[i+1], a_row[i]
    return a_row

new_correct_rows = []
for incorrect_row in incorrect_rows:
    row_fix = incorrect_row.split(',')
    new_correct_row = row_rules_fixer(row_rules_fixer(row_rules_fixer(row_fix)))
    new_correct_row = row_rules_fixer(row_rules_fixer(row_rules_fixer(new_correct_row)))
    new_correct_row = row_rules_fixer(row_rules_fixer(row_rules_fixer(new_correct_row)))
    new_correct_row = row_rules_fixer(row_rules_fixer(row_rules_fixer(new_correct_row)))
    new_correct_rows.append(new_correct_row)

new_middle_sum = 0
for new_correct_row in new_correct_rows:
    row_size = len(new_correct_row)
    if row_size != 0:
        ind = int((row_size-1)/2)
        if ind != 0:
            new_middle_number = (new_correct_row[ind])
            new_middle_sum += int(new_middle_number)
print(f"New middle numbers sum: {new_middle_sum}")
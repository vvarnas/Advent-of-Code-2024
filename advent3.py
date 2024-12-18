import re
test_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5)do()mul(1,1)don't()don't()mul(1, 2))"

with open("/Users/varnas/Desktop/vscode/input3.txt", "r") as file:
    data = file.read()

#Part 1
def remove_intervals_between_b_and_c(arr):
    result = []
    skip = False 
    for item in arr:
        if item[0] == "don't":
            skip = True
        if not skip:
            result.append(item)
        if item[0] == "do" and skip:
            skip = False
    return result

def pair_product_format(sample_string):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mul_matches = [
        (match.start(), 'mul', match.group())
        for match in re.finditer(mul_pattern, sample_string)
    ]
    do_matches = [
        (match.start(), 'do', match.group())
        for match in re.finditer(do_pattern, sample_string)
    ]
    dont_matches = [
        (match.start(), "don't", match.group())
        for match in re.finditer(dont_pattern, sample_string)
    ]
    
    logic_array = mul_matches + do_matches + dont_matches
    
    logic_array.sort(key=lambda x: x[0])
    
    # Return the logic array without the start index
    return [item[1:] for item in logic_array]

our_list = pair_product_format(data)

total_sum = 0
for item in our_list:
    match = re.match(r"mul\((\d+),(\d+)\)", item[1])
    if match:
        X = int(match.group(1))
        Y = int(match.group(2))
        total_sum += X*Y
    else:
        total_sum +=0
print("Total number pair product sum: ", total_sum)

#Part 2
def remove_intervals_between_do_and_dont(arr):
    result = []
    skip = False 
    for item in arr:
        if item[0] == "don't":
            skip = True
        if not skip:
            result.append(item)
        if item[0] == "do" and skip:
            skip = False
    return result

filtered_list = remove_intervals_between_do_and_dont(our_list)

total_sum = 0
for item in filtered_list:
    match = re.match(r"mul\((\d+),(\d+)\)", item[1])
    if match:
        X = int(match.group(1))
        Y = int(match.group(2))
        total_sum += X*Y
    else:
        total_sum +=0
print("Total number pair product sum: ", total_sum)
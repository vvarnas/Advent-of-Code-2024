import numpy as np 
with open('/input.txt') as f:
    result = list(zip(*[line.split() for line in f]))
    array1 = np.array(result[0], dtype=float)
    array2 = np.array(result[1], dtype=float)
array1.sort()
array2.sort()

#Part 1:
i, j = 0, 0
total_difference = 0
while i < array1.size and j < array2.size:
    total_difference += abs(array1[i] - array2[j])
    i += 1
    j += 1

print(f"Total array distance: {total_difference:.2f}")

#Part 2:

#Count instances of the same element in array
def value_count(value, lister):
    count = 0
    for vall in lister:
        if vall == value:
            count +=1
    return count

#Get the array similarity score
score = 0
for x in array1:
    score += x*value_count(x, array2)

print(f"Array simlarity score: {score:.2f}")

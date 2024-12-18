import re
import time
from itertools import permutations, product

# Read input data
with open(r"/input7") as file:
    raw_data = file.read().splitlines()

# Sample data for debugging
sample_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
data = sample_data.split("\n")

data = raw_data
def evaluate_left_to_right(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result

def is_valid_equation(target, numbers):
    # Generate all combinations of operators for n-1 positions
    operator_combinations = product(['+', '*'], repeat=len(numbers) - 1)
    
    for operators in operator_combinations:
        # Evaluate the expression with the current operator combination
        if evaluate_left_to_right(numbers, operators) == target:
            return True
    return False

# Main logic
calibration_result = 0

for line in data:
    # Parse the target and the numbers
    target, numbers = line.split(":")
    target = int(target)
    numbers = list(map(int, numbers.split()))
    
    # Check if the equation is valid
    if is_valid_equation(target, numbers):
        calibration_result += target

print(f"Total Calibration Result: {calibration_result}")

def evaluate_left_to_right_2(numbers, operators):
    """
    Evaluates the expression left-to-right using the given numbers and operators.
    """
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result
def is_valid_equation_2(target, numbers):
    # Generate all combinations of operators for n-1 positions
    operator_combinations = product(['+', '*', '||'], repeat=len(numbers) - 1)
    
    for operators in operator_combinations:
        # Debug: Print the current operators and result
        result = evaluate_left_to_right_2(numbers, operators)
        
        if result == target:
            return True
    return False


calibration_result = 0

for line in data:
    # Parse the target and the numbers
    target, numbers = line.split(":")
    target = int(target)
    numbers = list(map(int, numbers.split()))
    
    # Check if the equation is valid
    if is_valid_equation_2(target, numbers):
        calibration_result += target

print(f"Total New Calibration Result: {calibration_result}")

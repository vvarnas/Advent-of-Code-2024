#Part 1
def is_safe_report(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    increasing = all(0 < diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff < 0 for diff in differences)
    return increasing or decreasing


def count_safe_reports(data):
    safe_count = 0
    for line in data:
        report = list(map(int, line.split()))
        if is_safe_report(report):
            safe_count += 1
    return safe_count

# Read input data
with open("/Users/varnas/Desktop/vscode/input2.txt", "r") as file:
    data = file.read().strip().split("\n")
safe_reports = count_safe_reports(data)
print(f"Number of safe reports: {safe_reports}")

#Part 2
def check_safe_reports_new(data):
    safe_count = 0
    for line in data:
        report = list(map(int, line.split()))
        if is_safe_report(report):
            # The report is already safe
            safe_count += 1
        else:
            # Try removing each level to see if the report becomes safe
            for i in range(len(report)):
                new_report = report[:i] + report[i+1:]
                if is_safe_report(new_report):
                    safe_count += 1
                    break
    
    return safe_count
safe_reports_count = check_safe_reports_new(data)
print(f"Number of safe reports after modying one level: {safe_reports_count}")

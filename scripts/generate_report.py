import csv
from collections import Counter
import os

# Get the directory where this script is located
base_dir = os.path.dirname(os.path.dirname(__file__))
input_file = os.path.join(base_dir, "data", "patient_data.csv")

total_records = 0
valid_records = 0
error_count = 0
error_types = []

with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        total_records += 1
        errors = []

        # Age validation
        try:
            age = int(row["Age"])
            if age < 0 or age > 120:
                errors.append("Invalid Age")
        except:
            errors.append("Missing Age")

        # Billing Code
        if not row["BillingCode"]:
            errors.append("Missing Billing Code")

        # Amount
        try:
            amount = float(row["Amount"])
            if amount < 0:
                errors.append("Negative Amount")
        except:
            errors.append("Invalid Amount")

        if errors:
            error_count += 1
            error_types.extend(errors)
        else:
            valid_records += 1

# Count most common errors
error_summary = Counter(error_types)

# Output report
summary_report = os.path.join(base_dir, "output", "summary_report.txt")
with open(summary_report, "w") as report:
    report.write("=== DATA REPORT ===\n")
    report.write(f"Total Records: {total_records}\n")
    report.write(f"Valid Records: {valid_records}\n")
    report.write(f"Records with Errors: {error_count}\n\n")
    
    report.write("Most Common Errors:\n")
    for error, count in error_summary.items():
        report.write(f"{error}: {count}\n")

print("Report generated: summary_report.txt")
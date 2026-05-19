import csv
import os

# Get the directory where this script is located
base_dir = os.path.dirname(os.path.dirname(__file__)) #go up one level
input_file = os.path.join(base_dir, "data", "patient_data.csv")

error_log = []
valid_records = []

with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        errors = []

        # Validate Age
        try:
            age = int(row["Age"])
            if age < 0 or age > 120:
                errors.append("Invalid age")
        except:
            errors.append("Missing or non-numeric age")

        # Validate Billing Code
        if not row["BillingCode"]:
            errors.append("Missing billing code")

        # Validate Amount
        try:
            amount = float(row["Amount"])
            if amount < 0:
                errors.append("Negative billing amount")
        except:
            errors.append("Invalid amount")

        if errors:
            error_log.append({"PatientID": row["PatientID"], "Errors": ", ".join(errors)})
        else:
            valid_records.append(row)

# Write error log
error_log_file = os.path.join(base_dir, "output", "error_log.csv")
with open(error_log_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["PatientID", "Errors"])
    writer.writeheader()
    writer.writerows(error_log)

# Write clean data
clean_data_file = os.path.join(base_dir, "output", "clean_data.csv")
with open(clean_data_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(valid_records)

print("Processing complete. Check error_log.csv and clean_data.csv.")
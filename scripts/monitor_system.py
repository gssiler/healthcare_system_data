import os

# Get the directory where this script is located
base_dir = os.path.dirname(os.path.dirname(__file__))
log_file = os.path.join(base_dir, "logs", "system_log.txt")

error_count = 0
warning_count = 0

# Check if file exists
if not os.path.exists(log_file):
    print("Log file not found.")
    exit()

with open(log_file, "r") as file:
    lines = file.readlines()

for line in lines:
    if "ERROR" in line:
        error_count += 1
    elif "WARNING" in line:
        warning_count += 1

# File size check (simulate system monitoring)
file_size = os.path.getsize(log_file)

print("=== SYSTEM MONITOR REPORT ===")
print(f"Errors Found: {error_count}")
print(f"Warnings Found: {warning_count}")
print(f"Log File Size: {file_size} bytes")

# Simple alert logic
if error_count > 0:
    print("ALERT: Errors detected in system log!")

if file_size > 500:
    print("ALERT: Log file size is unusually large!")
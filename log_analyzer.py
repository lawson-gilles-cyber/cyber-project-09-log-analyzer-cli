# Log Analyzer CLI Tool

import sys

# Check if user provided a file
if len(sys.argv) < 2:
    print("Usage: python log_analyzer.py <logfile>")
    sys.exit(1)

# Get filename from command-line argument
log_file = sys.argv[1]

# Initialize counters
failed_logins = 0
successful_logins = 0
file_access_events = 0

# Open and read the log file
try:
    with open(log_file, "r") as file:
        logs = file.readlines()

except FileNotFoundError:
    print(f"Error: File '{log_file}' not found.")
    sys.exit(1)

# Process logs
for log in logs:
    log = log.strip()  # Remove newline characters

    # Detect failed logins
    if "LOGIN FAILED" in log:
        failed_logins += 1

    # Detect successful logins
    elif "LOGIN SUCCESS" in log:
        successful_logins += 1

    # Detect file access
    elif "FILE ACCESS" in log:
        file_access_events += 1

# Display results
print("\n=== Log Analysis Report ===\n")

print(f"Failed logins: {failed_logins}")
print(f"Successful logins: {successful_logins}")
print(f"Sensitive file access events: {file_access_events}\n")

# Detection logic
if failed_logins >= 3:
    print("[ALERT] Possible brute force attack detected")

if successful_logins > 0 and failed_logins > 0:
    print("[ALERT] Suspicious login pattern detected")

if file_access_events > 0:
    print("[ALERT] Sensitive file access detected")

import sys
import subprocess
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

scripts = [
    "validate_data.py",
    "monitor_system.py",
    "generate_report.py"
]

print("Starting Healthcare Data Processing System...\n")

for script in scripts:
    script_path = os.path.join(base_dir, "scripts", script)
    
    print(f"Running {script}...")
    
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    
    if result.stderr:
        print(f"Error in {script}:\n{result.stderr}")

print("All processes completed.")
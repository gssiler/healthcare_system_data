# Healthcare Data System

A Python-based data processing system that validates, cleans, and generates reports from structured healthcare datasets.

---

## Overview

This project simulates a lightweight data pipeline for processing healthcare-style structured data. It focuses on validation, cleaning, logging, and automated reporting using modular Python scripts. The system demonstrates core software engineering concepts including data validation, automation, modular design, and file-based data processing workflows.

---

## Features

- Automated data validation with structured error detection  
- Data cleaning pipeline for processing raw patient datasets  
- Automated report generation (summary and error logs)  
- System logging for execution tracking and debugging  
- Modular architecture using separate Python scripts for each function  

---

## Project Structure

healthcare_data_system/  
├── data/  
│   └── patient_data.csv  
├── logs/  
│   └── system_log.txt  
├── output/  
│   ├── clean_data.csv  
│   ├── error_log.csv  
│   └── summary_report.txt  
├── scripts/  
│   ├── generate_report.py  
│   ├── monitor_system.py  
│   └── validate_data.py  
├── main.py  
└── README.md  

---

## How It Works

1. main.py serves as the entry point and runs the full pipeline  
2. validate_data.py checks raw input data for missing values, formatting issues, and inconsistencies  
3. monitor_system.py records system events and execution status into log files  
4. generate_report.py produces cleaned dataset, error report, and summary report outputs  

---

## Architecture Flow

Raw Data → validate_data.py → Clean Data  
Clean Data → generate_report.py → Reports  
System Events → monitor_system.py → Logs

---

## How to Run

Run the full data processing pipeline:

python main.py

This will automatically:
- Validate input data
- Clean dataset
- Generate reports
- Write logs and outputs locally

---

## Tools & Technologies

- Python  
- Object-Oriented Programming (OOP)  
- File Handling (CSV and TXT processing)  
- Data Validation and Cleaning Logic  
- Automation Scripting  
- Logging and Monitoring Systems  
- Modular Software Design  

---

## Key Skills Demonstrated

- Building modular data processing pipelines  
- Automating repetitive data validation tasks  
- Implementing structured error handling and logging  
- Designing reusable and maintainable Python scripts  
- Simulating real-world data engineering workflows  

---

## Sample Outputs (Example)

When the system is executed, it generates the following outputs:

### Cleaned Data
A processed version of the dataset with invalid or missing entries removed.

File: `output/clean_data.csv`

---

### Error Report
Structured log of all validation issues detected during processing.

File: `output/error_log.csv`

---

### Summary Report
High-level overview of dataset quality, errors detected, and processing results.

File: `output/summary_report.txt`

---

### System Logs
Execution tracking logs used for debugging and monitoring pipeline activity.

File: `logs/system_log.txt`

---

## Note

Output and log files are generated dynamically at runtime and are excluded from version control to maintain a clean and production-style repository structure.
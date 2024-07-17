#!/usr/bin/env python3

import csv

# Function to read the employees from the CSV file
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(dict(data))
    return employee_list

# Function to process the employee data and count the number of employees per department
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

# Function to write the report to a text file
# ovaj dio je drugaciji nego u origigi labu!!
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()

# Main script execution
if __name__ == "__main__":
    employee_list = read_employees('/home/user/Google-IT-Automation-with-Python/Qwiklabs_assessments/employees.csv')
    dictionary = process_data(employee_list)
    write_report(dictionary, '/home/user/Google-IT-Automation-with-Python/Qwiklabs_assessments/report.txt')

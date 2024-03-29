import csv

def read_employees(csv_file_location):
    f = open(csv_file_location, "r")
    employee_file = csv.DictReader(f)
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_list = []
    for data in employee_file:
      employee_list.append(data)
    return employee_list

def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    print(f"Employee_data = {employee_data}")
    department_list.append(employee_data[' Department'])
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data

def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k) + ':' + str(dictionary[k]) + '\n')
    f.close()


employee_list = read_employees("csv_test.csv")
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)

write_report(dictionary, "report.txt")
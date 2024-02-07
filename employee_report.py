import csv

employees = open('employee_data.csv','r')

csv_file = csv.reader(employees)
next(csv_file)

print('Highly Efficient Individuals:')

for rec in csv_file:
    prod = float(rec[5])
    hours = float(rec[4])
    eff = prod/hours
    if eff > 2:
        print(rec[1])

employees.close()
print()
print()
employees = open('employee_data.csv','r')

csv_file = csv.reader(employees)
next(csv_file)

print('Low Efficiency Individuals:')

for rec in csv_file:
    prod = float(rec[5])
    hours = float(rec[4])
    eff = prod/hours
    if eff < 1:
        print(rec[1])

employees.close()
print()
print()
employees = open('employee_data.csv','r')

csv_file = csv.reader(employees)
next(csv_file)

print("Employees in their 40s")
i = 0
for rec in csv_file:
    age = float(rec[2])
    if 40 <= age < 50:
        i+=1
        print(rec[1])
print()
print('Total number of employees in their 40s:',i)
print()
print()
employees.close()
employees = open('employee_data.csv','r')

csv_file = csv.reader(employees)
next(csv_file)
a = 0
print("Employees in their 30s")
for rec in csv_file:
    age = float(rec[2])
    if 30 <= age < 40:
        a+=1
        print(rec[1])
print()
print('Total number of employees in their 30s:',a)
print()
print()
employees.close()
employees = open('employee_data.csv','r')

csv_file = csv.reader(employees)
next(csv_file)
b = 0
print("Employees in their 30s")
for rec in csv_file:
    age = float(rec[2])
    if 20 <= age < 30:
        b+=1
        print(rec[1])
print()
print('Total number of employees in their 20s:',b)
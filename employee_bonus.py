import csv

employees = open('employee_data.csv','r')

csv_file = csv.reader(employees)
next(csv_file)

for rec in csv_file:
    salary = float(rec[3])
    bonus = float(rec[7])
    fin_bonus = salary*bonus
    pay = salary + fin_bonus
    print(f'Name: {rec[1]}\nSalary: $  {salary:>9,.2f}\nBonus:  $  {fin_bonus:>9,.2f}\nPay:    $  {pay:>9,.2f}\n')
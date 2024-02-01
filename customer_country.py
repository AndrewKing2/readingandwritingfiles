import csv

customers = open('customers.csv','r')

csv_file = csv.reader(customers)
outfile = open('customer_country.csv','w')
next(csv_file)
i = 0
outfile.write('Full Name,Country\n')
for rec in csv_file:
    i+=1
    outfile.write(f'{rec[1]} {rec[2]},{rec[4]}\n')
outfile.write(f'Total Customers: {i}')
outfile.close()
customers.close()

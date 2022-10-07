
import csv

# read data file
with open("house-sales-data.csv") as csvfile:
    reader = csv.reader(csvfile)
    data = [ row for row in reader ]

# filter and type convert
data = [ [ row[0], row[1], int(row[2]), int(row[3]), int(row[4]),
           float(row[5]), int(row[6]) ]
         for row in data if row[5] != '' and row[5] != '0.0' ]

# count (and print) number of sales per property

# count (and print/plot) number of properties with a given number
# of sales, or more

sale_count = dict()
    
for sale in data:
    address = tuple(sale[0:2])

    if address in sale_count:
        sale_count[address] = sale_count[address] + 1
    else:
        sale_count[address] = 1
        

    
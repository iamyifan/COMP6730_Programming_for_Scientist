#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


# read the data from a CSV file into a list of lists
with open('03-25-2022.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    data = [ row for row in reader ]
    
# select country names from the data, possibly with duplicates
countries = [ row[3] for row in data ]

# a 'verbose' way to do the same as list comprehension above
countries2 = []
for row in data:
    countries2.append(row[3])
    
# select all rows for country 'Australia'    
data_au = [ row for row in data if row[3] == "Australia" ]

# a 'verbose' way to do the same as list comprehension above
data_au2 = []
for row in data:
    if row[3] == "Australia":
        data_au2.append(row)
        
# calculating total number of cases worldwide
total_cases = 0
for row in data:
    total_cases = total_cases + int(row[7])
    
print("total cases:", total_cases)

# one-liner code to calculate total_cases using list comprehension
total_cases = sum( [ int(row[7]) for row in data ] )

# one-liner code to calculate total deaths using list comprehension
total_deaths = sum( [ int(row[8]) for row in data ] )


# the following part of code calculate number of cases and deaths per country
country_names = []
country_cases = []
country_deaths = []

for row in data:
    country = row[3]
    cases = int(row[7])
    deaths = int(row[8])
    
    if country in country_names:
        # add up cases for the country
        cid = country_names.index(country)
        country_cases[cid] = country_cases[cid] + cases
        country_deaths[cid] = country_deaths[cid] + deaths
    else:
        # add new country into list
        country_names.append(country)
        country_cases.append(cases)
        country_deaths.append(deaths)

# build a list of lists, with country names in the 1st column and cases in 2nd column
country_data = [ [ country_cases[i], country_names[i], country_deaths[i] ] for i in range(len(country_names)) ]

country_data2 = [ [ country_cases[i], country_names[i] ] for i in range(len(country_names)) ]

country_top10 = sorted(country_data, reverse = True)[0:10]

import matplotlib.pyplot as plt


plt.bar([ row[1] for row in country_top10 ], [ row[0] for row in country_top10 ])

plt.show()

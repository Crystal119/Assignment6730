import csv
#import numpy as np
#with open('Rainfall_Canberra_070247.csv') as csvfile_Canberra:
#    reader = csv.reader(csvfile_Canberra, delimiter=',', quoting=csv.QUOTE_NONE)
#    for row in reader:
#        print(row)
        
import pandas as pd

data = pd.read_csv('Rainfall_Canberra_070247.csv')

june = data[data['Month']==6]

sum_june = june['Rainfall amount (millimetres)'].sum()

number_of_years = pd.value_counts(data['Year']).index.tolist()
number_of_years.sort()

canberra_june_annual = []

for year in number_of_years:
    canberra_june_annual.append(data[data['Year']==year][data[data['Year']==year]['Month']==6]['Rainfall amount (millimetres)'].sum())

table = pd.pivot_table(data, values='Rainfall amount (millimetres)', index=['Year', 'Month'],aggfunc=np.sum)

table.loc[(2017, 1)].values[0]


import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as mpl
#import csv
#with open('Rainfall_Canberra_070247.csv') as csvfile_Canberra:
#    reader = csv.reader(csvfile_Canberra, delimiter=',', quoting=csv.QUOTE_NONE)
#    for row in reader:
#        print(row)
        

# select the path to the file to be read
file_index = input('select weather observation station: \n1. Sydney \n2. Canberra \n3. Queanbeyan \nEnter your choice: ')
if file_index == '1':
    file = 'Rainfall_Sydney_066062.csv'
if file_index == '2':
    file = 'Rainfall_Canberra_070247.csv'
if file_index == '3':
    file = 'Rainfall_Queanbeyan_070072.csv'
data = pd.read_csv(file)

##把 aggre 空值 变 0 
data['aggre']=data['Rainfall amount (millimetres)']*data['Period over which rainfall was measured (days)']
data['aggre']=data['aggre'].fillna(0)

data['daily']=data['Rainfall amount (millimetres)']/data['Period over which rainfall was measured (days)']
data['daily']=data['daily'].fillna(0)

## 把 year 和 month 连起来
data['Year&Month']=data['Year'].astype(str)+' and '+data['Month'].astype(str)

# 按平均值 补了 空行 
days=list(data[data['Period over which rainfall was measured (days)']>1]['Period over which rainfall was measured (days)'])
amount=list(data[data['Period over which rainfall was measured (days)']>1]['daily'])
index =list(data[data['Period over which rainfall was measured (days)']>1].index)
day=[]
for i in range(0,len(days)):
    day.append(int(days[i]))
for j in range(0,len(day)):
    for i in range(0,day[j]):
        data.loc[data.index == (index[1]-i), 'Period over which rainfall was measured (days)'] = amount[j]   
      

# select month
month = int(input('Select the month: \n1. January \n2. February \n3. March \n4. April \n5. May \n6. June \n7. July \n8. August \n9. September \n10. October \n11. November \n12. December \nEnter your choice: '))

# select the type of time series aggregation
time = int(input('Select time series aggregation (it should be an integer): '))




# table of total rainfall amount every month in every year
table = pd.pivot_table(data, values='Rainfall amount (millimetres)', index=['Month'], columns=['Year'], aggfunc=np.sum)

# list of total rainfall values
rainfall_month = list(table.loc[(month)].values)

# list of years in the table above
years = list(table.columns)


# find threshold line
entries = len(rainfall_month)

once_threshold = math.floor(entries * (1/time))

rainfall_month_sort = rainfall_month[:]

rainfall_month_sort.sort()

threshold_line = rainfall_month_sort[- once_threshold]
    

# bar chart
y = rainfall_month
x = np.arange(0, len(y))
mpl.bar(x + 0.25, y, 0.5, color='blue')
mpl.plot([0, len(y) + 1], [threshold_line, threshold_line], '--k')  # the threshold line
mpl.xticks(x + 0.5, years, rotation=90)
mpl.show()

# scatter plot
mpl.plot(x, y, '.b', markersize=5)
mpl.plot([0, len(y) + 1], [threshold_line, threshold_line], '--k')
mpl.xticks(x, years, rotation=90)
mpl.show()




#june = data[data['Month']==6]

#sum_june = june['Rainfall amount (millimetres)'].sum()

#number_of_years = pd.value_counts(data['Year']).index.tolist()
#number_of_years.sort()

#canberra_june_annual = []

#for year in number_of_years:
    #canberra_june_annual.append(data[data['Year']==year][data[data['Year']==year]['Month']==6]['Rainfall amount (millimetres)'].sum())
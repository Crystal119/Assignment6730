import pandas as pd

#数据读取
data1=pd.read_csv('Rainfall_Canberra_070247.csv')
city1=['Canberra']*len(data1)
data1['city']=city1
data2=pd.read_csv('Rainfall_Sydney_066062.csv')
city2=['Sydney']*len(data2)
data2['city']=city2
data3=pd.read_csv('Rainfall_Queanbeyan_070072.csv')
city3=['Queanbeyan']*len(data3)
data3['city']=city3
data =pd.concat([data1,data2,data3])
data.reset_index(drop=True, inplace=True)


# 数据处理
##把 aggre 空值 变 0 
data['aggre']=data['Rainfall amount (millimetres)']*data['Period over which rainfall was measured (days)']
data['aggre']=data['aggre'].fillna(0)

data['daily']=data['Rainfall amount (millimetres)']/data['Period over which rainfall was measured (days)']
data['daily']=data['daily'].fillna(0)
## 把 year 和 month 连起来
data['Year&Month']=data['Year'].astype(str)+' and '+data['Month'].astype(str)
#data.head(2)

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
        

# 按月分类 统计 

data.groupby('Year&Month')['aggre'].sum()

datam=pd.DataFrame(data.groupby('Year&Month')['aggre'].sum())
datamonth = pd.DataFrame({'Year&Month':list(datam.index),'aggre':list(datam['aggre'])})
datamonth.head(2)


# 按某一年的每个月 
year = 1971
datay = data[data['Year']==year]
#datay.groupby('Year&Month')['aggre'].sum()


# 按年分类统计 
datayear=pd.DataFrame(data.groupby('Year')['aggre'].sum())
datayears = pd.DataFrame({'year':list(datayear.index),'aggre':list(datayear['aggre'])})
datayears.head(2)



# 找 n 年 大值 
n1 = 12
# ------- 
m1 = int(round(len(datayears)/n1 -0.5,0))   # 1/n th, 多少个

print(len(datayears),m1)
print (datayears.sort_values(['aggre'],ascending=False).head(m1))


# 找 n 月份最大 
n2 = 100
# ------- 
m2 = int(round(len(datamonth)/n2 -0.5,0))   # 1/n th, 多少个

print(len(datamonth),m2)
print(datamonth.sort_values(['aggre'],ascending=False).head(m2))



# 找 n 天里最大  
n3 = 5000
# ------- 
m3 = int(round(len(data)/n3 -0.5,0))   # 1/n th, 多少个

print(len(data),m3)
print(data.sort_values(['Rainfall amount (millimetres)'],ascending=False)[['Year','Month','Day','Rainfall amount (millimetres)','Period over which rainfall was measured (days)']].head(m3))
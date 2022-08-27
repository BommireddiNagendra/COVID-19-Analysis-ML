import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear model import LinearRegression
data=pd.read_csv("") print (status)
status = data.head()
print (data.keys())
df=data[['Total Cases', 'Active']]
print (df)
print (df.shape)
x = data.iloc[:,1].values y = data.iloc[:,2].values
plt.title('Covid-19 Analysis')
plt.xlabel('Total Cases")
plt.ylabel("Active Cases') plt.scatter(x,y,color 'r')
plt.show()
z = data[[ 'Death Ratio (2)"]]
dich_rate= data[[ Discharge Ratio (x) '11
#2» np.mean(2) dich_rate= np.mean(dich_rate)
print("Average death percent ,m_z)
print('Average recovery: dich_rate)
x= data.iloc[:,8].values y data.iloc[:,7].values
plt.title('Covid-19 Analysis')
plt.xlabel('States')
 plt.ylabel('Death percent') plt.plot(x,y,color = 'g')
plt.show()
deaths test data[['Deaths"]][Active_test = data[['Total Cases ']][:]
model LinearRegression() model.fit (deaths_test,Active_test)
#Active total cases and deaths in india
plt.title("Total Cases VS Deaths')
plt.scatter(deaths test, Active test,color c)
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

#Read CSV
df = pd.read_csv('workHours.csv')

#Convert dates to datetime object
#Then convert to individual date values
df['Date'] = pd.to_datetime(df['Date']).dt.strftime("%d.%m.%y")
df['Day'] = pd.to_datetime(df['Date']).dt.strftime('%a')
df['Month'] = pd.to_datetime(df['Date']).dt.strftime('%B')

#Aggregate mean by month & day
df = df.groupby(['Month', 'Day'])['Total'].agg(['mean']).reset_index() #Deleting reset index will break

#Pivot, get the data in form that makes it easy to plot group value
#Save in variable fig to plot in GUI
fig = df.pivot(index="Day", columns="Month", values='mean').plot(kind='bar', figsize=(12, 6))
plt.title('Mean pay by day per month')
plt.xlabel('Day')
plt.ylabel('Amount (£)')
plt.legend(loc='upper right')
plt.show()
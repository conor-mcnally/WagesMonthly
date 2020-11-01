import pandas as pd
import matplotlib.pyplot as plt
import datetime

with open('workHours.csv') as csv_file:
    return

df = pd.read_csv('workHours.csv')
#df.at['SumPay', 'Total'] = df['Total'].sum()
df.sort_values('Date')
df['Date'] = [date.weekday() for date in df['Date']]

#Id want the groups to be Days
#Id want the diff bars be months

plt.figure(figsize=(13, 5))
plt.title("Avg pay per day per month")
plt.ylabel("£££")
plt.xlabel("Day")
plt.bar(df['Date'], df['Total'])
plt.show()
print(df)

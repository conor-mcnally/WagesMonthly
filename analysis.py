import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime



df = pd.read_csv('workHours.csv')
# df.at['SumPay', 'Total'] = df['Total'].sum()

df['Date'] = pd.to_datetime(df['Date']).dt.strftime("%d.%m.%y")
df['Day'] = pd.to_datetime(df['Date']).dt.strftime('%A')
df['Month'] = pd.to_datetime(df['Date']).dt.strftime('%B')
print(df)
df.plot(x='Day', y='Total')
plt.show()


#Id want the groups to be Days
#Id want the diff bars be months


# plt.title('Pay per month Avg')
# plt.ylabel('£')
# plt.xlabel('Days')
# for i in df:
#     plt.plot(df['Day'], df['Total'])

# plt.show()
# plt.figure(figsize=(13, 5))
# plt.title("Avg pay per day per month")
# plt.ylabel("£££")
# plt.xlabel("Day")
# plt.bar(df['Date'], df['Total'])
# plt.show()
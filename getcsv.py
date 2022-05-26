from pandas_datareader import data
import pandas_datareader.data as web
import matplotlib.pyplot as plt

mname=input("model name")

df=data.DataReader(name=mname,data_source="yahoo")
df.head(5)

plt.plot(df["Close"])
plt.title(mname+" stock price over time")
plt.xlabel("time")
plt.ylabel("price")
plt.show()
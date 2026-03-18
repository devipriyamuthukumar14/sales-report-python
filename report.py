#importing libraries
from ast import mod
import pandas as pd
import matplotlib.pyplot as plt

#read data
df = pd.read_csv("sales.csv", encoding='latin1')
print(df.columns)
df.head()

#sales sum up
total_sales = df['Sales'].sum()
print("Total Sales",total_sales)

#top products graph
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=True).head(5)
plt.barh(top_products.index, top_products.values)
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.title("Top 5 Products by Sales")
plt.tight_layout()
plt.show()

#converting normal text to date format
df["Order Date"] = pd.to_datetime(df["Order Date"])

#monthly sales report graph
monthly_sales = df.resample("ME", on="Order Date")["Sales"].sum()
monthly_sales.head()
plt.plot(monthly_sales.index, monthly_sales.values)
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.title("Monthly Sales")
plt.tight_layout()
plt.savefig("sales_report.png")
plt.show()

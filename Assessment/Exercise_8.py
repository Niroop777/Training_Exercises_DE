#Ex 8

# DataFrame Plotting


import pandas as pd
import matplotlib.pyplot as plt


data = {
    "category": ["Electronics", "Clothing", "Electronics", "Grocery", "Clothing", "Grocery"],
    "sales": [50000, 20000, 30000, 15000, 25000, 18000]
}

df = pd.DataFrame(data)

category_sales = df.groupby("category")["sales"].sum()

print("Total Sales / Category:\n", category_sales)

category_sales.plot(kind="bar")
plt.title("Total Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()



"""

Creates a DataFrame of sales data.

Groups sales by product category to get totals.

Plots the result as a bar chart.

"""
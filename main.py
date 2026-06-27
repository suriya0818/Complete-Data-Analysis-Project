import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")

print("=== DATASET PREVIEW ===")
print(df.head())

print("\n=== DATASET INFORMATION ===")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

total_revenue = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()

best_product = df.groupby("Product")["Quantity"].sum()

print("\n=== SALES REPORT ===")
print(f"Total Revenue: ₹{total_revenue}")
print(f"Average Sales: ₹{average_sales:.2f}")
print(f"Highest Sale: ₹{highest_sale}")
print("Best Selling Product:", best_product.idxmax())

plt.figure(figsize=(6,4))
best_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig("visualizations/bar_chart.png")
plt.close()

region_sales = df.groupby("Region")["Total_Sales"].sum()

plt.figure(figsize=(6,6))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/pie_chart.png")
plt.close()

print("\nCharts saved successfully inside the visualizations folder.")

import pandas as pd

# Load data
df = pd.read_csv("data/expenses.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# KPIs
total_spend = df["Amount"].sum()
average_spend = df["Amount"].mean()
total_customers = df["Customer_ID"].nunique()

print("Total Spend:", total_spend)
print("Average Spend:", round(average_spend, 2))
print("Total Customers:", total_customers)

# Category-wise spending
category_summary = df.groupby("Category")["Amount"].sum()
print("\nCategory-wise Spending:")
print(category_summary)

# Monthly trend
df["Month"] = df["Date"].dt.to_period("M")
monthly_summary = df.groupby("Month")["Amount"].sum()
print("\nMonthly Spending Trend:")
print(monthly_summary)

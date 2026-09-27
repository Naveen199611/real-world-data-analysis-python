# ============================================================
# REAL-WORLD SALES DATA ANALYSIS PROJECT
# ============================================================
#
# Technologies:
# - Python
# - Pandas
# - NumPy
# - Matplotlib
#
# Workflow:
# Raw Data → Data Cleaning → Analysis → Statistics
#          → Visualization → Business Insights
# ============================================================


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 2. LOAD THE DATA
# ============================================================

df = pd.read_csv("data/monthly_sales_5000_raw.csv")

print("\n========== DATA LOADED ==========")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")


# ============================================================
# 3. DATA CLEANING
# ============================================================

print("\n========== DATA CLEANING ==========")

# Check missing values before cleaning
print("\nMissing values before cleaning:")
print(df.isnull().sum())


# Handle missing categorical values using the mode
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])

df["Sales_Rep"] = df["Sales_Rep"].fillna(
    df["Sales_Rep"].mode()[0]
)


# Handle missing numerical values using the median
df["Discount"] = df["Discount"].fillna(
    df["Discount"].median()
)

df["Customer_Rating"] = df["Customer_Rating"].fillna(
    df["Customer_Rating"].median()
)


# Remove duplicate rows
df = df.drop_duplicates()


# Verify cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print(f"\nDuplicate rows after cleaning: {df.duplicated().sum()}")

print(f"\nClean dataset shape: {df.shape}")


# ============================================================
# 4. BASIC BUSINESS METRICS
# ============================================================

print("\n========== BASIC BUSINESS METRICS ==========")


# Q1: Total Revenue
total_revenue = df["Revenue"].sum()

print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")


# Q2: Average Revenue
average_revenue = df["Revenue"].mean()

print(f"Average Revenue: ₹{average_revenue:,.2f}")


# Q3: Total Profit
total_profit = df["Profit"].sum()

print(f"Total Profit: ₹{total_profit:,.2f}")


# Q4: Average Profit Margin
average_profit_margin = df["Profit_Margin"].mean()

print(f"Average Profit Margin: {average_profit_margin:.2f}%")


# Q5: Total Units Sold
total_units = df["Units_Sold"].sum()

print(f"Total Units Sold: {total_units:,}")


# ============================================================
# 5. PRODUCT ANALYSIS
# ============================================================

print("\n========== PRODUCT ANALYSIS ==========")


# Q6: Revenue by Product

product_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Product:")
print(product_revenue.apply(lambda x: f"₹{x:,.2f}"))


# Highest Revenue Product
highest_revenue_product = product_revenue.idxmax()

print(
    f"\nHighest Revenue Product: "
    f"{highest_revenue_product}"
)


# Q7: Units Sold by Product

product_units = (
    df.groupby("Product")["Units_Sold"]
    .sum()
    .sort_values(ascending=False)
)

print("\nUnits Sold by Product:")
print(product_units)


# Best-Selling Product
best_selling_product = product_units.idxmax()

print(
    f"\nBest-Selling Product by Units: "
    f"{best_selling_product}"
)


# ============================================================
# 6. REGIONAL ANALYSIS
# ============================================================

print("\n========== REGIONAL ANALYSIS ==========")


# Q8: Revenue by Region

region_revenue = (
    df.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Region:")
print(region_revenue.apply(lambda x: f"₹{x:,.2f}"))


# Highest Revenue Region
highest_revenue_region = region_revenue.idxmax()

print(
    f"\nHighest Revenue Region: "
    f"{highest_revenue_region}"
)


# Q9: Units Sold by Region

region_units = (
    df.groupby("Region")["Units_Sold"]
    .sum()
    .sort_values(ascending=False)
)

print("\nUnits Sold by Region:")
print(region_units)


# Best Region by Units
best_region_by_units = region_units.idxmax()

print(
    f"\nBest Region by Units Sold: "
    f"{best_region_by_units}"
)


# ============================================================
# 7. SALES CHANNEL ANALYSIS
# ============================================================

print("\n========== SALES CHANNEL ANALYSIS ==========")


# Q10: Revenue by Sales Channel

channel_revenue = (
    df.groupby("Sales_Channel")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Sales Channel:")
print(channel_revenue.apply(lambda x: f"₹{x:,.2f}"))


# Highest Revenue Sales Channel
highest_revenue_channel = channel_revenue.idxmax()

print(
    f"\nHighest Revenue Sales Channel: "
    f"{highest_revenue_channel}"
)


# ============================================================
# 8. MONTHLY REVENUE ANALYSIS
# ============================================================

print("\n========== MONTHLY REVENUE ANALYSIS ==========")


# Calculate monthly revenue
# sort_index() keeps the months in chronological order
monthly_revenue = (
    df.groupby("Month")["Revenue"]
    .sum()
    .sort_index()
)


print("\nMonthly Revenue:")
print(monthly_revenue.apply(lambda x: f"₹{x:,.2f}"))


# Best and worst performing months
best_month = monthly_revenue.idxmax()
worst_month = monthly_revenue.idxmin()


print(f"\nHighest Revenue Month: {best_month}")
print(f"Lowest Revenue Month: {worst_month}")


# ============================================================
# 9. NUMPY STATISTICS
# ============================================================

print("\n========== NUMPY STATISTICS ==========")


# Convert Revenue column to NumPy array
revenue = df["Revenue"].to_numpy()


# Mean
revenue_mean = np.mean(revenue)

# Median
revenue_median = np.median(revenue)

# Minimum
revenue_minimum = np.min(revenue)

# Maximum
revenue_maximum = np.max(revenue)

# Standard deviation
revenue_std = np.std(revenue)


print(f"\nRevenue Mean: ₹{revenue_mean:,.2f}")
print(f"Revenue Median: ₹{revenue_median:,.2f}")
print(f"Revenue Minimum: ₹{revenue_minimum:,.2f}")
print(f"Revenue Maximum: ₹{revenue_maximum:,.2f}")
print(f"Revenue Standard Deviation: ₹{revenue_std:,.2f}")


# Difference between mean and median
mean_median_difference = revenue_mean - revenue_median

print(
    f"\nDifference Between Mean and Median: "
    f"₹{mean_median_difference:,.2f}"
)


# ============================================================
# 10. DATA VISUALIZATION — MATPLOTLIB
# ============================================================

print("\n========== CREATING VISUALIZATIONS ==========")


# ------------------------------------------------------------
# Q14: Monthly Revenue Trend
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "charts/Monthly_Revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ------------------------------------------------------------
# Q15: Revenue by Region
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.bar(
    region_revenue.index,
    region_revenue.values
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "charts/Region_Revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ------------------------------------------------------------
# Q16: Revenue by Product
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.bar(
    product_revenue.index,
    product_revenue.values
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "charts/Revenue_by_Product.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 11. SAVE CLEANED DATA
# ============================================================

df.to_csv(
    "data/monthly_sales_5000_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")


# ============================================================
# 12. ADDITIONAL BUSINESS METRICS
# ============================================================

print("\n========== ADDITIONAL BUSINESS METRICS ==========")


# Q17: Top 5 Products by Revenue

top_5_products = product_revenue.head(5)

print("\nTop 5 Products by Revenue:")

for product, revenue_value in top_5_products.items():
    print(f"{product}: ₹{revenue_value:,.2f}")


# Q18: Average Order Value

average_order_value = df["Revenue"].mean()

print(
    f"\nAverage Order Value: "
    f"₹{average_order_value:,.2f}"
)


# Q19: Return Rate

return_count = (
    df["Returned"] == "Yes"
).sum()

return_rate = (
    return_count / len(df)
) * 100

print(f"\nReturned Orders: {return_count:,}")
print(f"Return Rate: {return_rate:.2f}%")


# Q20: Average Customer Rating

average_customer_rating = (
    df["Customer_Rating"].mean()
)

print(
    f"\nAverage Customer Rating: "
    f"{average_customer_rating:.2f}/5"
)


# ============================================================
# 13. FINAL INSIGHTS
# ============================================================

print("\n")
print("=" * 55)
print("                 FINAL INSIGHTS")
print("=" * 55)

print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")

print(f"Total Profit: ₹{total_profit:,.2f}")

print(
    f"Highest Revenue Product: "
    f"{highest_revenue_product}"
)

print(
    f"Best-Selling Product by Units: "
    f"{best_selling_product}"
)

print(
    f"Highest Revenue Region: "
    f"{highest_revenue_region}"
)

print(
    f"Best Region by Units Sold: "
    f"{best_region_by_units}"
)

print(
    f"Highest Revenue Sales Channel: "
    f"{highest_revenue_channel}"
)

print(
    f"Highest Revenue Month: "
    f"{best_month}"
)

print(
    f"Lowest Revenue Month: "
    f"{worst_month}"
)

print(
    f"Return Rate: "
    f"{return_rate:.2f}%"
)

print(
    f"Average Customer Rating: "
    f"{average_customer_rating:.2f}/5"
)

print("\n" + "=" * 55)
print("             ANALYSIS COMPLETE")
print("=" * 55)
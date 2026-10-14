"""Task 4: Transform raw Zomato order data into a summary table (total spend per user)."""
import pandas as pd

# 1. Load raw data
orders = pd.read_csv("raw_orders.csv")
print("Raw orders:")
print(orders.to_string(index=False))

# 2. Transform: total spend per user (and items ordered)
summary = (
    orders.groupby("user")
    .agg(items_ordered=("item", lambda x: ", ".join(x)),
         total_spend=("price", "sum"))
    .reset_index()
)

# 3. Output
print("\nSummary - total spend per user:")
print(summary.to_string(index=False))
summary.to_csv("summary_total_spend_per_user.csv", index=False)

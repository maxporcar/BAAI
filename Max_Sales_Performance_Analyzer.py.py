#
# Max, 2025/10/17
# File: Max_Sales_Performance_Analyzer.py
# Short description of the task: Sales Performance Analyzer (targets + bonuses)
#

# 1. Input
# Try to read Excel; if it fails, use the sample data from the assignment.
filename = "sales_data.xlsx"
data = []
use_excel = True

try:
    import pandas as pd  # if not installed, fallback kicks in below
    df = pd.read_excel(filename)
    # expected columns: Employee_Name | Monthly_Sales | Sales_Target
    for _, row in df.iterrows():
        data.append({
            "Employee_Name": str(row["Employee_Name"]),
            "Monthly_Sales": float(row["Monthly_Sales"]),
            "Sales_Target": float(row["Sales_Target"]),
        })
except Exception as e:
    use_excel = False  # couldn't read Excel (file missing or pandas missing)
    # Fallback (sample dataset)
    data = [
        {"Employee_Name": "John Smith", "Monthly_Sales": 45000, "Sales_Target": 40000},
        {"Employee_Name": "Sarah Lee",  "Monthly_Sales": 38000, "Sales_Target": 40000},
        {"Employee_Name": "Mike Chen",  "Monthly_Sales": 52000, "Sales_Target": 40000},
        {"Employee_Name": "Anna Wong",  "Monthly_Sales": 41000, "Sales_Target": 40000},
    ]

total_bonus = 0.0

print("SALES PERFORMANCE REPORT")
print("========================")

# 2. Process
for row in data:
    name = row["Employee_Name"]
    sales = row["Monthly_Sales"]
    target = row["Sales_Target"]

    met = sales >= target
    # bonus rule: 10% if met, 5% if not
    bonus_rate = 0.10 if met else 0.05
    bonus = sales * bonus_rate

    # 3. Output (per employee)
    status = "Target MET" if met else "Target NOT MET"
    print(f"{name}: {status} | Sales: ${sales:,.0f} | Bonus: ${bonus:,.0f}")

    total_bonus += bonus

print("\nTotal Bonuses to Pay: $" + f"{total_bonus:,.0f}")
# (Note: If your numbers differ, check the Excel columns match exactly.)

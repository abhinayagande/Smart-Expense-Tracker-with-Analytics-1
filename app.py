import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("expenses.csv")

st.title("Smart Expense Tracker with Analytics")

# Display data
st.subheader("Expense Data")
st.dataframe(df)

# Total expenses
total_expense = df["Amount"].sum()
st.metric("Total Expenses", f"₹{total_expense}")

# Category analysis
category_expense = df.groupby("Category")["Amount"].sum()

st.subheader("Category Wise Spending")

fig, ax = plt.subplots()
ax.pie(
    category_expense,
    labels=category_expense.index,
    autopct="%1.1f%%"
)
st.pyplot(fig)

# Bar chart
st.subheader("Expenses by Category")

fig2, ax2 = plt.subplots()
ax2.bar(category_expense.index, category_expense.values)
plt.xticks(rotation=45)
st.pyplot(fig2)

# Monthly trend
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

monthly = df.groupby("Month")["Amount"].sum()

st.subheader("Monthly Trend")

fig3, ax3 = plt.subplots()
ax3.plot(monthly.index, monthly.values, marker='o')
st.pyplot(fig3)

# Highest expense category
highest = category_expense.idxmax()

st.success(
    f"Highest spending category: {highest} "
    f"(₹{category_expense.max()})"
)
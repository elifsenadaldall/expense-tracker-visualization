import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
import os

# Constants
DATA_FILE = "expenses.csv"

# Function to load data
def load_data():
    if os.path.exists(DATA_FILE):
        data = pd.read_csv(DATA_FILE)
        # Drop unnamed columns if they exist
        data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
        return data
    else:
        return pd.DataFrame(columns=["Type", "Date", "Category", "Amount", "Description"])
# Function to save data
def save_data(data):
    data.to_csv(DATA_FILE, index=False)

# Updated function to add a new expense
def add_data(type, date ,category, amount, description):
    data = load_data()
    new_entry = pd.DataFrame(
        [[type, date, category, amount, description]],
        columns=["Type", "Date", "Category", "Amount", "Description"]
    )
    data = pd.concat([data, new_entry], ignore_index=True)  
    save_data(data)

def view_expenses(year, month):
    data = load_data()

    data["Date"] = pd.to_datetime(data["Date"])
    filtered_data = data[(data["Date"].dt.year == year) & (data["Date"].dt.month == month)]

    if not data.empty:
        st.dataframe(filtered_data)
    else:
        st.warning("No expenses found. Add some expenses to get started!")

def display_chart(chart_type, year, month):
    data = load_data()

    # Ensure the Date column is in datetime format
    data["Date"] = pd.to_datetime(data["Date"])
    # Filter data by year and month
    data = data[(data["Date"].dt.year == year) & (data["Date"].dt.month == month)]

    if chart_type == "Expenses_PieChart":
        # Filter data for expenses
        filtered_data = data[(data["Type"] == "Expense")]
        fig = px.pie(filtered_data, names="Category", values="Amount", title="Spending by Category")
        st.plotly_chart(fig)

    elif chart_type == "Expenses_LineGraph":
        # Filter data for expenses
        filtered_data = data[(data["Type"] == "Expense")]
        # Group and sort by Date
        filtered_data = filtered_data.groupby("Date", as_index=False).agg({"Amount": "sum"})
        filtered_data = filtered_data.sort_values("Date")
        fig = px.line(filtered_data, x="Date", y="Amount", title="Expenses Over Time")
        st.plotly_chart(fig)

    elif chart_type == "Incomes_BarChart":
        # Filter data for incomes
        filtered_data = data[(data["Type"] == "Income")]
        fig = px.bar(filtered_data, x="Category", y="Amount", title="Income by Category")
        st.plotly_chart(fig)


# Main Streamlit app
st.title("Expense Tracker App")

# Sidebar navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Add Expense", "Add Income", "View Expenses & Incomes", "Visualize Trends"])

if menu == "Add Expense":
    st.header("Add a New Expense")
    with st.form("expense_form", clear_on_submit= True):
        date = st.date_input("Date", datetime.now())
        category = st.selectbox("Category", ["Food", "Rent", "Transportation","Clothing", "Health", "Entertainment", "Other"])
        amount = st.number_input("Amount", min_value=0.01, format="%.2f")
        description = st.text_input("Description (optional)")
        submit = st.form_submit_button("Add Expense")
        
        if submit:
            if amount <= 0:
                st.warning("Amount must be greater than 0")
            else:
                add_data("Expense", date, category, amount, description)
                st.success("Expense added successfully!")
elif menu == "Add Income":
    st.header("Add a New Income")
    with st.form("Income_form", clear_on_submit=True):
        date = st.date_input("Date", datetime.now())
        category = st.selectbox("Category",
                                ["Salary", "Financial Gains" ,"Cash Back" ,"Other"])
        amount = st.number_input("Amount", min_value=0.01, format="%.2f")
        description = st.text_input("Description (optional)")
        submit = st.form_submit_button("Add Income")

        if submit:
            if amount <= 0:
                st.warning("Amount must be greater than 0")
            else:
                add_data("Income", date, category, amount, description)
                st.success("Incomes added successfully!")

elif menu == "View Expenses & Incomes":
    st.header("View Expenses & Incomes")
    with st.form("View List"):
        df = load_data()

        df["Date"] = pd.to_datetime(df["Date"])

        years = df["Date"].dt.year.unique()
        selected_year = st.selectbox("Select a year", years)
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        selected_month = st.selectbox("Select a month", months)

        month_number = months.index(selected_month) + 1

        submit = st.form_submit_button("View")

        if submit:
            view_expenses(selected_year, month_number)


elif menu == "Visualize Trends":
    st.header("Visualize Trends")
    with st.form("View List"):
        data = load_data()

        if not data.empty:
            chart_type = st.selectbox("Select Chart Type", ["Expenses_PieChart", "Expenses_LineGraph", "Incomes_BarChart"])

            df = load_data()

            df["Date"] = pd.to_datetime(df["Date"])

            years = df["Date"].dt.year.unique()
            selected_year = st.selectbox("Select a year", years)
            months = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
            selected_month = st.selectbox("Select a month", months)

            month_number = months.index(selected_month) + 1

            submit = st.form_submit_button("Display Chart")

            if submit:
                display_chart(chart_type ,selected_year, month_number)


        else:
            st.warning("No data to visualize. Add some data first!")

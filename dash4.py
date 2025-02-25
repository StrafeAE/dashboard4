import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Customer Data")
df = pd.read_csv("customer_data.csv")

# Let's get a KPI for Average Purchase Value
# We can add a pie chart for Preferred Payment Method

st.metric("Average Purchase Value:", f"${df['AveragePurchaseValue'].mean():,.2f}")

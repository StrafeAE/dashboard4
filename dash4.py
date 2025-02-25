import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Customer Data")
df = pd.read_csv("customer_data.csv")


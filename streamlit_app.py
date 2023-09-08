import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd
import numpy as np
from PIL import Image
from deta import Deta
import sys

# Print Python version
st.write(f"Python Version: {sys.version}")

# Print installed packages
st.write("Installed Packages:")
for package in sys.modules:
    st.write(package)

# Print sys.path
st.write("sys.path:")
for path in sys.path:
    st.write(path)

# Replace 'your_project_key' with your actual Deta project key.
deta = Deta('a05n6m237pg_eAeKLR4a87uSMGwSqUnK4J17ViG8F7ES')

# Name your drive
drive = deta.Drive("Data")

day = timedelta(days=1)

df = pd.read_excel("EC_holidays.xlsx")
df = df.drop(df[df.Holiday == 'Luxembourg National Day (Luxembourg)'].index)

# create a function to check if a date is a holiday
def is_holiday(date):
    return not df.loc[df['Date'] == date.strftime('%Y-%m-%d'), 'Holiday'].empty

# create a function to add business days to a date
def add_business_days(start_date, days_to_add):
    current_date = start_date
    days_added = 0
    while days_added < days_to_add:
        current_date += timedelta(days=1)
        if current_date.weekday() >= 5:
            continue
        if is_holiday(current_date):
            continue
        days_added += 1
    return current_date.strftime('%d %B %Y')

# create a function to add business days to a date
def add_business_days2(start_date, days_to_add):
    current_date = start_date
    days_added = 0
    while days_added < days_to_add:
        current_date += timedelta(days=1)
        if current_date.weekday() >= 5:
            continue
        if is_holiday(current_date):
            continue
        days_added += 1
    return current_date.strftime('(%A)')

image = Image.open('Rhino.png')

st.write("""
# EUMR Deadline Calculator App

This app calculates EUMR merger deadlines!

***
""")

st.header('Enter notification date')
d = st.date_input("Notification date")
st.subheader('Phase I')
End_date = add_business_days(d, 25)
st.write(f'Expiry of 25 working day review period: :green[**{add_business_days(d, 25)}**] {add_business_days2(d, 25)}')
st.write(f'Expiry of 35 working day review period: :green[**{add_business_days(d, 35)}**] {add_business_days2(d, 35)}')
st.subheader('Phase II')
st.write('Earliest deadline (expiry of 90 working days)')
st.write(f'If Phase I lasted 25 working days: :blue[**{add_business_days(d, 115)}**] {add_business_days2(d, 115)}')
st.write(f'If Phase I lasted 35 working days: :blue[**{add_business_days(d, 125)}**] {add_business_days2(d, 125)}')
st.write(f'Latest deadline (expiry of 125 working days)')
st.write(f'If Phase I lasted 25 working days: :red[**{add_business_days(d, 150)}**] {add_business_days2(d, 150)}')
st.write(f'If Phase I lasted 35 working days :red[**{add_business_days(d, 160)}**] {add_business_days2(d, 160)}')

st.image(image, use_column_width=True)

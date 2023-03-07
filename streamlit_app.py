import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd
import numpy as np
from PIL import Image

st.write("""
# EUMR Deadlines Calculator App

This app calculates EUMR merger deadlines!

***
""")

st.header('Enter notification date')

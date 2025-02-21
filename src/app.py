import streamlit as st
import datetime as dt
import time

from utils import calc_time

birthday = st.date_input(label="Enter your birthday", format="DD/MM/YYYY", max_value="today", min_value=dt.datetime(1900, 1, 1))
if st.button(label="Submit"):
    stop = st.button(label="Stop")
    with st.empty():
        while not stop:
            st.write(calc_time(birthday=str(birthday)))
            time.sleep(0.01)

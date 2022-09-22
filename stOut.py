# creating function to output stream log on webpage

from numpy import empty
import streamlit as st
import time


def stout(msg):
    c = st.empty()
    c.text_area(label="Logs", value=msg) # creating a text area to display the logs
    time.sleep(0.17) # waiting for 0.17 seconds
    c.empty() # clearing the text area for dynamic output


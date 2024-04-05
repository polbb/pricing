import pandas as pd
import numpy as np
# import seaborn as sns
import random
import numpy as np
# import matplotlib.pyplot as plt
import plotly.graph_objects as go

import math
from random import randrange
from datetime import datetime


import re
import streamlit as st
from dotenv import load_dotenv
import os
import json

# Streamlit UI
st.set_page_config(layout="wide")  # Force wide mode
with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# AWS Credentials
aws_access_key_id = st.secrets.AWS_ACCESS_KEY_ID
aws_secret_access_key = st.secrets.AWS_SECRET_ACCESS_KEY
aws_default_region = st.secrets.AWS_DEFAULT_REGION

st.title("ArgoXai - Pricing Tool")
col1, col2, _, _, _, _, _, _ = st.columns([3,3,1,1,1,1,1,1])
number_of_simulations = col1.text_input("Enter Number of Simulations")
data = st.button("Search")
st.divider()


# Notice Percentage Distribution
with st.container(border=True):
    st.subheader("Notice Percentage Distribution")
    col1, col2, col3, col4 = st.columns([2,2,2,2])
    notice_pct_dist_x1 = col1.text_input("Left", value=".05", key="notice_left")
    notice_pct_dist_x2 = col2.text_input("Center", value=".15", key="notice_center")
    notice_pct_dist_x3 = col3.text_input("Right", value=".25", key="notice_right")
    notice_pct_dist_x4 = col4.text_input("Size", value="100000", key="notice_size")
    
    if data:
        # Generate Notice Percentage Distribution Plot
        fig_notice_pct = go.Figure()
        fig_notice_pct.add_trace(go.Histogram(x=np.random.triangular(
            float(notice_pct_dist_x1), 
            float(notice_pct_dist_x2), 
            float(notice_pct_dist_x3), 
            int(notice_pct_dist_x4)
        ), name="Notice %"))
        st.plotly_chart(fig_notice_pct)

# Notice Percentage Loss Distribution
with st.container(border=True):
    st.subheader("Notice Percentage Loss Distribution")
    col5, col6, col7, col8 = st.columns([2,2,2,2])
    notice_pct_loss_dist_x1 = col5.text_input("Left", value=".15", key="loss_left")
    notice_pct_loss_dist_x2 = col6.text_input("Center", value=".25", key="loss_center")
    notice_pct_loss_dist_x3 = col7.text_input("Right", value=".35", key="loss_right")
    notice_pct_loss_dist_x4 = col8.text_input("Size", value="100000", key="loss_size")
    
    if data:
        # Generate Notice Percentage Loss Distribution Plot
        fig_notice_pct_loss = go.Figure()
        fig_notice_pct_loss.add_trace(go.Histogram(x=np.random.triangular(
            float(notice_pct_loss_dist_x1), 
            float(notice_pct_loss_dist_x2), 
            float(notice_pct_loss_dist_x3), 
            int(notice_pct_loss_dist_x4)
        ), name="Notice % Loss"))
        st.plotly_chart(fig_notice_pct_loss)

# Severity Distribution
with st.container(border=True):
    st.subheader("Severity Distribution")
    col9, col10, col11, col12 = st.columns([2,2,2,2])
    severity_dist_x1 = col9.text_input("Left", value=".65", key="severity_left")
    severity_dist_x2 = col10.text_input("Center", value=".7", key="severity_center")
    severity_dist_x3 = col11.text_input("Right", value=".75", key="severity_right")
    severity_dist_x4 = col12.text_input("Size", value="100000", key="severity_size")
    
    if data:
        # Generate Severity Distribution Plot
        fig_severity = go.Figure()
        fig_severity.add_trace(go.Histogram(x=np.random.triangular(
            float(severity_dist_x1), 
            float(severity_dist_x2), 
            float(severity_dist_x3), 
            int(severity_dist_x4)
        ), name="Severity"))
        st.plotly_chart(fig_severity)


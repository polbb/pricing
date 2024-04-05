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
from utils import severity_generator, DV_generator



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


notice_pct_dist = np.random.triangular(float(notice_pct_dist_x1), float(notice_pct_dist_x2), float(notice_pct_dist_x3), int(notice_pct_dist_x4))
notice_pct_loss_dist = np.random.triangular(float(notice_pct_loss_dist_x1), float(notice_pct_loss_dist_x2), float(notice_pct_loss_dist_x3), int(notice_pct_loss_dist_x4))
severity_dist = np.random.triangular(float(severity_dist_x1), float(severity_dist_x2), float(severity_dist_x3), int(severity_dist_x4))

notice_pct, notice_pct_loss, low_severity_pct, med_severity_pct, high_severity_pct = severity_generator(notice_pct_dist, notice_pct_loss_dist, severity_dist)
st.write("Notice %:", notice_pct)
st.write("Notice % Loss:", notice_pct_loss)
st.write("Low Severity %:", low_severity_pct)
st.write("Medium Severity %:", med_severity_pct)
st.write("High Severity %:", high_severity_pct)

with st.container(border=True):
    col13, col14, col18, col19 = st.columns([2,2,2,2])
    deal_count = col13.number_input("Deal Count", value=100)
    DV_range = col14.number_input("DV Range", value=2500000)
    sme_pct = col18.number_input("SME %", value=0.35, format="%.2f")
    mm_pct = col19.number_input("MM %", value=0.55, format="%.2f")

with st.container(border=True):
    col15, col16, col17, col20 = st.columns([2,2,2,2])
    sme_low_DV, sme_upper_DV = col15.slider("Select SME DV Range", min_value=1000000, max_value=100000000, value=(10000000, 75000000))
    mm_low_DV, mm_upper_DV = col16.slider("Select MM DV Range", min_value=50000000, max_value=1000000000, value=(75000000, 750000000))
    j_low_DV, j_upper_DV = col17.slider("Select J DV Range", min_value=500000000, max_value=10000000000, value=(750000000, 5000000000))
    j_pct = col20.number_input("J %", value=0.1, format="%.2f")
DV_list = DV_generator(deal_count, DV_range, sme_low_DV, sme_upper_DV, mm_low_DV, mm_upper_DV, sme_pct, mm_pct, j_pct, j_low_DV, j_upper_DV)

st.write(f'DV list: {DV_list}')
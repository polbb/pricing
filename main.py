import pandas as pd
import numpy as np
# import seaborn as sns
import random
import numpy as np
# import matplotlib.pyplot as plt
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

# load_dotenv('./.env.txt')
# aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
# aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
# aws_default_region = os.getenv('AWS_DEFAULT_REGION')

# AWS Services Clients
# dynamodb = boto3.resource('dynamodb', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_default_region)
# s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_default_region)

st.title("ArgoXai - Pricing Tool")
col1, col2, _, _, _, _, _, _ = st.columns([3,3,1,1,1,1,1,1])
number_of_simulations = col1.text_input("Enter Number of Simulations")
data = st.button("Search")
st.divider()

with st.container(border=True):
    st.title("Notice Percentage Distribution")
    col1, col2, col3, col4 = st.columns([2,2,2,2])
    notice_pct_dist_x1 = col1.slider("Left", min_value=0.0, max_value=0.14, value=0.05, step=0.01)
    notice_pct_dist_x2 = col2.slider("Center", min_value=0.06, max_value=0.24, value=0.15, step=0.01)
    notice_pct_dist_x3 = col3.slider("Right", min_value=0.16, max_value=0.3, value=0.25, step=0.01)
    notice_pct_dist_x4 = col4.text_input("Size", value="100000")



if data:

    st.write(number_of_simulations)
    st.write(f'Enter notice_pct_dist_x1: {notice_pct_dist_x1}')
    st.write(f'Enter notice_pct_dist_x2: {notice_pct_dist_x2}')
    st.write(f'Enter notice_pct_dist_x3: {notice_pct_dist_x3}')
    st.write(f'Enter notice_pct_dist_x4: {notice_pct_dist_x4}')


    # for i in range(num_simulations):

    #     notice_pct, notice_pct_loss, low_severity_pct, med_severity_pct, high_severity_pct = severity_generator(notice_pct_dist, notice_pct_loss_dist, severity_dist)
    #     DV_list = DV_generator(deal_count, DV_range, sme_low_DV, sme_upper_DV, mm_low_DV, mm_upper_DV, sme_pct, mm_pct, j_pct)
    #     limit_list, attachment_pt_list, primary_xs_list = structure_generator(DV_list, low_limit, upper_limit, limit_range, primary_pct, xs_pct, pri_attachment_pt_range)
    #     pricing_list = pricing_generator(DV_list, limit_list, attachment_pt_list, primary_xs_list, pricing_range, sme_pricing_low, sme_pricing_high, mm_pricing_low, mm_pricing_high, j_pricing_low, j_pricing_high)
    #     notice_list = notice_generator(deal_count, notice_pct, notice_pct_loss, low_severity_pct, med_severity_pct, high_severity_pct)
    #     loss_list = loss_generator(notice_list, limit_list, low_low_severity_loss, low_high_severity_loss, med_low_severity_loss, med_high_severity_loss)
    #     df = df_generator(DV_list, pricing_list, attachment_pt_list, notice_list, loss_list, limit_list)
    #     performance_stats.append(df['Performance'].sum().round(0))

    # sns.displot(performance_stats, bins=100, kde=True);



import datetime
import boto3
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
import re
import streamlit as st
import pandas as pd
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

if data:
    st.write(number_of_simulations)


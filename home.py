import streamlit as st
import datetime



year = today.year

with st.expander('Laatvlieger'):
  Laatvlieger_date = st.date_input("Period", value=(datetime.date(year, 4, 15), datetime.date(year, 5, 15)), 
                                   min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, 
                                   kwargs=None,format="DD/MM/YYYY", disabled=False, label_visibility="visible")
  Laatvlieger_days = st.number_input("How many days", min_value=0, max_value=2, value="max", step=1, format=None, key=None, 
                                     help=None, on_change=None, args=None, kwargs=None,
                                     placeholder=None, disabled=False, label_visibility="visible")

with st.expander('Kraamverblif'):
  Kraamverblif_date = st.date_input("Period", value=(datetime.date(year, 5, 15), datetime.date(year, 7, 15)), 
                                   min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, 
                                   kwargs=None,format="DD/MM/YYYY", disabled=False, label_visibility="visible")
  Kraamverblif_days = st.number_input("How many days", min_value=0, max_value=3, value="max", step=1, format=None, key=None, 
                                     help=None, on_change=None, args=None, kwargs=None,
                                     placeholder=None, disabled=False, label_visibility="visible")

with st.expander('Winterverblijf'):
  Winterverblijf_date = st.date_input("Period", value=(datetime.date(year, 4, 15), datetime.date(year, 5, 15)), 
                                   min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, 
                                   kwargs=None,format="DD/MM/YYYY", disabled=False, label_visibility="visible")
  Winterverblijf_days = st.number_input("How many days", min_value=0, max_value=2, value="max", step=1, format=None, key=None, 
                                     help=None, on_change=None, args=None, kwargs=None,
                                     placeholder=None, disabled=False, label_visibility="visible")

with st.expander('Paarverblijf'):
  Paarverblijf_date = st.date_input("Period", value=(datetime.date(year, 4, 15), datetime.date(year, 5, 15)), 
                                   min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, 
                                   kwargs=None,format="DD/MM/YYYY", disabled=False, label_visibility="visible")
  Paarverblijf_days = st.number_input("How many days", min_value=0, max_value=2, value="max", step=1, format=None, key=None, 
                                     help=None, on_change=None, args=None, kwargs=None,
                                     placeholder=None, disabled=False, label_visibility="visible")

with st.expander('Tweekleirige'):
  Tweekleirige_date = st.date_input("Period", value=(datetime.date(year, 4, 15), datetime.date(year, 5, 15)), 
                                   min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, 
                                   kwargs=None,format="DD/MM/YYYY", disabled=False, label_visibility="visible")
  Tweekleirige_days = st.number_input("How many days", min_value=0, max_value=2, value="max", step=1, format=None, key=None, 
                                     help=None, on_change=None, args=None, kwargs=None,
                                     placeholder=None, disabled=False, label_visibility="visible")


number_areas = st.number_input("How many areas", min_value=0, max_value=None, value="min", step=1, format=None, key=None, 
                                   help=None, on_change=None, args=None, kwargs=None,
                                   placeholder=None, disabled=False, label_visibility="visible")

Laatvlieger_date
  
  
  
  

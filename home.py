import streamlit as st
import datetime



year = datetime.datetime.now().year

with st.expander('Laatvlieger'):
  Laatvlieger_date = st.date_input("Period", value=(datetime.date(year, 4, 15), datetime.date(year, 5, 15)), 
                                   min_value=None, max_value=None, key="Laatvlieger_date", help=None, on_change=None, args=None, 
                                   kwargs=None,format="DD/MM/YYYY", disabled=False, label_visibility="visible")
  # Laatvlieger_days = st.number_input("How many days", min_value=0, max_value=2, value=2, step=1, format=None, key="Laatvlieger_days", 
  #                                    help=None, on_change=None, args=None, kwargs=None,
  #                                    placeholder=None, disabled=False, label_visibility="visible")
  number_areas_Laatvlieger = st.number_input("How many areas", min_value=0, max_value=None, value="min", step=1, format=None, key="number_areas_Laatvlieger", 
                                   help=None, on_change=None, args=None, kwargs=None,
                                   placeholder=None, disabled=False, label_visibility="visible")

with st.expander('Kraamverblif'):
  Kraamverblif_date = st.date_input("Period", value=(datetime.date(year, 5, 15), datetime.date(year, 7, 15)), 
                                   min_value=None, max_value=None, key="Kraamverblif_date", help=None, on_change=None, args=None, 
                                   kwargs=None,format="DD/MM/YYYY", disabled=False, label_visibility="visible")
  # Kraamverblif_days = st.number_input("How many days", min_value=0, max_value=3, value=3, step=1, format=None, key="Kraamverblif_days", 
  #                                    help=None, on_change=None, args=None, kwargs=None,
  #                                    placeholder=None, disabled=False, label_visibility="visible")
  number_areas_Kraamverblif = st.number_input("How many areas", min_value=0, max_value=None, value="min", step=1, format=None, key="number_areas_Kraamverblif", 
                                   help=None, on_change=None, args=None, kwargs=None,
                                   placeholder=None, disabled=False, label_visibility="visible")

with st.expander('Winterverblijf'):
  Winterverblijf_date = st.date_input("Period", value=(datetime.date(year, 4, 15), datetime.date(year, 5, 15)), 
                                   min_value=None, max_value=None, key="Winterverblijf_date", help=None, on_change=None, args=None, 
                                   kwargs=None,format="DD/MM/YYYY", disabled=False, label_visibility="visible")
  # Winterverblijf_days = st.number_input("How many days", min_value=0, max_value=2, value=2, step=1, format=None, key="Winterverblijf_days", 
  #                                    help=None, on_change=None, args=None, kwargs=None,
  #                                    placeholder=None, disabled=False, label_visibility="visible")
  number_areas_Winterverblijf = st.number_input("How many areas", min_value=0, max_value=None, value="min", step=1, format=None, key="number_areas_Winterverblijf", 
                                   help=None, on_change=None, args=None, kwargs=None,
                                   placeholder=None, disabled=False, label_visibility="visible")

with st.expander('Paarverblijf'):
  Paarverblijf_date = st.date_input("Period", value=(datetime.date(year, 9, 1), datetime.date(year, 10, 1)), 
                                   min_value=None, max_value=None, key="Paarverblijf_date", help=None, on_change=None, args=None, 
                                   kwargs=None,format="DD/MM/YYYY", disabled=False, label_visibility="visible")
  # Paarverblijf_days = st.number_input("How many days", min_value=0, max_value=2, value=2, step=1, format=None, key="Paarverblijf_days", 
  #                                    help=None, on_change=None, args=None, kwargs=None,
  #                                    placeholder=None, disabled=False, label_visibility="visible")
  number_areas_Paarverblijf = st.number_input("How many areas", min_value=0, max_value=None, value="min", step=1, format=None, key="number_areas_Paarverblijf", 
                                   help=None, on_change=None, args=None, kwargs=None,
                                   placeholder=None, disabled=False, label_visibility="visible")

with st.expander('Tweekleurige'):
  Tweekleirige_date = st.date_input("Period", value=(datetime.date(year, 10, 1), datetime.date(year, 11, 1)), 
                                   min_value=None, max_value=None, key="Tweekleirige_date", help=None, on_change=None, args=None, 
                                   kwargs=None,format="DD/MM/YYYY", disabled=False, label_visibility="visible")
  # Tweekleirige_days = st.number_input("How many days", min_value=0, max_value=2, value=2, step=1, format=None, key="Tweekleirige_days", 
  #                                    help=None, on_change=None, args=None, kwargs=None,
  #                                    placeholder=None, disabled=False, label_visibility="visible")
  number_areas_Tweekleirige = st.number_input("How many areas", min_value=0, max_value=None, value="min", step=1, format=None, key="number_areas_Tweekleirige", 
                                   help=None, on_change=None, args=None, kwargs=None,
                                   placeholder=None, disabled=False, label_visibility="visible")
@st.dialog(" ")
def calculate():
  if number_areas_Laatvlieger > 0:
    days_Laatvlieger =  (Laatvlieger_date[1] - Laatvlieger_date[0]).days
    days_work_Laatvlieger = 2*number_areas_Laatvlieger
    days_off = days_Laatvlieger - days_work_Laatvlieger
    days_off_percent = round((days_off*100)/days_Laatvlieger)
    days_off_week = round((days_off_percent/100)*7,1)
    st.write(f"""If you cover {number_areas_Laatvlieger} areas during the Laatvleger period you will work {days_work_Laatvlieger} days, 
    and {days_off} days off which is the {days_off_percent}% of the total number in that peroid, corrispondig to almost {days_off_week} days off per week""")
  else:
    days_work_Laatvlieger = 0
  
  days_Kraamverblif =  (Kraamverblif_date[1] - Kraamverblif_date[0]).days

  if number_areas_Kraamverblif > 0:
    days_work_Kraamverblif_continued = 2*number_areas_Kraamverblif
    days_off_continued = days_Kraamverblif - days_work_Kraamverblif_continued
    days_off_percent_continued = round((days_off_continued*100)/days_Kraamverblif)
    days_off_week_continued = round((days_off_percent_continued/100)*7,1)
    st.write(f"""If you cover {number_areas_Kraamverblif} areas during the Kraamverblif period you will work 
    {days_work_Kraamverblif_continued} days continued, and {days_off_continued} days off which is the {days_off_continued}% of the total number in that period
    , corrispondig to almost {days_off_week_continued} days off per week""")  

    days_work_Kraamverblif_single = 3*number_areas_Kraamverblif
    days_off_single = days_Kraamverblif - days_work_Kraamverblif_single
    days_off_percent_single = round((days_off_single*100)/days_Kraamverblif)
    days_off_week_single = round((days_off_percent_single/100)*7,1)
    st.write(f"""If you cover {number_areas_Kraamverblif} areas during the Kraamverblif period you will work 
    {days_work_Kraamverblif_single} days single, and {days_off_single} days off which is the {days_off_percent_single}% of the total number in that period
    , corrispondig to almost {days_off_week_single} days off per week""")  
  else:
    days_work_Kraamverblif_single = 0
    
  if number_areas_Winterverblijf > 0:
    days_Winterverblijf =  (Winterverblijf_date[1] - Winterverblijf_date[0]).days
    days_work_Winterverblijf = 2*number_areas_Winterverblijf
    days_off = days_Winterverblijf - days_work_Winterverblijf
    days_off_percent = round((days_off*100)/days_Winterverblijf)
    days_off_week = round((days_off_percent/100)*7,1)
    st.write(f"""If you cover {number_areas_Winterverblijf} areas during the Winterverblijf period you will work {days_work_Winterverblijf} days, 
    and {days_off} days off which is the {days_off_percent}% of the total number in that peroid, corrispondig to almost {days_off_week} days off per week""")
  else:
    days_work_Winterverblijf = 0
    
  if number_areas_Paarverblijf > 0:
    days_Paarverblijf =  (Paarverblijf_date[1] - Paarverblijf_date[0]).days
    days_work_Paarverblijf = 2*number_areas_Paarverblijf
    days_off = days_Paarverblijf - days_work_Paarverblijf
    days_off_percent = round((days_off*100)/days_Paarverblijf)
    days_off_week = round((days_off_percent/100)*7,1)
    st.write(f"""If you cover {number_areas_Paarverblijf} areas during the Paarverblijf period you will work {days_work_Paarverblijf} days, 
    and {days_off} days off which is the {days_off_percent}% of the total number in that peroid, corrispondig to almost {days_off_week} days off per week""")
  else:
    days_work_Paarverblijf = 0
    
  if number_areas_Tweekleirige > 0:
    days_Tweekleirige =  (Tweekleirige_date[1] - Tweekleirige_date[0]).days
    days_work_Tweekleirige = 2*number_areas_Tweekleirige
    days_off = days_Paarverblijf - days_work_Tweekleirige
    days_off_percent = round((days_off*100)/days_Tweekleirige)
    days_off_week = round((days_off_percent/100)*7,1)
    st.write(f"""If you cover {number_areas_Tweekleirige} areas during the Tweekleurige vlermuis period you will work {days_work_Tweekleirige} days, 
    and {days_off} days off which is the {days_off_percent}% of the total number in that peroid, corrispondig to almost {days_off_week} days off per week""")
  else:
    days_work_Tweekleirige = 0  
    
  total_days = days_work_Laatvlieger + days_work_Kraamverblif_single + days_work_Winterverblijf + days_work_Paarverblijf + days_work_Tweekleirige
  payment = total_days * 200 
  st.write(f"You will work in total {total_days} bat rounds, earning {payment} euros considering 200 euros per round")
      

if st.button("Calculate"):
  calculate()
 

import streamlit as st
import pickle
import numpy as np
import pandas as pd

def model():
    with open('model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

def prediction(start_date,end_date,model):
    future_predictions = model.get_prediction(start=pd.to_datetime(start_date), end=pd.to_datetime(end_date))
    future_predicted_means = future_predictions.predicted_mean
    return future_predicted_means

def date(month):
  match month:
    case "January":
      start_date="2022-01-01"
      end_date="2022-01-31"
      return start_date,end_date
    case "February":
      start_date="2022-02-01"
      end_date="2022-02-28"
      return start_date,end_date
    case "March":
      start_date="2022-03-01"
      end_date="2022-03-31"
      return start_date,end_date
    case "April":
      start_date="2022-04-01"
      end_date="2022-04-30"
      return start_date,end_date
    case "May":
      start_date="2022-05-01"
      end_date="2022-05-31"
      return start_date,end_date
    case "June":
      start_date="2022-06-01"
      end_date="2022-06-30"
      return start_date,end_date
    case "July":
      start_date="2022-07-01"
      end_date="2022-07-31"
      return start_date,end_date
    case "August":
      start_date="2022-08-01"
      end_date="2022-08-31"
      return start_date,end_date
    case "September":
      start_date="2022-09-01"
      end_date="2022-09-30"
      return start_date,end_date
    case "October":
      start_date="2022-10-01"
      end_date="2022-10-31"
      return start_date,end_date
    case "November":
      start_date="2022-11-01"
      end_date="2022-11-30"
      return start_date,end_date
    case "December":
      start_date="2022-12-01"
      end_date="2022-12-31"
      return start_date,end_date
    case _:
        start_date="2022-01-01"
        end_date="2022-12-31"
        return start_date,end_date
      
    
def average_or_eachday(option,predicted_means,formated_predicted_means):
  match option:
    case "Average of the month":
      return "{:,}".format(int(predicted_means.mean()))
    case "Every day":
      return formated_predicted_means
    case _:
      return formated_predicted_means


def format(series):
  rounded_integers = series.round(0).astype(int)
  comma_separated_values = rounded_integers.apply('{:,}'.format)
  return comma_separated_values

def display(month,day):
    start_date,end_date=date(month)
    prediction_model=model()
    predicted_means=prediction(start_date,end_date,prediction_model)
    predicted_means.index.name="Date"
    formated_predicted_means=format(predicted_means)
    data=average_or_eachday(day,predicted_means,formated_predicted_means)
    return data

  


def show():
    st.title("Scanned Receipts Prediction-2022")
    months=["Make selection","January","February","March","April","May","June","July","August","September","October",
            "November","December"]
    month = st.selectbox("Month",months)
    Option=["Make selection","Every day","Average of the month"]
    day = st.selectbox("Average/Each day",Option)
    button=st.button("Start Prediction")   
    if button:
      display_data=display(month,day)
      if day=="Every day":
        st.write("Predited Number of Scanned Receipts for every day in",month,"-2022:")
        st.dataframe(display_data)
      elif day == "Average of the month":
        st.write("Assumed average for Number Scanned Receipts in",month,"-2022: ",display_data)


show()  


from delphi_epidata import Epidata
import pandas as pd
from meteostat import Stations, Monthly, Daily, Point
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.dtypes.generic import ABCSeries
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sodapy import Socrata
import json

def fetch_weather(start, end, location):

    state = open('../Config/locations.json')
    datafile = json.load(state)
    point = Point(
    datafile[location]['Latitude'],
    datafile[location]['Longitude'],
    datafile[location]['Altitude'])
    data = Daily(point, start, end)
    weather_df = data.fetch()
    weather_df = pd.DataFrame.from_dict(weather_df, orient="columns")
    weather_df.reset_index('time',inplace=True)
    weather_df = weather_df.rename(columns = {'time':'date'})
    weather_dataframe = weather_df[['date', 'tavg']]
    pd.DataFrame(weather_dataframe)
    return weather_dataframe

def fetch_hospitalization_record(state ,epi_start, epi_end):
    results = Epidata.covid_hosp(state, Epidata.range(epi_start, epi_end))
    records = results['epidata']
    hospitalization_df = pd.DataFrame.from_dict(records, orient="columns")
    hospitalization_df['date'] = pd.to_datetime(hospitalization_df['date'], format='%Y%m%d')
    hospital_df = hospitalization_df[['date', 'inpatient_beds_utilization', 'inpatient_bed_covid_utilization','percent_of_inpatients_with_covid']]
    pd.DataFrame(hospital_df)
    return hospital_df

def fetch_vaccination_record():
    client = Socrata("opendata.maryland.gov", None)
    vaccine = client.get("4tar-3iht", limit=8000)
    vaccine_df = pd.DataFrame.from_records(vaccine)
    vaccination_df = vaccine_df
    vaccination_df['vaccination_date'] = pd.to_datetime(vaccination_df['vaccination_date'])
    vaccination_df['vaccination_date'] = pd.to_datetime(vaccination_df['vaccination_date'], format ='%Y%m%d')
    return vaccination_df



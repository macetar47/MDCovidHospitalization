import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import preprocessing

def plot_temperature_covid(final_dataset):
    ax = sns.scatterplot(x="ScaledAvgTemp", y = "ScaledAvgCovid", data = final_dataset);
    ax.set_title("Percentage of impatients with covid based on weather (scaled)")
    ax.set_xlabel("Average Temperature in Celsius (Scaled)")
    ax.set_ylabel("Percentages of Hospstal Impatients with Covid (Scaled)")
    return ax
def regression_temperature_covid(final_dataset):
    regression1 = stats.pearsonr(final_dataset['ScaledAvgTemp'], final_dataset['ScaledAvgCovid'])
    return regression1
def plot_covid_vaccination(final_dataset):
    ax1 = sns.scatterplot(x="Percentage MD Population Vaccinated", y = "percent_of_inpatients_with_covid", data = final_dataset);
    ax1.set_title("Percentage of impatients with covid based on percentage of population that is vaccinated")
    ax1.set_xlabel("Percentage of Maryland Residents Vaccinated")
    ax1.set_ylabel("Percentages of Hospital Impatients with Covid")
    return ax1
def regression_covid_vaccination(final_dataset):
    regression2 = stats.pearsonr(final_dataset['Percentage MD Population Vaccinated'], final_dataset['percent_of_inpatients_with_covid'])
    return regression2


def train_data(final_dataset, train_year):
    modeldata = final_dataset[["date_year", "tavg","percent_of_inpatients_with_covid", "Percentage MD Population Vaccinated"]]
    train_data = modeldata.loc[modeldata.date_year == train_year]
    return train_data
def train_data_X(Train_data,X1,X2):
    train_data_X = Train_data[[X1,X2]]
    return train_data_X
def train_data_Y(Train_data,Y):
    train_data_Y = Train_data[Y]
    return train_data_Y




def test_data(final_dataset, test_year):
    modeldata = final_dataset[["date_year", "tavg","percent_of_inpatients_with_covid", "Percentage MD Population Vaccinated"]]
    test_data = modeldata.loc[modeldata.date_year == test_year]
    return test_data

def test_data_X(Test_data,X1,X2):
    test_data_X = Test_data[[X1,X2]]
    return test_data_X
def test_data_Y(Test_data,Y):
    test_data_Y = Test_data[Y]
    return test_data_Y

def prediction(Train_data_X, Train_data_Y, Test_data_X):
    model = LinearRegression()
    model.fit(Train_data_X, Train_data_Y)
    predictions = model.predict(Test_data_X)
    return predictions

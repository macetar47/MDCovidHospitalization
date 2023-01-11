import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
import numpy as np

def vaccination_cleanup(dataframe_2):
   vaccine = dataframe_2[dataframe_2['vaccination_date'].dt.strftime("%Y") >= '2021'] 
   vaccine.reset_index()
   vaccine['fullyvaccinatedcumulative'] = vaccine['fullyvaccinatedcumulative'].astype('int')
   vaccination_data = vaccine.groupby(['vaccination_date']).agg(fullyvaxed = pd.NamedAgg(column = 'fullyvaccinatedcumulative', aggfunc = lambda x: x.sum())).reset_index()
   vaccination_data['date_year'] = vaccination_data.vaccination_date.transform(lambda x:str(x.year))
   vaccination_data['MD_Population'] = np.where(vaccination_data['date_year']=='2021', '6165000', '6257958')
   vaccination_data['MD_Population'] = vaccination_data['MD_Population'].astype('int')
   vaccination_data['Percentage MD Population Vaccinated'] = vaccination_data['fullyvaxed']/vaccination_data['MD_Population']
   vaccination_data = vaccination_data.rename(columns={'vaccination_date': 'date'}) 
   vaccination_data['date'] = pd.to_datetime(vaccination_data['date']).dt.date
   vaccination_data['date'] = pd.to_datetime(vaccination_data['date'])
   vaccination_data['date'] = pd.to_datetime(vaccination_data['date'], format ='%Y%m%d')
   return vaccination_data

def data_merge(dataframe_0, dataframe_1, vaccination_data):
   
    merge_1 = pd.merge(dataframe_0, dataframe_1)
    scale = StandardScaler()
    X = merge_1[['tavg', 'percent_of_inpatients_with_covid']]
    scaledX = scale.fit_transform(X)
    ScaledAvgTemp = (scaledX[0:710, 0])
    ScaledAvgCovid = (scaledX[0:710, 1])
    merge_1['ScaledAvgTemp'] = ScaledAvgTemp.tolist()
    merge_1['ScaledAvgCovid'] = ScaledAvgCovid.tolist()
    final_dataset = pd.merge(merge_1,vaccination_data)
    return final_dataset



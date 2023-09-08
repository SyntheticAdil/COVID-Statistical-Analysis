import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')
death = pd.read_csv('time_series_covid19_deaths_global.csv')
recovered = pd.read_csv('time_series_covid19_recovered_global.csv')

confirmed = confirmed.drop(['Province/State' , 'Lat', 'Long'],axis=1)
death = death.drop(['Province/State' , 'Lat', 'Long'],axis=1)
recovered = recovered.drop(['Province/State' , 'Lat', 'Long'],axis=1)

confirmed = confirmed.groupby(confirmed['Country/Region']).aggregate('sum')
death = death.groupby(death['Country/Region']).aggregate('sum')
recovered = recovered.groupby(recovered['Country/Region']).aggregate('sum')

confirmed = confirmed.T
death = death.T
recovered = recovered.T

active_cases = confirmed.copy()
for day in range(0, len(confirmed)):
    active_cases.iloc[day] = confirmed.iloc[day] - death.iloc[day] - recovered.iloc[day]

overall_growthrate = confirmed.copy()
for day in range(1, len(confirmed)):
    overall_growthrate.iloc[day] = ((active_cases.iloc[day]-active_cases.iloc[day-1])/active_cases.iloc[day-1])*10000

death_rate = confirmed.copy()
for day in range(0, len(confirmed)):
    death_rate.iloc[day] = (death.iloc[day]/confirmed.iloc[day])*10000

hospitalisation_rate_estimate = 0.05

hospitalisation_needed = confirmed.copy()
for day in range(0, len(confirmed)) :
    hospitalisation_needed.iloc[day] = active_cases.iloc[day]*hospitalisation_rate_estimate

#Visualisation maatje

countries = ['India', 'Saudi Arabia']
for country in countries :
    confirmed[country].plot(label=country)

plt.legend(loc='upper left')
plt.show()
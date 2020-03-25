import pandas as pd
confirmed = pd.read_csv("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
deaths = pd.read_csv("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
recovered = pd.read_csv("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv")

if(confirmed.keys()[-1] not in (recovered.keys())):
    recovered[confirmed.keys()[-1]] = recovered[recovered.keys()[-1]]

confirmed = confirmed.melt(['Province/State','Country/Region','Lat','Long'], var_name ="date", value_name="confirmed")
deaths = deaths.melt(['Province/State','Country/Region','Lat','Long'], var_name ="date", value_name="deaths")
recovered = recovered.melt(['Province/State','Country/Region','Lat','Long'], var_name ="date", value_name="recovered")

data = confirmed.merge(deaths, on=['Province/State','Country/Region','Lat','Long',"date"] )
data = data.merge(recovered,on=['Province/State','Country/Region','Lat','Long',"date"], how="left")

data['date'] = data['date'].apply(lambda x: "'"+x)

data = data.groupby(['Country/Region','date']).sum()
data['recovered'] = data['recovered'].astype(int)

data.to_csv("time_series_19-covid-transformed.csv" )

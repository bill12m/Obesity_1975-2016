import pandas as pd
import subprocess as sp
import matplotlib.pyplot as plt
import seaborn as sns

sp.call('clear', shell = True)

data_clean = pd.read_csv('data_clean.csv')
multi_index = pd.MultiIndex.from_frame(data_clean[['Continent','Country','Region']])
data_clean = data_clean.set_index(multi_index)
data_clean = data_clean.drop(columns = ['Continent', 'Country', 'Region'])

eastern_europe = data_clean.xs('Eastern Europe', level = 2).reset_index()
#eastern_europe['Region'] = eastern_europe['Country']

central_europe = ['Austria', 'Czechia', 'Hungary', 'Poland', 'Slovakia', 'Central Europe']
baltics = ['Estonia', 'Latvia', 'Lithuania', 'Baltics']
caucuses = ['Armenia', 'Azerbaijan', 'Georgia', 'Caucuses']
slavic_europe = ['Belarus', 'Republic of Moldova', 'Romania', 'Russian Federation', 'Ukraine', 'Slavic Europe']
list_of_lists = [eastern_europe, central_europe, baltics, caucuses, slavic_europe]

for index in eastern_europe.index:
    for region in list_of_lists:
        for country in region:
            if eastern_europe.at[index,'Country'] == country:
                eastern_europe.at[index,'Region'] = region[-1]

del(index, region)
regions = eastern_europe['Region'].unique()
for region in regions:
    df_region = eastern_europe['Region'] == region
    g = sns.relplot(data = df_region, kind = 'line',
                   x = 'Year', y = 'BMI', hue = 'Country')    
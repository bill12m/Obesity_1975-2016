import pandas as pd
import subprocess as sp

sp.call('clear', shell = True)

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

obesity = pd.read_csv('obesity_males_2016.csv')
data_raw = pd.read_csv('obesity-cleaned.csv')
del data_raw['Unnamed: 0']
data_raw['Region'] = obesity['Region']

for index in data_raw.index:
    country = data_raw.at[index,'Country']
    region = obesity[obesity['Country'] == country]
    data_raw.at[index,'Region'] = region.iat[0,3]
    
multi_index = pd.MultiIndex.from_frame(data_raw[['Country','Sex', 'Year']])

data_clean = pd.DataFrame(data_raw[['Obesity (%)','Region']])
data_clean = data_clean.set_index(multi_index)
del(multi_index)

for index in data_clean.index:
    left, right = data_clean.at[index,'Obesity (%)'].split(' ',1)
    if is_float(left) == True:
        float(left)
    else:
        left = 0
    data_clean.at[index,'BMI'] = left
data_clean['BMI'] = data_clean['BMI'].convert_dtypes(convert_integer = True)
del(left,right)

data_clean.to_csv('data_clean.csv')

countries = data_raw['Country'].unique()
for country in countries:
    new_df = data_clean.xs(country, level = 0)
    new_df.to_csv('bycountry/'+str(country)+'.csv')

genders = data_raw['Sex'].unique()
for gender in genders:
    new_df = data_clean.xs(gender, level = 1)
    new_df.to_csv('bygender/'+str(gender)+'.csv')

years = data_raw['Year'].unique()
for year in years:
    new_df = data_clean.xs(year, level = 2)
    new_df.to_csv('byyear/'+str(year)+'.csv')

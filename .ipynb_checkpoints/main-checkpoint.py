import pandas as pd
import subprocess as sp
import matplotlib.pyplot as plt
import seaborn as sns

sp.call('clear', shell = True)

continents = ['europe', 'asia', 'north_america', 'south_america', 'africa', 'oceania']

#Plot each continent's change in BMI by gender
for continent in continents:
    continent_df = pd.read_csv('bycontinent/'+str(continent)+'.csv')
    del(continent_df['Unnamed: 0'])
    #Remove 'Both sexes' from the gender column
    continent_df = continent_df.where(
        continent_df['Sex'] != 'Both sexes').dropna()
    
    sns.set_palette('Paired')
    g = sns.catplot(kind = 'bar', data = continent_df,
                    x = 'Year', y = 'BMI',
                    hue = 'Sex')
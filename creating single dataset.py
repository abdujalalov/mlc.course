import pandas as pd
import os

df1 = pd.read_csv('datasets/annual-working-hours-per-worker.csv')
df2 = pd.read_csv('datasets/gdp-per-capita-worldbank.csv')
df3 = pd.read_csv('datasets/life-expectancy.csv')
df4 = pd.read_csv('datasets/number-of-internet-users.csv')
df5 = pd.read_csv('datasets/population.csv')
df6 = pd.read_csv('datasets/share-with-mental-and-substance-disorders.csv')
df7 = pd.read_csv('datasets/suicide-death-rates_per_10k.csv')
df8 = pd.read_csv('datasets/unemployment-rate.csv')

df_list = [df1, df2, df3, df4, df5, df6, df7, df8]


#%%

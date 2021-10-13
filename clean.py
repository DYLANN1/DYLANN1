import pandas as pd
dataset = pd.read_csv('C:/Users/DYLAN/Downloads/FIT3179 asgn2/UFO.csv', encoding='cp1252')

dataset = dataset.drop('X.1', axis=1)
dataset = dataset.drop('X', axis=1)
dataset = dataset[dataset.Country != 'CANADA']

dataset.to_csv('C:/Users/DYLAN/Downloads/FIT3179 asgn2/UFO.csv')

import pandas as pd

TITANIC_CSV_DATA_URL = 'http://vincentarelbundock.github.io/Rdatasets/csv/datasets/Titanic.csv'



df = pd.read_csv('train.csv',index_col = 0)


print(df[['Survived','Age']].fillna(0))

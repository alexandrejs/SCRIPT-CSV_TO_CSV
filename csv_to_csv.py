import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

dados = pd.read_csv('C:\AB_NYC_2019.csv')

dados1 = dados[['id', 'host_id', 'price', 'number_of_reviews', 'last_review']]

dados1.to_csv(r'C:\AB_NYC_2019_edit.csv', index=False)




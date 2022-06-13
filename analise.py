#algebra linear 
import numpy as np
#leitura de dados
from pandas_datareader import data as wb    
#plots
import matplotlib.pyplot as plt

#ativos apple desde 2013
AAPL = wb.DataReader('AAPL', data_source='yahoo', start='2013-01-01', end='2022-06-13')

#divide o numero de fechamento pelo fechamento do dia anterior, usando shift
AAPL['simple_return'] = (AAPL['Adj Close'] / AAPL['Adj Close'].shift(1)) - 1
#print(AAPL['simple_return'])

#plotando a taxa de retorno simples
AAPL['simple_return'].plot(figsize=(10,5))
#plt.show()

#retorno medio diário ao longo dos dias
retorno_medio_diario = AAPL['simple_return'].mean() * 250
print('Retorno médio diário:', round(retorno_medio_diario, 5) * 100, '%')
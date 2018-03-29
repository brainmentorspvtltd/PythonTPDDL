import pandas

data = pandas.read_csv('weather_2012.csv')

X = data.iloc[:,0:3]
y = data.iloc[:,-1]
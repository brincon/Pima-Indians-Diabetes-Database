import pandas as pd

# cargamos el archivo
data = pd.read_csv("diabetes.csv")
print(data.head())

# tamaño del archivo
print(data.shape)

# nombre de las columnas
print(data.columns)

# información de cada tipo de datos
print(data.info())

#revisar nulos con headmap
print(data.isnull().sum())

# imprimir las estadisticas de los datos numericos con describe
print(data.describe().T)
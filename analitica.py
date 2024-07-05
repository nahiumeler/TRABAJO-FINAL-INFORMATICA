#https://colab.research.google.com/drive/182Q9SMP8A4OoeF3_YeYpg4nKZdO0FnTV?usp=sharing#scrollTo=lQWTLlgdRpgW 

import sqlite3
import pandas as pd

ruta_base = 'base1.db'
conexion = sqlite3.connect(ruta_base)
cursor = conexion.cursor()

cursor.execute("SELECT precio, servicios, nombre FROM profesionales")
data = cursor.fetchall()

# obtener los nombres de las columnas
columnas = ['precio', 'servicios', 'nombre']

# crear un dataframe con los datos obtenidos
df = pd.DataFrame(data, columns=columnas)

# guarda lo anterior en un archivo csv
df.to_csv('profesionales.csv', index=False)

conexion.close()

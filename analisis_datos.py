import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_profesionales = pd.read_csv('profesionales.csv')

if 'servicios' in df_profesionales.columns and 'precio' in df_profesionales.columns and 'nombre' in df_profesionales.columns:

    # 1. Precio promedio por servicio
    precio_promedio_por_servicio = df_profesionales.groupby('servicios')['precio'].mean().reset_index()
    plt.figure(figsize=(12, 8))
    sns.barplot(x='servicios', y='precio', data=precio_promedio_por_servicio)
    plt.title('Precio promedio por servicio')
    plt.xlabel('Servicio')
    plt.ylabel('Precio promedio')
    plt.xticks(rotation=45)
    plt.show()

    print ()
    # 2. Valor del servicio según cada oferente
    plt.figure(figsize=(12, 8))
    sns.barplot(x='nombre', y='precio', hue='servicios', data=df_profesionales)
    plt.title('Valor del servicio según cada oferente')
    plt.xlabel('Profesional')
    plt.ylabel('Precio')
    plt.xticks(rotation=45)
    plt.legend(title='Servicio')
    plt.show()

    print ()
    # 3. Distribución de precios por servicio en un diagrama de bogotes
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='servicios', y='precio', data=df_profesionales)
    plt.title('Distribución de precios por servicio')
    plt.xlabel('Servicio')
    plt.ylabel('Precio')
    plt.xticks(rotation=45)
    plt.show()

    print ()
    # 4. grafico de torta de la distribución de servicios
    plt.figure(figsize=(10, 6))
    df_profesionales['servicios'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de servicios ofrecidos por los profesionales')
    plt.ylabel('')
    plt.show()

    print ()
    # 5. Gráfico de barras de la cantidad de servicios ofrecidos por los profesionales
    servicios_count = df_profesionales['servicios'].value_counts()
    plt.figure(figsize=(12, 6))
    servicios_count.plot(kind='bar', color='brown')
    plt.title('Cantidad de profesionales que ofrece cada servicio')
    plt.xlabel('Servicios')
    plt.ylabel('Cantidad')
    plt.show()

else:
    print("Las columnas 'servicios', 'precio' y/o 'nombre' no existen en el DataFrame")

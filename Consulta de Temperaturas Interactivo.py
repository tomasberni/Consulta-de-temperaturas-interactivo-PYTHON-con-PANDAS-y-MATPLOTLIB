# MADE BY TOMAS BERNI

import pandas as pd
import matplotlib.pyplot as plt

ruta = "C:\\Users\\TB\\Downloads\\Datos+Meteorológicos_Arg_2023.csv"
df = pd.read_csv(ruta)

df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

lista_ciudades = []

for c in df['Ciudad']:
    if c not in lista_ciudades:
        lista_ciudades.append(c)

dict_meses = {1: 'Enero',
             2: 'Febrero',
             3: 'Marzo',
             4: 'Abril',
             5: 'Mayo',
             6: 'Junio',
             7: 'Julio',
             8: 'Agosto',
             9: 'Septiembre',
             10: 'Octubre',
             11: 'Noviembre',
             12: 'Diciembre'}

def consultar_temperaturas():
    while True:
        # solicitar la ciudad
        print("\nCiudades disponibles: ", lista_ciudades)
        ciudad_elegida = input("Elija la ciudad de la lista: ").title()
        
        # Solicitar el mes
        mes_elegido = int(input("Elija un número de mes (por ej. Enero = 1): "))
        
        # validar los inputs
        if ciudad_elegida not in lista_ciudades or mes_elegido not in range(1, 13):
            print("Ciudad o mes no válidos. Inténtale nuevamente.")
            continue
        
        # Crear el datafreme filtrado
        datos_ciudad_mes = df[(df['Ciudad'] == ciudad_elegida) & (df['Fecha'].dt.month == mes_elegido)]
        
        # Graficamos las temperaturas del dataframe
        plt.figure(figsize=(10, 6))
        plt.plot(datos_ciudad_mes['Fecha'], datos_ciudad_mes['Temperatura Maxima'], label="Maxima", color="red")
        plt.plot(datos_ciudad_mes['Fecha'], datos_ciudad_mes['Temperatura Minima'], label="Minima", color="blue")
        plt.title(f"Temperaturas en {ciudad_elegida} durante el mes de {dict_meses[mes_elegido]}")
        plt.xlabel("Fecha")
        plt.ylabel("Temperaturas")
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()
        
        # Preguntar al usuario si quiere continuar
        otra_consulta = input("¿Deseas continuar consultando? (s/n): ")
        if otra_consulta.lower() != 's':
            break

consultar_temperaturas()
import pandas as pd
#2 importar un csv
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame)

#4 hacer serie con una lista
# ages = pd.Series([23,45,7,34,6,63,36,78,54,34])
# print(ages)

#4.1 usa pd.data_range para crear una serie que vaya desde 05.01.2012 hasta 05.12.2012

# DatetimeIndex = pd.date_range(start = '05-01-2021', end = '05-12-2021')
# print(DatetimeIndex)

#4.2 usa my_series.apply para dividir entre 2 la siguiente serie (con pandas se puede usar directamente la barra para dividir)
# my_series = pd.Series([2, 4, 6, 8, 10])
# def dividir(n, x):
#     return n/x
# x= 2
# res= my_series.apply(dividir,args=(x,))
# print(res)
# divide=2
# my2= my_series / divide
# print(my2) (así también funciona)

#5 crea un dataframe con las siguientes datos y las etiquetas de las columnas serán: Brand, Model, Color

# data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]
# tabla=pd.DataFrame(data, columns= ["Brand", "Model", "Color"])
# print(tabla)

#5.1 Use this data to create a DataFrame but add a new row for a red, Tesla, model S.

# data = [
#     {
#         "brand": "Toyota",
#         "make": "Corolla",
#         "color": "Blue"
#     },
#     {
#         "brand": "Ford",
#         "make": "K",
#         "color": "Yellow"
#     },
#     {
#         "brand": "Porche",
#         "make": "Cayenne",
#         "color": "White"
#     }
# ]
# coches = pd.DataFrame(data)
# #print(coches)
# nueva = {"brand": "Tesla", "make": "Model S", "color": "Red"}
# coches = coches._append(nueva, ignore_index=True)
# print(coches)

#5.2 Crea un dataframe usando un .csv file located at .learn/assets/pokemon_data.csv, imprime la fila 133 y la columna 6 en el terminal.

# lista_Pokemon= pd.read_csv('.learn/assets/pokemon_data.csv')
# print(lista_Pokemon.iloc[133,6])

#5.3 Usa el mismo dataframe del anterior ejericio y usa la funcion DataFrame.head para imprimir las 3 primers filas del dataset.
# lista_Pokemon= pd.read_csv('.learn/assets/pokemon_data.csv')
# print(lista_Pokemon.head(3))

#5.4 usa el dataframe anterior y utiliza la funcion dataframe.tail para imprimir las 3 ultimas filas del dataset.
# lista_Pokemon= pd.read_csv('.learn/assets/pokemon_data.csv')
# print(lista_Pokemon.tail(3))

#5.5 usa el dataframe anterior e imprime solo la columna Name y Type y solo los 10 primeros elementos.
# lista_Pokemon= pd.read_csv('.learn/assets/pokemon_data.csv')
# print(lista_Pokemon[['Name','Type 1']][0:10])

#5.6 usa el datafraema anterior y, usando la funcion .loc, saca en el termianl todos los pokemon con un ataque mayor de 80.

# lista_Pokemon= pd.read_csv('.learn/assets/pokemon_data.csv')
# print(lista_Pokemon.loc[lista_Pokemon['Attack'] > 80])

#5.7 usa el dataframe anterior y usa la funcion loc con una operacion logica como indice.

# lista_Pokemon= pd.read_csv('.learn/assets/pokemon_data.csv')
# print(len(lista_Pokemon.loc[lista_Pokemon['Legendary']]))

#6 primero, imrprime las 10 primeras filas. luego, importa .learn/assets/us_baby_names_right.csv . Imprime las 5 primeras lineas en el terminal.

# lista_bebes= pd.read_csv('.learn/assets/us_baby_names_right.csv')
# print(lista_bebes[0:10])
# print(lista_bebes.head(5))

#6.1 quita la primera columna e imprime las 5 primeras lineas again.

# lista_bebes= pd.read_csv('.learn/assets/us_baby_names_right.csv')
# del lista_bebes[lista_bebes.columns[0]]
# print(lista_bebes.head(5))

#6.2 usa la funcion value_counts para sacar el valor de cada genero.

# lista_bebes= pd.read_csv('.learn/assets/us_baby_names_right.csv')
# genero=lista_bebes['Gender'].value_counts()
# print(genero)

#6.3 usa la funcion groupby para agrupar el dataframe por nombres. Usa la funcion sum() despues de agrupar para contar el numero de grupos obtenidos. Usa la funcion len(result) para contar el numero de grupos.

lista_bebes= pd.read_csv('.learn/assets/us_baby_names_right.csv')
grupos=lista_bebes.groupby("Name").sum()
print(len(grupos))

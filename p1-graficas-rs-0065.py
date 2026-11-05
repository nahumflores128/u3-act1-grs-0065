import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#crearemos nuestra tabla y la guardaremos con pandas
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# crea,os una lista de lista (conformado la tabla)
lista_redes_sociales=[fb, twt, ig, wsp, tel, lkn]
# print(lista_redes_sociales)
# utilizar panda para organizar la tabla(dataframe o marco de datos)
# a cada columna le ponemos nombre
df_redes_sociales=pd.DataFrame(lista_redes_sociales,columns=("Nombre","Cantidad","Es_Fb","Año"))
print(df_redes_sociales)
# creamos el archivo CSV y lo guardamos en CSV
df_redes_sociales.to_csv("redessociales.csv", index=False)
# crear grafics
# donde X es nombre es el eje horizontal
# donde Y es cantidad es el eje vertical
plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title("Grafica redes sociales 0065")
plt.xlabel("Nombre de la redes")
plt.ylabel("Cantidas de usuarios")
plt.show()
plt.scatter(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.show()
# Grafica dew barras
plt.bar(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.show()
# etiquetas y titulos
plt.title("redes sociales 0065")
plt.xlabel("las redes")
plt.ylabel("catidad de usuario")
# mostrar graficas
plt.show()
# ordenar grafica de barras de manera descendente
# de la mas grande a la pequeña
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"], df_rs_ordenar["Cantidad"])
plt.show()
# coloreando la grafica
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"], df_rs_ordenar["Cantidad"],
         color=["b","g","c","m","r","y"])
plt.show()

# Grafica de pastel
plt.pie(df_redes_sociales["Cantidad"],labels=df_redes_sociales["Nombre"])
plt.show()


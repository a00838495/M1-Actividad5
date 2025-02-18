import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
def space():

    print("\n")

#Ejercicio 1

#1) Crear un vector “x” con 10 ceros y mostrarlo
print("1")
x = np.zeros(10)
print(x)
space()

#2) Modificar el quinto elemento del vector x para que su valor sea 3.
print("2")
x[4] = 3
print(x)
space()

#3) Crear un vector “y” con valores del 1 al 20, de 1 en 1. Utiliza la función arange.
print("3")
y = np.arange(1,21,1)
print(y)
space()

#4)  Crear un vector “z” con valores del 1 al 20, de 2 en 2.
print("4")
z = np.arange(1,21, 2)
print(z)
space()

#5) Crear una matriz w de 3x2, con valores iniciales en 0.
print("5")
w = np.zeros((3,2))
print(w)
space()

#6) Modificar el elemento en la posición 2,2 de la matriz w para que su valor sea 5.
print("6")
w[1][1] = 5
print(w)
space()

#7)  Crear un vector de 5 elementos, con valores aleatorios enteros entre 1 y 10.
print("7")
rand_vector = np.random.randint(1,11, (5))
print(rand_vector)
space()

#8)  Crear el arreglo x1 de la lista [1,2,3]
print("8")
x1 = np.array([1,2,3])
print(x1)
space()

#9) Sumar 10 a cada elemento del vector
print("9")
x1 = x1 + 10
print(x1)
space()


#Ejercicio 2
datos = pd.read_csv("/content/titanic.csv")

#1) Generar un DataFrame con los datos del archivo
df = pd.DataFrame(datos)

#2) Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas

print(f"dimension del dataframe: {df.shape}\n" )
print(f"cantidad de datos en el dataframe: {df.size}\n")
print("Columnas del dataframe:")
print(df.columns)
space()
print("Tipo de valores por columna:")
print(df.dtypes)
space()
print("10 primeras filas:")
print(df.iloc[:10])
space()
print("ultimas 10 filas")
print(df.iloc[-10:])
space()

#3) Mostrar por pantalla los datos del pasajero con identificador 148.

print("3)")
print(df.loc[df["PassengerId"] == 148])

#4) Mostrar por pantalla las filas pares del DataFrame.

print(df.iloc[::2])

#5) Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.

first_class = df.loc[df.Pclass == 1]

first_class = first_class.sort_values(by= "Name")
print(first_class.Name)
space()

#6) Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.

print("porcentaje de gente que sobrevivio")
porc = (df.loc[df["Survived"]==1]).shape[0] / df.shape[0] * 100
print(porc)
print("porcentaje de gente que murio")
print(100 - porc)

#7) Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.

print("porcentaje de gente que sobrevivio por clase")
second_class = df.loc[df["Pclass"] == 2]
third_class = df.loc[df["Pclass"] == 3]
print(round((df.loc[(df["Survived"] ==1) & (df["Pclass"] == 1)]).shape[0] / first_class.shape[0] * 100, 2))
print(round((df.loc[(df["Survived"] ==1) & (df["Pclass"] == 2)]).shape[0] / second_class.shape[0] * 100, 2))
print(round((df.loc[(df["Survived"] ==1) & (df["Pclass"] == 3)]).shape[0] / third_class.shape[0] * 100, 2))

#8) Eliminar del DataFrame los pasajeros con edad desconocida.

space()
print("gente con datos de edad")
with_age = df.dropna(subset = ["Age"])
print(with_age.shape[0])

#9) Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.

space()
mujeres_1 = first_class.loc[first_class["Sex"] == "female"]
mujeres_2 = second_class.loc[second_class["Sex"] == "female"]
mujeres_3 = third_class.loc[third_class["Sex"] == "female"]
print("Edad media de mujeres")
print(mujeres_1["Age"].mean())
print(mujeres_2["Age"].mean())
print(mujeres_3["Age"].mean())


#10) Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
df["Menor"] = df["Age"] < 18
print(df[["Age", "Menor"]])
space()

#11) Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
kids_first_class_survived = df[(df["Menor"] == True) & (df["Survived"] == 1) & (df["Pclass"] == 1)]
kids_second_class_survived = df[(df["Menor"] == True) & (df["Survived"] == 1) & (df["Pclass"] == 2)]
kids_third_class_survived = df[(df["Menor"] == True) & (df["Survived"] == 1) & (df["Pclass"] == 3)]

print("Porcentaje de niños que sobrevivieron por clase")
print(f'primer clase: {kids_first_class_survived.shape[0] / df[(df["Menor"] == True) & (df["Pclass"] == 1)].shape[0] * 100 }')
print(f'segunda clase: {kids_second_class_survived.shape[0] / df[(df["Menor"] == True)  & (df["Pclass"] == 2)].shape[0] * 100}')
print(f'tercera clase: {kids_third_class_survived.shape[0] / df[(df["Menor"] == True) & (df["Pclass"] == 3)].shape[0] * 100}')
space()



#Ejercicio 3

#1) Generar un dataframe con los datos del archivo.

df2 = pd.read_csv("/content/casasboston.csv")

#2) Reduce el dataframe utilizando y renombrando las columnas de acuerdo a los siguiente:

esperados = ["CIUDAD", "INDICE_CRIMEN", "PCT_ZONA_INDUSTRIAL", "RIO_CHARLES", "N_HABITANTES_MEDIO", "VALOR_MEDIANO", "PCT_CLASE_BAJA", "EDAD"]
actuales = ["TOWN", "CRIM", "INDUS", "CHAS", "RM", "MEDV", "LSTAT", "AGE"]
df3 = pd.DataFrame()

i = 0
for columna in esperados:
    df3[columna] = df2[actuales[i]]
    i += 1
print(df3)

#3) Muestra los datos descriptivos para cada columna (conteo, media, cuartiles)
print(df3.describe())

#4) Genera un histograma de número de habitaciones promedio

df3["N_HABITANTES_MEDIO"].hist()
plt.show()

#5) Genera un diagrama de dispersión que muestre el índice de criminalidad vs la zona

plt.scatter(df3["INDICE_CRIMEN"], df3["PCT_ZONA_INDUSTRIAL"])
plt.show()

#6) Realiza un gráfico de barras que muestre por ciudad el valor mediano de la propiedad

plt.bar(df3["CIUDAD"], df3["N_HABITANTES_MEDIO"])
plt.show()

#7) Realiza un diagrama de caja para la variable de edad

plt.boxplot(df3["EDAD"])
plt.show()




#Ejercicio 4

pd.set_option('display.max.columns', 100)
# to draw pictures in jupyter notebook
%matplotlib inline

# we don't like warnings
# you can comment the following 2 lines if you'd like to
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('adult.data.csv')
data.head()

num_mujeres = data["sex"].value_counts().get("Female", 0)
print(f"Numero de mujeres: {num_mujeres}")

num_hombres = data["sex"].value_counts().get("Male", 0)
print(f"Numero de hombres: {num_hombres}")

mujeres = data.loc[data["sex"] == "Female"].copy()
edad_media_mujeres = mujeres['age'].mean()
print(f"Promedio de edad de las mujeres: {round(edad_media_mujeres, 2)}")

total_personas = data.shape[0]

total_alemanes = data.loc[data["native-country"] == "Germany"].shape[0]

print(f"Porcentaje de alemanes: {round(total_alemanes / total_personas , 4) * 100}%")

gana_50k = data.loc[data["salary"] == ">50K"]
gana_50k_edad_media = gana_50k["age"].mean()
gana_50k_desviacion = gana_50k["age"].std()

gana_menos_50k = data.loc[data["salary"] == "<=50K"]
gana_menos_50k_edad_media = gana_menos_50k["age"].mean()
gana_menos_50k_desviacion_edad = gana_menos_50k["age"].std()

print(f"Edad media de las personas que ganan mas de 50k: {round(gana_50k_edad_media, 2)}")
print(f"Desviacion estandar de las personas que ganan mas de 50k: {round(gana_50k_desviacion, 2)}")
space()
print(f"Edad media de las personas que ganan menos de 50k: {round(gana_menos_50k_edad_media, 2)}")
print(f"Desviacion estandar de las personas que ganan menos de 50k: {round(gana_menos_50k_desviacion_edad, 2)}")

gana_50k_sin = gana_50k.loc[gana_50k["education-num"] < 13].shape[0]
print(f"Hay {gana_50k_sin} personas que ganan mas de 50k sin tener por lo menos la preparatoria")

edad_clasf = data.groupby(["race", "sex"])["age"].describe()
edad_max = edad_clasf.loc[("Amer-Indian-Eskimo", "Male"), "max"]
print(f"Edad maxima de los hombres de Amer-Indian-Eskimo: {edad_max}")

max_hours = data["hours-per-week"].max()

personas_max_hours = data.loc[data["hours-per-week"] == max_hours]

personas_max_hours_count = personas_max_hours.shape[0]

personas_max_hours_50k = personas_max_hours.loc[personas_max_hours["salary"] == ">50K"].shape[0]
promedio_50k = personas_max_hours_50k / personas_max_hours_count * 100
print(f"Maximo numero de horas trabajadas por semana: {max_hours}")
print(f"Numero de personas que trabajan el maximo numero de horas: {personas_max_hours_count}")
print(f"Porcentaje de personas que ganan mas de 50k entre las que trabajan el maximo numero de horas: {round(promedio_50k, 2)}%")


group = data.groupby(["salary", "native-country"])["hours-per-week"].mean()
hours_min = group.loc[("<=50K", "Japan")]
hours_max = group.loc[(">50K", "Japan")]
print(hours_min)
print(hours_max)

sns.boxplot(data = data, x = "salary", y = "hours-per-week")
plt.show()

sns.boxplot(data = data, x = "salary", y = "age")
plt.show()



#Ejercicio 5 Laboratorio 1


#3
sales = pd.read_csv("sales_data_type.csv")

#4
#Eliminar espacios de los nombres de las columnas
columnas = sales.columns.tolist()
nuevas_columnas = []


for columna in columnas:
  nuevas_columnas.append(columna.replace(" ", "_"))
sales.columns = nuevas_columnas

#5
#Tipos de datos por columna
print(sales.dtypes)



#6
total_16_17 = sales["2016"].sum() + sales["2017"].sum()
print(total_16_17)

#Cuando tratas de sumer las ventas totales se suman en forma de string, para corregir esto debemos cambiarlo a float
years = ["2016", "2017"]
if sales["2016"].dtype == "object":
  for year in years:
    sales[year] = sales[year].str.replace("$", "")
    sales[year] = sales[year].str.replace(",", "")
    sales[year] = sales[year].astype(float)
total = (sales["2016"].sum() + sales["2017"].sum())
print(f"total de ventas en 2016 y 2017 es de: ${total}")


#7
sales["Customer_Number"] = sales["Customer_Number"].astype(int)
sales["Customer_Name"] = sales["Customer_Name"].astype(str)
if sales["Percent_Growth"].dtype == "object":
  sales["Percent_Growth"] = sales["Percent_Growth"].str.replace("%", "")
sales["Percent_Growth"] = sales["Percent_Growth"].astype(float)
sales
if sales["Jan_Units"  ].dtype == "object":
  sales["Jan_Units"] = sales["Jan_Units"].str.replace("Closed", "0")
sales["Jan_Units"] = sales["Jan_Units"].astype(float)
for i in range(len(sales["Active"])):
  item = sales.loc[i, "Active"]
  if item == "Y":
    sales.loc[i, "Active"] = True
  else:
    sales.loc[i, "Active"] = False
sales["Active"] = sales["Active"].astype(bool)


#8 Agregar columna de fecha

fechas = []
for i in range(sales.shape[0]):
  fecha = f"{sales.loc[i, 'Month']}/{sales.loc[i, 'Day']}/{sales.loc[i, 'Year']}"
  fechas.append(fecha)
sales["Start_date"] = pd.to_datetime(fechas)
#sales["Start_date"].to_datetime()
sales

#9 
print("Primeras 3 filas y columnas del DataFrame")
print(sales.iloc[:3, :3])
space()
print("Primeras 2 columnas y filas con indices 1 y 2")
print(sales.iloc[[1,2], :2])



#10
print(sales.sort_values(by = "2016", ascending = True))


#11 
media_2016 = sales["2016"].mean()
print(f"La media_2016 fue de ${media_2016}")


#12
sales.describe()


# Laboratorio 2



#1
iris = pd.read_csv("iris.csv")
iris

#2
iris.dtypes
iris["variety"] = iris["variety"].astype(str)

assert all(isinstance(x, str) for x in iris["variety"])

#3
keys = list(sns.palettes.SEABORN_PALETTES.keys())


titulos = [iris.columns.tolist()]
for i in range(4):
  x = random.randint(0, 10)
  color = sns.palettes.SEABORN_PALETTES[keys[x]]
  sns.boxplot(data = iris.iloc[:, i], palette = color)
  plt.title(titulos[0][i])
  plt.show()

#4


sns.boxplot(data = iris , x ="variety", y = "sepal.width")
plt.title("Sepal width")
plt.xlabel("Especie")
plt.show()

#5 
sns.boxplot(data = iris , x ="variety", y = "sepal.width")
plt.title("Sepal width")
plt.xlabel("Especie")
sns.swarmplot(x="variety", y="sepal.width", data=iris, color="black")

plt.show()

#6
fig, axs = plt.subplots(2, 2, figsize = (11, 11))

sns.boxplot(data = iris , x ="variety", y = "sepal.width", ax = axs[0, 0])
sns.boxplot(data = iris , x ="variety", y = "sepal.length", ax = axs[0, 1])
sns.boxplot(data = iris, x ="variety", y = "petal.length", ax = axs[1,0])
sns.boxplot(data = iris, x = "variety", y = "petal.width", ax = axs[1,1])

axs[0,0].set_title("Sepal width")
axs[0,1].set_title("Sepal length")
axs[1,0].set_title("Petal length")
axs[1,1].set_title("Petal width")

plt.show()

'''En este proyecto, se comparó las preferencias musicales de las ciudades de Springfield y Shelbyville. Se estudiaron 
datos reales de transmisión de música online para probar la hipótesis de "La actividad de los usuarios difiere según el día
de la semana y dependiendo de la ciudad", y comparar el comportamiento de los usuarios de estas dos ciudades.'''

import pandas as pd

df = pd.read_csv("/datasets/music_project_en.csv")

# Se muestran las primeras 10 filas de la tabla para obtener observaciones de la información. 
df.head(10)

# Se obtiene información general sobre la tabla.
df.info()

'''Según la documentación, contiene 7 columnas que almacenan los mismos tipos de datos: "object".

Podemos ver tres problemas con el estilo en los encabezados de la tabla:
    - Algunos encabezados están en mayúsculas, otros en minúsculas.
    - Hay espacios en algunos encabezados.
    - Se podría poner un "_" en vez de espacios.
    
En los datos observamos lo siguiente:
    1.   Los datos presentados en las filas son tipo string, significando que son variables categoricas.
    2.   Hay suficientes datos para hacer una comprobación de la hipótesis.
    3.   Se observan valores ausentes y duplicados por lo que será necesario limpiar la infomración.'''
    
# Muestra los encabezados
df.columns

# Bucle 'for' para iterar sobre los encabezados y arreglarlos
new_columns = []

for column in df.columns:
    new_column = column.lower()
    new_column = column.strip()
    new_columns.append(new_column)

df.columns = new_columns

print(df.columns)

# Metodo 'snake_case'
column_new = {"userid":"user_id"}

df.rename(columns = column_new, inplace = True)

print(df.columns)

'''Limpieza de valores'''

# Encontrar el número de valores ausentes en la tabla
print(df.isnull().sum())

# Reemplazar los valores ausentes creando una lista e iterando sobre ella
missing_values = []

for columns in ["track", "artist", "genre"]:
    if df[column].isnull().any():
        missing_values.append(column)
    
for column in missing_values:
    df[column] = df[column].fillna("unkown")

print(df.isnull().sum())

# Encontrar el número de valores duplicados explícitos en la tabla
print(df.duplicated().sum())

# Eliminar los duplicados
df = df.drop_duplicates()

print(df.duplicated().sum())

# Encontrar los valores duplicados implícitos en la columna "genre"
print(df["genre"].unique())

# Corregir valores implícitos mediante una función
def replace_wrong_genres(wrong_genres, correct_genres):
    for wrong_genre in wrong_genres:
        df["genre"] = df["genre"].replace(wrong_genre, correct_genre)
        
wrong_genre = ["hip", "hop", "hip-hop"]
correct_genre = "hiphop"

replace_wrong_genres(wrong_genre, correct_genre)

print(df["genre"].unique())

'''Al analizar los duplicados, hubo valores que representan el mismo género escritas de diferentes formas. Este tipo de 
variaciones causan inconsistencias en los datos, especialmente al intentar hacer un análisis.

Para abordar esta situación, se utilizó la función llamada "replace_wrong_genres()" que toma dos argumentos:
    - Una lista de géneros incorrectos (wrong_genres), que son los valores que a reemplazar.
    - Un valor correcto (correct_genre).

El proceso consistió en iterar sobre la lista de géneros incorrectos y usar el método ".replace()" para reemplazar los 
valores, obteniendo así un reemplazo exitoso por "hiphop", teniendo un término uniforme.'''

# Prueba de hipótesis

'''La hipótesis afirma que existen diferencias en la forma en que los usuarios de Springfield y Shelbyville consumen música. 
Para comprobar esto, se considerarán datos de tres días: lunes, miércoles y viernes.'''

# Para evaluar la actividad de los usuarios en cada ciudad, se agrupan los datos por ciudad y encuentran la cantidad de 
# canciones reproducidas en cada grupo.'''
print(df.groupby(by = "city")["user_id"].count())

# Agrupar los datos por día y encontrar el número de canciones reproducidas.
songs_per_day = df.groupby(by = "day")["user_id"].count()

print(songs_per_day.loc[["Monday", "Wednesday", "Friday"]])

# Declarar la función 'number_tracks()' con dos parámetros: 'day=' y 'city='.
def number_tracks(day, city):
    
    # Almacenar las filas del DataFrame donde el valor en la columna 'day' es igual al parámetro day=
    # y filtrar las filas donde el valor en la columna 'city' es igual al parámetro city=
    filtered_data = df[(df["day"] == day) & (df["city"] == city)]
    
    # Extraer la columna 'user_id' de la tabla filtrada y aplica el método count()
    track_count = filtered_data["user_id"].count()
    
    # Devolver el número de valores de la columna 'user_id'
    return track_count

print(number_tracks("Monday", "Springfield"))
print(number_tracks("Monday", "Shelbyville"))
print(number_tracks("Wednesday", "Springfield"))
print(number_tracks("Wednesday", "Shelbyville"))
print(number_tracks("Friday", "Springfield"))
print(number_tracks("Friday", "Shelbyville"))

'''A partir de los resultados obtenidos, se observa que la mayor actividad en Springfield son los viernes, lo cual podría 
indicar que las personas en esa ciudad tienden a interactuar más en este día. Mientras que en Shelbyville, podría sugerir 
una menor variabilidad en el comportamiento de los usuarios a lo largo de la semana, ya que no muestra un día de moda.

La diferencia entre los totales de cada ciudad también resalta que Springfield tiene una mayor base de usuarios, lo cual 
podría implicar mayor actividad en esa ciudad.'''
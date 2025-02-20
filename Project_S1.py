'''Como parte del equipo de análisis, lo primero que se debe hacer es evaluar la calidad de una muestra de datos 
recopilados y prepararla para un analisis posterior.'''

# Datos proporcionado por el cliente
users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

# Extracto de data
user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']

'''Se puede identificar que algunos datos en la columna de los nombres incluyen guiones bajos y espacios innecesarios, por 
lo que hay que eliminarlos, y adicional también es necesario homogenizar todo en minúsculas. 
Los datos de la columna "user_age" son de clase "float", por lo que se deberá cambiar a clase "int"'''

# Se implementan los cambios identificados en la columna "user_name"
user_name = ' mike_reed '
user_name = user_name.strip()
user_name = user_name.replace("_"," ")
user_name = user_name.split() # Se divide la variable "user_name" en dos subcadenas.

print(user_name)

# Se implementa el cambio de clase a la columna "user_age"
user_age = 32.0
user_age = int(user_age)

print(user_age)

'''Hay que de considerar escenarios en los que el valor de "user_age" no se pueda convertir en un número entero. Para 
evitar que el sistema se bloquee, hay que tomar medidas con anticipación.'''

# Se presenta un código que intente convertir la variable "user_age" en un número entero. Si el intento falla, mostramos un 
# mensaje pidiendo al user que proporcione su edad como un valor numérico.
user_age = 'treinta y dos'

try:
    user_age = int(user_age)
except:
    print('Please provide your age as a numerical value.')
    
'''El equipo de dirección de Store 1 pidió ayuda para organizar los datos de sus clientes para analizarlos y gestionarlos.'''

users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

#Se ordena esta lista por ID de usuario de forma ascendente.
users.sort()

print(users)

'''Se tiene la información de los hábitos de consumo de nuestros usuarios, incluyendo la cantidad gastada en cada una de 
sus categorías favoritas. La dirección está interesada en conocer la cantidad total gastada por el usuario.'''

fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]

# Se calcula el valor total gastado en las categorías
total_amount = sum(spendings_per_category)

print(total_amount)

'''La dirección de la empresa pide un resumen de toda la información de un usuario.'''

user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

# Se crea una cadena formateada que utilice información de las variables "user_id", "user_name" y "user_age".
user_info = "User {} is {} who is {} years old.".format(user_id,user_name[0],user_age)
print(user_info)

'''La dirección también quiere una forma fácil de conocer la cantidad de clientes con cuyos datos cuentan.'''
users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

#  Se crea una cadena formateada que muestre la cantidad de datos de clientes registrados.
user_info = f"We have registered data on {len(users)} clients."
print(user_info)

# Se aplican todos los cambios a un extracto de la lista de clientes
users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
]

users_clean = []

    # Limpieza al primer usuario
user_name_1 = users[0][1].strip().replace("_"," ")
user_age_1 = int(users[0][2])
user_name_1 = user_name_1.split()
users_clean.extend([users[0][0], user_name_1, user_age_1, users[0][3], users[0][4]])

    # Limpieza al segundo usuario
user_name_2 = users[1][1].strip().replace("_"," ")
user_age_2 = int(users[1][2])
user_name_2 = user_name_2.split()
users_clean.extend([users[1][0], user_name_2, user_age_2, users[1][3], users[1][4]])

    # Limpieza al tercer usuario
user_name_3 = users[2][1].strip().replace("_"," ")
user_age_3 = int(users[2][2])
user_name_3 = user_name_3.split()
users_clean.extend([users[2][0], user_name_3, user_age_3, users[2][3], users[2][4]])

print(users_clean)
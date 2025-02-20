'''En el último fragmento del "Project_S1" se escribió un código para:
        - Eliminar todos los espacios iniciales y finales de los nombres, así como cualquier guion bajo.
        - Convertir todas las edades en números enteros.
        - Separar todos los nombres y apellidos en una sublista.

Ahora se hará una función para que usarla en cualquier cliente.'''

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

# Se define la función
def clean_user(user_info, name_index, age_index):
    # Elimina del nombre espacios iniciales y finales, así como guiones
    user_name = user_info[name_index].strip().replace("_"," ")
    # Convierte la edad en entero
    user_age = int(user_info[age_index])
    # Separa el nombre y el apellido en una sublista
    user_name = user_name.split()

    # Se prepara la lista con la información completa del usuario
    user_info[name_index] = user_name
    # Se reemplaza el nombre y la edad originales con los datos limpios
    user_info[age_index] = user_age

    return user_info

# Test de la función
test_user = ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]
name_index = 1
age_index = 2

print(clean_user(test_user, name_index, age_index))
      
'''Todas las categorías favoritas están almacenadas en mayúsculas, por lo que habrá que llenar una nueva lista con las 
mismas categorías, pero en minúsculas'''

fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []

# Se itera sobre cada categoría en 'fav_categories', para convertir a minúsculas y se agrega a 'fav_categories_low'
for category in fav_categories:
    fav_categories_low.append(category.lower())

print(fav_categories_low)

'''Ahora se hace lo mismo, pero para cada uno de los usuarios de la empresa.'''

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

# Lista vacía dónde se agregarán los nuevos valores.
users_categories_low = []

# Se itera sobre cada categoría en 'user', para convertir a minúsculas y se agrega a 'categories_low'
for user in users:
    categories_low = []
    # Anexa las categorías en minúsculas a la lista de categorías original del usuario
    for category in user[3]:
        # Convierte la categoría a minúsculas
        lowered_category = category.lower()
        # Añade la categoría a la lista original
        categories_low.append(lowered_category)
    
    # Elimina la lista de categorías original (posición 3) usando 'pop()'
    user.pop(3)
    
    # Inserta la nueva lista de categorías en minúsculas usando 'insert()'
    user.insert(3, categories_low)

    # Agrega el usuario actualizado a la lista 'users_categories_low'
    users_categories_low.append(user)

print(users_categories_low)

# Se complementa el código de la función 'clear_user' para limpiar la categoría 'fav_categories'
def clean_user(user_info, name_index, age_index, cat_index):
    # Pone todo en minúsculas y elimina del nombre espacios iniciales y finales, así como guiones
    user_name_1 = user_info[name_index].lower().strip().replace("_", " ")

    # Convierte la edad en entero
    user_age_1 = int(user_info[age_index])

    # Separa el nombre y el apellido en una sublista
    user_name_1 = user_name_1.split()

    # Limpia las categorías, poniéndolas en minúsculas
    categories_low = [category.lower() for category in user_info[cat_index]]

    # Prepara la lista con la información completa del usuario y
    # reemplaza el nombre, la edad y las categorías originales con los datos limpios
    user_info[name_index] = user_name_1
    user_info[age_index] = user_age_1
    user_info[cat_index] = categories_low

    return user_info

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

name_index = 1
age_index = 2
cat_index = 3
users_cleaned = []

for user in users:
    user_cleaned = clean_user(user, name_index, age_index, cat_index)
    users_cleaned.append(user_cleaned)

print(users_cleaned)

'''La empresa desea conocer sus ingresos totales y pide que se proporcione este valor.'''

users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

revenue = 0

# Se utiliza un bucle 'for' para iterar en 'users'
for user in users:
    # Extrae los gastos de los usuarios
    spending_list = user[4]
    # Suma los gastos
    revenue += sum(spending_list)

print(revenue)

'''La empresa quiere ofrecer descuentos a sus clientes leales. Los clientes que realizan compras por un importe total mayor
a $1500 se consideran leales y recibirán un descuento.'''

# Se crea un bucle 'while' que compruebe el importe total gastado.
from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent < target_amount:
    # Genera un número aleatorio de 30 a 80
    new_purchase = randint(30, 80)
    total_amount_spent +=  new_purchase

print(total_amount_spent)

# Se recorre la lista de usuarios para identificar clientes menores a 30 años.
users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

for user in users:
    if user[2] < 30:
        print(user[1][0])

# Se recorre la lista de usuarios mediante un bucle para identificar clientes menores a 30 años y con gastos mayores a 1K USD.
users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

for user in users:
    edad = user[2]
    gastos = user[4]
    
    if edad < 30 and sum(gastos) > 1000:
        print(user[1][0])
        
# Se recorre la lista de usuarios mediante un bucle para identificar clientes que hayan comprado ropa.
users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

for user in users:
    if "clothes" in user[3]:
            print(user[1][0],user[2])
            
'''La dirección requiere de una función que proporcione información sobre los clientes, incluyendo sus nombres, edades y 
gasto total, filtrada por categorías específicas.

La función devuelve una lista de sublistas. Cada sublista contiene:
    - El número ID del cliente.
    - Una sublista con el nombre y apellido del cliente.
    - La edad del cliente.
    - Un entero que representa la cantidad total gastada por el cliente.
'''
# Se define la función
def get_client_by_cat(users, id_index, name_index, age_index, category_index, amounts_index, filter_category):
    
    filtered_clients = []
    
    for user in users:
        if filter_category in user[category_index]:
            total_spent = sum(user[amounts_index])
            
            client_info = [
                user[id_index],
                user[name_index],
                user[age_index],
                total_spent
            ]
            
            filtered_clients.append(client_info)
    
    return filtered_clients

# La lista de usuarios
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]
]

# Llama a la función con la categoría 'home'
result = get_client_by_cat(users, 0, 1, 2, 3, 4, "home")

print(result)
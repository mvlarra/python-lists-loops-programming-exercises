import datetime

people = [
	{ "name": 'Joe', "birth_date": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birth_date": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birth_date": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birth_date": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birth_date": datetime.datetime(2003,4,24) }
]

def calculate_age(date_of_birth):
    today = datetime.date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age

def format_greeting(person):
    # Your code here
    name = person["name"]
    age = calculate_age(person["birth_date"])
    return f"Hello, my name is {name} and I am {age} years old"
    

name_list = list(map(format_greeting, people))

print(name_list)



#*************** EXPLICACION: *****************************************
# Este código genera una lista de saludos personalizados con el nombre y 
# la edad calculada de cada persona de la lista people. 
# Vamos a desglosarlo paso a paso:

#   1. Importar datetime ************************
#   El módulo datetime permite trabajar con fechas y horas. 
#   Es usado aquí para manejar las fechas de nacimiento y calcular edades.

#   2. La lista peoplE ************************
#   Esta es una lista de diccionarios. 
#   Cada diccionario representa a una persona con las claves:
#       "name": el nombre de la persona.
#       "birth_date": su fecha de nacimiento, representada como un objeto datetime.

#   3. La función calculate_age ************************
#   Esta función calcula la edad de una persona dada su fecha de nacimiento date_of_birth:
#   Obtiene la fecha actual con datetime.date.today().
#   Calcula la diferencia de años entre el año actual y el de nacimiento (today.year - date_of_birth.year).
#   Ajusta el resultado si la persona aún no ha cumplido años este año:
#   Compara (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
#       Si es True, resta 1 porque aún no ha llegado su cumpleaños.
#       Si es False, no resta nada porque ya lo cumplió.

#   4. La función format_greeting ************************
#   Esta función toma un diccionario de persona y:
#       Extrae su nombre (person["name"]).
#       Calcula su edad usando la función calculate_age con la 
#       fecha de nacimiento (person["birth_date"]).
#       Devuelve un saludo formateado con el nombre y la edad.

#   5. Generar la lista de saludos ************************
#   La función map aplica la función format_greeting a cada elemento de la lista people.
#   list(map(...)) convierte el resultado de map (un iterador) en una lista.
#   La lista resultante (name_list) contiene los saludos personalizados para cada persona.

#   6. Imprimir la lista ************************
#   Se imprimen los saludos en la consola. La salida será algo así:
# 
#   [
#     'Hello, my name is Joe and I am 38 years old',
#     'Hello, my name is Bob and I am 49 years old',
#     'Hello, my name is Erika and I am 35 years old',
#     'Hello, my name is Dylan and I am 25 years old',
#     'Hello, my name is Steve and I am 21 years old'
#   ]

#   Resumen ************************
#   El código toma una lista de personas con sus fechas de nacimiento, 
#   calcula su edad actual y genera saludos personalizados en un formato específico. 
#   Combina el manejo de fechas, cálculos lógicos y formato de cadenas en Python.











# ChatGPT puede cometer errores. Considera verificar la información importante.
# ?

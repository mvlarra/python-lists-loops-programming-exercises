names = ['Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Logan','Sophia','Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail','Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia','Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria','Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']

# Your code here

given_sting = "am"

def filter_names_with(name):
    if given_sting.lower() in name.lower(): return name

Selected_Names = list(filter(filter_names_with, names))

print(Selected_Names)


# ***** SOLUCION DEL CURSO ***********
# filtered = list(filter(lambda name: 'am' in name.lower(), names))
# print(filtered)

# Explicacion de LAMBDA:
# Un lambda es una forma de crear una función corta y anónima en una sola línea. 
# La sintaxis es:
    # lambda argumentos: expresión
    # Aquí:
    # lambda name: 'am' in name.lower()
    # Toma un argumento name (un elemento de la lista names).
    # Devuelve True si 'am' está presente en el nombre convertido a minúsculas (name.lower()), y False si no.
    # Ejemplo: 
    # Si el nombre es "Samuel":
        # name.lower() convierte "Samuel" a "samuel".
        # 'am' in name.lower() evalúa si 'am' está contenido en "samuel". 
        # En este caso, es True.
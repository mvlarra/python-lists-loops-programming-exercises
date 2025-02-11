tasks = [
	{ "label": 'Eat my lunch', "done": True },
	{ "label": 'Make the bed', "done": False },
	{ "label": 'Have some fun', "done": False },
	{ "label": 'Finish the replits', "done": False },
	{ "label": 'Replit the finishes', "done": True },
	{ "label": 'Ask for a raise', "done": False },
	{ "label": 'Read a book', "done": True },
	{ "label": 'Make a trip', "done": False }
]

# Your code here

def filter_done_tasks(task):
    return task["done"]

done_tasks = list(filter(filter_done_tasks, tasks))

print(done_tasks)

# NOTES: *********************************

# La lista tasks es una lista de diccionarios en Python. 
# Cada diccionario tiene dos claves:
# 	"label": Una descripción de la tarea como texto.
# 	"done": Un valor booleano (True o False) que indica si la 
#	 tarea está completada.

# La función filter_done_tasks:
# Esta función toma un diccionario (representando una tarea) 
# como argumento y devuelve el valor del campo "done".
# Si el valor de task["done"] es True, la función devuelve True.
# Si el valor de task["done"] es False, devuelve False.

# filter es una función incorporada de Python que selecciona 
# elementos de una lista (o iterable) en función de si una 
# condición es verdadera o falsa.
# Sintaxis:
# filter(function, iterable)
# function: Una función que devuelve True o False para cada elemento del iterable.
# iterable: La lista (o cualquier otro iterable) que queremos filtrar.
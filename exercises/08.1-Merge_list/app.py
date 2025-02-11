chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    merged_list = []
    for item in chunk_one:
        merged_list.append(item)
    for item in chunk_two:
        merged_list.append(item)
    return merged_list
print(merge_list(chunk_one, chunk_two))

# ****************   ¿Por qué no se necesitan parámetros?   *****************
#
# No es necesario incluir parámetros de inicio y fin al usar un bucle for con listas en Python
# porque el bucle for está diseñado para iterar automáticamente sobre todos los elementos 
# de una lista (o cualquier iterable), desde el primer elemento hasta el último. 
# Esto hace que el código sea más limpio y fácil de leer.
#   Cuando usas:
#   
#     for item in my_list:
#           print(item)
#   El for:
#   Sabe dónde empezar: Siempre comienza desde el primer elemento de la lista.
#   Sabe dónde terminar: Automáticamente se detiene cuando no quedan más elementos en la lista.
#   Python maneja esto internamente mediante un iterador, 
#   que recorre cada elemento uno a uno hasta que llega al final.


# ****************    ¿Y si quieres controlar inicio y fin?  ****************   

# Si necesitas controlar desde dónde empezar y dónde terminar, 
# puedes usar rebanado de listas o un índice manual con range().
# Ambos métodos son útiles si necesitas trabajar solo con una parte específica de la lista.

    # Usando rebanado (slicing):
        # my_list = [10, 20, 30, 40, 50]
        # for item in my_list[1:4]:  # Del índice 1 al 3 (el índice 4 no se incluye)
        #     print(item)
        # # Salida: 20, 30, 40

    # Usando índices con range():
        # my_list = [10, 20, 30, 40, 50]
        # for i in range(1, 4):  # Del índice 1 al 3
        #     print(my_list[i])
        # # Salida: 20, 30, 40


# ****************    Conclusión  ****************    
# No necesitas especificar inicio y fin al usar un for con listas porque 
# Python automáticamente itera por completo la lista. 
# Pero, si quieres controlar la porción de la lista que recorres, 
# puedes usar rebanado o el índice con range(). 
my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here

def max_integer(lst): 
    aux = lst[0]  # Comenzamos con el primer elemento como máximo
    for num in lst:  # Recorremos los elementos de la lista
        if num > aux:  # Si encontramos un número mayor
            aux = num  # Lo asignamos como el nuevo máximo
    return aux 

print(max_integer(my_list))
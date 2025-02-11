my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here

def sum_odds(list):
    total = 0
    
    for num in list:
        if num % 2 !=0:
            total += num  
            # Use el operador de suma acumulativa que es "+=" Ejemplo x+=3 es igual a hacer x = x + 3
            # aqui "total = total + num" es lo mismo que poner "total += num"
            # print(total)    
    return total
    
print(sum_odds(my_list))
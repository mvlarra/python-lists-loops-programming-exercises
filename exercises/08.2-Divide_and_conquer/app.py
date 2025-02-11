list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here

def sort_odd_even(lista):
    odd_List = []
    even_List = []
    for item in lista:
        if item % 2 == 0:
            even_List.append(item)
            #print("Pares: " + format(even_List))
        else:
            odd_List.append(item)
            #print("Impares: " + format(odd_List))
    return (odd_List + even_List)
       
print(sort_odd_even(list_of_numbers))

# ******* Other solution *******
# def sort_odd_even(numbers):
#     sorted_list = []
#     even = []
#
#     for i in numbers:
#         if (i % 2 == 1):
#             sorted_list.append(i)
#         elif (i % 2 == 0):
#             even.append(i)
#
#     sorted_list.extend(even)
#     return sorted_list
#
# print(sort_odd_even(list_of_numbers))

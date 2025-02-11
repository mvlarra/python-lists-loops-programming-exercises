incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here

def data_transformer(name):
    return name['name'] + ' ' + name['last_name']

Full_name = list(map(data_transformer, incoming_ajax_data))
print(Full_name)


# OTRA SOLUCION:

# def data_transformer(data_list):
#     return list(map(lambda element: f"{element['name']} {element['last_name']}", data_list))

# print(data_transformer(incoming_ajax_data))
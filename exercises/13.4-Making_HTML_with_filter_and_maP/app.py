all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here

def generate_li(color):
    return f"<li>{color['label']}</li>"

def filter_colors(color):
    return color["sexy"]

sexy_colors = list(filter(filter_colors, all_colors))
# esta funcion filtra los colores que son sexy, 
# es decir que tienen true en esa key, y los convierte a una lista

formatted_colors = list(map(generate_li, sexy_colors))
# esta funcion devuelve una lista de string, 
# donde cada string es un li con el key label de cada color

print(formatted_colors)








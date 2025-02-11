people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here

    # Mi código aquí usando un bucle for
    updated_people = []
    for person in people:
        if person != person_name:  # Si no es el nombre a eliminar, lo añadimos a la nueva lista
            updated_people.append(person)
    return updated_people

    # Mi codigo aqui Si no usara el bucle for:
    # NO esta utilizando un bucle para recorrer la lista de people, si no que usa directamente el método .remove() para eliminar un elemento, 
    # Lo cual es válido, pero no cumple con el requisito del test de usar el for.

        # updated_people = list(people)
        # if person_name in updated_people:
        #     updated_people.remove(person_name)
        # return updated_people

# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))

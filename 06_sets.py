###### Sets ###### es un tipo de dato
my_set = set()                 # Formas de declarar un set  tipo set
my_other_set = {}              # Formas de declarar un set tipo dict

print(type(my_set))            # Tipo / Clase "set"
print(type(my_other_set))      # Tipo / Clase "dict" Diccionario cuando esta {}

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))     # Cuando tiene Elementos el tipo es  "set"

print(len(my_other_set))      # Cuenta los 3 elementos del set

#print(my_other_set[1])       # No se puede acceder al indice como en una lista

my_other_set.add("MoureDev")  # No es una estructura Ordenado
print(my_other_set)

my_other_set.add("MoureDev")  # No admnite repetidos
print(my_other_set)

print("Moure" in my_other_set) # Verificar si existe un elemento en UN set
print("Mouri" in my_other_set)

my_other_set.remove("Moure")  # Borrar un elemento, se pueden hacer  operaciones
print(my_other_set)

my_other_set.clear()          # Borrar Todos los elementos 
print(my_other_set)

my_set = {"Brais", "Moure", 35}  # Convertir a lista y buscar por indice [0]
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))

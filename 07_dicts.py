###### Dictionaries ###### Se pueden guardar datos en estructuras tipo clave valor

my_dict = dict()             # Formas de declarar un diccionario
my_other_dict = {}           # Formas de declarar un diccionario
print(type(my_dict))         # Tipo "dict"
print(type(my_other_dict))   # Tipo "dict"

my_other_dict = {"Nombre":"Brais", "Apellido": "Moure", "Edad": 35, 1:"Python"} #Claves/Valor

my_dict = {
     "Nombre":"Brais",
     "Apellido": "Moure",
     "Edad": 35,
     "Lenguajes": {"Python", "Swift", "Kotlin"}, #Agregar un set dentro del dict
     1: 1.77
     }
print(my_dict)         
print(my_other_dict)

print(len(my_other_dict))  #Imprime 4 - por 4 elementos de clave/valor
print(len(my_dict))        #Imprime 5 - por 5 elementos de clave/valor

print(my_dict["Nombre"])  #LLamar a un elemento del diccionario

my_dict["Nombre"] = "Pedro" #Actualizar valor
print(my_dict["Nombre"])

my_dict["Calle"] = "MoureDev" #Agregar un nuevo campo al diccionario
print(my_dict)

del my_dict["Calle"]   #Eliminar un solo elemento con "del"
print(my_dict)

print("Moure" in my_dict)  # Busca por Clave por eso da "False" 

print(my_dict.items())  # Con "items" Retorna Listado completo
print(my_dict.keys())   # Con "keys" Retorna Listado solo de Clave
print(my_dict.values())   # Con "items" Retorna Listado solo de Valores

my_new_dict = dict.fromkeys(my_dict) #Crear un nuevo dict con las claves solamente
print(my_new_dict)

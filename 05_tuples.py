##### TUPLES ##### CONJUNTO DE VALORES CONSTANTES

my_tuple = tuple()    # Formas de Definirlas
my_other_tuple = ()   # Formas de Definirlas

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
print(my_tuple)
print(type(my_tuple))   # Muestra el tipo  (tuple)

my_other_tuple = (35, 60, 30)

print(my_tuple[0])     # Traer elementos (35) igual que en listas

print(my_tuple.count("Brais")) # Cuenta los Elementos 1
print(my_tuple.index("Moure")) # Dice el indice (posicion)

#my_tuple[1] = 1.80   # Error no se puede modificar los valores.
print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

my_tuple = list(my_tuple) #Declarar una tupla como clase lista
print(type(my_tuple))

my_tuple[4] = "MaureDev"  # MOdificar la ahora lista
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple) #Volver a declarar como tuple
print(my_tuple)
print(type(my_tuple))   #Ver el tipo/clase que ahora es duple


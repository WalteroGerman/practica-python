##### Lists #####
my_list = list()     #Constructores de listas
my_other_list  = []  #Constructores de listas

print(len(my_list)) # Longitud cero, No tiene elementos la lista

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list)) # Cuenta el Largo de lista  "7"

my_other_list  = [35, 1.77, "Brais", "Moure"]

print(type(my_other_list))
print(my_other_list[1]) # Imnprime el elemento 1.75
print(my_other_list[-2]) # Imnprime el elemento "Brais"
print(my_list.count(30)) # Imprime un 2 que son las ocurrencia de un valor

age, height, name, surname = my_other_list
print(name)  # Imprime  "Brais" 

print(my_list + my_other_list) # Concatena las dos listas

my_other_list.append("MaureDev") # Añadir elemento a lista con append
print(my_other_list)

my_other_list.insert(1, "Azul") # Añador elemento en una posición concreta
print(my_other_list)

my_other_list[1] = "Rojo" # Cambiar valor insertado 
print(my_other_list)

my_other_list.remove(35) # Borrar un elemento de la lista
print(my_other_list)


my_list.pop()    # Borra el ultimo elemento
print(my_list)
my_list.pop(2)    # Borra segun el indice
print(my_list)

my_new_list = my_list.copy()  #LLamar a Copy para hacer una copia de my_list
my_list.clear()     # Borrar my_list
print(my_list)      # my_list borrada
print(my_new_list)   # Copia de my_list pero como my_new_list

my_new_list.reverse()     #llamar a reverse para invertir la lista
print(my_new_list) 

my_new_list.sort()  # Ordenar la lista
print(my_new_list) 
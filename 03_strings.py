####### Strings #######
my_string = "Mi String" #Declar definir un String
my_other_string = 'Mi otro Strings'

print(len(my_string)) # 9 Ver largo 
print(len(my_other_string)) # 15 Ver largo

print(my_string + "   " + my_other_string) # Concatenar 

my_new_line_string = "Esto es un String\nCon salto de linea" #Imprime en 2 lineas
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" #Imprime con un tab al inicio 
print(my_tab_string) #Para cancelar funcion con \\

##### Formateo #####   

name, surname, age = "Brais", "Moure", 35  # Parsear datos
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age)) # Con .format
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Con %s %d
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Con f

##### Desempaquetado de caracteres #####
language = "PyThon"
a, b, c, d, e, f = language # Imprimir la P y la O en dos lineas
print(a)   
print(e)

##### División #####
language_slice = language[1:3] # Imprime la Y y la T
print(language_slice)
language_slice = language[1:] # Imprime ython (cero es la P)
print(language_slice)
language_slice = language[-2] # Imprime o 
print(language_slice)

###### Funciones del lenguaje ######
print(language.capitalize()) # Imprime primer letra Mayúscula
print(language.upper())     # Imprime todo Mayúscula
print(language.isnumeric()) # Imprime es un nuemero ? False
print(language.lower())     # Imprime todo Minúscula
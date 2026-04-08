# imprimir distintos tipos de datos
my_string_variable = "My String variable"
print(my_string_variable)

my_bool_variable = True
print(my_bool_variable)

my_int_variable = 5
print(my_int_variable)

# Transformar una Entero en cadena de texto
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables en un print
print(my_int_to_str_variable, my_bool_variable, my_string_variable)
print("Este es el valor de:", my_bool_variable)

# Funciones pre cargadas en el Sistema
print(len(my_string_variable))

# Variables en una sola línea
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35 
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Sobrenombre:", alias,)

# Imputs, responder desde consolo para que ejecute
name = input("¿Cuál es tu nombre")
age = input("¿Cuántos años tienes?")
print(name)
print(age)

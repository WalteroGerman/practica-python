##### Functions ###### Definir que hace y luego llamarla para ejecutar todo eso definido

def my_functions ():             # Declarar una función
    print("Esto es un función")

my_functions()                  # Llamar a la función

def sum_two_values (first_values, second_values):    # Definir una funcion con parametros ()
    print(first_values + second_values)

sum_two_values(5, 7)
sum_two_values(3213, 3233)
sum_two_values("5", "7")    #Concatena como cadena de texto 57
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_values, second_values):   
    return first_values + second_values

my_result = sum_two_values_with_return(10,5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Moure", name = "Brais")

# Dentro de los parametros de entrada le indico cual es su valor por defecto
def print_name_with_default (name, surname, alias = "Sin alias"):  # Parametros por defectos
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")

# Pasar un numero de parametros dinamicos
def print_texts (*text): 
    print(text)

print_texts("Brais", "Python", "Moure")
print_texts("Hola")

# Mediante un loop "For" para elementos, imprimir el texto en Mayúscula  "upper"
def print_upper_texts(*texts): 
    print(type(texts))            # Ver tipo de dato "tuple"
    for text in texts: 
        print(text.upper())

print_upper_texts("Brais", "Python", "Moure")
print_upper_texts("Hola")
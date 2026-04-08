##### Conditional ###### Decidir si algo de nuestro codigo se va ejecutar o no
##### Si se cumple una condicion ejecuta lo que esta dentro del condicional

my_condition = False  # Ejecuta la accion si se cumple if

if my_condition:
        print("Se ejecuta la condición del if")

print("La ejecución continúa")

my_condition = 5 * 5

if my_condition == 10:   
        print("Se ejecuta la condición del segundo if")

print("La ejecución continúa")
                                 # Tiene que estar tabulado para ejecuar if y else
if my_condition > 10:              
        print("Es mayor que 10")
else:                                 # Si If no se cumple ejectuta la otra (else)
        print("Es menor o igual que 10")

if my_condition > 10 and my_condition < 20:     # Utilizar operador logico "and" como condicional    
        print("Es mayor que 10 y menor que 20")
else:                                 
        print("Es menor o igual que 10 y menor que 20")

if my_condition > 10 and my_condition < 20:   
     print("Es mayor que 10 y menor que 20")
elif my_condition == 25:                     # poner una condicion por gerarquia
    print("Es igual a 25")
else:                                 
        print("Es menor o igual que 10 y menor que 20")

my_string = ""                # Si declaro una cadena de texto vacia y niego el if es True

if not my_string:
    print("Mi cadena de testo es vacía")
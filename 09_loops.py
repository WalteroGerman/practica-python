#### Loops Ciclos Bucles ##### Ejecutar una accion hasta que esta sea Verdadera

### While = Se le pasa una condición, mientras sea falsa esa condicion se ejecuta 

my_condition = 0

while my_condition < 10:
        print(my_condition)   # Bucle infinito
        my_condition += 2     # Buscar que la condicion sea diferente 0+2+4+6+8
else:
        print("Mi condicion es mayor o igual 10") 

while my_condition < 20:
        print("Mi condicion es menor que 20")
        my_condition += 1
        if my_condition == 15:
                print("Se detiene la ejecucion")
                break                          #Detener la ejecución cuando es True Break
        print(my_condition)

print("La ejecución continúa")


###### For   Sirve para iterar un listado de elementos

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:                # Ejecuta los elementos 
        print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
for element in my_tuple:                
        print(element)

my_set = {"Brais", "Moure", 35}        # Ejecuta los elementos 
for element in my_set:                
        print(element)

my_dict = {"Nombre":"Brais", "Apellido": "Moure", "Edad": 35, 1:"Python"}
for element in my_dict:                # Ejecuta la clave "Nombre" NO los valores "Brais"
        print(element)

for element in my_dict:                # Ejecuta los valores "Brais" .value()
        print(element)
        if element == "Edad":
         break
else:
        print("El bucle for a finalizado")
        
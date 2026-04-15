####### Exception Handling ##### Capturas de excepciones 

numberOne = 5
numberTwo = 1
numberTwo = "1"
#Criterios de aceptacion    Manera manual de parchear una excepcion
#if type(numberTwo) == int: # Si numerTwo es un entero, imprimir la suma, como no lo es imprime "No se cumplió"
 #   print(numberOne + numberTwo)
#else:
 #   print("No se cumplió")

# try except
try: # No ejecuta lo que esta en el try porque esta mal e imprime "se ah producido un error"
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except: 
    # Se ejecuta si se produce una excepcion 
    print("Se ha producido un error")


# try y except siempre, opcional  else finally
try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepcion 
    print("La ejecuución continúa correctamente")
finally: 
    # Se ejecuta siempre
    print("La ejecución continúa")
    

# Captura de Excepciones por tipo    

try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    # Se ejecuta si se produce una Excepción
    print("Se ha producido un error de tipo ValueError")
    # Crear codigo para este tipo de error

except TypeError:
    # Se ejecuta si se produce una Excepción
    print("Se ha producido un error de tipo TypeError")
    # Crear codigo para este tipo de error


# Captura de la información de la  Excepción    

try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: #"error" nombre de variable que contiene la información
    print(error) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
except Exception as exception: # Información de cualquier excepción TypeErrpr
    print(exception)

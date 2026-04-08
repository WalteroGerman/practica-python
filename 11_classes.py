##### Classes #####

class MyEmptyPerson:  #Crear una clase vacia 
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

# Constructur/Inicializador de clase "init" crea la instancia, luego puedo modificar esos datos/valores

class Person:           # Person: no es una persona es la definición de cómo es una persona
    def __init__(self):
        pass

    #Crear una variable y llamar a Person

class Person:
    def __init__(self, name, surname, alias): #Constructor Se ejecuta cuando creás un Objeto "my_person"
        self.full_name = f"{name} {surname} {alias}" #Guarda el nombre completo dentro del objeto

    def walk (self):   #Método (acción) → la persona puede “caminar”
        print(f"{self.full_name} está caminando")

my_person = Person("Brais", "Moure", "MoureDev") # Se crea Objeto my_person con los datos
print(my_person.full_name)
my_person.walk()

#  f"" = texto con variables
#  {} = lugar donde va la variable
#  Si el objeto necesita datos al nacer → constructor con parámetros
#  Si los datos llegan después → constructor vacío

# 1ro- Clases Humano (Constructor def __init__(self))
# 2do- Atributos: Caracteristicas que son variables ej: edad
# 3ro- Metodos: Acciones/Comportamiento ej: correr. Se crea igual que un función
# 4to- Crear Objeto: ej: juan = Humano (crear el nombre y lo iguales a la clase Humano())
# 5to- Invocar/Utilizar una Función del Metodo o Clase se utiliza ej: juan.corre() 

class Humano:
    def __init__(self,edad,nombre): # Parametros de una funcion, que inicializa/Contruye los atributos (edad)
        self.edad = edad  #Definir atributos (self.edad) puede variar 27/28 
        self.nombre = nombre  #Definir atributos (self.nombre) puede variar Juan/Pepe
        self.edad_nombre = f"{edad} {nombre}"
    def correr(self):
        print("Corre 10K ",self.nombre) #self.nombre Acceder a los datos del objeto
        print("Corre 10K ",self.nombre) #self.nombre Acceder a los datos del objeto
    def datos_persona(self):
        print("Estos son los datos de",self.edad_nombre)
juan = Humano(27, "Juan") # Al crear Objeto juan, se ejecuta init y va a pedir "edad y nombre"
juan.correr()   # Ejecutar el Metodo "Correr" a través de Objeto.Metodo 
juan.datos_persona()  # Imprime: "Estos son los datos de 27 juan"

# 1- Clase     →  ECU
# 2- Atributos →  nombre, direccion, version, estado
# 3- Métodos   →  actualizar(), diagnostico(), verificar_comunicacion()
# 4- Objeto    →  ecu_hub  (una ECU concreta del sistema)

class Sembradora:  # La velicdad es opcional al crear un objeto con "None"
    def __init__(self, numero_surcos, velocidad_kmh=None):
        self.numero_surcos = numero_surcos
        self.velocidad_kmh = velocidad_kmh # Guardamos el número para compararlo

    def verificar_estado(self):
        # 1. Chequeamos si el valor NO exite (is None)
        if self.velocidad_kmh is None:
            print(f"Surco {self.numero_surcos} No siembra, Sin Velocidad")
            
        # 2. Si exite, evaluamos la velocidad    
        # Usamos un condicional para que la respuesta sea inteligente
        elif self.velocidad_kmh > 12:
            print(f"⚠️ Velocidad excesiva {self.velocidad_kmh} km/h")
        else:
           print(f"✅ Velocidad óptima {self.velocidad_kmh} km/h para {self.numero_surcos} surcos")
# Instanciar Objetos para casos de pruebas
my_sembradora_no_siembra = Sembradora(16,)  #Datos al objeto
my_sembradora_no_siembra.verificar_estado() #Surco 16 No siembra, Sin Velocidad
my_sembradora_siembra = Sembradora(16, 7)
my_sembradora_siembra.verificar_estado() #✅ Velocidad óptima 7 km/h para 16 surcos
my_sembradora_siembra_rapido = Sembradora(16, 14)
my_sembradora_siembra_rapido.verificar_estado() #⚠️ Velocidad excesiva 14 km/h
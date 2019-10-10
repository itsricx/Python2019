class Persona():

    #Inicializador/Constructor atributos ocultos
    def __init__(self, nombre, apellidos):
        self.__nombre = nombre
        self.__apellidos = apellidos
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter    
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos
    
    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos       

p = Persona("Miguel", "Campos")
p.nombre = "Ignacio"
print(p.nombre)
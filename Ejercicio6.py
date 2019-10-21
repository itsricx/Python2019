class Alumno:
    
    def __init__(self, nombre, apellido): 
         self.nombre = nombre
         self.apellido = apellido
      
    @property  
    def get_nombre(self): 
        return self.nombre
     
    @nombre.setter   
    def set_nombre(self, nombre): 
        self.nombre = nombre

    @property
    def get_apellido(self): 
        return self.apellido
    @apellido.setter 
    def set_apellido(self, apellido): 
        self.apellido = apellido

class Nota:

    def __init__(self, puntuacion): 
         self.puntuacion = puntuacion
         
    @property  
    def get_puntuacion(self): 
        return self.puntuacion
     
     
    @puntuacion.setter  
    def set_puntuacion(self, puntuacion): 
        self.puntuacion = puntuacion

class Evaluacion:

    def __init__(self, Alumno, Nota): 
         self.Alumno = Alumno
         self.Nota = Nota

    @property  
    def get_Alumno(self): 
        return self.Alumno
     
     
    @Alumno.setter  
    def set_Alumno(self, Alumno): 
        self.Alumno = Alumno 

    @property  
    def get_Nota(self): 
        return self.Nota
     
     
    @Nota.setter  
    def set_Nota(self, Nota): 
        self.Nota = Nota

    def evaluarAlumno():

        
class Punto: 
    
    def __init__(self, puntoX, puntoY): 
         self.puntoX = puntoX
         self.puntoY = puntoY
      
    @property  
    def get_PuntoX(self): 
        return self.puntoX 
     
    @puntoX.setter   
    def set_PuntoX(self, x): 
        self.puntoX = x

    @property
    def get_puntoY(self): 
        return self.puntoY 
    @puntoY.setter 
    def set_puntoY(self, y): 
        self.puntoY = y      
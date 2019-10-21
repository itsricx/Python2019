class Rectangulo():
 
    def _init_(self, punto1, punto2, punto3, punto4):
        self.__punto1 = punto1
        self.__punto2 = punto2
        self.__punto3 = punto3
        self.__punto4 = punto4
    
    @property
    def punto1(self):
        return self.__punto1
 
    @punto1.setter
    def punto1(self, punto1):
        self.__punto1 = punto1
 
    @property
    def punto2(self):
        return self.__punto2
 
    @punto2.setter
    def punto2(self, punto2):
        self.__punto2 = punto2
 
    @property
    def punto3(self):
        return self.__punto3
 
    @punto3.setter
    def punto3(self, punto3):
        self.__punto3 = punto3
 
    @property
    def punto4(self):
        return self.__punto4
 
    @punto4.setter
    def punto4(self, punto4):
        self.__punto4 = punto4
 
    def _str_(self):
        return str(self.punto1) + " " + str(self.punto2) + " " + str(self.punto3) + " " + str(self.punto4)
 
 
r = Rectangulo(punto1 = 1, punto2 = 2, punto3 = 3, punto4 = 4)
print(r)
class Pila:

    def __init__(self, lista):
        self.list = lista

    @property  
    def get_lista(self): 
        return self.lista 
     
    
    def set_lista(self, newlista): 
        self.lista = newlista

    def push(self,x):
        list.insert(x)

    def pop(self,x):
        list.pop(x)
    
    def empty(self):
        if list == None:
            return True
        else:
            return False     

    #Poner -1 para la pila nos daria el ultimo lugar de la misma                   
class Punto:
    def __init__(self, ejex, ejey):
        self.__ejex = ejex
        self.__ejey = ejey

    @property
    def ejex(self):
        return self._ejex

    @ejex.setter
    def ejex(self,ejex):
        self._ejex = ejex
    
    @property
    def ejey(self):
        return self._ejey

    @ejey.setter
    def ejey(self,ejey):
        self._ejey = ejey    



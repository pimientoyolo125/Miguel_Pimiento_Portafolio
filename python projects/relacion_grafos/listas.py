class nodo:
    def __init__(self, nombre, idd):
        self.nombre = nombre
        self.idd = idd
    
    def __str__(self):
        return str(self.idd)
    
    def getNombre(self):
        name = str(self.nombre)
        return name
    
    def getGustos(self):
        return self.gustos
    
    def getId(self):
        return self.idd
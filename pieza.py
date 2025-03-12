class Pieza:
    def __init__(self):
        self.id = None
        self.descripcion = None
        self.stock = None

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getStock(self):
        return self.stock

    def setStock(self, stock):
        self.stock = stock
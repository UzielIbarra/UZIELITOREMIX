class Reparacion:
    def __init__(self):
        self.folio = None
        self.matricula = None
        self.fecha_entrada = None
        self.fecha_salida = None
        self.pieza_id = None
        self.cantidad = None

    def getfolio(self):
        return self.folio

    def setfolio(self, folio):
        self.folio = folio

    def getmatricula(self):
        return self.matricula

    def setmatricula(self, matricula):
        self.matricula = matricula

    def getfecha_entrada(self):
        return self.fecha_entrada

    def setfecha_entrada(self, fecha_entrada):
        self.fecha_entrada = fecha_entrada

    def getfecha_salida(self):
        return self.fecha_salida

    def setfecha_salida(self, fecha_salida):
        self.fecha_salida = fecha_salida

    def getpieza_id(self):
        return self.pieza_id

    def setpieza_id(self, pieza_id):
        self.pieza_id = pieza_id

    def getcantidad(self):
        return self.cantidad

    def setcantidad(self, cantidad):
        self.cantidad = cantidad
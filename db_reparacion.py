import mysql.connector
import conexion as con
import reparacion as rep

class DbReparacion:
    def __init__(self):
        self.lista = []
        self.lista_clientes = []

    def saveDetail(self, detReparacion):
        self.con = con.Conexion()
        self.conn = self.con.open()
        self.cursor = self.conn.cursor()
        # pendiente crear detalle_folio = getNDetfolio()
        self.sql = "INSERT INTO det_reparaciones(folio_detalle, folio, pieza_id, cantidad) VALUES (%s, %s, %s, %s)"
        self.datos = (detReparacion.getdetallefolio(), detReparacion.getfolio(), detReparacion.getpieza_id(), detReparacion.getcantidad())
        self.cursor.execute(self.sql, self.datos)
        self.conn.commit()
        self.con.close()

    def save(self, reparacion):
        self.con = con.Conexion()
        self.conn = self.con.open()
        self.cursor = self.conn.cursor()

        # Validaciones
        if not self.validar(reparacion):
            return False

        self.sql = "INSERT INTO reparaciones(folio, matricula, fecha_entrada, fecha_salida) VALUES (%s, %s, %s, %s)"
        self.datos = (reparacion.getfolio(), reparacion.getmatricula(), reparacion.getfecha_entrada(), reparacion.getfecha_salida())
        self.cursor.execute(self.sql, self.datos)
        self.conn.commit()
        self.con.close()
        return True

    def search(self, folio):
        aux = None
        try:
            self.con = con.Conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT * FROM reparaciones WHERE folio = {}".format(folio)
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.conn.commit()
            self.conn.close()
            if row:
                aux = rep.Reparacion()
                aux.setfolio(int(row[0]))
                aux.setmatricula(row[1])
                aux.setfecha_entrada(row[2])
                aux.setfecha_salida(row[3])
        except Exception as e:
            print(e)
        return aux

    def edit(self, reparacion):
        self.con = con.Conexion()
        self.conn = self.con.open()
        self.cursor = self.conn.cursor()

        # Validaciones
        if not self.validar(reparacion):
            return False

        self.sql = "UPDATE reparaciones SET matricula = %s, fecha_entrada = %s, fecha_salida = %s WHERE folio = {}".format(reparacion.getfolio())
        self.datos = (reparacion.getmatricula(), reparacion.getfecha_entrada(), reparacion.getfecha_salida())
        self.cursor.execute(self.sql, self.datos)
        self.conn.commit()
        self.con.close()
        return True

    def remove(self, folio):
        self.con = con.Conexion()
        self.conn = self.con.open()
        self.cursor = self.conn.cursor()
        self.sql = "DELETE FROM reparaciones WHERE folio = {}".format(folio)
        self.cursor.execute(self.sql)
        self.conn.commit()
        self.con.close()

    def validar(self, reparacion):
        # No es posible realizar una reparación si no existen vehículos y piezas.
        if not self.exist_vehicles_and_parts():
            print("No existen vehículos y piezas.")
            return False

        # No es posible realizar una reparación si con fecha de entrada superior a la fecha de salida.
        if reparacion.getfecha_entrada() > reparacion.getfecha_salida():
            print("Fecha de entrada es superior a la fecha de salida.")
            return False

        # No es posible realizar una reparación si falta algún campo por llenar.
        if not (reparacion.getfolio() and reparacion.getmatricula() and reparacion.getfecha_entrada() and reparacion.getfecha_salida()):
            print("Falta algún campo por llenar.")
            return False

        # Si las piezas se encuentran en 0, no es posible registrar la reparación.
        if not self.check_stock(reparacion.getpieza_id(), reparacion.getcantidad()):
            print("Stock insuficiente.")
            return False

        return True

    def exist_vehicles_and_parts(self):
        # Verificar si existen vehículos y piezas
        self.cursor.execute("SELECT COUNT(*) FROM vehiculos")
        vehicles_count = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT COUNT(*) FROM piezas")
        parts_count = self.cursor.fetchone()[0]
        return vehicles_count > 0 and parts_count > 0

    def check_stock(self, pieza_id, cantidad):
        # Verificar si hay suficiente stock de la pieza
        self.cursor.execute("SELECT stock FROM piezas WHERE id = {}".format(pieza_id))
        stock = self.cursor.fetchone()[0]
        return stock >= cantidad

    def descontar_stock(self, pieza_id, cantidad):
        # Descontar el stock de la pieza
        self.cursor.execute("UPDATE piezas SET stock = stock - {} WHERE id = {}".format(cantidad, pieza_id))
        self.conn.commit()
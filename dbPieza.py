import mysql.connector
import conexion as con
import pieza as pz

class DbPieza:
    def save(self, pieza):
        con_instance = con.Conexion()
        conn = con_instance.open()
        cursor = conn.cursor()
        sql = "INSERT INTO piezas (id, descripcion, stock) VALUES (%s, %s, %s)"
        datos = (pieza.getId(), pieza.getDescripcion(), pieza.getStock())
        cursor.execute(sql, datos)
        conn.commit()
        conn.close()

    def search(self, pieza):
        aux = None
        try:
            con_instance = con.Conexion()
            conn = con_instance.open()
            cursor = conn.cursor()
            sql = "SELECT * FROM piezas WHERE id = {}".format(pieza.getId())
            cursor.execute(sql)
            row = cursor.fetchone()
            conn.commit()
            conn.close()
            if row:
                aux = pz.Pieza()
                aux.setId(int(row[0]))
                aux.setDescripcion(row[1])
                aux.setStock(row[2])
        except Exception as e:
            print(e)
        return aux

    def edit(self, pieza):
        con_instance = con.Conexion()
        conn = con_instance.open()
        cursor = conn.cursor()
        sql = "UPDATE piezas SET descripcion = %s, stock = %s WHERE id = {}".format(pieza.getId())
        datos = (pieza.getDescripcion(), pieza.getStock())
        cursor.execute(sql, datos)
        conn.commit()
        conn.close()

    def remove(self, pieza):
        con_instance = con.Conexion()
        conn = con_instance.open()
        cursor = conn.cursor()
        sql = "DELETE FROM piezas WHERE id = {}".format(pieza.getId())
        cursor.execute(sql)
        conn.commit()
        conn.close()

    def is_duplicate(self, pieza):
        con_instance = con.Conexion()
        conn = con_instance.open()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM piezas WHERE id = {}".format(pieza.getId())
        cursor.execute(sql)
        row = cursor.fetchone()
        conn.close()
        return row[0] > 0
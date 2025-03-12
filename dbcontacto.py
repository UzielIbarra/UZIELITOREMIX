import conexion as con

class dbcontacto:
    def salvar(self, contacto):
        # Crear instancia de conexión y abrirla
        self.conn = con.Conexion()
        self.conn = self.conn.open()
        self.cursor = self.conn.cursor()

        # SQL para insertar datos
        self.sql = "INSERT INTO contactos (id, nombre, direccion) VALUES (%s, %s, %s)"
        
        # Obtener los datos del objeto contacto
        self.datos = (contacto.getID(), contacto.getNombre(), contacto.getDireccion())

        # Ejecutar la consulta
        self.cursor.execute(self.sql, self.datos)

        # Confirmar la transacción
        self.conn.commit()

        # Cerrar la conexión
        self.cursor.close()
        self.conn.close()
from tkinter import messagebox
import mysql.connector
import conexion as con
import usuario as user

class DbUsuario:
    def save(self, usuario):
        con_instance = con.Conexion()
        conn = con_instance.open()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios(usuario_id, nombre, username, password, perfil) VALUES (%s, %s, %s, %s, %s)"
        datos = (usuario.getUsuario_id(), usuario.getNombre(), usuario.getUsername(), usuario.getPassword(), usuario.getPerfil())
        cursor.execute(sql, datos)
        conn.commit()
        conn.close()

    def search(self, usuario):
        aux = None
        try:
            con_instance = con.Conexion()
            conn = con_instance.open()
            cursor = conn.cursor()
            sql = "SELECT * FROM usuarios WHERE usuario_id = {}".format(usuario.getUsuario_id())
            cursor.execute(sql)
            row = cursor.fetchone()
            conn.commit()
            conn.close()
            if row:
                aux = user.Usuario()
                aux.setUsuario_id(int(row[0]))
                aux.setNombre(row[1])
                aux.setUsername(row[2])
                aux.setPassword(row[3])
                aux.setPerfil(row[4])
        except Exception as e:
            print(e)
        return aux

    def edit(self, usuario):
        con_instance = con.Conexion()
        conn = con_instance.open()
        cursor = conn.cursor()
        sql = "UPDATE usuarios SET nombre = %s, username = %s, perfil = %s WHERE usuario_id = {}".format(usuario.getUsuario_id())
        datos = (usuario.getNombre(), usuario.getUsername(), usuario.getPerfil())
        cursor.execute(sql, datos)
        conn.commit()
        conn.close()

    def remove(self, usuario):
        con_instance = con.Conexion()
        conn = con_instance.open()
        cursor = conn.cursor()
        sql = "DELETE FROM usuarios WHERE usuario_id = {}".format(usuario.getUsuario_id())
        cursor.execute(sql)
        conn.commit()
        conn.close()

    def get_max_id(self):
        con_instance = con.Conexion()
        conn = con_instance.open()
        cursor = conn.cursor()
        sql = "SELECT MAX(usuario_id) AS id FROM usuarios"
        cursor.execute(sql)
        row = cursor.fetchone()
        conn.commit()
        conn.close()
        return row[0] if row else None

    def autenticar(self, usuario):
        aux = None
        try:
            con_instance = con.Conexion()
            conn = con_instance.open()
            cursor = conn.cursor()
            sql = "SELECT * FROM usuarios WHERE username = '{}'".format(usuario.getUsername())
            cursor.execute(sql)
            row = cursor.fetchone()
            conn.commit()
            conn.close()
            if row:
                aux = user.Usuario()
                aux.setUsuario_id(int(row[0]))
                aux.setNombre(row[1])
                aux.setUsername(row[2])
                aux.setPassword(row[3])
                aux.setPerfil(row[4])
        except Exception as e:
            print(e)
        return aux
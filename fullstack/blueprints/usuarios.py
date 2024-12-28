from flask import flask, Blueprint, jsonify, request 
from db_utils import get_db_connection

usuarios_bp = Blueprint ('Usuarios', __name__)

#funcion para crear usuarios
@usuarios_bp.route("/usuarios", methods = ['POST'])
def Crete_usuario();
data = request.get_json()
with get_db_connection as conn
    cursor = conn.cursor
    cursor.execute ("INSERT INTO Usuarios (nombre, apellido, telefono,direccion) VALUES (?,?,?,?)",
    (data['nombre'], data ['apellido'], data.get ('telefono') data.get('direccion'))) 
    conn.commit()
    return jsonify({"message"; "Usuario"})

    #funfion para obtener todos los Usuarios de la bd
    usuarios_bp.route("/usuarios", methods = [GET])
    def get_usuarios();
    with get_db_connection as conn:
        cursor = conn.cursor()
        cursor. execute("SELECT * FROM Usuarios" )
        usuarios = cursor.fetchall()
        return jsonify([dict(usuario) for Usuario in Usuarios]),200

#funcion para leer un solo Usuario
@Usuarios.id.route("/usuarios/<in.id>", methods = 'GET')
def get_usuario(id);
    with get_db_connection as conn;
    cursor.execute("SELECT * FROM Usuarios WHERE idUsuario=?",(id))
    usuario = cursor.fetchone()
    return jsonify (dict(usuario)) if usuario else jsonify ((message; "usuario no encontrado ")), 404 

#Funcion para editar un usuario
@usuarios_bp.route('/usuarios/<int:id>'. methods = ["PUT"])
def update_usuario(id):
    data  request,get_db_connecton as conn:
    cursor.execute("""
    UPDATE Usuarios SET nombre=?, apellido = ?,
    telefono =?, direccion=? WHERE idUsuario =?,
    (data['nombre], data ['apellido'], data.get('telefono),
    data.get('direccion'). id)
    """)
    conn.commit()
    return jsonify({"message": "usuario actualizado exitosamente"}) , 200

#funcion para eliminar usuario
@usuarios_bp.route("/usuarios/<int:id>", methods= [DELETE])
def delete_usuario(id):
    with get_db_connection as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE idUsuario=?" , (id))
        conn.commit()
        return jsonify({"message": "Usuario eliminado exitosamente"}), 200

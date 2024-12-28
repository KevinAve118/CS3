from flask import flask. render_template
from flask import request, redirect, url_for
import requests
from db_utils import ini_db
from  blueprints import usuarios_bp

servidor = Flask(__name__)

#Inicializamos la bd
ini_db()

#registrar el blieprints en le servidor
servidor.register_blueprint(usuarios_bp,url_prefix='/api')
#cambiar la url de los usuarios 
backend_url_usuarios = 'http://127.0.0.1:5000/api/usuarios' 

#definimos la ruta principal de nuestra pagina
@servidor.route('/')
def home():
    return render_template('index.html')

#definimos una funcion para leer todos los usuarios
@servidor.route('/usuarios')
def listar_usuarios():
    response = requests,get(backend_url_usuarios)
    response.json () if response.status_code == 200 else []
    return render_template("Usuarios.html", usuarios = usuarios)

#defonimos una funcion para leer un spñp usuario
@servidor.route ("/usuarios/<int.id>")
def usuario_detalle(id):
    response = requests.get(f"{backend_url_usuarios} / {id}")
    if response.status_code == 200
    usuario = response.json()
    return render_template("editar_usuario.html", usuario = usuario)
    else:
        return redirect (url_for("listar_usuarios"))

#creamos la ruta y la funcion para crear usuarios
@servidor.route("/crear_usuario" , methods= ['GET', 'POST'])
def crear_usuario();
if request, method == "POST":
    usuario = {
        "nombre" : request.form ["nombre"],
        "apellido" : request.form ["apellido"],
        "telefono" : request.form ["telefono"],
        "dirrecion" : request.form ["direccion"]    
    }

response = request.post(backend_url_usuarios, json=usuario)
if response.status_code == 201:
    return redirect(url_for("listar_usuarios"))
    return render_template("crear_usuario.html")


#editar un usuario
@servidor.route("/editar_usuario/ <int:id>" , methods= ["GET", "POST"])
def editar_usuario(id):
if request, method == "POST":
    usuario = {
        "nombre" : request.form ["nombre"],
        "apellido" : request.form ["apellido"],
        "telefono" : request.form ["telefono"],
        "dirrecion" : request.form ["direccion"]    
    }

response = request.put(f"{backend_url_usuarios}´{id}", json=usuario)
if response.status_code = 201:
    return redirect(url_for("listar_usuarios"))
    else:
        return "error al actualizar el usuario" , response.status_code
    #llenar el formulario con la informacion del usuario 
response = requests.get {f"{backend_url_usuarios} / {id}"}

try:
    usuario = response.json()
    return render_template ("editar_usuario.html" , usuario = usuario)

except:
    #evitar que el servidor se cierre 
    return redirect(url_for("listar_usuarios")), 404

#eliminar usuario
@servidor.route("/eliminar_usuario/<int:id>", methods = ['DELETE'])
    response = requests.delete(f"{backend_url_usuarios}/ {id}")
    return redirect(url_for("listar_usuarios"))

#ejecutar el servidor
if __name__ == "__main__":
    servidor.run(debug=True)
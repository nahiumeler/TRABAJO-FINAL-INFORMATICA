from flask import Flask, jsonify, request
from database import ver_contratistas, crear_tablas,ver_profesionales, login, editar_perfil,cambiar_contrasena,verificar_contrasena,eliminar_cuenta,verCitasContratista,verCitasProf

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Bienvenido al Mercado de Trabajo! Aquí, los contratistas pueden publicar ofertas de empleo y los profesionales pueden ofrecer sus servicios."


@app.route("/contratistas")
def get_contratistas():
    contratistas = ver_contratistas('base1.db')
    return jsonify(contratistas)

@app.route("/profesionales")
def get_profesionales():
    profesionales = ver_profesionales('base1.db')
    return jsonify(profesionales)


@app.route("/login", methods=["POST"])
def login_api():
    data = request.json
    categoria = data.get("categoria")
    userid = data.get("userid")
    contrasenia = data.get("contrasenia")
    user_data = login(categoria, userid, contrasenia)
    if user_data:
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

@app.route("/editar_perfil", methods=["PUT"])
def editar_perfil_api():
    data = request.json
    user_id = data.get("user_id")
    campo = data.get("campo")
    nuevo_valor = data.get("nuevo_valor")
    editar_perfil(user_id, campo, nuevo_valor)
    return jsonify({"mensaje": "Perfil actualizado correctamente"}), 200

@app.route("/configuracion/cambiar_contrasena", methods=["POST"])
def api_cambiar_contrasena():
    data = request.json
    user_id = data.get("user_id")
    contrasena_actual = data.get("contrasena_actual")
    nueva_contrasena = data.get("nueva_contrasena")

    if verificar_contrasena(user_id, contrasena_actual):
        cambiar_contrasena(user_id, nueva_contrasena)
        return jsonify({"message": "Contraseña cambiada correctamente"}), 200
    else:
        return jsonify({"message": "Contraseña actual incorrecta"}), 400


@app.route("/configuracion/eliminar_cuenta", methods=["DELETE"])
def api_eliminar_cuenta():
    data = request.json
    user_id = data.get("user_id")
    contrasena = data.get("contrasena")

    if verificar_contrasena(user_id, contrasena):
        eliminar_cuenta(user_id)
        return jsonify({"message": "Cuenta eliminada exitosamente"}), 200
    else:
        return jsonify({"message": "Contraseña incorrecta"}), 400
    

@app.route("/citas/contratista/<user_id>", methods=["GET"])
def get_citas_contratista(user_id):
    citas = verCitasContratista(user_id)
    if citas:
        return jsonify(citas)
    else:
        return jsonify({"message": user_id}), 404

@app.route("/citas/profesional/<nombre_prof>", methods=["GET"])
def get_citas_prof(nombre_prof):
    citas = verCitasProf(nombre_prof)
    if citas:
        return jsonify(citas)
    else:
        return jsonify({"message": nombre_prof}), 404



if __name__ == "__main__":
    crear_tablas('base1.db') 
    app.run(debug=True, port=4000)

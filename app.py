from flask import Flask, request, render_template, redirect
from database.Supabase import supabase
import urllib.parse

app = Flask(__name__)

@app.route('/exito-restablecer-contrasena')
def exito_restablecer_contrasena():
    return render_template('confirmed-succed.html')


@app.route('/request-reset', methods=['POST'])
def request_reset():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return "Se requiere un email", 400

    try:
        # Enviar correo de restablecimiento de contraseña usando Supabase
        response = supabase.auth.reset_password_for_email(
            email=email,
            options={
                "redirect_to": "http://localhost:5000/update-password"
            }
        )
        return {"message": "Se ha enviado un correo con instrucciones para restablecer tu contraseña"}, 200

    except Exception as e:
        print(f"Error detallado: {str(e)}")
        return {"error": f"Error al enviar el correo: {str(e)}"}, 400


# @app.route('/update-password', methods=['GET'])
# def update_password():
#     """
#     Ruta para recibir los tokens de la URL y mostrarlos en un formulario.
#     Aquí extraemos el fragmento de la URL, lo pasamos al template y dejamos que el
#     usuario complete su nueva contraseña.
#     """
#     # Obtener el fragmento de la URL (hash) que se envía desde el frontend
#     full_url = request.args.get('url', '')
#
#     # Extraer los parámetros de la URL del hash
#     hash_params = urllib.parse.parse_qs(urllib.parse.urlparse(full_url).fragment)
#     access_token = hash_params.get('access_token', [None])[0]
#     refresh_token = hash_params.get('refresh_token', [None])[0]
#
#     if not access_token or not refresh_token:
#         return "Tokens no proporcionados", 401
#
#     return render_template('confirmar-password.html', access_token=access_token, refresh_token=refresh_token)


@app.route('/update-password', methods=['GET', 'POST'])
def update_password():
    if request.method == 'GET':
        return render_template('confirmar-password.html')
    elif request.method == 'POST':
     try:
        data = request.get_json()
        access_token = data.get('access_token')
        refresh_token = data.get('refresh_token')

        if not access_token or not refresh_token:
            return {"error": "Tokens no proporcionados"}, 401

        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        # Validaciones de contraseña
        if not new_password or len(new_password) < 8:
            return {"error": "La contraseña debe tener al menos 8 caracteres"}, 400

        if new_password != confirm_password:
            return {"error": "Las contraseñas no coinciden"}, 400

        # Establecer la sesión en Supabase usando los tokens
        session_response = supabase.auth.set_session(access_token, refresh_token)

        # Actualizar la contraseña del usuario
        update_response = supabase.auth.update_user({
            "password": new_password
        })


        return {"message": "Contraseña actualizada exitosamente"}, 200

     except Exception as e:
        return {"error": f"Error al actualizar contraseña: {str(e)}"}, 400


if __name__ == '__main__':
    app.run(debug=True)

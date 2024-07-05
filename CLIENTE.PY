import requests
from api_externa import obtener_foto
from database import insertarReserva, selecFecha

class Usuario:
    def __init__(self, nombre, userid, contraseña):
        self.nombre = nombre
        self.user_id = userid
        self.__password = contraseña
        # self.localidad = localidad

    def Saludar(self):
        print("Hola,", self.nombre, "bienvenido")

    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return self.__password


class Profesional(Usuario):
    def __init__(self, nombre, userid, contraseña, servicios, precio, direccion, telefono):
        super().__init__(nombre, userid, contraseña)
        self.servicios = servicios
        self.precio = precio
        self.direccion = direccion
        self.telefono = telefono

    def Saludar(self):
        print("Hola", self.nombre, "en esta aplicacion podras ofrecer tus servicios de", self.servicios)


url = "http://127.0.0.1:4000"


def verContratistas(base_url):
    try:
        url = f"{base_url}/contratistas"
        response = requests.get(url)
        response.raise_for_status()
        rows = response.json()
        print(rows)
        return rows
    except requests.RequestException as e:
        print(f"Error al obtener contratistas: {e}")
        return []


def verProfesionales(base_url, user_id):
    try:
        url = f"{base_url}/profesionales"
        response = requests.get(url)
        response.raise_for_status()
        rows = response.json()
        prof = []
        print()
        print("--- SERVICIOS DISPONIBLES ---")
        print("- maquillaje\n- peluqueria\n- barberia\n- manicura\n- pedicura\n- estetica\n")
        servicio = input("Que tipo de servicio estas buscando? ")
        existe = False
        for profesional in rows:
            if servicio == profesional["servicios"]:
                existe = True
                pro = Profesional(profesional["nombre"], profesional["userid"], profesional["contraseña"],
                                  profesional["servicios"], profesional["precio"], profesional["direccion"],
                                  profesional["telefono"])
                prof.append(pro)
                print("NOMBRE:", pro.nombre)
                print("SERVICIO:", pro.servicios)
                print("PRECIO", pro.precio)
                direccion = pro.direccion.replace(' ', '+')
                print("DIRECCION: ", "https://www.google.com.ar/maps/place/" + direccion)
                foto = obtener_foto()
                print(foto)
                print()
        if existe:
            while True:
                reservar = input("Queres reservar algun profesional? (si/no): ")
                if reservar == "si":
                    registrarReserva(user_id, prof)
                    break
                elif reservar == "no":
                    break
                else:
                    print("Ingresa una opcion valida")
        else:
            print("Servicio inexistente")
    except requests.RequestException as e:
        print(f"Error al obtener profesionales: {e}")
    except Exception as e:
        print(f"Error en verProfesionales: {e}")


def registrarReserva(user_id, prof):
    try:
        prof_select = input("Ingrese el nombre del profesional con el que quieras reservar: ")
        existe = False
        for profesional in prof:
            if profesional.nombre == prof_select:
                existe = True
                while True:
                    fecha = input("Ingrese la fecha que queres reservar (dd/mm/yyyy): ")
                    if formatoFechaCorrecto(fecha):
                        if selecFecha(prof_select, fecha) == 0:
                            insertarReserva(user_id, prof_select, fecha)
                            print("Reserva creada exitosamente")
                            return
                        else:
                            res = input("Lo sentimos, esa fecha ya esta registrada, queres ingresar otra? (si/no): ")
                            if res != "si":
                                return
                    else:
                        print("Fecha invalida, ingrese la fecha con el formato adecuado")
        if not existe:
            print("Profesional no encontrado")
    except Exception as e:
        print(f"Error en registrar reserva: {e}")


def formatoFechaCorrecto(fecha):
    try:
        if fecha[2] != "/" or fecha[5] != "/":
            return False
        dia = int(fecha[:2])
        mes = int(fecha[3:5])
        ano = int(fecha[6:])
        if dia > 31 or mes > 12 or ano < 2024:
            return False
        return True
    except Exception as e:
        print(f"Error en el formato de fecha: {e}")
        return False

# # Solicitamos la fecha al usuario
# fecha = input("Escribe la fecha dd/mm/aaaa: ")
# es_valida = formatoFechaCorrecto(fecha)

# if es_valida:
#     print("La fecha es válida.")
# else:
#     print("La fecha no tiene el formato correcto.")

def EsProfesional(base_url, user_id):
    try:
        url = f"{base_url}/profesionales"
        response = requests.get(url)
        response.raise_for_status()
        rows = response.json()
        for profesional in rows:
            if user_id == profesional["userid"]:
                return "profesionales"
        return "contratistas"
    except requests.RequestException as e:
        print(f"Error al verificar categoría: {e}")
        return None

#verProfesionales(url)

def realizar_login(base_url, categoria, userid, contrasenia):
    try:
        url = f"{base_url}/login"
        data = {"categoria": categoria, "userid": userid, "contrasenia": contrasenia}
        response = requests.post(url, json=data)
        response.raise_for_status()
        user_data = response.json()
        print("Login exitoso!")
        return user_data
    except requests.RequestException as e:
        print(f"Error de login: {e}")
        return False


def actualizar_perfil(base_url, user_id, campo, nuevo_valor):
    try:
        url = f"{base_url}/editar_perfil"
        data = {"user_id": user_id, "campo": campo, "nuevo_valor": nuevo_valor}
        response = requests.put(url, json=data)
        response.raise_for_status()
        print("Perfil actualizado correctamente")
    except requests.RequestException as e:
        print(f"Error al actualizar el perfil: {e}")
    except Exception as e:
        print(f"Error en actualizar_perfil: {e}")


def configuracion(user_id, password):
    print("-----CONFIGURACION-----")
    opcion = int(input("Elegi la opcion que desees realizar: \n1. Modificar contraseña\n2. Eliminar cuenta\n"))
    if opcion == 1:
        contrasena_actual = input("Ingresa la contraseña actual: ")
        if contrasena_actual == password:
            nueva_contrasena = input("Ingresa la nueva contraseña: ")
            response = requests.post("http://127.0.0.1:4000/configuracion/cambiar_contrasena", json={
                "user_id": user_id,
                "contrasena_actual": contrasena_actual,
                "nueva_contrasena": nueva_contrasena
            })
            print(response.json().get("message"))
        else:
            print("Contraseña incorrecta")

    elif opcion == 2:
        contrasena = input("Ingresa la contraseña: ")
        response = requests.delete("http://127.0.0.1:4000/configuracion/eliminar_cuenta", json={
            "user_id": user_id,
            "contrasena": contrasena
        })
        print(response.json().get("message"))


def cambiar_contraseña(user_id, password):
    try:
        contrasena_actual = input("Ingresa la contraseña actual: ")
        if contrasena_actual == password:
            nueva_contrasena = input("Ingresa la nueva contraseña: ")
            response = requests.post("http://127.0.0.1:4000/configuracion/cambiar_contrasena", json={
                "user_id": user_id,
                "contrasena_actual": contrasena_actual,
                "nueva_contrasena": nueva_contrasena
            })
            print(response.json().get("message"))
        else:
            print("Contraseña incorrecta")
    except requests.RequestException as e:
        print(f"Error al cambiar la contraseña: {e}")


def eliminar_cuenta(user_id, password):
    try:
        contrasena = input("Ingresa la contraseña: ")
        if contrasena == password:
            response = requests.delete("http://127.0.0.1:4000/configuracion/eliminar_cuenta", json={
                "user_id": user_id,
                "contrasena": contrasena
            })
            print(response.json().get("message"))
        else:
            print("Contraseña incorrecta")
    except requests.RequestException as e:
        print(f"Error al eliminar cuenta: {e}")


def obtener_citas_contratista(base_url, user_id):
    try:
        response = requests.get(f"{base_url}/citas/contratista/{user_id}")
        response.raise_for_status()
        rows = response.json()
        for cita in rows:
            print("Profesional: ", cita["nombre_prof"])
            print("Fecha: ", cita["fecha"])
    except requests.RequestException as e:
        print(f"Error al obtener citas del contratista: {e}")


def obtener_citas_profesional(base_url,nombre_prof):
    response = requests.get(f"{base_url}/citas/profesional/{nombre_prof}")
    if response.status_code == 200:
        rows = response.json()
        for citas in rows:
            print("Contratista: ",citas["userid"])
            print("Fecha: ",citas["fecha"])
    else:
        return None


def main():
    try:
        while True:
            url = "http://127.0.0.1:4000"
            userid = input("Ingrese el userid: ")
            contrasenia = input("Ingrese la contraseña: ")
            categoria = EsProfesional(url, userid)
            if not categoria:
                print("Error al determinar la categoría del usuario.")
                continue
            pase = realizar_login(url, categoria, userid, contrasenia)
            if pase:
                if categoria == "contratistas":
                    while True:
                        print()
                        print("MENU PRINCIPAL")
                        print("Opciones:")
                        print("1. Ver profesionales")
                        print("2. Ver citas proximas")
                        print("3. Salir")
                        print()
                        try:
                            opcion = int(input("Elegi la opción que desees realizar: "))
                            if opcion == 1:
                                verProfesionales(url, userid)
                            elif opcion == 2:
                                obtener_citas_contratista(url, userid)
                            elif opcion == 3:
                                break
                            else:
                                print("Opcion no valida")
                        except ValueError:
                            print("Entrada inválida, debe ser un número")
                
                elif categoria == "profesionales":
                    while True:
                        print()
                        print("MENU PRINCIPAL")
                        print("Opciones:")
                        print("1. Editar Perfil")
                        print("2. Configuracion")
                        print("3. Ver citas")
                        print("4. Cerrar Sesion")
                        print()
                        try:
                            opcion = int(input("Elegi la opcion que desees realizar: "))
                            if opcion == 1:
                                while True:
                                    print("MODIFICAR PERFIL")
                                    print("- precio")
                                    print("- direccion")
                                    print("- telefono")
                                    campo = input("Ingresa que queres modificar: ")
                                    if campo in ["precio", "direccion", "telefono"]:
                                        nuevo_valor = input(f"Ingresa el nuevo {campo}: ")
                                        actualizar_perfil(url, userid, campo, nuevo_valor)
                                        break
                                    else:
                                        print("Ingresa una opcion valida")
                            elif opcion == 2:
                                configuracion(userid, contrasenia)
                            elif opcion == 3:
                                obtener_citas_profesional(url, userid)
                            elif opcion == 4:
                                break
                            else:
                                print("Opcion no valida")
                        except ValueError:
                            print("Entrada inválida, debe ser un número")
    except Exception as e:
        print(f"Error en main: {e}")


if __name__ == "__main__":
    main()

import sqlite3 
ruta_base='base1.db'

def crear_tablas(ruta_b): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    try:
        tabla1='CREATE TABLE profesionales (nombre VARCHAR(100),userid VARCHAR(100), contraseña VARCHAR(100),servicios VARCHAR(100),precio INTEGER, direccion VARCHAR(100), telefono INTEGER)' 
        cursor.execute(tabla1) 
        tabla2='CREATE TABLE contratistas (userid VARCHAR(100), contraseña VARCHAR(100), direccion VARCHAR(100))' 
        cursor.execute(tabla2) 
        tabla3='CREATE TABLE reservas (userid VARCHAR(100), nombre_prof VARCHAR(100), fecha VARCHAR(100))' 
        cursor.execute(tabla3) 
        conexion.close() 
        return True
    except:
        return False
 

existe = crear_tablas(ruta_base) 

def agregar_profesional(ruta_b,nombre,userid,contraseña,servicios,precio,direccion,telefono): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "INSERT INTO profesionales VALUES('"+nombre+"','"+userid+"','"+contraseña+"','"+servicios+"',"+str(precio)+",'"+direccion+"',"+str(telefono)+")" 
    cursor.execute(sentenciasql) #aca ve si hay error 
    conexion.commit()   #si hay error no llena la tabla. 
    conexion.close() 
 
def agregar_contratista(ruta_b,userid,contraseña,direccion): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "INSERT INTO contratistas VALUES('"+userid+"','"+contraseña+"','"+direccion+"')" 
    cursor.execute(sentenciasql)  
    conexion.commit()    
    conexion.close() 
    
if(existe):
    agregar_profesional(ruta_base,"Lucila Katz","lkatz","hola123","maquillaje",1000,"2374 Cuenca, CABA, Buenos Aires",1132598325) #esto despues lo hacemos con inputs 
    agregar_contratista(ruta_base,"wanda","perro123","2344 Arregui, CABA, Buenos Aires ") 
 
def insertar_lista_profesionales(ruta_b,lista): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "INSERT INTO profesionales VALUES(?,?,?,?,?,?,?)" 
    cursor.executemany(sentenciasql,lista) 
    conexion.commit()   
    conexion.close() 
 
def insertar_lista_contratista(ruta_b,lista): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "INSERT INTO contratistas VALUES(?,?,?)" 
    cursor.executemany(sentenciasql,lista) 
    conexion.commit()   
    conexion.close() 



    
profesionales = [
    ("Silvia Gonzalez", "silvigonzalez","hola","peluqueria",1000,"Navarro 2887,CABA,Buenos Aires",1132598326),
    ("Ernesto Rodriguez", "ert","234","maquillaje",100,"Pedernera 3215,CABA,Buenos Aires",1132598327),
    ("Clara Villalba", "clara","vet","peluqueria",1050,"Pastor Obligado 70,Villa Sarmiento,Buenos Aires",1132598526),
    ("Nahuel Melero", "nahi","mel","maquillaje",180,"Maestro Santana 451,San Isidro,Buenos Aires",1132598336),
    ("Marcela Gonzalez", "marcela89", "324", "barberia", 800, "Av. Corrientes 1234, Buenos Aires, Buenos Aires",1132598396),
    ("Martin Fernandez", "martin2023", "martin123", "manicura", 1500, "Av. Libertador 5678, Vicente López, Buenos Aires",1132598320),
    ("Ana Gomez", "ana_belleza", "anabella2023", "manicura", 500, "Av. San Martín 4321, San Miguel, Buenos Aires",1132596326),
    ("Juan Perez", "juan_peluquero", "juanpelu", "peluqueria", 600, "Calle Lavalle 987, Ramos Mejía, Buenos Aires",1132598376),
    ("Sofia Carlos", "sofia_estilista", "sofia123", "maquillaje", 1200, "Av. Rivadavia 6543, Morón, Buenos Aires",1132598336),
    ("Diego Mecina", "diego_medico", "diegom", "estetica", 900, "Av. Cabildo 2101, Belgrano, Buenos Aires",1132598726),
    ("Lucia Pedemonte", "lucia_ped", "lucia", "estetica", 1200, "Calle Ituzaingó 345, Olivos, Buenos Aires",1132598026),
    ("Carlos Fanga", "carlos_fotografia", "carlitosfotos", "peluqueria", 1800, "Av. Santa Fe 7890, Martínez, Buenos Aires",1132598520),
    ("Ana Flores", "ana_estetica", "anita2023", "estetica", 1100, "Av. Cabildo 4321, Nuñez, Buenos Aires",1132598586),
    ("Juan Martinez", "juan_cocinero", "juan_cocina", "maquillaje", 2000, "Av. Scalabrini Ortiz 876, Palermo, Buenos Aires",1132592326),
    ("Luis Fraga", "luis_pintor", "luisarte", "estetica", 1500, "Dorrego 123, Vicente López, Buenos Aires",1132597626),
    ("Claudia Susic", "claudia_eventos", "clau_organiza", "pedicura", 2500, "Av. Santa Fe 5678, Recoleta, Buenos Aires",1132598456),
    ("Diego Carrera", "diego_entrenador", "diegofit", "pedicura", 800, "Av. Belgrano 321, Caballito, Buenos Aires",1132598323),
    ("Laura Frigo", "laura_limpieza", "lau321", "manicura", 600, "Monroe 789, Villa Urquiza, Buenos Aires",1132598344),
    ("Carlos Tech", "carlos_tech", "carlotech", "barberia", 1200, "Av. Corrientes 9876, Almagro, Buenos Aires",1132596626),
    ("Rosa Mauric", "rosa_costura", "rosasews", "barberia", 1300, "Billinghurst 2345, Chacarita, Buenos Aires",1132598387)]

 
contratistas=[("nmeler","12345","2322 Navarro, CABA, Buenos Aires"),
              ("martu122","simona321","6425 Arregui,CABA,Buenos Aires"),
              ("nico","123","3742 Campana, CABA, Buenos Aires"),
              ("julieta95", "clave123", "500 Av. Cabildo, Belgrano, Buenos Aires"),
              ("roberto_gym", "gym1234", "1200 Av. Rivadavia, Flores, Buenos Aires"),
              ("luciana_p", "luciana456", "700 Av. Santa Fe, Recoleta, Buenos Aires"),
              ("marcos_viajes", "viajero321", "3400 Av. Corrientes, Almagro, Buenos Aires"),
              ("valentina_tech", "valen_tech", "900 Calle Tucumán, Centro, Buenos Aires"),
              ("lucas_figue", "lucasfi333", "250 Av. Córdoba, Palermo, Buenos Aires"),
              ("carolina_t", "carovet", "1500 Av. Libertador, Vicente López, Buenos Aires"),
              ("leo_fit", "leo123", "1800 Calle Dorrego, Chacarita, Buenos Aires")] 
 
if existe:
    insertar_lista_profesionales(ruta_base,profesionales) 
    insertar_lista_contratista(ruta_base,contratistas) 



 
def ver_profesionales(ruta_b): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "SELECT * FROM profesionales" 
    cursor.execute(sentenciasql) 
    profesionales = cursor.fetchall()
    conexion.commit()   
    conexion.close() 
    diccionario_profesionales=[]
    for profesional in profesionales:
        diccionario = {
            "nombre": profesional[0],
            "userid": profesional[1],
            "contraseña": profesional[2],
            "servicios": profesional[3],
            "precio": profesional[4],
            "direccion": profesional[5],
            "telefono": profesional[6]
        }
        diccionario_profesionales.append(diccionario)

    return diccionario_profesionales

def ver_contratistas(ruta_b): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "SELECT * FROM contratistas" 
    cursor.execute(sentenciasql) 
    contratistas = cursor.fetchall()
    conexion.commit()
    conexion.close() 
    diccionario_contratistas=[]
    for contratista in contratistas:
        diccionario = {
            "userid": contratista[0],
            "contraseña": contratista[1],
            "direccion": contratista[2]
        }
        diccionario_contratistas.append(diccionario)

    return diccionario_contratistas


def login(categoria,userid, contrasenia):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {categoria} WHERE userid=? AND contraseña=?", (userid, contrasenia))
    user_data = cursor.fetchone()
    if user_data:
        return user_data
    conn.close()


def editar_perfil(user_id, campo, nuevo_valor):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    if campo == "precio":
        cursor.execute("UPDATE profesionales SET precio = ? WHERE userid = ?", (nuevo_valor, user_id))
    elif campo == "direccion":
        cursor.execute("UPDATE profesionales SET direccion = ? WHERE userid = ?", (nuevo_valor, user_id))
    elif campo == "telefono":
        cursor.execute("UPDATE profesionales SET telefono = ? WHERE userid = ?", (nuevo_valor, user_id))
    conn.commit()
    conn.close()

def cambiar_contrasena(user_id, nueva_contrasena):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE profesionales SET contraseña = ? WHERE userid = ?", (nueva_contrasena, user_id))
    conn.commit()
    conn.close()

def eliminar_cuenta(user_id):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM profesionales WHERE userid = ?", (user_id,))
    conn.commit()
    conn.close()

def verificar_contrasena(user_id, contrasena):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM profesionales WHERE userid = ? AND contraseña = ?", (user_id, contrasena))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def insertarReserva(user_id,nombre_prof,fecha):
    conexion=sqlite3.connect("base1.db") 
    cursor=conexion.cursor() 
    cursor.execute("INSERT INTO reservas VALUES(?,?,?)", (user_id, nombre_prof, fecha))
    # cursor.executemany(sentenciasql,lista) 
    conexion.commit()   
    conexion.close() 

def selecFecha(nombre_Prof,fecha):
    conexion=sqlite3.connect("base1.db") 
    cursor=conexion.cursor() 
    cursor.execute("SELECT 1 FROM reservas WHERE fecha=? AND nombre_prof=?",(fecha,nombre_Prof))
    result = cursor.fetchone()
    conexion.close()
    return result is not None

def verCitasContratista(user_id):
    conexion = sqlite3.connect("base1.db") 
    cursor = conexion.cursor() 
    cursor.execute("SELECT * FROM reservas WHERE userid=?", (user_id,))
    citas = cursor.fetchall()
    conexion.close() 

    diccionario_citas_contra = []
    for cita in citas:
        diccionario = {
            "userid": cita[0],
            "nombre_prof": cita[1],
            "fecha": cita[2]
        }
        diccionario_citas_contra.append(diccionario)

    return diccionario_citas_contra

def verCitasProf(nombre_prof):
    conexion=sqlite3.connect("base1.db") 
    cursor=conexion.cursor() 
    cursor.execute("SELECT * FROM reservas WHERE nombre_prof=(SELECT nombre FROM profesionales WHERE userid=?)",(nombre_prof,))
    citas = cursor.fetchall()
    conexion.close() 

    diccionario_citas_prof=[]
    for cita in citas:
        diccionario = {
            "userid": cita[0],
            "nombre_prof": cita[1],
            "fecha": cita[2]
        }
        diccionario_citas_prof.append(diccionario)

    return diccionario_citas_prof


# def obtener_profesionales():
#     conn = sqlite3.connect("base1.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT userid, contraseña, nombre, servicios, precio FROM profesionales")
#     profesionales_data = cursor.fetchall()
#     conn.close()
#     lista_profesionales = []
#     for data in profesionales_data:
#         if len(data) == 5:
#             try:
#                 user_id, contraseña, nombre, servicio, precio = data
#                 profesional = Profesional(user_id, contraseña, nombre, servicio, precio)
#                 lista_profesionales.append(profesional)
#             except Exception as e:
#                 print(f"Error al crear Profesional con data {data}: {e}")
#         else:
#             print(f"Data inválida: {data}")
#     print(lista_profesionales)
#     return lista_profesionales




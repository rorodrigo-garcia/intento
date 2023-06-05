import json

from pathlib import Path

nombre = input("Ingrese su Nombre: ").strip().capitalize()
contraseña = input("Ingrese su contraseña: ").strip().capitalize()

def obtenerRuta ():
    BASE_DIR = Path(__file__).resolve().parent 
    return BASE_DIR

def datos(contraseña) -> dict:
    formulario = {"Nombre" : nombre, "Contrasenia" : contraseña}
    print("Usuario creado")
    return formulario
    #recordar validar

#def comprabar_contraseña():
    if contraseña == contraseña.value():
        print("la contraseña es correcta")
    else:
        print("La contraseña es incorrecta")
   

def guardar_datos(datos_ingresados,ruta,nombre_archivo):
    with open(f"{ruta}/{nombre_archivo}","w") as archivo:
        json.dump(datos_ingresados,archivo)
        print("Registro guardado")


 #def mostrar_datos():
  #  obtenerRuta()
   # ruta = BASE_DIR / "ususarios.json"
   # data = pandas.read_csv(ruta)
   # return data

def main():
   nombre_archivo = "usuarios.json"
   ruta = obtenerRuta()
   datos_ingresados = datos( "contraseña")
   guardar_datos(datos_ingresados,ruta,nombre_archivo)
   #mostrar_datos()

main() #aca es donde voy a guardar todas las funciones
#comprabar_contraseña()

#def comprabar_contraseña(ingreso: str) -> str and int | None:
 #   ingreso = ingreso.strip()
 #   if ingreso and ingreso.isdigit():
 #       contraseña = ingreso
  #      if contraseña == contraseña.value():
 #           return contraseña
 #   contraseña = None
  #  return contraseña
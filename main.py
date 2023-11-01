import db_helper

# Base de datos emulada con un diccionario
usuarios_db = {}

# Función para registrar un usuario
def registrar_usuario():
    while True:
        nombre_usuario = input("Introduce el nombre de usuario: ").strip()
        if nombre_usuario in usuarios_db:
            print("El usuario ya existe. Por favor, elige otro nombre de usuario.")
        else:
            contrasena = input("Introduce una contraseña: ").strip()
            usuarios_db[nombre_usuario] = contrasena
            print("Usuario registrado con éxito.")
            break

# Función para loguear un usuario
def login_usuario():
    nombre_usuario = input("Introduce tu nombre de usuario: ").strip()
    if nombre_usuario not in usuarios_db:
        print("El usuario no existe.")
        return

    contrasena = input("Introduce tu contraseña: ").strip()
    if usuarios_db[nombre_usuario] == contrasena:
        print("Login exitoso.")
    else:
        print("Contraseña incorrecta.")

# Función para mostrar todos los usuarios
def mostrar_usuarios():
    if not usuarios_db:
        print("No hay usuarios registrados.")
        return

    print("Usuarios registrados:")
    for usuario in usuarios_db:
        print(usuario)

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar usuario")
        print("2. Login de usuario")
        print("3. Mostrar usuarios")
        print("4. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login_usuario()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

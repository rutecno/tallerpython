import random
import sys

# Datos de usuarios y servicio iniciales (10 registros con lista de 30 consumos cada uno)
usuarios_servicio = [
    {
        "id": i + 1,
        "nombre": f"Usuario{i+1}",
        "documento": str(1000 + i),
        "estrato": random.randint(1, 6),
        "consumoEnergetico": [random.randint(50, 300) for _ in range(30)],
        "estado": random.choice(["ACTIVO", "SUSPENDIDO"]),
    }
    for i in range(10)
]

usuarios_registrados = []  # lista de dicts {email, password}


def registrar_usuario():
    print("--- Registro de usuario ---")
    correo = input("Correo: ").strip()
    password = input("Password: ").strip()
    if not correo or not password:
        print("Correo y password obligatorios.")
        return

    for u in usuarios_registrados:
        if u["correo"] == correo:
            print("Usuario ya existe. Intenta con otro correo.")
            return

    usuarios_registrados.append({"correo": correo, "password": password})
    print("Registro exitoso. Ahora haz login para continuar.")


def login():
    print("--- Login ---")
    intentos_restantes = 3

    while intentos_restantes > 0:
        correo = input("Correo: ").strip()
        password = input("Password: ").strip()

        match = next(
            (u for u in usuarios_registrados if u["correo"] == correo and u["password"] == password),
            None,
        )

        if match:
            print("Login exitoso")
            return True

        intentos_restantes -= 1
        if intentos_restantes > 0:
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")
        else:
            print("Cuenta bloqueada temporalmente")
            return False


def mostrar_usuarios():
    print("--- Usuarios de servicio ---")
    for u in usuarios_servicio:
        total = sum(u["consumoEnergetico"])
        print(
            f"ID: {u['id']} | Nombre: {u['nombre']} | Estrato: {u['estrato']} | Estado: {u['estado']} | Consumo total mes: {total} kWh"
        )


def ordenar_usuarios_por_consumo():
    # Usamos sort para modificar la lista in-place (requisito de método lista sort)
    usuarios_servicio.sort(key=lambda x: sum(x["consumoEnergetico"]))
    print("Usuarios ordenados por consumo total (menor a mayor).")


def agregar_usuario_servicio():
    print("--- Agregar usuario de servicio ---")
    nid = max([u["id"] for u in usuarios_servicio], default=0) + 1
    nombre = input("Nombre: ").strip()
    documento = input("Documento: ").strip()
    estrato = int(input("Estrato (1-6): ").strip() or 1)
    estado = input("Estado (ACTIVO/SUSPENDIDO): ").strip().upper()
    if estado not in ["ACTIVO", "SUSPENDIDO"]:
        estado = "ACTIVO"

    consumos = [random.randint(50, 300) for _ in range(30)]

    nuevos = {
        "id": nid,
        "nombre": nombre,
        "documento": documento,
        "estrato": estrato,
        "consumoEnergetico": consumos,
        "estado": estado,
    }

    usuarios_servicio.append(nuevos)  # uso de append
    print("Usuario de servicio agregado.")


def insertar_usuario_servicio():
    print("--- Insertar usuario servicio en posición 0 (ejemplo) ---")
    if not usuarios_servicio:
        print("No hay usuarios activos para insertar antes de ninguno.")
        return

    nuevo = {
        "id": max([u["id"] for u in usuarios_servicio], default=0) + 1,
        "nombre": "Insertado",
        "documento": "9999",
        "estrato": 3,
        "consumoEnergetico": [random.randint(50, 300) for _ in range(30)],
        "estado": "ACTIVO",
    }
    usuarios_servicio.insert(0, nuevo)  # uso de insert
    print("Usuario insertado en la posición 0.")


def remover_usuario_servicio():
    print("--- Quitar un usuario de servicio ---")
    id_eliminar = int(input("ID a eliminar: ").strip())
    encontrado = next((u for u in usuarios_servicio if u["id"] == id_eliminar), None)
    if encontrado:
        usuarios_servicio.remove(encontrado)  # uso de remove
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")


def pop_usuario_servicio():
    print("--- Extraer último usuario de servicio con pop ---")
    if not usuarios_servicio:
        print("No hay usuarios para extraer.")
        return
    eliminado = usuarios_servicio.pop()  # uso de pop
    print(f"Usuario {eliminado['nombre']} eliminado con pop.")


def generar_500_registros_consumo():
    consumos_500 = [random.randint(1, 1000) for _ in range(500)]
    minimo = min(consumos_500)
    maximo = max(consumos_500)
    promedio = sum(consumos_500) / len(consumos_500)
    print("--- Análisis 500 registros numéricos de consumo ---")
    print(f"Min: {minimo}, Max: {maximo}, Promedio: {promedio:.2f}")
    return consumos_500


def menu_gestion_usuarios():
    while True:
        print("\n--- Menú de gestión de usuarios del servicio ---")
        print("1. Mostrar usuarios")
        print("2. Ordenar usuarios por consumo (menor a mayor)")
        print("3. Agregar usuario")
        print("4. Insertar usuario en inicio")
        print("5. Eliminar usuario con remove")
        print("6. Eliminar último usuario con pop")
        print("7. Generar y procesar 500 consumos aleatorios")
        print("8. Volver al menú principal")
        choice = input("Selecciona opción: ").strip()

        if choice == "1":
            mostrar_usuarios()
        elif choice == "2":
            ordenar_usuarios_por_consumo()
        elif choice == "3":
            agregar_usuario_servicio()
        elif choice == "4":
            insertar_usuario_servicio()
        elif choice == "5":
            remover_usuario_servicio()
        elif choice == "6":
            pop_usuario_servicio()
        elif choice == "7":
            generar_500_registros_consumo()
        elif choice == "8":
            break
        else:
            print("Opción no válida")


def menu_principal():
    while True:
        print("\n--- Menú principal ---")
        print("1. Registrar usuario")
        print("2. Login")
        print("3. Salir")
        elección = input("Elige una opción: ").strip()

        if elección == "1":
            registrar_usuario()
        elif elección == "2":
            if login():
                menu_gestion_usuarios()
            else:
                sys.exit(0)
        elif elección == "3":
            print("Saliendo...")
            sys.exit(0)
        else:
            print("Opción inválida, intenta nuevamente.")


if __name__ == "__main__":
    print("Bienvenido al prototipo de gestión de energía")
    menu_principal()

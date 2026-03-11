Estoy haciendo un taller de Python para una empresa de servicios públicos. Necesito un prototipo que cumpla con todos estos requisitos:

1) Registro/Login (mode sencillo)
- Registro de usuario con correo y contraseña.
- Guardar usuarios en una estructura (lista de diccionarios).
- Login con máximo 3 intentos.
- En cada fallo mostrar: "Credenciales incorrectas. Intentos restantes: X".
- Si el login es correcto mostrar: "Login exitoso" y continuar.
- Si se agotan los intentos mostrar: "Cuenta bloqueada temporalmente" y terminar.

2) Estructura de datos de usuarios de servicio
- `usuarios_servicio`: lista con 10 diccionarios iniciales.
- Cada diccionario: 
  - id (int),
  - nombre (str),
  - documento (str o int),
  - estrato (int 1..6),
  - consumoEnergetico (lista de 30 consumos en kWh),
  - estado ("ACTIVO" o "SUSPENDIDO").

3) Funciones y menú
- Implementar todas las funcionalidades con `def`.
- Menú principal:
   - Registrar usuario
   - Login
   - Salir
- Después del login exitoso, mostrar menú de “Gestión de usuarios del servicio”:
   - Mostrar usuarios
   - Ordenar usuarios por consumo total (menor a mayor)
   - Agregar usuario (append)
   - Insertar usuario (insert)
   - Eliminar usuario (remove)
   - Eliminar último usuario (pop)
   - Generar y procesar 500 consumos numéricos aleatorios
   - Volver al menú principal

4) Requisitos didácticos
- Uso explícito de métodos de listas: `append`, `insert`, `remove`, `pop`, `sort`.
- Uso de listas de diccionarios.
- Estructura y flujo con funciones.
- Resultado ejecutable en un solo archivo Python.

Genera código en un solo fichero `taller.py`. Incluye breves comentarios señalando la función de cada bloque.

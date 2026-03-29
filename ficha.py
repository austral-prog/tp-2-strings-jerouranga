def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    nombre = input("Nombre completo: ")
    email = input("Email: ")
    nota_1 = int(input("Nota 1: "))
    nota_2 = int(input("Nota 2: "))
    nota_3 = int(input("Nota 3: "))

    suma = nota_1 + nota_2 + nota_3
    promedio = suma/3
    promedio_entero = suma//3

    print("""========================
    FICHA DEL ALUMNO
========================""")
    print(f"Nombre: {nombre.lstrip().rstrip().title()}")
    print(f"Email: {email.lower().strip()}")
    print(f"Caracteres en nombre: {len(nombre.lstrip().rstrip())}")
    espacio = nombre.lstrip().rstrip().find(" ")
    print(f"Iniciales: {nombre.title().lstrip()[0] + nombre.lstrip().title()[espacio + 1]}")
    apellido = nombre.lower().rstrip().lstrip()[espacio+1:]
    nombre_solo = nombre.lower().lstrip()[:espacio]
    print(f"Usuario: {apellido}.{nombre_solo}")
    print(f"Email valido: {'@' in email}")
    arroba = email.lower().rstrip().find("@")
    print(f"Dominio: {email.lower()[arroba+1: ]}")
    archivo = nombre.title().rstrip().lstrip().replace(" ", "_")
    print(f"Nombre para archivo: {archivo}")
    print(f"Cantidad de a: {nombre.lower().count('a')}")
    print(f"Codigo secreto: {nombre.lstrip().rstrip().upper()[-1::-1]}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    print("=" * 24)




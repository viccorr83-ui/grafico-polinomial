 # ******************************************************
# Estructura de control de ciclo FOR
# ******************************************************

# Lista de nombres de estudiantes
nombres = [
    "ANGEL MAURICIO", "MARCO ANTONIO", "EDGAR DANIEL", "BETHZY ALEYDIZ", "FABIOLA MICHEL",
    "FRIDA VICTORIA", "ERNESTO YAHIR", "ANGEL YAEL", "AMBAR NAHOMI", "URIEL", "LUIS ENRIQUE",
    "BRAYAN ALEXANDER", "ERICK", "FERNANDA ABIGAIL", "ESTEFANI SARAHI", "YUMIKO JATZERY",
    "HANSEL DANIEL", "JULIO ALBERTO", "ENRIQUE LUIS", "PEDRO EDUARDO",
    "MIREYA YAMILE", "ALISON DAYANA", "PRISCILA", "YOJAN JOEL", "SERGIO ALEXIS", "RICARDO",
    "SAMUEL JESHUA", "VANESSA ISABEL", "SARAHI VALERIA", "DAVID GERSSAYN", "JOSE ANGEL",
    "GABRIEL", "CHRISTIAN YUREM", "ARTURO AZAEL", "ARMANDO"
]

# 1. Cuántos nombres inician con vocal
vocales = ("A", "E", "I", "O", "U")       # Tupla con las vocales
inicio_vocal = 0                          # Contador para nombres que inician con vocal

# Recorre cada nombre en la lista
for nombre in nombres:
    # Si la primera letra del nombre está en las vocales
    if nombre[0] in vocales:
        inicio_vocal += 1                 # Aumenta el contador

# Muestra la cantidad de nombres que inician con vocal
print("Nombres que inician con vocal:", inicio_vocal)

# 2. Cuántos nombres tienen más de 10 letras
mas_de_10 = 0                             # Contador para nombres largos

# Recorre cada nombre en la lista
for nombre in nombres:
    # Reemplaza espacios y cuenta caracteres
    if len(nombre.replace(" ", "")) > 10:
        mas_de_10 += 1                    # Aumenta el contador

# Muestra cuántos nombres tienen más de 10 caracteres
print("Nombres con más de 10 caracteres (sin espacio):", mas_de_10)

# 3. Primeros 3 nombres en orden alfabético
nombres_ordenados = sorted(nombres)       # Ordena la lista alfabéticamente
print("Primeros 3 nombres en orden alfabético:")
for nombre in nombres_ordenados[:3]:      # Toma los primeros 3 nombres
    print(nombre)                         # Los imprime

# 4. Buscar nombres que contienen la letra "Y"
con_y = []                                # Lista vacía para guardar los nombres con "Y"

# Recorre cada nombre
for nombre in nombres:
    if "Y" in nombre:                     # Si contiene la letra Y
        con_y.append(nombre)              # Agrega el nombre a la lista

# Muestra los nombres que contienen la letra Y
print("Nombres que contienen la letra Y:")
for nombre in con_y:
    print(nombre)


# ******************************************************
# Estructura de control utilizando condicional if - else
# ******************************************************

# Lista de calificaciones de estudiantes
calificaciones = [85, 60, 78, 45, 92, 55, 70, 100, 39, 68, 80, 59]

# 1. Clasificar cada calificación usando if - else
print("Clasificación de cada calificación:")
aprobados = 0                             # Contador de aprobados
reprobados = 0                            # Contador de reprobados

# Recorre cada calificación
for cal in calificaciones:
    if cal >= 60:                         # Si la calificación es 60 o más
        print(f"{cal}: Aprobado")         # Muestra que aprobó
        aprobados += 1                    # Aumenta el contador de aprobados
    else:                                 # Si no cumple la condición
        print(f"{cal}: Reprobado")        # Muestra que reprobó
        reprobados += 1                   # Aumenta el contador de reprobados

# 2. Contar cuántos aprobaron y reprobaron
print("Total de aprobados:", aprobados)   # Muestra el total de aprobados
print("Total de reprobados:", reprobados) # Muestra el total de reprobados

# 3. Encontrar la calificación más alta y más baja usando if - else
maxima = calificaciones[0]                # Asigna el primer valor como máximo inicial
minima = calificaciones[0]                # Asigna el primer valor como mínimo inicial

# Recorre la lista de calificaciones
for cal in calificaciones:
    if cal > maxima:                      # Si encuentra un valor mayor
        maxima = cal                      # Lo guarda como nuevo máximo
    if cal < minima:                      # Si encuentra un valor menor
        minima = cal                      # Lo guarda como nuevo mínimo

# Muestra los resultados
print("Calificación más alta:", maxima)
print("Calificación más baja:", minima)


# ******************************************************
# Análisis con ciclo WHILE
# ******************************************************

datos = [10, -3, 0, 5, -7, 8, 0, 2, -1]   # Lista de datos numéricos
n = len(datos)                            # Longitud de la lista
indice = 0                                # Índice inicial
suma = 0                                  # Acumulador para la suma
maximo = datos[0]                         # Asigna primer valor como máximo
minimo = datos[0]                         # Asigna primer valor como mínimo
positivos = 0                             # Contador de números positivos
negativos = 0                             # Contador de números negativos
ceros = 0                                 # Contador de ceros

# Bucle while que recorre toda la lista
while indice < n:
    valor = datos[indice]                 # Toma el valor actual
    suma += valor                         # Lo suma al total
    if valor > maximo:                    # Si el valor es mayor que el máximo actual
        maximo = valor                    # Lo asigna como nuevo máximo
    if valor < minimo:                    # Si el valor es menor que el mínimo actual
        minimo = valor                    # Lo asigna como nuevo mínimo
    if valor > 0:                         # Si es positivo
        positivos += 1                    # Aumenta el contador de positivos
    elif valor < 0:                       # Si es negativo
        negativos += 1                    # Aumenta el contador de negativos
    else:                                 # Si es cero
        ceros += 1                        # Aumenta el contador de ceros
    indice += 1                           # Aumenta el índice para avanzar

# Resultados finales
promedio = suma / n                       # Calcula el promedio
print("\nResultados del análisis:")       # Encabezado de resultados
print("Datos ingresados:", datos)         # Muestra la lista original
print("Suma:", suma)                      # Muestra la suma total
print("Promedio:", promedio)              # Muestra el promedio
print("Valor máximo:", maximo)            # Muestra el valor máximo
print("Valor mínimo:", minimo)            # Muestra el valor mínimo
print("Cantidad de positivos:", positivos)# Muestra cuántos positivos hay
print("Cantidad de negativos:", negativos)# Muestra cuántos negativos hay
print("Cantidad de ceros:", ceros)        # Muestra cuántos ceros hay
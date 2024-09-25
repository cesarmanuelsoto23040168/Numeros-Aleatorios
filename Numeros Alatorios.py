import random

def generar_centros_al_cuadrado(cantidad):
    semilla = random.randint(10, 99)
    numeros_generados = []

    for _ in range(cantidad):
        cuadrado = semilla ** 2

        # Convertimos el cuadrado a una cadena para extraer los digitos centrales
        cuadrado_str = str(cuadrado)

        # Aseguramos que tenemos al menos 4 digitos para trabajar
        while len(cuadrado_str) < 4:
            cuadrado_str = '0' + cuadrado_str

        # Se extraen los dos digitos centrales
        if len(cuadrado_str) % 2 == 0:
            centro = cuadrado_str[len(cuadrado_str) // 2 - 1:len(cuadrado_str) // 2 + 1]
        else:
            centro = cuadrado_str[len(cuadrado_str) // 2]

        # Se convierte el centro a un numero
        semilla = int(centro)

        # Verificamos que el nuevo numero no este ya en la lista
        if semilla not in numeros_generados:
            numeros_generados.append(semilla)
        else:
            # Si ya existe, usamos una nueva semilla para evitar duplicados
            semilla = (semilla + 1) % 100 

            # Aseguramos que no repetimos el numero
            while semilla in numeros_generados:
                semilla = (semilla + 1) % 100

            numeros_generados.append(semilla)

    return numeros_generados

# Generar 100 numeros aleatorios
numeros_aleatorios_centros = generar_centros_al_cuadrado(100)
print("Numeros Aleatorios por el metodo de centros al cuadrado:\n")
for i, num in enumerate(numeros_aleatorios_centros, 1):
    print(f"Num {i} = {num}")

# Metodo Medios Cuadrados
def generar_medios_cuadrados(cantidad):
    # Semilla inicial aleatoria de cuatro digitos
    semilla = random.randint(1000, 9999)
    numeros_generados = []

    for _ in range(cantidad):
        # Calculamos el cuadrado de la semilla
        cuadrado = semilla ** 2

        # Convertimos el cuadrado a una cadena
        cuadrado_str = str(cuadrado)

        # Aseguramos que tenemos al menos 8 digitos para trabajar
        while len(cuadrado_str) < 8:
            cuadrado_str = '0' + cuadrado_str

        # Extraemos los cuatro digitos centrales
        centro = cuadrado_str[len(cuadrado_str)//2 - 2:len(cuadrado_str)//2 + 2]

        # Convertimos el centro a un numero
        semilla = int(centro)

        # Agregamos el nuevo numero a la lista
        numeros_generados.append(semilla)

    return numeros_generados

# Generar 100 numeros aleatorios
numeros_aleatorios_medios = generar_medios_cuadrados(100)
print("\nNumeros Aleatorios por Medios Cuadrados:\n")
for i, num in enumerate(numeros_aleatorios_medios, 1):
    print(f"Num {i} = {num}")



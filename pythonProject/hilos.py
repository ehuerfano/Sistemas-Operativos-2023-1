import threading

def calcular_media(numeros):
    media = sum(numeros) / len(numeros)
    print("El valor promedio es", media)

def calcular_maximo(numeros):
    maximo = max(numeros)
    print("El valor máximo es", maximo)

def calcular_minimo(numeros):
    minimo = min(numeros)
    print("El valor mínimo es", minimo)

# Ingresa los números separados por comas
numeros = input("Ingresa una serie de números separados por comas: ")
numeros = [int(n) for n in numeros.split(",")]

# Crea los hilos para realizar los cálculos
hilo_media = threading.Thread(target=calcular_media, args=(numeros,))
hilo_minimo = threading.Thread(target=calcular_minimo, args=(numeros,))
hilo_maximo = threading.Thread(target=calcular_maximo, args=(numeros,))

# Inicia los hilos
hilo_media.start()
hilo_minimo.start()
hilo_maximo.start()

# Espera a que los hilos terminen
hilo_media.join()
hilo_minimo.join()
hilo_maximo.join()

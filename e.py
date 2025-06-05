import time

reservas = [f"Ticket número {i}" for i in range(1, 10001)]

objetivo = "Ticket número 7351"

# Función de Búsqueda Lineal (O(n))
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return

# Función de Búsqueda Binaria (O(log n))
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return


# Medir tiempo de Búsqueda Lineal
inicio = time.time()
indice_lineal = busqueda_lineal(reservas, objetivo)+1
tiempo_lineal = time.time() - inicio

# Medir tiempo de Búsqueda Binaria
inicio = time.time()
indice_binario = busqueda_binaria(reservas, objetivo)
tiempo_binario = time.time() - inicio

# Resultados
print(f"Búsqueda Lineal: Encontrado en índice {indice_lineal} → Tiempo: {tiempo_lineal:.6f} segundos")
print(f"Búsqueda Binaria → Tiempo: {tiempo_binario:.6f} segundos")
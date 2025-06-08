import time

# Funciones de búsqueda
def busqueda_lineal(lista, objetivo):
    for producto in lista:
        if producto[0] == objetivo:
            return producto
    return None

def busqueda_binaria(lista, objetivo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio][0] == objetivo:
            return lista[medio]
        elif lista[medio][0] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

# Lista de productos base
productos_base = ["Auriculares", "Celular", "Laptop", "Monitor", "Mouse", "Teclado", "Tablet"]

# Diferentes tamaños de inventario
tamanios = [1000, 5000, 10000, 50000, 100000]

for tam in tamanios:
    inventario = []  # Lista vacía

    # Generar productos con nombres y códigos
    for i in range(1, tam + 1):
        producto = productos_base[i % len(productos_base)]  # Alternamos productos en orden
        inventario.append((f"{producto} {i}", 1000 + i))

    inventario.sort()  # Ordenamos la lista alfabéticamente para búsqueda binaria

    # Producto específico a buscar
    producto_a_buscar = inventario[len(inventario) // 2][0]  # Tomamos un producto que sabemos que existe para que nos nos quede fuera de rango

    # Medir tiempo de búsqueda lineal
    inicio = time.time()
    resultado_lineal = busqueda_lineal(inventario, producto_a_buscar)
    fin = time.time()
    print(f"Búsqueda Lineal en {tam} productos tomó {fin - inicio:.6f} segundos. Resultado: {resultado_lineal}")

    # Medir tiempo de búsqueda binaria
    inicio = time.time()
    resultado_binaria = busqueda_binaria(inventario, producto_a_buscar)
    fin = time.time()
    print(f"Búsqueda Binaria en {tam} productos tomó {fin - inicio:.6f} segundos. Resultado: {resultado_binaria}")
import random
import time

# Funciones de ordenamiento

def bubble_sort(lista): 
    n = len(lista) # Obtenemos el tamaño de la lista
    for i in range(n):
        swapped = False # Indicador de si se realizaron intercambios
        
        # Recorremos la lista hasta el penúltimo elemento
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]: # Comparamos el elemento actual con el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True # Realizamos el intercambio si el elemento actual es mayor que el siguiente
        
        # Si no se realizaron intercambios, la lista ya está ordenada
        if not swapped: 
            break
    return lista # Devolvemos la lista ordenada

def selection_sort(lista):
    n = len(lista) # Obtenemos el tamaño de la lista
    
    # Recorremos la lista para encontrar el elemento mínimo en cada iteración
    for i in range(n):
        min_idx = i # Suponemos que el primer elemento es el mínimo
        for j in range(i + 1, n): # Recorremos el resto de la lista
            if lista[j] < lista[min_idx]: # Comparamos el elemento actual con el mínimo encontrado
                # Si encontramos un elemento menor, actualizamos el índice del mínimo
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i] # Intercambiamos el elemento actual con el mínimo encontrado
    return lista # Devolvemos la lista ordenada

def insertion_sort(lista): 
    for i in range(1, len(lista)): # Recorremos la lista desde el segundo elemento
        key = lista[i] # Guardamos el elemento actual
        j = i - 1 # Inicializamos j como el índice del elemento anterior
        while j >= 0 and lista[j] > key: # Mientras j sea válido y el elemento anterior sea mayor que el actual
            # Desplazamos el elemento hacia la derecha
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key # Insertamos el elemento actual en su posición correcta
    return lista # Devolvemos la lista ordenada

def quick_sort(lista): 
    if len(lista) <= 1: # Si la lista tiene 0 o 1 elementos, ya está ordenada
        return lista
    pivot = lista[len(lista) // 2] # Elegimos el pivote como el elemento del medio
    # Particionamos la lista en menores, iguales y mayores al pivote
    menores = [x for x in lista if x < pivot]
    iguales = [x for x in lista if x == pivot]
    mayores = [x for x in lista if x > pivot]

    # Recursivamente ordenamos las particiones y las combinamos 
    return quick_sort(menores) + iguales + quick_sort(mayores) 

def merge_sort(lista):
    if len(lista) <= 1: # Si la lista tiene 0 o 1 elementos, ya está ordenada
        return lista
    # Dividimos la lista en dos mitades
    mid = len(lista) // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])
    merged = [] # Lista para almacenar la lista ordenada
    i = j = 0 # Índices para recorrer las dos mitades
    
    # Combinamos las dos mitades ordenadas
    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            merged.append(left[i]); i += 1 
        else:
            merged.append(right[j]); j += 1

    # Añadimos los elementos restantes de las mitades
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged # Devolvemos la lista ordenada

# Datos de prueba y medición de tiempos

tamanios = [1_000, 5_000, 10_000, 50_000, 100_000]
algoritmos = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort
}

for n in tamanios:
    # Generar lista aleatoria de n elementos y desordenarla
    lista_base = list(range(n))
    random.shuffle(lista_base)
    print(f"\n== Tamaño: {n} elementos ==")

    # Probar cada algoritmo de ordenamiento
    for nombre, funcion in algoritmos.items():
        copia = lista_base.copy()
        t1 = time.time()
        resultado = funcion(copia)
        t2 = time.time()
        # Verificamos que quedó ordenada
        assert resultado == sorted(lista_base)
        print(f"{nombre:13s}: {t2 - t1:.4f} s")
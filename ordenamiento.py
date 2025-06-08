import random
import time

# Funciones de ordenamiento

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivot]
    iguales = [x for x in lista if x == pivot]
    mayores = [x for x in lista if x > pivot]
    return quick_sort(menores) + iguales + quick_sort(mayores)

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

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

    for nombre, funcion in algoritmos.items():
        copia = lista_base.copy()
        t1 = time.time()
        resultado = funcion(copia)
        t2 = time.time()
        # Verificamos que quedó ordenada
        assert resultado == sorted(lista_base)
        print(f"{nombre:13s}: {t2 - t1:.4f} s")
# Búsqueda lineal por nombre
def busqueda_lineal(productos, nombre_buscado):
    nombre_buscado = nombre_buscado.lower()
    for producto in productos:
        if producto.nombre.lower() == nombre_buscado:
            return producto
    return None

# Búsqueda binaria (requiere lista ordenada por nombre)
def busqueda_binaria(productos, nombre_buscado):
    nombre_buscado = nombre_buscado.lower()
    productos.sort(key=lambda x: x.nombre.lower())  # Ordenar ignorando mayúsculas/minúsculas
    izq = 0
    der = len(productos) - 1
    while izq <= der:
        medio = (izq + der) // 2
        nombre_medio = productos[medio].nombre.lower()  # Normalizo a minúsculas
        if nombre_medio == nombre_buscado:
            return productos[medio]
        elif nombre_medio < nombre_buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return None

# Bubble Sort por precio
def bubble_sort(productos):
    n = len(productos)
    for i in range(n):
        for j in range(0, n-i-1):
            if productos[j].precio > productos[j+1].precio:
                productos[j], productos[j+1] = productos[j+1], productos[j]

# Quick Sort por stock
def quick_sort(productos):
    if len(productos) <= 1:
        return productos
    pivote = productos[0]
    menores = [p for p in productos[1:] if p.stock <= pivote.stock]
    mayores = [p for p in productos[1:] if p.stock > pivote.stock]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Inventario con búsqueda y ordenamiento en Python

## 📌 Descripción
Este proyecto simula un **sistema de inventario de productos**, enfocado en aplicar algoritmos clásicos de **búsqueda** y **ordenamiento** sobre un conjunto de datos cargados desde un archivo `.csv`. El programa permite buscar productos por nombre, ordenar por precio o stock, y guardar los resultados ordenados.

Está pensado como un caso práctico para aplicar conocimientos de algoritmos, análisis de eficiencia y estructuras de datos en Python.


## 🚀 Funcionalidades
- ✅ Carga de productos desde archivo `inventario_productos.csv` o `productos_aleatorios.csv`
- ✅ Búsqueda de productos por nombre con:
  - Búsqueda Lineal
  - Búsqueda Binaria (requiere orden previo)
- ✅ Ordenamiento de productos por:
  - Precio (Bubble Sort)
  - Stock (Quick Sort)
- ✅ Medición del tiempo de ejecución de cada algoritmo
- ✅ Guardado de resultados ordenados en archivos CSV (`ordenado_precio.csv`, `ordenado_stock.csv`)
- ✅ Interfaz por menú en consola para interacción clara
- ✅ Código modular, separado en archivos `main.py`, `ordenamiento.py`, y `busqueda.py`

## 🐍 Tecnologías
- 🐍 **Python 3.13.0**
- 📄 **csv**: para lectura y escritura de archivos de productos
- ⏱️ **time.perf_counter()**: para medición precisa del rendimiento de los algoritmos
- 🧮 Algoritmos clásicos:
  - **Búsqueda lineal**: O(n)
  - **Búsqueda binaria**: O(log n)
  - **Bubble sort**: O(n²)
  - **Quick sort**: O(n log n)
  - 
## 🎓 Reflexión
- Este trabajo permitió aplicar la teoría de búsqueda y ordenamiento a un caso práctico, reforzando conceptos clave y evaluando la eficiencia de cada algoritmo en un entorno simulado.

## ▶️ Cómo ejecutar
1. Asegurate de tener Python instalado (versión 3.x).
2. Colocá en la misma carpeta:
   - `main.py`
   - `busqueda.py`
   - `ordenamiento.py`
   - `inventario_productos.csv` o `productos_aleatorios.csv`
3. Abrí una terminal y ejecutá:

```bash
python main.py

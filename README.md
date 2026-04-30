# Proyecto: Fundamentos de Python – Estructuras de Datos

### Autor
Mateo Úsuga Álvarez

## Descripción del proyecto

Este proyecto reúne una serie de retos prácticos desarrollados en Python con el objetivo de aplicar y reforzar los conceptos fundamentales de estructuras de datos.
A través de ejercicios progresivos se trabajó con listas, tuplas, diccionarios, conjuntos (sets) y comprehensions, resolviendo problemas como gestión de inventarios, análisis de catálogos y procesamiento de datos.

## Temas aprendidos

### Listas

* Creación y manipulación de listas
* Uso de índices positivos y negativos
* Métodos como append(), insert(), extend()
* Eliminación con remove(), pop() y clear()
* Recorridos con for

### Tuplas

* Estructuras inmutables
* Desempaquetado de valores
* Uso del operador *
* Retorno múltiple en funciones

### Diccionarios

* Estructura clave → valor
* Métodos como items(), values(), get()
* Operaciones CRUD (update(), pop())
* Iteración y ordenamiento con sorted()

### Conjuntos (Sets)

* Elementos únicos y eliminación de duplicados
* Operaciones: unión, intersección, diferencia
* Uso de operadores &, |, -, ^
* Verificación de subconjuntos

### Comprehensions

* List comprehension
* Dict comprehension
* Set comprehension
* Uso de filtros y transformaciones
* Optimización del código

## Evidencia de retos resueltos

### Reto 1 – Listas (Gestión de inventario)

Se implementó un sistema para añadir productos, actualizar precios, registrar ventas y mostrar el inventario.

### Reto 2 – Tuplas (Catálogo de películas)

Se trabajó con tuplas anidadas, búsqueda por director y cálculo de estadísticas.

### Reto 3 – Diccionarios (Ventas por región)

Se utilizaron diccionarios anidados para calcular totales, porcentajes y ordenar resultados.

### Reto 4 – Conjuntos (Tiendas y recomendaciones)

Se aplicaron operaciones de conjuntos para analizar productos y preferencias.

### Reto 5 – Comprehensions (Análisis de ventas)

Se usaron list, dict y set comprehension para transformar y filtrar datos de manera eficiente.

## Capturas de ejecución

### Reto 1

![evidencia template](/images/Reto%201.png)

La ejecución del reto 1 muestra el inventario final después de varias operaciones. Se actualizó el precio de "pan", se registró una venta de "manzana" reduciendo su cantidad, "leche" se mantuvo igual y se añadió el producto "huevos". El resultado se imprime recorriendo la lista con un ciclo for, demostrando cómo las listas permiten modificar y gestionar datos dinámicamente.

### Reto 2

![evidencia template](/images/Reto%202.png)

La ejecución del reto 2 muestra un catálogo de películas almacenado en una tupla de tuplas. Se imprime cada película usando desempaquetado en un ciclo for, luego se separa la primera película del resto con el operador *. También se filtran las películas de un director específico y se calculan estadísticas como puntuación mínima, máxima y promedio. Esto demuestra el uso de tuplas, desempaquetado y funciones que retornan múltiples valores.

### Reto 3 

![evidencia template](/images/Reto%203.png)

La ejecución del reto 3 muestra un reporte de ventas usando diccionarios. Se calculan los totales por región, se identifica la región con mayores ventas, se suman las ventas por trimestre y se obtienen los porcentajes de cada región. Esto demuestra el uso de diccionarios, iteración y cálculo de datos.

### Reto 4

![evidencia template](/images/Reto%204.png)

La ejecución del reto 4 muestra el uso de conjuntos para analizar productos y preferencias. Se obtiene el catálogo completo, los productos comunes y los exclusivos de cada tienda, además de verificar si hay elementos en común. También se comparan gustos de usuarios usando operaciones de conjuntos. Esto demuestra el uso de sets y sus operaciones básicas.

### Reto 5

![evidencia template](/images/Reto%205.png)

La ejecución del reto 5 muestra el uso de comprehensions para procesar datos de ventas. Se calculan los valores totales por producto, se filtran productos destacados, se crea un diccionario con información detallada y se identifican categorías únicas y productos baratos. Finalmente, se obtiene un resumen y el total general de ventas. Esto demuestra el uso de list, dict y set comprehension para trabajar con datos de forma eficiente.

## Reflexión personal del aprendizaje

Durante el desarrollo de este proyecto logré comprender cómo funcionan las principales estructuras de datos en Python y cómo aplicarlas en situaciones prácticas.
Al inicio algunos conceptos resultaron complejos, pero con la práctica se volvieron más claros.

Este proceso me permitió mejorar mi lógica de programación, organizar mejor la información y escribir código más estructurado.


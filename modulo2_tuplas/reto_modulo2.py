# Definir catalogo como tupla de subtuplas
catalogo = (
    ("El Padrino", "Francis Ford Coppola", 1972, 9.2),
    ("Cadena Perpetua", "Frank Darabont", 1994, 9.3),
    ("El Caballero Oscuro", "Christopher Nolan", 2008, 9.0),
    ("Pulp Fiction", "Quentin Tarantino", 1994, 8.9),
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("Forrest Gump", "Robert Zemeckis", 1994, 8.8),
)

# Recorrer catalogo con for desempaquetando los cuatro campos
print("CATALOGO DE PELICULAS\n")
for titulo, director, año, puntuacion in catalogo:
    print(titulo, "(", año, ") - Dirigida por", director, "- Puntuacion:", puntuacion)

# Usar operador * para separar primera pelicula del resto
primera_pelicula, *resto_peliculas = catalogo

print("\nPrimera pelicula:")
print(primera_pelicula[0], "(", primera_pelicula[2], ")")

print("\nResto de peliculas:")
for titulo, director, año, puntuacion in resto_peliculas:
    print("-", titulo, "(", año, ")")

# Definir buscar_por_director(director)
def buscar_por_director(director):
    coincidencias = []
    for pelicula in catalogo:
        if pelicula[1] == director:
            coincidencias.append(pelicula)
    return tuple(coincidencias)

# Definir obtener_estadisticas(peliculas)
def obtener_estadisticas(peliculas):
    if len(peliculas) == 0:
        return (0.0, 0.0, 0.0)

    # Inicializar con el primer valor
    min_punt = peliculas[0][3]
    max_punt = peliculas[0][3]
    suma = 0

    for pelicula in peliculas:
        puntuacion = pelicula[3]

        if puntuacion < min_punt:
            min_punt = puntuacion

        if puntuacion > max_punt:
            max_punt = puntuacion

        suma = suma + puntuacion

    promedio = suma / len(peliculas)
    return (min_punt, max_punt, promedio)

# Llamar a buscar_por_director e imprimir coincidencias
director_buscar = "Christopher Nolan"
peliculas_encontradas = buscar_por_director(director_buscar)

print("\nPeliculas de", director_buscar, ":")
for titulo, director, año, puntuacion in peliculas_encontradas:
    print("-", titulo, "(", año, ") -", puntuacion)

# Desempaquetar retorno de obtener_estadisticas
min_puntuacion, max_puntuacion, promedio_puntuacion = obtener_estadisticas(catalogo)

# Imprimir minima, maxima y promedio
print("\nEstadisticas:")
print("Minima:", min_puntuacion)
print("Maxima:", max_puntuacion)
print("Promedio:", promedio_puntuacion)
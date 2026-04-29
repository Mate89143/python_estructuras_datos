# Definir tienda_centro, tienda_norte y tienda_sur
tienda_centro = {"pan", "leche", "huevos", "arroz"}
tienda_norte  = {"leche", "queso", "arroz", "pollo"}
tienda_sur    = {"pan", "carne", "huevos", "pescado"}

# Calcular catalogo_completo con union()
catalogo_completo = tienda_centro.union(tienda_norte).union(tienda_sur)

# Calcular productos_comunes con intersection()
productos_comunes = tienda_centro.intersection(tienda_norte).intersection(tienda_sur)

# Exclusivos de cada tienda con difference(union())
exclusivos_centro = tienda_centro.difference(tienda_norte.union(tienda_sur))
exclusivos_norte  = tienda_norte.difference(tienda_centro.union(tienda_sur))
exclusivos_sur    = tienda_sur.difference(tienda_centro.union(tienda_norte))

# Verificar pares con isdisjoint()
centro_norte = tienda_centro.isdisjoint(tienda_norte)
centro_sur   = tienda_centro.isdisjoint(tienda_sur)
norte_sur    = tienda_norte.isdisjoint(tienda_sur)

# Definir usuario1, usuario2, usuario3
usuario1 = {"accion", "comedia", "drama"}
usuario2 = {"drama", "terror", "accion"}
usuario3 = {"comedia", "romance", "drama"}

# Calcular con & | - ^ <= y mostrar resumen
comunes_1_2 = usuario1 & usuario2
universo    = usuario1 | usuario2 | usuario3
exclusivos_1 = usuario1 - usuario2
dif_1_3     = usuario1 ^ usuario3
subconjunto = usuario1 <= universo

print("CATALOGO COMPLETO:", catalogo_completo)
print("PRODUCTOS COMUNES:", productos_comunes)

print("\nEXCLUSIVOS:")
print("Centro:", exclusivos_centro)
print("Norte:", exclusivos_norte)
print("Sur:", exclusivos_sur)

print("\nSOLAPAMIENTOS (isdisjoint):")
print("Centro-Norte:", centro_norte)
print("Centro-Sur:", centro_sur)
print("Norte-Sur:", norte_sur)

print("\nRECOMENDACIONES DE USUARIOS:")
print("Comunes usuario1 y usuario2:", comunes_1_2)
print("Universo de generos:", universo)
print("Exclusivos usuario1:", exclusivos_1)
print("Diferencias usuario1 y usuario3:", dif_1_3)
print("usuario1 es subconjunto del universo:", subconjunto)
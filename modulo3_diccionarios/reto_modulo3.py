# Definir ventas_por_region
ventas_por_region = {
    "Norte": {"Q1": 15000, "Q2": 18000, "Q3": 20000, "Q4": 22000},
    "Sur":   {"Q1": 12000, "Q2": 14000, "Q3": 16000, "Q4": 18000},
    "Este":  {"Q1": 10000, "Q2": 13000, "Q3": 17000, "Q4": 21000},
    "Oeste": {"Q1": 9000,  "Q2": 11000, "Q3": 15000, "Q4": 19000}
}

# Calcular ventas totales con items() y sum(values())
totales_por_region = {}
for region, trimestres in ventas_por_region.items():
    total = sum(trimestres.values())
    totales_por_region[region] = total

# Encontrar region con max() key=lambda
region_mayor = max(totales_por_region, key=lambda r: totales_por_region[r])

# Inicializar totales_por_trimestre
totales_por_trimestre = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}

# Acumular con iteracion anidada
for region, trimestres in ventas_por_region.items():
    for trimestre, valor in trimestres.items():
        totales_por_trimestre[trimestre] = totales_por_trimestre[trimestre] + valor

# Calcular gran_total
gran_total = sum(totales_por_region.values())

# Generar porcentajes con dict comprehension
porcentajes = {
    region: (total / gran_total) * 100
    for region, total in totales_por_region.items()
}

# Imprimir reporte ordenado
print("REPORTE DE VENTAS\n")

print("Totales por region:")
for region, total in sorted(totales_por_region.items(), key=lambda x: x[1], reverse=True):
    print(region, ":", total)

print("\nRegion con mayores ventas:", region_mayor)

print("\nTotales por trimestre:")
for trimestre, total in totales_por_trimestre.items():
    print(trimestre, ":", total)

print("\nPorcentaje por region:")
for region, pct in porcentajes.items():
    print(region, ":", round(pct, 2), "%")
# Definir ventas con 6 productos (producto, unidades, precio, categoria)
ventas = [
    {"producto": "laptop",  "unidades": 10, "precio": 800, "categoria": "tecnologia"},
    {"producto": "teclado", "unidades": 40, "precio": 30,  "categoria": "tecnologia"},
    {"producto": "mouse",   "unidades": 50, "precio": 20,  "categoria": "tecnologia"},
    {"producto": "monitor", "unidades": 15, "precio": 200, "categoria": "tecnologia"},
    {"producto": "silla",   "unidades": 20, "precio": 150, "categoria": "muebles"},
    {"producto": "mesa",    "unidades": 5,  "precio": 300, "categoria": "muebles"}
]

# List comp: valor_total = unidades * precio
valor_total = [i["unidades"] * i["precio"] for i in ventas]

# List comp con filtro: productos_destacados (valor > 1000)
productos_destacados = [
    i["producto"] for i in ventas
    if i["unidades"] * i["precio"] > 1000
]

# Dict comp: producto_info  nombre: {valor, unidades}
producto_info = {
    i["producto"]: {
        "valor": i["unidades"] * i["precio"],
        "unidades": i["unidades"]
    }
    for i in ventas
}

# Dict comp con filtro: ranking_premium (precio > 50) desc
ranking_premium = {
    k: v for k, v in sorted(
        {
            i["producto"]: i["unidades"] * i["precio"]
            for i in ventas if i["precio"] > 50
        }.items(),
        key=lambda x: x[1],
        reverse=True
    )
}

# Set comp: categorias_unicas
categorias_unicas = {i["categoria"] for i in ventas}

# Set comp con filtro: productos_baratos (precio <= 50)
productos_baratos = {
    i["producto"] for i in ventas if i["precio"] <= 50
}

# Combinar: resumen_formateado dict comp filtrado
resumen_formateado = {
    i["producto"]: i["unidades"] * i["precio"]
    for i in ventas if i["unidades"] * i["precio"] > 500
}

# Calcular e imprimir gran_total
gran_total = sum(valor_total)

print("VALOR TOTAL POR PRODUCTO:", valor_total)
print("PRODUCTOS DESTACADOS:", productos_destacados)
print("PRODUCTO INFO:", producto_info)
print("RANKING PREMIUM:", ranking_premium)
print("CATEGORIAS UNICAS:", categorias_unicas)
print("PRODUCTOS BARATOS:", productos_baratos)
print("RESUMEN:", resumen_formateado)
print("GRAN TOTAL:", gran_total)
import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("resultados", exist_ok=True)

datos_ventas = [
    {"producto": "Teclado Mecanico", "cantidad": 5, "precio": 45000, "fecha": "2026-01-15"},
    {"producto": "Mouse Gamer", "cantidad": 10, "precio": 24000, "fecha": "2026-01-20"},
    {"producto": "Monitor 24 FHD", "cantidad": 2, "precio": 185000, "fecha": "2026-02-05"},
    {"producto": "Teclado Mecanico", "cantidad": 3, "precio": 45000, "fecha": "2026-02-12"},
    {"producto": "Auriculares XT", "cantidad": 7, "precio": 32000, "fecha": "2026-03-01"},
    {"producto": "Mouse Gamer", "cantidad": 12, "precio": 25000, "fecha": "2026-03-22"},
    {"producto": "Monitor 24 FHD", "cantidad": 1, "precio": 180000, "fecha": "2026-04-10"},
    {"producto": "Auriculares XT", "cantidad": 4, "precio": 35000, "fecha": "2026-04-18"},
    {"producto": "Teclado Mecanico", "cantidad": 6, "precio": 46000, "fecha": "2026-05-02"},
    {"producto": "Mouse Gamer", "cantidad": 15, "precio": 25000, "fecha": "2026-05-15"},
    {"producto": "Monitor 24 FHD", "cantidad": 3, "precio": 178000, "fecha": "2026-05-20"},
    {"producto": "Auriculares XT", "cantidad": 5, "precio": 35000, "fecha": "2026-05-25"}
]

cantidades = np.array([item["cantidad"] for item in datos_ventas])
precios = np.array([item["precio"] for item in datos_ventas])
productos = [item["producto"] for item in datos_ventas]

ingresos_por_venta = cantidades * precios
ventas_totales = np.sum(ingresos_por_venta)

conteo_productos = {}
for prod, cant in zip(productos, cantidades):
    conteo_productos[prod] = conteo_productos.get(prod, 0) + cant
producto_mas_vendido = max(conteo_productos, key=conteo_productos.get)
unidades_producto_mas_vendido = conteo_productos[producto_mas_vendido]

meses_etiquetas = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
ventas_mensuales = np.zeros(5)

for item, ingreso in zip(datos_ventas, ingresos_por_venta):
    mes = int(item["fecha"].split("-")[1])
    ventas_mensuales[mes - 1] += ingreso

plt.figure(figsize=(8, 5))
plt.plot(meses_etiquetas, ventas_mensuales, marker='o', color='blue', linewidth=2)
plt.title("Evolucion de Ventas - Primer Semestre 2026")
plt.xlabel("Mes")
plt.ylabel("Total ($)")
plt.grid(True, alpha=0.5)

ruta_grafico = os.path.join("resultados", "grafico_resultados.png")
plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
plt.close()

ruta_reporte = os.path.join("resultados", "reporte.txt")
with open(ruta_reporte, "w") as f:
    f.write("=== REPORTES DE VENTAS - CELULA COMERCIAL ===\n\n")
    f.write(f"Total Facturado: ${ventas_totales:,.2f}\n")
    f.write(f"Producto mas vendido: {producto_mas_vendido} ({unidades_producto_mas_vendido} un.)\n\n")
    f.write("Detalle mensual:\n")
    for m, v in zip(meses_etiquetas, ventas_mensuales):
        f.write(f" * {m}: ${v:,.2f}\n")

print("Procesamiento completo. Archivos creados.")

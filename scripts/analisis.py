import os
import numpy as np

print("Ejecutando el analisis estadistico de la celula comercial...")

datos = [23.45, 12, 67, 34, 89, 21, 54]
promedio = np.mean(datos)

os.makedirs("resultados", exist_ok=True)
with open("resultados/reporte.txt", "w") as f:
    f.write(f"Resultado del Analisis Estadistico\n")
    f.write(f"Promedio calculado: {promedio}\n")

print("¡Analisis completado con exito! El reporte se guardo en /resultados.")

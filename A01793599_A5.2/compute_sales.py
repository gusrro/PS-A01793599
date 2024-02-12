"""
Ejercicio 1 - Actividad 5.2 - Compute sales
"""
import sys
import time
import json


# Se inicia el contador de tiempo
start = time.time()

print("Ejercicio 1 - Compute sales")

# Leyendo ambos archivos desde los parámetros
fileName1 = sys.argv[1]
fileName2 = sys.argv[2]
PREFIX = "TC1"
if "TC1" in fileName2.upper():
    PREFIX = "TC1"
elif "TC2" in fileName2.upper():
    PREFIX = "TC2"
elif "TC3" in fileName2.upper():
    PREFIX = "TC3"


# Abriendo el archivo 1
with open(f"{PREFIX}/{fileName1}", mode='r', encoding='utf-8') as file1:
    dataCatalog = json.load(file1)

# Abriendo el archivo 2
with open(f"{PREFIX}/{fileName2}", mode='r', encoding='utf-8') as file2:
    dataSales = json.load(file2)

groupedSales = {}
allProducts = {}

for item in dataSales:
    currentProduct = item.get('Product')
    if None is groupedSales.get(currentProduct):
        groupedSales[currentProduct] = item.get('Quantity', 0)
    else:
        groupedSales[currentProduct] = groupedSales[currentProduct] \
            + item.get('Quantity', 0)

for item in dataCatalog:
    currentProduct = item.get('title')
    allProducts[currentProduct] = item.get('price', 0.0)

ACCUMULATED = 0.0
for product, quantity in groupedSales.items():
    if None is allProducts.get(product):
        print(f"El producto '{product}' no existe en el catálogo de productos")
    else:
        ACCUMULATED += quantity * allProducts[product]

# Una vez obtenido el acumulado se imprimen los resultados
with open("SalesResults.txt", "w", encoding='utf-8') as new_file:
    temp_string = f"Resultado caso {PREFIX}: {round(ACCUMULATED, 2)}"
    new_file.write(temp_string)
    print(temp_string)
    temp_string = f"\n{len(groupedSales)} registros de venta considerados."
    new_file.write(temp_string)
    print(temp_string)
    new_file.close()

# Se obtiene el contador de tiempo de fin de proceso
end = time.time()
print(f"Tiempo de ejecución: {str( round((end - start),5) )} segundos")

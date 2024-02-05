"""
Este es el ejercicio 1 - Compute Statistics
"""
import math
import sys
import time
from collections import Counter


# Funciones el programa para cálculos estadísticos
def is_float(string):
    """Definiendo la funcion de verificación de números float"""    
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_mean( data ):
    """ Función para obtener el promedio"""
    total_sum = 0
    for item in data:
        total_sum += item
    return total_sum/len(data)

def get_median( data ):
    """ Función para obtener la mediana"""
    answer = 0
    data_sorted = sorted( data )
    length = len(data_sorted)
    if length % 2 == 0:
        answer = ( data_sorted[ (int)(length/2)  ] + data_sorted[ (int)((length/2) + 1)  ] ) / 2
    else:
        answer = data_sorted[ (int)((length + 1) /2)  ]
    return answer

def get_mode( data ):
    """ Función para obtener la moda"""
    c = Counter(data)
    mode_list = [k for k, v in c.items() if v == c.most_common(1)[0][1]]
    if len(data) == len(mode_list):
        string_buffer = "No existe moda para el set de datos"
    else:
        string_buffer = f"Tamaño de la moda {len(mode_list)}"
        for item in mode_list:
            string_buffer += "\n[ " + str(item) + " ]"
    return string_buffer

def get_standard_deviation( data ):
    """ Función para obtener la desviación"""
    return math.sqrt( get_variance(data))

def get_variance( data ):
    """ Función para obtener la varianza"""
    mean = get_mean( data )
    square_result = 0
    for item in data:
        square_result += math.pow( item - mean, 2 )
    return square_result/(len(data)-1)

start = time.time()

print("Ejercicio 1 - Compute statistics")

# Leyendo nombre del archivo desde los parametros
fileName = sys.argv[1]

# Abriendo el archivo
with open("P1/" + fileName, mode='r', encoding='utf-8') as file1:
    linesList = file1.readlines()

# Una vez obtenida la lista de elementos, convertiremos a nùmeros
numberList = []
COUNTER = 0
for line in linesList:
    COUNTER += 1
    if is_float(line):
        numberList.append( float(line) )
    else:
        print(f"La línea {COUNTER} contiene caracteres inválidos {line} ... continua la ejecución")
print("\nLectura y conversión terminada\n")

print(f"Se convirtieron {len(numberList)} números de una lectura total de {len(linesList)} líneas")

end = time.time()

print(f"Valor promedio: {get_mean(numberList)}")
print(f"Valor mediana : {get_median(numberList)}")
print(f"Valor moda    : {get_mode(numberList)}")
print(f"Valor varianza: {get_variance(numberList)}")
print(f"Valor Desv. E.: {get_standard_deviation(numberList)}")

print(f"Tiempo de ejecución: {str( end - start )}" )

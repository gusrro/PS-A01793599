"""
Este es el ejercicio 2 - Convert numbers
"""
import sys
import time

# Funciones del programa
def is_float(string):
    """Definiendo la funcion de verificación de números float"""    
    try:
        float(string)
        return True
    except ValueError:
        return False

def convert_to_hex( float_number ):
    """ Función para obtener el número a Hexadecimal"""
    hex_characters = "0123456789ABCDEF"
    hexadecimal = ''
    number = int(float_number)

    if number == 0:
        return '0'
    if number < 0:
        return 'Negative numbers are not supported'

    while number > 0:
        remainder = number % 16
        hexadecimal = hex_characters[remainder] + hexadecimal
        number = number // 16
    return hexadecimal


def convert_to_bin( float_number ):
    """ Función para obtener el número a Binario"""
    binary = ''
    number = int(float_number)

    if number == 0:
        return '0'
    if number < 0:
        return 'Negative numbers are not supported'

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    return binary

start = time.time()

print("Ejercicio 2 - Convert Numbers")

# Leyendo nombre del archivo desde los parametros
fileName = sys.argv[1]

# Abriendo el archivo
with open("P2/" + fileName, mode='r', encoding='utf-8') as file1:
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

with open("ConvertionResults.txt", "w", encoding='utf-8') as new_file:
    for item in numberList:
        temp_string = f"Bin({item}): {convert_to_bin(item)} - Hex({item}): {convert_to_hex(item)}\n"
        print( temp_string)
        new_file.write(temp_string)

    temp_string = f"\nSe escribieron {len(numberList)} palabras ejecutando {fileName}\n"
    print( temp_string )
    new_file.write(temp_string)

    new_file.close()

end = time.time()
print(f"Tiempo de ejecución: {str( end - start )}" )

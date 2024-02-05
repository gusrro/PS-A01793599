"""
Este es el ejercicio 3 - Word count
"""
import sys
import time

# Funciones del programa
def is_word( text ):
    """Función para determinar si el texto es una palabra"""    
    return text.isalpha()


start = time.time()

print("Ejercicio 3 - Counting words")

# Leyendo nombre del archivo desde los parametros
fileName = sys.argv[1]

# Abriendo el archivo
with open("P3/" + fileName, mode='r', encoding='utf-8') as file1:
    linesList = file1.readlines()

# Una vez obtenida la lista de elementos, convertiremos a nùmeros
wordsList = []
word_counts = {}
COUNTER = 0
for line in linesList:
    COUNTER += 1
    line = line.strip().lower()
    if is_word(line):
        wordsList.append( line )
        word_counts[line] = word_counts.get(line, 0) + 1
    else:
        print(f"El elemento {line} es inválido ... continua la ejecución")

print("\nLectura y conversión terminada\n")

print(f"Se obtuvieron {len(wordsList)} palabras de una lectura total de {len(linesList)} líneas")

# Agrupando los resultados en listas conforme su cantidad de ocurrencias
another_dict = {}
for word, times in word_counts.items():
    if None is another_dict.get(times):
        transport = []
        another_dict[times] = transport
    else:
        transport = another_dict[times]
    transport.append(word)
    transport.sort()

# Juntando todas las listas de mayor a menor ocurrencias
finalList = []
for key in range(1000, 0, -1):
    if None is not another_dict.get(key):
        finalList.extend( another_dict.get(key) )

# Imprimiendo resultado final
with open("WordCountResults.txt", "w", encoding='utf-8') as new_file:
    for key in finalList:
        temp_string = f"Palabra: {key}  -  counts: {word_counts.get(key)} \n"
        print( temp_string )
        new_file.write(temp_string)

    temp_string = f"\nSe escribieron {len(finalList)} palabras ejecutando {fileName}\n"
    print( temp_string )
    new_file.write(temp_string)

    new_file.close()


end = time.time()



print(f"Tiempo de ejecución: {str( round((end - start),5) )} segundos" )

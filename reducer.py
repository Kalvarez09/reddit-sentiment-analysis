#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # saltar líneas vacías
    parts = line.split('\t', 1)
    if len(parts) != 2:
        continue  # línea mal formada
    word, count_str = parts
    try:
        count = int(count_str)
    except ValueError:
        continue  # si no es entero, saltar
    if current_word == word:
        current_count += count  # acumular cuenta para palabra actual
    else:
        if current_word is not None:
            # cuando cambia la palabra, imprimir la acumulada
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# imprimir la última palabra procesada
if current_word is not None:
    print(f"{current_word}\t{current_count}")

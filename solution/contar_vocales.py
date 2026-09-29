"""
Escribir un programa que cuente la cantidad de vocales en una frase

Paso 0. Entender con un ejemplo
Ejemplo: ¿Cuántas vocales hay en la frase: "Hola, mundo."?
Respuesta: Hay 4 vocales: la "o" y la "a" de "Hola" y la "u" 
           y la "o" de "mundo".
           
Paso 1. Análisis
"""
# Declaraciones
VOCALES = "aeiouáéíóúü"

# Entradas
frase = input("Frase: ")

# Proceso
posicion = 0
contar_vocales = 0
while posicion < len(frase):
    caracter = frase[posicion].lower()
    if caracter in VOCALES:
        contar_vocales += 1
    posicion += 1
    
print(f"La frase analizada contiene {contar_vocales} vocales.")
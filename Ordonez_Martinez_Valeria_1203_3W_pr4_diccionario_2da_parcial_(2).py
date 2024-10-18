# Diccioario
print(" ")
print("Ordonez Martinez Valeria 1203 3W Practica 4")
print(" ")

diccionario = {}

# Solicitamos las palabras y las traducimos
palabras = input("Escribe las palabras en el formato: Hola: Hello, Dog: Perro, Casa: House \n")

# Convertimos la entrada en formato título
palabras = palabras.title()

# Creamos el diccionario a partir de la entrada
for i in palabras.split(","):
    clave, valor = i.split(":")
    diccionario[clave.strip()] = valor.strip()  # Usamos strip para eliminar espacios

# Solicitamos la frase a traducir
frase = input("Escribe una frase en español para traducir: \n")

# Traducimos la frase
for j in frase.split(" "):
    if j in diccionario:
        print(diccionario[j], end=" ")  # Imprimimos la traducción en la misma línea
    else:
        print(j, end=" ")  # Imprimimos la palabra original si no está en el diccionario
print()  




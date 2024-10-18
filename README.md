# Ordonez_Martinez_Valeria_1203_practica_4_2do_parcial_3W
Practica 4

# Diccioarios ejercicio 1
print(" ")
print("Ordonez Martinez Valeria 1203 3W Practica 4")
print(" ")

#Abrir diccioanrio para imprimir la informacion
info={}
x = 1
#Abrir ciclo while
while x==1:
    #Solicitar al usuario que ingrese un dato de su informacion
    dato=str(input("Que informacion vas a agregar? (Nombre, Edad, Sexo, Teléfono, Correo electrónico): \n"))
    print(" ")
    #Convertit mensaje en minusculuas
    dato=dato.lower()
    #Ingresar el dato
    valor=str(input("Ingrese el dato: "))
    print(" ")
    info[dato]=valor
    #Imprimir la informacion
    print(info)
    print(" ")
    #Continuar o no el programa
    print("Si quieres seguir ejecutando el programa presione 1, de lo contrario presione 2: ")
    #Volver a poner el mensaje
    x=int(input())
    print (" ")
    ![image](https://github.com/user-attachments/assets/baf09303-1312-44c2-996a-e4254ad21c51)
    ![image](https://github.com/user-attachments/assets/9f8eb706-3a1a-4605-a4a8-56b4919a009e)


# Diccioario Ejercicio 2
print(" ")
print("Ordonez Martinez Valeria 1203 3W Practica 4")
print(" ")

diccionario = {}

#Solicitamos las palabras y las traducimos
palabras = input("Escribe las palabras en el formato: Hola: Hello, Dog: Perro, Casa: House \n")

#convertimos la entrada en formato título
palabras = palabras.title()

#Creamos el diccionario a partir de la entrada
for i in palabras.split(","):
    clave, valor = i.split(":")
    diccionario[clave.strip()] = valor.strip()  # Usamos strip para eliminar espacios

#colicitamos la frase a traducir
frase = input("Escribe una frase en español para traducir: \n")

#Traducimos la frase
for j in frase.split(" "):
    if j in diccionario:
        print(diccionario[j], end=" ")  # Imprimimos la traducción en la misma línea
    else:
        print(j, end=" ")  # Imprimimos la palabra original si no está en el diccionario
print()  
![image](https://github.com/user-attachments/assets/a21fa04d-d014-48c4-92b6-7842f8d84855)
![image](https://github.com/user-attachments/assets/fd9bf506-301c-48d2-b82a-4605318345a3)




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
    
    
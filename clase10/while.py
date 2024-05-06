#Adivinar el número generado aleatoriamente
#importamos la libreria random
import random
num_sec = random.randint(1,100)
#print (num_sec)

intentos = 0
while True:
    intento = int(input("Ingresa un número del 1 al 100: "))
    intentos +=1

    #decisión para saber si es mayor o menor
    if intento < num_sec:
        print(f"El número ingresado es menor al secreto con intentos {intentos}")
    elif intento > num_sec:
        print(f"El número ingresado es mayor al secreto con intentos {intentos}")
    else:
        print(f"Felicitaciones, el número ingresado es el correcto con intentos {intentos}, el número secreto era {num_sec}")
        break
print("Fin del juego.")
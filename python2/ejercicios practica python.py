#1. Calculadora Indice masa corporal
#Definición de variables
kg = float(input("Ingrese su peso en kilogramos: "))
mts = float(input("Ingrese su altura en metros: "))
#Formula de IMC
imc = kg / (mts ** 2)
#Mensaje de resultado
print("Su índice de masa corporal es:", imc)
#2. Inversor de cadenas
# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingresa una frase: ")

# Invertir la cadena
cadena_invertida = cadena[::-1]

# Mostrar la cadena invertida
print("La cadena invertida es:", cadena_invertida)
#3. Detector de números pares e impares
#Solicitar al usuario que ingrese un número entero
num = int(input("Ingrese un número entero. "))
if  num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")
#4. Contador de vocales
# Solicitar al usuario una cadena de texto
text = input("Ingrese una cadena de texto: ")
contador_vocales = sum(text.lower().count(vocal) for vocal in "aeiou")
print(f"Cantidad de vocales en la cadena: {contador_vocales}")

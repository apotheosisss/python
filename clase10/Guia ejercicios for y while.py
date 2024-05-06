#Ejercicio 1
"""Realiza construcción de un programa que deba realizar lo siguiente:
Comienza con la inicialización de variables y solicita al usuario la cantidad de bul-
tos. Luego, utiliza un bucle FOR para procesar cada bulto, solicitando el peso al
usuario y manejando posibles errores (agregar excepciones). Dependiendo del
peso ingresado, acumula valores y contadores correspondientes para bultos livia-
nos y normales. Finalmente, imprime el total a pagar por bultos livianos y norma-
les, así como la cantidad de bultos en cada categoría"""
bultos = int(input("Ingrese la cantidad de bultos."))
bultoslivianos = 0
bultosnormales = 0
for bultos in range(bultos):
    try:
        pesobulto = int(input("Ingrese el peso del bulto."))
        if pesobulto in range(6,10):
            bultosnormales += 1
            print(f"Es un bulto normal, usted tiene hasta ahora {bultosnormales} bultos normales.")
        elif pesobulto in range(1,5):
            bultoslivianos += 1
            print(f"Es un bulto liviano, usted tiene hasta ahora {bultoslivianos} bultos livianos.")
    except pesobulto > 10:    
        print("Valor ingresado no válido el peso debe de estar en un rango del 1 al 10, reintente la operación.")
total= (1000 * bultoslivianos) + (2000 * bultosnormales)
print(f"Usted tiene que pagar el total de {total} pesos por los {bultoslivianos} bultos livianos y {bultosnormales} bultos normales.")

#ejemplo de una division utilizando try:
def dividir(numero1, numero2):

    try:
        resultado = numero1/numero2
        print(f"El resultado es de la división es {resultado:.0f}")
    except ZeroDivisionError:
        print("No se puede dividir por 0.")    
    except TypeError:
        print("Ingresa un número valido.")
    else:
        print("La división se ejecutó correctamente.")
    finally:
        print("Fin de la operación.")
numero1 = input("Ingresa el primer número: ")
numero2 = input("Ingresa el segundo número: ")    
dividir(numero1, numero2)

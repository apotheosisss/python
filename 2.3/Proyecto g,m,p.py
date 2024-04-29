"""
Escribir un programa que solicite al usuario ingresar 
el tipo de proyecto (pequeño, mediano o grande) y el 
lenguaje de programación utilizado. El programa debe
estimar el tiempo de desarrollo basado en esta información,
y validar si el usuario ingresa una opción desconocida.
"""
proyecto = input("Ingrese el tipo de proyecto: grande, mediano o pequeño").lower()
lenguaje = input("Tipo de lenguaje: ").lower()

if proyecto=="pequeño":
    if lenguaje=="python":
        print("El proyecto tardará 1 mes")
    else:
        print("El proyecto tardará 2 meses.")
elif proyecto=="mediano":
    if lenguaje == "python":
        print("El proyecto tardará 2 meses")
    else:
        print("El proyecto tardará 3 meses.")
elif proyecto == "grande":
    if lenguaje=="python":
        print("El proyecto tardará 3 meses.")
    else:
        print("El proyecto tardará 4 meses.")
else:
    print("Ingresa una opción valida.")        
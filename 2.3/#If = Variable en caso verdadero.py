#If = Variable en caso verdadero
#Elif = Variable en caso falso
#Else = Variable Invalida (Cierre)
"""
Escribir un programa que solicite al usuario ingresar el día de la semana.
Dependiendo dle día, el programa determinará si se debe organizar una reunión
de equipo o no. Por ejemplo, las reuniones podrían ser los lunes y jueves.

"""
#Entrada/Proceso/Salida
#Entrada
dia = input("Ingresa el día :").lower()
#Proceso
if dia == "lunes" or dia =="jueves":
    print("Hoy debes agendar una reunión.")
elif dia == "viernes":
    print("Hoy es viernes, dea")
else:
    print("Hoy no hay reunión, continua programando.")
    
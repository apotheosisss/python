#Venta de pasajes
try:
    pasajes = int(input("Ingresa la cantidad de pasajes que deseas vender: "))
except ValueError:
    print("Ingresa un valor válido.")

for _ in range(pasajes): 
    try:
        preciopasajes = int(input("Ingresa el precio de los pasajes."))
        totalingresos = pasajes * preciopasajes
    except ValueError:
        print("Ingresa un valor valido, reintenta la operación.") 
    else:
        print("Se ejecutó correctamente la operación.")
    finally:
        print(f"El total de ingresos es de: {totalingresos}")
    break
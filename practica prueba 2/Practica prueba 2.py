#Práctica Prueba 2
#ingreso de datos del paquete
while True:
    nom= input("Ingrese su nombre: ")
    if len(nom) > 30:
        print("El nombre debe tener máximo 30 caracteres, reintente la operación.")
    else:
        print(f"Bienvenido, {nom}.")
    try:
       
        peso = float(input("Por favor, ingrese el peso del paquete(KG): "))
        km = float(input("Ingrese la distancia de envío en kilómetros: "))
        if peso or km > 0:
            costo_base = 5000
            costo_kg = 500
            km_extra = km - 100
            if km > 100:
                costo_total = costo_base + (peso * costo_kg) + (100 * km_extra)
                desglose = print(f"Nombre del cliente: {nom} \nPeso del paquete: {peso}\nDistancia de envío: {km}\nCosto total de envío: {costo_total}")
                with open(f"envio_{nom}.txt", "w") as informe:
                    informe.write(f"Nombre del cliente: {nom} \nPeso del paquete: {peso}kg\nDistancia de envío: {km}km\nCosto total de envío: {costo_total}")
                    break
            elif km <= 100:
                costo_total = costo_base + (peso*costo_kg)
                desglose = print(f"Nombre del cliente: {nom} \nPeso del paquete: {peso}kg\nDistancia de envío: {km}km\nCosto total de envío: {costo_total}")
                with open(f"envio_{nom}.txt", "w") as informe:
                    informe.write(f"Nombre del cliente: {nom} \nPeso del paquete: {peso}kg\nDistancia de envío: {km}km\nCosto total de envío: {costo_total}")
                    break
        else:
            print("Ingrese valores numéricos positivos, reintente la operación.") 
    except ValueError:
        print("Ingrese un tipo de dato válido, reintente la operación.")
        #NOTA: EJECUTAR EL CÓDIGO EN UNA CARPETA DE VISUAL STUDIO, PARA LA GENERACIÓN DEL .txt
#1 Calculo de liquidación de sueldo
while True:
    #Ingreso de datos
    nom = input("Ingrese el nombre del trabajador: ")
    try:
        sueldo = int(input("Ingrese el sueldo base: "))
        nhoras= int(input("Ingrese el número de horas trabajadas en la semana: "))
    except ValueError:
        print("Un valor ingresado no es númerico, reintente la operación.")
    #Analisis de longitud del nombre
    if len(nom) > 30:
        print("El nombre debe tener máximo 30 caracteres, reintente la operación.")
    else:
        try:
            #Situación horas extra
            if nhoras > 45:
            #Cálculo de valores
                horasextra = nhoras - 45
                pagaextra = (horasextra * (sueldo/45)) * 1.5
                totalingreso = sueldo + pagaextra
                descfon= totalingreso * 0.07
                descafp= totalingreso * 0.10
                sueldoneto= totalingreso - descfon - descafp
            #Desglose de información
                print(f"NOMBRE DEL TRABAJADOR: {nom}\n SUELDO BASE: {sueldo}\n PAGO HORAS EXTRA: {pagaextra}\n TOTAL DE INGRESOS: {totalingreso}\n DESCUENTO SEGURIDAD SOCIAL: {descafp+descfon}\n SUELDO NETO A PAGAR: {sueldoneto}\n")
            #Creación de archivo .txt
                with open(f"liquidación_{nom}.txt", "w") as informe:
                    informe.write(f"NOMBRE DEL TRABAJADOR: {nom}\n SUELDO BASE: {sueldo}\n PAGO HORAS EXTRA: {pagaextra}\n TOTAL DE INGRESOS: {totalingreso}\n DESCUENTO SEGURIDAD SOCIAL: {descafp+descfon}\n SUELDO NETO A PAGAR: {sueldoneto}")
                    #Pregunta de repetición/finalización
                    rep = input("¿Desea realizar otro cálculo? (si/no)")
                    if rep == "si":
                        print("Reiniciando la operación...")
                    elif rep == "no":
                        break
        #Situación sin horas extra
            else:
            #Cálculo de valores sin horas extra
                totalingreso = sueldo
                descfon = totalingreso * 0.07
                descafp = totalingreso * 0.10
                sueldoneto = totalingreso - descfon - descafp
            #Desglose de información
                info = print(f"NOMBRE DEL TRABAJADOR: {nom}\n SUELDO BASE: {sueldo}\n PAGO HORAS EXTRA: 0\n TOTAL DE INGRESOS: {totalingreso}\n DESCUENTO SEGURIDAD SOCIAL: {descafp+descfon}\n SUELDO NETO A PAGAR: {sueldoneto}\n")    
                #Creación de archivo .txt sin horas extra
                with open(f"liquidación_{nom}.txt", "w") as informe:
                    informe.write(f"NOMBRE DEL TRABAJADOR: {nom}\n SUELDO BASE: {sueldo}\n PAGO HORAS EXTRA: 0\n TOTAL DE INGRESOS: {totalingreso}\n DESCUENTO SEGURIDAD SOCIAL: {descafp+descfon}\n SUELDO NETO A PAGAR: {sueldoneto}")
                    #Pregunta de repetición/finalización
                    rep = input("¿Desea realizar otro cálculo? (si/no)")
                    if rep == "si":
                        print("Reiniciando la operación...")
                    elif rep == "no":
                        break
        finally:
            print("El código ha finalizado correctamente.")
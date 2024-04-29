#declarar variables
dolar_aust= 0.0016
yen= 6.04
pesarg= 1.07

total= 0
total= int(input("Ingrese el total a convertir: "))


#Sentencia de condición
print("-----CONVERTIDOR DE MONEDAS----- \n Elija la opción que desee. \n 1.- Dollar. \n 2.- Yen. \n 3.- Peso Argentino.")
opcion= int(input("Ingrese una opción--> "))

if opcion==1:
    resultado=total*dolar_aust;
    print(f"${total} es igual a {resultado} dolares australianos.")     
elif opcion==2:
    resultado=total*yen;
    print(f"${total} es igual a {resultado} Yenes.")     

elif opcion==3:
    resultado=total*pesarg;
    print(f"${total} es igual a {resultado} pesos argentinos.")                
           
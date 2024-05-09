with open("ventas.txt", "r") as archivo:
    # Leemos el contenido del archivo y lo dividimos por líneas
    lineas = archivo.read().splitlines()

print(lineas)


with open("informe_ventas.txt", "w") as informe:
    # Escribimos el encabezado del informe
    informe.write("Informe de Ventas - Cafetería de Grano\n Ventas del dia 1\n Pan Ciabatta: 100000 \n Pie de limón: 140000 \n Café: 132000 \n Té: 72000 \n Aljafor: 55000 \n Total de ventas del día Lunes: 499000  \n Ventas del dia 2\n Pan Ciabatta: 80000 \n Pie de limón: 87500 \n Café: 77000 \n Té: 44800 \n Aljafor: 32000 \n Total de ventas del día Martes: 321300\n Ventas del día 3\n Pan Ciabatta: 40000 \n Pie de limón: 52500 \n Café: 55000 \n Té: 28800 \n Aljafor: 22000\n Total de ventas del día Miercoles: 198300 \n Ventas del día 4\n Pan Ciabatta: 20000 \n Pie de limón: 28000 \n Café: 26400 \n Té: 14400 \n Aljafor: 11000 \n Total de ventas del dia Jueves: 88800 ")
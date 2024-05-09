#Ventas Cafetería
#Definición de precios y variables
ciabatta = 2000
pielimon = 3500
cafe = 2200
te = 1600
alfajor = 1000
#Ventas y promedio de ventas de cada producto 
ventas1 = ciabatta * (50+30+20+10)
prom1 = ventas1/4
ventas2 = pielimon * (40+25+15+8)
prom2= ventas2/4
ventas3= cafe * (60+35+25+12)
prom3= ventas3/4
ventas4= te * (45+28+18+9)
prom4= ventas4/4
ventas5= alfajor * (55+32+22+11)
prom5= ventas5/4
# Resultados
print(f"Ventas de Pan ciabatta: {ventas1} | Promedio de ventas por día: {prom1} \n Ventas de pie de limón: {ventas2} | Promedio de ventas por día: {prom2} \n Ventas de Café: {ventas3} | Promedio de ventas por día: {prom3} \n Ventas de Té: {ventas4} | Promedio de ventas por día: {prom4} \n Ventas de alfajores: {ventas5} | Promedio de ventas por día: {prom5} \n VENTAS TOTALES: {(ventas1+ventas2+ventas3+ventas4+ventas5)} | PROMEDIO DE VENTAS TOTAL POR DÍA: {(prom1+prom2+prom3+prom4+prom5)}")


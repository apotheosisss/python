#1 Información personal
informacion = ("Nombre: Claudio","Edad: 18", "Ciudad de Residencia: Puerto Montt" )
print(informacion)
#Desempaquetado de la tupla
a,b,c = informacion
print(a)
print(b)
print(c)
#2 Operaciones con tuplas numericas
numeros = (1,2,3,4,5,6,7,8,9,10)
#Print de la suma de números
print(sum(numeros))
#Print del número máximo
print(max(numeros))
#Print del número mínimo
print(min(numeros))
#Conteo de la cantidad de números 5 en la tupla
print(numeros.count(5))
#3 Rebanado de tuplas
letras= ("a","b","c","d","e","f","g","h","i","j")
#Primeras 5 letras
print(slice(letras[0:5]))
#Ultimas 3 letras
print(slice(letras[7:10]))
#Saltos de 2 letras
print(slice(letras[0:10:2]))

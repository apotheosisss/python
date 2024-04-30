#Consulta de edad
edad= 18
edad = int(input("Ingrese su edad."))
if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted no es mayor de edad.")
#Validación de usuario y contraseña
user1= "pedro"
user2= "angel"
pwd1= "1234"
pwd2= "a4s1"
user = input("Ingrese el nombre de usuario. ")
pwd = input("Ingrese su contraseña. ")
if user == user1 and pwd == pwd1:
    print("Bienvenido, Pedro. ")
elif user == user2 and pwd== pwd2:
    print ("Bienvenido, Angel. ")
else:
    print("Ingrese un usuario y contraseña válidos.") 
#Promedio 3 notas
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3)/3
if promedio >= 4.0:
    print("Usted ha aprobado con un promedio de: ",promedio)
else:
    print("Usted ha reprobado con un promedio de: ",promedio)
#Animales que viven en el agua
opcion1= "1"
opcion2= "2"
opcion3= "3"
opcion4 = "4"
puntos= 0 
opcion = input("¿Cuales de los siguientes animales viven en el agua? \n 1. Perro \n 2. Cocodrilo \n 3. Conejo \n 4. Tiburón \n")
if opcion == opcion2:
    puntaje = puntos + 0.5
    print(f"Usted ha obtenido {puntaje} puntos.")
elif opcion == opcion4:
    puntaje = puntos + 1
    print(f"Usted ha obtenido {puntaje} punto.")
else:
    print(f"Usted ha obtenido {puntos} puntos.")
#Formulario de lugares del mundo
opciona1= "1"
opciona2= "2"
opciona3= "3"
opciona4= "4"
opcionb1= "1"
opcionb2= "2"
opcionb3= "3"
opcionb4= "4"
opcionc1= "1"
opcionc2= "2"
opcionc3= "3"
opcionc4= "4"
pts= 0
opciona = input("¿Cual de los siguientes paises es conocido por tener píramides? \n 1. Grecia \n 2. España \n 3. Egipto \n 4. Reino Unido \n")
if opciona == opciona3:
    print("Respuesta correcta, +5 puntos.")
    puntaje1 = pts + 5
else:
    print("Respuesta incorrecta, la Opción correcta era: Egipto")
opcionb = input("¿Cual de los siguientes paises es conocido por tener un coliseo? \n 1. Roma \n 2. Italia \n 3. Grecia \n 4. Perú \n")
if opcionb == opcionb2:
    print("Respuesta correcta, +5 puntos.")
    puntaje2 = puntaje1 + 5
elif opcionb == opcionb1:
    print("Casi!, Roma es parte de Italia, el país del Coliseo Romano.")
else:
    print("Respuesta incorrecta, la opción correcta era: Italia.")
opcionc = input("¿Que pais es conocido por la gran Torre Eiffel? \n 1. Paris \n 2. Francia \n 3. Alemania \n 4. Noruega \n") 
if opcionc == opcionc2:
    print("Respuesta correcta, +5 puntos.")
    puntaje3= puntaje2 + 5
elif opcionc == opcionc1:
    print("Casi! Paris es la capital de Francia, el país de la torre Eiffel.")
else:
    print("Respuesta Incorrecta, la opcion correcta era: Francia")

print(f"Usted tiene {puntaje3}/15 puntos.")
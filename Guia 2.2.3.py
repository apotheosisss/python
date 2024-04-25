#1

#Definicion de variables

rut =  input("Ingrese rut apoderado: ")

nomAlum = input("Ingrese el nombre del alumno: ")

curso = input("Ingrese curso al cual el alumno debe matricularse: ")

matricula = int(25000)

mensualidad = int(30000)

#Ecuaciones

resultadoAnual = (mensualidad * 10)+matricula

#Datos de salida

print(f"-Detalle Anualidad Colegio-")

print(f"NOMBRE ALUMNO: {nomAlum}") 
print(f"RUT APODERADO: {rut}")

print(f"CURSO MATRICULADO: {curso}")

print(f"VALOR MATRÍCULA: {matricula}") 
print(f"VALOR MENSUALIDAD: {mensualidad}")

print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")
 #2 ValorNetodelProducto

producto = input ("Ingrese el nombre del producto: ")
valorProducto = int(input("Ingrese el valor del producto: "))
valorNeto = float(0.81)
valorSinIva = float(valorProducto * valorNeto)
print(f"Detalle producto")
print (f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIva}")
"""
Se utiliza el tipo de dato float para que el código permita la lectura de decimales, ya que si fuera int
el código solo leería números enteros.
Tambien, se utiliza el tipo de dato float para permitir al código calcular el iva, 
cuya formula involucra un número decimal que no se podría calcular si se usara el tipo de dato "Int".
"""
#3

numero = 0
print(numero)
siguiente = 1
print(siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
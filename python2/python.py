# Numeros complejos
numeroComplejo= 1j
print(type(numeroComplejo))
# Datos de tipo range (rango)
coordenadas = range(1, 10)
print(coordenadas)
print(type(coordenadas))

#Datos set() conjunto
numeros= {2,3,5,7,9}
numeros.add(13)
print(numeros)
letras= set("Python3")
letras.remove("3")
print(type(letras))
print(letras)

"""
Frozenset: Es una colección inmutable parecida a un set, es inmutable
ya que no se puede modificar.

"""
frutas = frozenset({"arándanos","manzana","naranja","melón","frambuesa"})
print(frutas)
print(type(frutas))

"""
Bytes:
Es un tipo de dato inmutable
parten desde el 0 - 255.
"""
# Crear un objeto a partir de un byte

variableBytes = bytes("hola que sucede","utf-8")
print(variableBytes)

# Crear un texto a partir de número bytes

b = bytes((72, 111, 188, 97))
print(b)

#byteArray
c = bytearray("Hola que tal", "utf-8")
print(c)
#modificar un byteArray
c[0] = 83
print(c)
#Datos de tipo none: Es un tipo de dato único que no representa un valor.
variableNone = None
print(variableNone)

#
hola= "Hola bebe"
print(hola[5:9])

print("hola  "DUOC"")
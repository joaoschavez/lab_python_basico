
#"""Operaciones comunes"""
#""" SUMA """
var1 = "7000"
var2 = 35000
var3 = 40.85


suma1 = int(var1) + var2
suma2 = int(var1) + var2 + var3

print(suma1)
print(suma2)

""" RESTA """

resta1 = 20 - 120
resta2 = 3000 - 500
resta3 = 200.98 - 5000 - 480

print("Tipo de dato para la variable 'resta1' es: {}".format(type(resta1)))
print("Tipo de dato para la variable 'resta2' es: {}".format(type(resta2)))
print("Tipo de dato para la variable 'resta3' es: {}".format(type(resta3)))


"""MULTIPLICACIÓN"""

multiplica1 = 9 * 1000
multiplica2 = 90 * 9.9
multiplica3 = 9.5 * 100.5

print("El valor de mi variable 'multiplica1' es: {}".format(multiplica1))
print("El valor de mi variable 'multiplica2' es: {}".format(multiplica2))
print("El valor de mi variable 'multiplica3' es: {}".format(multiplica3))

#\n salto de linea
multiplica4 = "\nMeses de invierno del 2024"

print(multiplica4 * 4)


"""DIVISIÓN"""

#división entre enteros
division1 = 3000/20

#división entre flotante y entero
division2 = 545.45/3

#división entre flotantes
division3 = 333.33/2.22

print("El valor de mi variable 'division1' es: {} y el tipo de dato es: {}".format(division1, type(division1)))
print("El valor de mi variable 'division2' es: {} y el tipo de dato es: {}".format(division2, type(division2)))
print("El valor de mi variable 'division3' es: {} y el tipo de dato es: {}".format(division3, type(division3)))

"""OPERADOR MODULO : RESIDUO %"""

VARMOD1 = 10 % 4
VARMOD2 = 100 % 6
VARMOD3 = 356 % 3

print("El valor para mi varmod1 es :{}".format(VARMOD1))
print("El valor para mi varmod2 es :{}".format(VARMOD2))
print("El valor para mi varmod3 es :{}".format(VARMOD3))


"""POTENCIACIÓN"""

varbase = 2
varpot = 10
resultadopot = varbase ** varpot

print(resultadopot)

varpot4 = pow(2, 10)

print(varpot4)


"""DIVISION CON RESULTADO ENTERO: //"""

diventero = 40 // 13

print(diventero)
print(type(diventero))






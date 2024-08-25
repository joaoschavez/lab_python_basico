"""
Requisitos:

1. Crear variables para los valores de nombre, profesión y ciudad
2. Crear 2 variables de remuneracion de enero y febrero.
3. Crear una variable donde se sumará el ingreso de los meses de enero y febrero.
4. Mostrar en pantalla el mensaje de
"Hola soy 'nombre' mi profesion es 'profesion' y mi remuneración acumulada es de 'remueración total'"

"""


nombre = "Joao Chavez"
profesion = "Contador"
ciudad = "Lima"
remenero = 3500
remfebrero = 3500
remtotal= remenero + remfebrero


print("Hola soy {} mi profesión es {} y mi remuneración acumulada es de {}".format(nombre, profesion, remtotal))
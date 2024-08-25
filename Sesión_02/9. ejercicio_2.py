"""
REQUISITOS:
1. Crear 2 variables enteras, 2 variables flotantes, 1 variable string, 1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica (realizar conversiones necesarias)
3. suma de las 2 variables enteras más la variable sting numérica y la variable flotante.
4. Obtener y mostrar el módulo de las 2 variables enteras: %
5. Obtener y mostrar el resultado entero de las  2 variables enteras : //
"""




varint_1 = 250
varint_2 = 15
varfloat_1= 15.24
varfloat_2= 99.98
varstr_1 = "Chavez"
varstr_2 = "100"
varbool_1 = True


print(varint_1 + int(varstr_2))
print(varint_1 + varint_2 + int(varstr_2) + varfloat_1)
print(varint_1 % varint_2)
print(varint_1 // varint_2)


# Comentarios
# Todo lo que tengamos detrás de este simbolo se ignora por el interprete

# En python no existe el comentario en bloque
# En python hay una chapuzilla que hacemos que es usar el operador triple comilla
"""
Lo que pongo aqui se ignora
Y lo que pongo aqui también
"""

# Es importante escribir comentarios en el código, cuando haya que escribirlos... no a lo loco
# Para que sirve un comentario
# Comentar vs Documentar
# Documentar : Explicar QUE HACE UN PROGRAMA
# Comentar   : Explicar COMO HACE UN PROGRAMA LO QUE HACE
# En general el código debe ser AUTOEXPLICATIVO

###########################################################################################
# Tipos de datos
###########################################################################################

# TIPOS SIMPLES

# Numeros enteros
17
23
-76
# Numeros decimales
-34.87
# Valores logicos
True
False
# Textos
"Hola"
'Amigo'
""" Como estas?
Yo estoy bien !!!!"""

# COLECCIONES DE DATOS

# Tupla: Secuencia ordenadas e inalterables de datos: ARRAY  <<< CONSTANTE
(1,2,3,4)
(1, True, "Hola")

# Listas: Secuencia ordenada y modificables de datos: ARRAY
[1,2,3,4]
[1, True, "Hola"]

# Diccionario (mapa): Coleccion no ordenada de datos y modificables, accesibles a través de un identificador
{ "Nombre": "Ivan", "Edad": 42 }
# Datos: Ivan y 42
# Identificadores: Nombre , Edad

# VARIABLES
VARIABLE_NUMERICA  = 17          # Esto no seria un nombre adecuado en python para una variable
texto              = "Hola"
mi_variable_logica = True

# En python las variables se escriben en snake-case: Minusculas y cada palabra va separada de la siguiente por un guion bajo.

# OPERADORES
# Operadores aritmeticos:
2+3-4/4*7
7//4         # Division entera -> 1
7%4          # Resto de la division entera -> 3
# Operadores relacionales
3>2 # > < >= <=  == !=
3==4 # > FALSE
# Operadores lógicos
True and False  # False
True or  False  # True
not False       # True 

# Funciones básicas integradas en python
print( "HOLA " )    # Imprimir un texto por consola
edad = input("Dame tu edad: ")       # Lee algo de la consola
print( edad )
# Práctico 3: Estructuras condicionales - Rotolo Martin

# Actividades:

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("ingrese su edad"))
if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = int(input("ingrese su nota"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("ingrese su numero par"))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("ingrese su edad:"))
if edad < 12:
    print("● Niño/a")
elif edad >= 12 and edad < 18:
    print("● Adolescente")
elif edad >= 18 and edad < 30:
    print("● Adulto/a joven")
else:
    print("● Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

password = str(input("Ingrese contraseña de entre 8 y 14 caracteres (incluyendo 8 y 14)"))
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)
print(mean(numeros_aleatorios),median(numeros_aleatorios),mode(numeros_aleatorios))
if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Hay sesgo positivo")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Hay sesgo negativo")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) and median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("Sin sesgo")
else:
    print("no se cumple ninguna condicion")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

cadena = str(input("ingrese una cadena de caracteres"))

if cadena[-1].lower() in 'aeiou':
    print(cadena + '!')
else:
    print(cadena)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = str(input("ingrese su nombre"))
num = int(input("ingrese un numero: 1. para mayusculas, 2 para minusculas, 3 para titulo"))

if num == 1:
    nombre = nombre.upper()
elif num == 2:
    nombre = nombre.lower()
elif num == 3:
    nombre = nombre.title()
else:
    print("numero incorrecto,  [1] [2] o [3]")
print(nombre)

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto:"))
print(magnitud)

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Magnitud fuera de rango")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Periodo del año    -    Estación en el hemisferio norte   -   Estación en el hemisferio sur
# Desde el 21 de diciembre hasta el 20 de marzo (incluidos) - Invierno - Verano
# Desde el 21 de marzo hasta el 20 de junio (incluidos) - Primavera - Otoño
# Desde el 21 de junio hasta el 20 de septiembre (incluidos) - Verano - Invierno
# Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) - Otoño - Primavera
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = str(input("en cuál hemisferio se encuentra (N/S)"))
mes = str(input("qué mes del año es"))
dia = int(input("qué día del mes es"))
print(hemisferio, mes, dia)

if hemisferio.upper() == 'N':
    if mes.lower() == 'diciembre':
        if dia >= 21:
            print("Usted esta en Invierno")
        else:
            print("Usted esta en Otoño")
    elif mes.lower() == 'marzo':
        if dia >= 21:
            print("Usted esta en Primavera")
        else:
            print("Usted esta en Invierno")
    elif mes.lower() == 'junio':
        if dia >= 21:
            print("Usted esta en Verano")
        else:
            print("Usted esta en Primavera")
    elif mes.lower() == 'septiembre':
        if dia >= 21:
            print("Usted esta en Otoño")
        else:
            print("Usted esta en Verano") 

    elif mes.lower() in 'enerofebrero':
        print("usted esta en Invierno")
    elif mes.lower() in 'abrilmayo':
        print("usted esta en Primavera")  
    elif mes.lower() in 'julioagosto':
        print("usted esta en Verano")  
    elif mes.lower() in 'octubrenoviembre':
        print("usted esta en Otoño")
    else:
        print("datos fuera de rango")      

elif hemisferio.upper() == 'S':
    if mes.lower() == 'diciembre':
        if dia >= 21:
            print("Usted esta en Verano")
        else:
            print("Usted esta en Primavera")
    elif mes.lower() == 'marzo':
        if dia >= 21:
            print("Usted esta en Otoño")
        else:
            print("Usted esta en Verano")
    elif mes.lower() == 'junio':
        if dia >= 21:
            print("Usted esta en Invierno")
        else:
            print("Usted esta en Otoño")
    elif mes.lower() == 'septiembre':
        if dia >= 21:
            print("Usted esta en Primavera")
        else:
            print("Usted esta en Invierno") 
            
    elif mes.lower() in 'enerofebrero':
        print("usted esta en Verano")
    elif mes.lower() in 'abrilmayo':
        print("usted esta en Otoño")  
    elif mes.lower() in 'julioagosto':
        print("usted esta en Invierno")  
    elif mes.lower() in 'octubrenoviembre':
        print("usted esta en Primavera") 
    else:
        print("datos fuera de rango")
# Práctico 2: Funciones en Python - Rotolo Martin

# Actividades:

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# Funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")
# Programa principal
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# Funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
# Programa principal
nombre = str(input("Ingrese su nombre: "))
saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario 
# y llamar a esta función con los valores ingresados.

# Funciones
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
# Programa principal
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
residencia = str(input("Ingrese su residencia: "))
informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
# y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio
# como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas 
# funciones para mostrar los resultados.

from math import pi
# Funciones
def calcular_area_circulo(radio):
    area =  pi * (radio**2)
    print(f"el area del circulo es {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    print(f"el perimetro del circulo es {perimetro}")
# Programa principal
radio = int(input("Ingrese el radio: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Funciones
def segundos_a_horas(segundos):
    horas = (segundos / 60) / 60
    print(f"{segundos} segundos son equivalentes a: {horas} hora(s)")
# Programa principal
segundos = int(input("Ingrese segundos: "))
segundos_a_horas(segundos)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Funciones
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(numero,"x",i,"=",numero*i)
# Programa principal
numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Funciones
def operaciones_basicas(a, b):
    print(f"{a} + {b} = {a+b}, {a} - {b} = {a-b}, {a} * {b} = {a*b}, {a} / {b} = {a/b}")

# Programa principal
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
operaciones_basicas(a, b)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para 
# mostrar el resultado con dos decimales.

# Funciones
def calcular_imc(peso, altura):
    imc = peso / (altura)**2
    imc_corto = round(imc,2)
    print(f"Tu indice de masa corporal es de: {imc_corto}")
# Programa principal
peso = float(input("Ingrese peso(kg): "))
altura = float(input("Ingrese altura(m): "))
calcular_imc(peso, altura)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# Funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius} grados celsius equivalen a {fahrenheit} grados fahrenheit")
# Programa principal
celsius = float(input("Ingrese grados celsius: "))
celsius_a_fahrenheit(celsius)

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# Funciones
def calcular_promedio(a, b, c):
    promedio = (a+b+c)/3
    return promedio
# Programa principal
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
c = int(input("Ingrese otro numero: "))

print(f"El promedio de los numeros ingresados es:",calcular_promedio(a, b, c))
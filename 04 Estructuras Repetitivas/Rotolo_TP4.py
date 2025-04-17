# Práctico 4: Estructuras repetitivas - Rotolo Martin

# Actividades

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101,1):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

num = int(input("Ingrese un numero entero:"))
print(num)

if num == 0:
    dig = 1
else:
    dig = 0
while num > 0:
    num //=10
    dig += 1
print(f"Su numero tiene {dig} digito(s)")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero entero:"))
print(num1)
num2 = int(input("Ingrese un numero entero:"))
print(num2)
suma = 0

for i in range (num1+1,num2):
    print(i)
    suma += i

print(suma)


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.

num = int(input("Ingrese un numero entero:"))
print(num)
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingrese otro numero entero:"))
    print(num)
print(suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_random = random.randint(0,9)

cont = 1
num = int(input("Ingrese un numero entero:"))
print(num)

while num != num_random:
    num = int(input("Ingrese otro numero entero:"))
    print(num)
    cont += 1

print(f"Adivinaste en {cont} intentos!")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

for i in range(98,0,-2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero entero:"))
print(num)
suma = 0

for i in range(0,num):
    print(i)
    suma += i

print(suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pos = 0
neg = 0
par = 0
impar = 0
# Modificar range(0,10) para probar el programa con una cantidad menor.
for i in range(0,100):
    num = int(input("Ingrese un numero entero:"))
    print(num)
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

print(f"En la lista de numeros hay {par} pares, {impar} impares, {neg} negativos y {pos} positivos")  

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

suma = 0
cont = 0
# Modificar a range(0,10) para probar el programa con una cantidad menor.
for i in range(0,100):
    num = int(input("Ingrese un numero entero:"))
    print(num)
    suma += num
    cont += 1

print(f"La media de los numeros ingresados es",suma/cont)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un numero: "))

invertido = 0
negativo = num < 0

while num != 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num //= 10

if negativo:
    invertido *= -1

print(f"Numero invertido: {invertido}")
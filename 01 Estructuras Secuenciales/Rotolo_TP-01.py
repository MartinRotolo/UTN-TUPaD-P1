#TP 1 Secuenciales - Rotolo Martin

#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
saludo = f"Buenas {nombre}!!"
print(saludo)

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
saludo = f"Buenas!! me llamo {nombre} {apellido} tengo {edad} años y vivo en {residencia}"
print(saludo)

#Ejercicio 4
import math
radio = int(input("Ingrese el radio del circulo: "))
perimetro = 2*radio*math.pi
area = math.pi*radio**2
print(f"El perimetro del circulo es: {perimetro} y el area: {area}")

#Ejercicio 5
segundos = int(input("Ingrese segundos: "))
horas = (segundos / 60) / 60
print(f"Los {segundos} segundos equivalen a {horas} horas")

#Ejercicio 6
numero = int(input("Ingrese un numero: "))
for i in range(1,11):
      print(f"{numero} x {i} = {numero*i}")

#Ejercicio 7
numero1 = float(input("Ingrese un numero distinto del cero: "))
numero2 = float(input("Ingrese otro numero distinto del cero: "))
while numero1 == 0 or numero2 == 0 :
   print("Los dos numeros deben de ser distintos del 0!")
numero1 = float(input("Ingrese un numero distinto del cero: "))
numero2 = float(input("Ingrese otro numero distinto del cero: "))
if numero1 != 0 and numero2 !=0 :
       print(f"{numero1} + {numero2} = {numero1+numero2}")
       print(f"{numero1} / {numero2} = {numero1/numero2}")
       print(f"{numero1} * {numero2} = {numero1*numero2}")
       print(f"{numero1} - {numero2} = {numero1-numero2}")

#Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kgs: "))
imc = peso/altura**2
print(f"IMC = {imc}")

#Ejercicio 9
celcius = float(input("Ingrese una temperatura en grados Celsius: "))
farenheit = (9/5)*celcius + 32
print(f"Los {celcius} grados celcius equivalen a {farenheit} grados farenheit")

#Ejercicio 10
numero1 = float(input("Ingrese un numero : "))
numero2 = float(input("Ingrese otro numero : "))
numero3 = float(input("Ingrese otro numero : "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los 3 numeros ingresados es: {promedio}")
a= 10
b = 3.0
c = a*b
d = a+b
print(f"c = {c}, d = {d}")

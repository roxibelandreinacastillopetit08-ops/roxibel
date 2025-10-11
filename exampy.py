      #python


#ejercicio1 
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
suma = numero1 + numero2
print(f"La suma es: {suma}")

#ejercicio2
frase = input("Introduce una frase o palabra: ")
longitud = len(frase)
mayusculas = frase.upper()
minusculas = frase.lower()

print(f"\nLongitud: {longitud} caracteres")
print(f"Mayúsculas: {mayusculas}")
print(f"Minúsculas: {minusculas}") 

#ejercicio3
base = 5
altura = 5

area = base * altura

print(f"El área del rectángulo es: {area}")

#ejercicio4
paises_favoritos = ["México", "España", "Japón", "Canadá"]

print(paises_favoritos)

primer_pais = paises_favoritos[0]
ultimo_pais = paises_favoritos[-1]

paises_favoritos.append("Brasil")

print(primer_pais)
print(ultimo_pais)
print(paises_favoritos)

#ejercicio5
edad = int(input("¿Cuál es tu edad? "))

if edad >= 18:
 print("¡Bienvenido!")
else:
  print("Lo siento, no puedes entrar.")

#ejercicio6
numero = int(input("Introduce un número entero: "))

print(f"\nTabla de multiplicar del {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#ejercicio7
def contar_vocales(texto):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

texto_ingresado = input("Introduce un texto para contar sus vocales: ")
total_vocales = contar_vocales(texto_ingresado)
print(f"El número total de vocales es: {total_vocales}")

#ejercicio8
agenda = {}

def agregar_contacto(n, t):
    agenda[n] = t

def buscar_contacto(n):
    if n in agenda:
       return agenda[n]
    return "No encontrado"

def eliminar_contacto(n):
    if n in agenda:
        del agenda[n]
        return "Eliminado"
    return "No encontrado"

agregar_contacto("Ana", "04246645513")
agregar_contacto("Luis", "04126703784")
print(buscar_contacto("Ana"))
print(eliminar_contacto("Luis"))
print(buscar_contacto("Luis"))

#ejercicio9

numero = 0
while numero <= 100:
    if numero % 2 == 0:
        print(numero)
    numero += 1

#ejercicio10

def sumar_elementos(lista_numeros):
    total = 0
    for numero in lista_numeros:
        total += numero
    return total

precios = [10.5, 5, 20.25, 15]
suma_total = sumar_elementos(precios)
print(f"La suma total de los elementos es: {suma_total}")

#ejercicio11
def es_palindromo(texto):
    texto_limpio = "".join(filter(str.isalnum, texto)).lower()
    return texto_limpio == texto_limpio[::-1]

palabra = input("Introduce una palabra o frase: ")

if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' NO es un palíndromo.")


#ejercicio12
class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")


mi_coche = Coche("Toyota", "Corolla", 2022)
otro_coche = Coche("Ford", "Mustang", 1969)

mi_coche.mostrar_info()
otro_coche.mostrar_info()

#ejercicio13
class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("Error: El monto a depositar debe ser positivo.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: El monto a retirar debe ser positivo.")
        elif cantidad > self.saldo:
            print(f"Error: Saldo insuficiente. Saldo actual: ${self.saldo}")
        else:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self.saldo}")

    def consultar_saldo(self):
        print(f"Su saldo actual es: ${self.saldo}")


mi_cuenta = CuentaBancaria(saldo_inicial=100.00)

mi_cuenta.consultar_saldo()
mi_cuenta.depositar(50.00)
mi_cuenta.retirar(25.00)
mi_cuenta.retirar(200.00)
mi_cuenta.consultar_saldo()

#ejercicio14
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos_en_rango(inicio, fin):
    primos = []
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

lista_primos = encontrar_primos_en_rango(1, 20)
print(lista_primos)
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos_en_rango(inicio, fin):
    primos = []
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

lista_primos = encontrar_primos_en_rango(1, 20)
print(lista_primos)

#ejercicio15
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

set1 = set(lista1)
set2 = set(lista2)

union = set1 | set2
interseccion = set1 & set2
diferencia = set1 - set2

print(union)
print(interseccion)
print(diferencia)







#python

#ejercio1 
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

 Valores de ejemplo (puedes cambiarlos)
base = 10
altura = 5

area = base * altura

print(f"El área del rectángulo es: {area}")


#ejercicio4

frutas = ["Manzana", "Banana", "Fresa"]
print(frutas[0])
print(frutas[-1])
frutas.append("Uva")
print(frutas)

#ejercicio5
edad = int(input("¿Cuál es tu edad? "))

if edad >= 18:
 print("¡Bienvenido al club!")
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
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in texto:
        if caracter in vocales:
          contador += 2
    return contador

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


ejercicio9
numero = 0
while numero <= 100:
    if numero % 2 == 0:
        print(numero)
    numero += 1
    
ejercicio10
def sumar_lista(lista_numeros):
   total = 0
    for numero in lista_numeros:
        total += numero
    return total

numeros = [5, 15, 25, 35]
resultado = sumar_lista(numeros)
print(resultado)


#ejercicio11
def es_palindromo(texto):
    texto_limpio = "".join(filter(str.isalnum, texto)).lower()
    return texto_limpio == texto_limpio[::-1]

palabra1 = "Ana "
palabra2 = "Hola Mundo"
print(es_palindromo(palabra1))
print(es_palindromo(palabra2))

#ejercicio12

class Coche:
   def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

   def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.ano}")

mi_coche = Coche("Toyota", "Corolla", 2020)
tu_coche = Coche("Ford", "Focus", 2018)

mi_coche.mostrar_info()
tu_coche.mostrar_info()



#ejercicio13

class CuentaBancaria:
    def __init__(self, saldo_inicial):
       self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
       print(f"Depósito de ${cantidad} realizado. Saldo actual: ${self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado. Saldo actual: ${self.saldo}")

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo}")

mi_cuenta = CuentaBancaria(1000)
mi_cuenta.consultar_saldo()
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
mi_cuenta.retirar(1500)
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


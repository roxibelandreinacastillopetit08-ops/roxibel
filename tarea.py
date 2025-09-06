print("CALCULADORA SIMPLE\n")

operaciones = input(" elige la operacion que deseas ingrear( SUMA, RESTA, DIVISION, MULTIPLICACION) ")

if operaciones == "SUMA":
    numero_1 = float(input("ingrsa el primer numero:"))
    numero_2 = float(input("ingrese el segundo numero"))

    resultado = numero_1 + numero_2

    print(f"El resultado de la SUMA es: {resultado}")

elif operaciones == "RESTA":
    numero_3 = float(input("ingresa el primer numero:"))
    numero_4 = float(input("ingresa el segundo numero:"))

    resultado = numero_3 - numero_4

    print(f" el resultadode la RESTA es: {resultado}")


elif operaciones == "DIVICION":
    numero_5 = float(input("ingresa el primer numero"))
    numero_6 = float(input("ingresa el segundo mumero"))

    resultado = numero_5 / numero_6

    print(f"el resultado de la DIVICION es: {resultado}")



elif operaciones == "MULTIPLICACION": 
    numero_7 = float(input("ingresa primer numero"))
    numero_8 = float(input("ingresa segundo mumero"))
    
    resultado = numero_7 * numero_8

    print(f"el resultado de la MULTIPLICACION es: {resultado}")



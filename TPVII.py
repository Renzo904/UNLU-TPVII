def problema1():
    for i in range(1, 101):
        print(i)

def problema2():
    for i in range(1, 101):
        if(i % 2 == 0):
            print(i)

def problema3():
    resultado = 0
    for i in range(75, 151):
        resultado = resultado + i
    print(f"Resultado: {resultado}")

def problema4():
    resultado = 1
    factorial = int(input("Ingrese un numero: "))
    for i in range(1, factorial+1):
        resultado = resultado * i
    print(f"El factorial de ese numero es {factorial}! = {resultado}")
    
def problema5():
    for i in range(10):
        numero = int(input("Ingrese un numero positivo, negativo o cero:"))
        if numero > 0:
            print("El numero es positivo")
        elif numero < 0:
            print("El numero es negativo")
        elif numero == 0:
            print("El numero es cero")
        
def problema6():
    maximo = 0
    posicion = 0
    for i in range(1, 11):
        numero = int(input("Ingrese un numero: "))
        if posicion == 0:
            maximo = numero
            posicion = i
        
        if numero > maximo:
            maximo = numero
            posicion = i
        if numero == maximo:
            posicion = i
    print(f"El mayor numero ingresado es {maximo}, y lo ingresaste en la posicion {posicion}")

def problema7():
    maximo = 0
    minimo = 0
    posicionmaximo = 0
    posicionminimo = 0
    for i in range(1, 11):
        numero = int(input("Ingrese un numero: "))
        if posicionmaximo == 0:
            maximo = numero
            minimo = numero
            posicionmaximo = i
            posicionminimo = i
        
        if numero > maximo:
            maximo = numero
            posicionmaximo = i
        if numero == maximo:
            posicionmaximo = i

        if numero < minimo:
            minimo = numero
            posicionminimo = i
        if numero == minimo:
            posicionminimo = i
    print(f"El mayor numero ingresado es {maximo}, y lo ingresaste en la posicion {posicionmaximo}")
    print(f"El minimo numero ingresado es {minimo}, y lo ingresaste en la posicion {posicionminimo}")

def problema8():
    sumatotal = 0
    maximo = -1
    diamaximo = 0
    for i in range(1, 8):        
        precipitacion = int(input("Ingrese la precipitacion del dia de hoy:"))
        sumatotal = sumatotal + precipitacion
        if precipitacion > maximo:
            maximo = precipitacion
            diamaximo = i
        if precipitacion == maximo:
            diamaximo = i
    promedio = sumatotal / 7
    diasemana = ""
    if diamaximo == 1:
        diasemana = "Domingo"
    elif diamaximo == 2:
        diasemana = "Lunes"
    elif diamaximo == 3:
        diasemana = "Martes"
    elif diamaximo == 4:
        diasemana = "Miercoles"
    elif diamaximo == 5:
        diasemana = "Jueves"
    elif diamaximo == 6:
        diasemana = "Viernes"
    elif diamaximo == 7:
        diasemana = "Sabado"
    
    print(f"El promedio de precipitaciones fue de {promedio} mls. diarios.")
    print(f"El dia de mas precipitaciones fue el {diasemana}.")

problema1()
problema2()
problema3()
problema4()
problema5()
problema6() 
problema7()
problema8()

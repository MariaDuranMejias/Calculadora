#En este file se encuentran las operaciones aritmeticas que se usaran el python de Calculadora

#generamos una funcion que sea capaz de sumar n numeros, ingresados por el usuario
def sumatoria():
    listavacia = [] #generamos una lista vacia para luego llenarla con los digitos que ingrese el usuario 
    continuar = True #hacemos una condicion que le permita al usuario ingresar los numeros que desee sumar sin que el programa sepa cuantos van a ser
    while continuar:
        num = int(input("Ingrese un numero mayor a 0. Ingrese 0 para salir \n")) #le solicitamos al usuario que digite los numeros que desea sumar y que utilice el 0 para salir 
        listavacia.append(num) #guardamos en una lista los digitos ingresados por el usuario y que queremos sumar
        if num == 0:  #generamos la condicion de fallo o stop, que en este caso seria cuando el usuario ingresa 0
            break

    listavacia.remove(0) #quitamos el cero de la lista
    suma = 0  #generamos una variable que sea cero al inicio y que se vaya sumando con cada valor de la lista
    for x in listavacia: #generamos un ciclo for para ir recorriendo cada digito de la lista
        suma = suma + x  #se suma cada valor encontrado en cada iteracion, y asi se van sumando los valores de la lista y de esta forma sumamos los valores que el usuario ingreso al inicio
    return  suma #retornamos el resultado obtenido

#se crea una funcion que sea capaz de multiplicar n numeros ingresados por el usuario
def multiplicacion():
    listavacia = [] #generamos una lista vacia para luego llenarla con los digitos que ingrese el usuario 
    continuar = True #hacemos una condicion que le permita al usuario ingresar los numeros que desee multiplicar sin que el programa sepa cuantos van a ser
    while continuar:
        num = int(input("Ingrese un numero mayor a 0. Ingrese 0 para salir \n")) #le solicitamos al usuario que digite los numeros que desea multiplicar y que utilice el 0 para salir 
        listavacia.append(num) #guardamos en una lista los digitos ingresados por el usuario y que queremos sumar
        if num == 0: #generamos la condicion de fallo o stop, que en este caso seria cuando el usuario ingresa 0
            break

    listavacia.remove(0) #quitamos el cero de la lista
    multiplicador = 1 # se genera una variable que al inicio sea 1 para que se multiplique con el digito de la lista en cada iteracion
    for x in listavacia:
        multiplicador = multiplicador * x #se multiplican los valores de las iteraciones, de esta forma se multiplican todos los numeros ingresados por el usuario
    
    return multiplicador #retorna el resultado

#Se crea una funcion que sea capaz de generar el factorial de un numero ingresado por el usuario
def factorial():
    N = input('Ingrese numero \n')  #Se le solicita al usuario que ingrese un numero
    num = int(N) #Se convierte este input un int
    if num <= 0: #Se pone un condicional por si el numero es menor o igual a cero, si lo es, poner un mensaje de error 
        print("Mensaje de error")
    i=0
    y=1 #Se crea una variable que recorra todos los numeros hasta llegar al que el usuario ingreso
    for i in range(1,num+1):
        y = y*i  #Se guarda en una variable el resultado de cada iteracion, que se vayan multiplicando por el nuevo resultado
    return y #Se mprime la variable con el resultado del factorial

def resta():
    n1 = int(input("Ingrese el primer numero: " ))
    n2 = int(input("Ingrese el segundo numero: " ))
    resultado = 0
    if n1 != n2:
        resultado = n1-n2
    return resultado

def division():
    n1 = int(input("Ingrese el primer numero:  "))
    n2 = int(input("Ingrese el segundo numero:  "))
    resultado = n1 / n2

    return resultado 

def potencia():
    n1 = int(input("Ingrese el primer numero:  "))
    n2 = int(input("Ingrese el segundo numero:  "))

    resultado = n1 ** n2
    return resultado
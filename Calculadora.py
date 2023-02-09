import Operaciones as op


print("Estas son las operaciones disponibles: \n1 = Suma: entre n números \n2 = Resta: entre 2 números \n3 = Multiplicación: entre n números \n4 = División: entre 2 número \n5 = Factorial: de 1 número \n6 = Potencia: 1 número elevado al otro")
a = int(input("Digite el digito de la operacion que desea realizar: \n"))

resultado = str("")
file = open("resultados.txt", "a")
#file.write("Se realizo la siguiente operacion: " +  strb + "/n")
#file.write("El resultado es" + resultado + "/n")

if a==1:
    b = str("Suma")
    resultado = str(op.sumatoria())
    file.write("Se realizo la siguiente operacion: " +  str(b) + "\n")
    file.write("El resultado es: " + resultado + "\n")
    print("Resultado: " + resultado)
elif a==2:
    b = str("Resta")
    resultado = str(op.resta())
    file.write("Se realizo la siguiente operacion: " +  str(b) + "\n")
    file.write("El resultado es: " + resultado + "\n")
    print("Resultado: " + resultado)

elif a==3:
    b = str("Multiplicacion")
    resultado = str(op.multiplicacion())
    file.write("Se realizo la siguiente operacion: " +  str(b) + "\n")
    file.write("El resultado es: " + resultado + "\n")
    print("Resultado: " + resultado)

elif a==4:
    b = str("Division")
    resultado = str(op.division())
    file.write("Se realizo la siguiente operacion: " +  str(b) + "\n")
    file.write("El resultado es: " + resultado + "\n")
    print("Resultado: " + resultado)

elif a==5:
    b = str("Factorial")
    resultado = str(op.factorial())
    file.write("Se realizo la siguiente operacion: " +  str(b) + "\n")
    file.write("El resultado es: " + resultado + "\n")
    print("Resultado: " + resultado)

elif a==6:
    b = str("Potencia")
    resultado = str(op.potencia())
    file.write("Se realizo la siguiente operacion: " +  str(b) + "\n")
    file.write("El resultado es: " + resultado + "\n")
    print("Resultado: " + resultado)
else:
    print("Error: Operacion invalida")
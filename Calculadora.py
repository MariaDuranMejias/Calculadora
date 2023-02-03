import Operaciones as op


print("Estas son las operaciones disponibles: \n1 = Suma: entre n números \n2 = Resta: entre 2 números \n3 = Multiplicación: entre n números \n4 = División: entre 2 número \n5 = Factorial: de 1 número \n6 = Potencia: 1 número elevado al otro")
a = int(input("Digite el digito de la operacion que desea realizar: \n"))

if a==1:
    print("Resultado: " + str(op.sumatoria()))

elif a==2:
    print("Resultado: " + str(op.resta()))

elif a==3:
    print("Resultado: " + str(op.multiplicacion()))

elif a==4:
    print("Resultado: " + str(op.division()))

elif a==5:
    print("Resultado: " + str(op.factorial()))

elif a==6:
    print("Resultado: " + str(op.potencia()))
else:
    print("Error: Operacion invalida")
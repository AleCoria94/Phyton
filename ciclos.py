#SUMAR 10 veces un numero#
#def multiplicar(n):
#    m=0
#    for i in range(10):
#        m=m+n
#    return m
#print (multiplicar (10))

#Implementar una sumatoria que reciba un numero enteroo n y devuelva la suma de todos los numeros del 0 al n
#def sumatoria(n):
   # m=0
   # for i in range(n+1):
   #     m=m+i
   # return m
#print (sumatoria(4))

def obtener_FizzBuzz(n):
    if(n % 5 == 0 and n % 3 == 0):
        return "Fizzbuzz"
    elif(n % 5 != 0 and n % 3 != 0):
        return n
    elif (n%3 == 0):
       return "fizz"
    else:
        return "buzz"


def sumatoria(n):
    m=0
    for i in range(n+1):
       m=m+i
       print("Posicion:" + str(i)+ " " +str (obtener_FizzBuzz(n))
    return m
print (sumatoria(4))
#def obtener_FizzBuzz(n):
    #if (n % 4 == 0 and n % 7 == 0):
        #return 'FuzzBizz'
    #if (n % 7 == 0):
        #return 'Fuzz'
    #if (n % 4 == 0):
        #return 'Bizz'
    #return n

#print (obtener_FizzBuzz(28))
#def fizzbuzz(n):
 #   lista =  []
 #   for i in range(n+1):
 #      lista.append(str(obtener_FizzBuzz(i)))
 #  return lista

#def g( n ) :
    #resultado = n
    #if n % 4 == 0 and n % 7 == 0:
        #resultado = 'FuzzBizz'
    #if n % 7 == 0:
        #resultado = 'Fuzz'
    #if n % 4 == 0:
        #resultado = 'Bizz'  
    #return resultado

#print (g(28))

#def h(lista, valor):
    #resultado = []
    #for elem in lista:

        #if elem != valor:
            #resultado.append(elem)

        #return resultado

#print (h([1,2,3,4,5,6,5,3],3))

def f( n ):
     M = 0
     for i in range(5):
         M = M + n
     return M

print (f(8))
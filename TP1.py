#Realizar un programa en Python que dados los valores correspondientes a la altura (h)) y el radio (r) 
# de un cilindro calcule el área de la base y el volumen del mismo y las informe al usuario. 

#Deberá utilizar dos funciones: una para el cálculo del área y otra que la utilice para el cálculo 
# del volumen teniendo en cuenta la siguiente fórmula:

#volumen = area de la base * h
#area de la base = 2πr

#La firma de las funciones deberá ser:

#volumen_cilindro(h, r)
#area_base(r)


#El programa deberá pedir las entradas al usuario y deberá informar la salida de forma legible
#El programa deberá notificar al usuario en caso que ingrese números negativos y terminar su ejecución

import math
def area_base(r):
    return r * 2 * math.pi

def volumen_cilindro(h,r):
    b = area_base(r)
    return (b*h)

def main():
    print("Bienvenido: ")

    L = int(input("Ingresa altura correspondiente:  "))
    while L < 0:
        print("¡Ha escrito un número negativo! Inténtelo de nuevo o el programa se cerrará")
        L = int(input("Escriba altura correspondiente: "))
        if (L<0):
            print ("Adios!")
            exit()

    F = int(input("Ingresa radio correspondiente:   "))
    while F < 0:
        print("¡Ha escrito un número negativo! Inténtelo de nuevo o el programa se cerrará")
        F = int(input("Escriba radio correspondiente:: "))
        if (F<0):
            print ("Adios!")
            exit()

    A = area_base(F) 
    R = volumen_cilindro(L,F)
    print("El area es de:  ",A)
    print("El volumen es de:  ",R)

main()
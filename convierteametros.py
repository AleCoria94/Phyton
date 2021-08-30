def convertir_a_metros(millas,pies,pulgadas):
    return 1609.344*millas + 0.3048 * pies + 0.0254 * pulgadas

def main():
    print ("convierte medidas inglesas a metros")
    L = int(input("Cuantas millas?:  "))
    F = int(input("Cuantos pies?:   "))
    P = int(input("Y cuantas pulgadaas"))
    M = convertir_a_metros(L,F,P)
    print("La longitud ingresa es de ",M," metros ");
    
main()
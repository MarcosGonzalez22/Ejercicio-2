class ViajeroFrecuente:
    __numViajero=0
    __nombre=""
    __apellido=""
    __dni=""
    __millasAcum=0
    
    def __init__(self,numViajero,nombre,apellido,dni,millasAcum):
        self.__numViajero=numViajero
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__millasAcum=millasAcum
        
    def cantidadTotaldeMillas(self):
        return print("La cantidad de millas acumuladas es: {}".format(self.__millasAcum))
        
    def acumularMillas(self,millas):
        acum=int(self.__millasAcum)+millas
        self.__millasAcum=acum
        return print("El valor actualizado de millas es de: ", acum)
    
    def canjearMillas(self,canje):
        if(canje<=int(self.__millasAcum)):
            restoMillas=int(self.__millasAcum)-canje
            self.__millasAcum=restoMillas
            print("La cantidad de Millas despues del canje es de: ", restoMillas)
        else:
             print("La cantidad de Millas acumuladas sin canje es de: ", self.__millasAcum)
  
              
import csv
if __name__ == '__main__':
    arch=open("ViajerosFrecuentes.csv")

    reader=csv.reader(arch,delimiter=';')
    lista=[]
    #viajeros=arch.read().split(';')
   # print(viajeros[1])
    c=0
    for fila in reader:
        
        numViajero=fila[0]
        nombre=fila[1]
        apellido=fila[2]
        dni=fila[3]
        millasAcum=fila[4]
        c+=1
        unViajero=ViajeroFrecuente(numViajero, nombre, apellido, dni, millasAcum)
        lista.append(unViajero)
        
    print(lista[1].cantidadTotaldeMillas())
        
    arch.close()    

    numviajero=int(input("Ingrese Numero de Viajero: "))
    opcion = input("Ingrese la opcion: ")
    menu = """
        ***MENU***
        [1] Consultar Cantidad de Millas
        [2] Acumular Millas
        [3] Canjear Millas  
        [0] SALIR
        """
    print(menu)
        
    if (opcion=='1'):
        print("accion 1")
        lista[numviajero-1].cantidadTotaldeMillas()
    elif (opcion=='2'):
        print("accion 2")
        millas = int(input("Ingrese cantidad de millas a acumular: "))
        lista[numviajero-1].acumularMillas(millas)
    elif (opcion=='3'):
        print("accion 3")
        canje = int(input("Ingrese cantidad de millas a canjear: "))
        lista[numviajero-1].canjearMillas(canje)
    elif (opcion=='0'):
        print("accion 0")

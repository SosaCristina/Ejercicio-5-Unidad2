from ClasePlanAhorro import PlanAhorro
from ClaseManejadorPlan import Manejador
import csv



if __name__=="__main__":
    objetoManejador = Manejador()
    objetoManejador.testPlan()
    print(objetoManejador)
    opcion= 0
    def menu():
        opc= int(input("Menu Principal\n" +
                      "1)Actualizar el valor del vehiculo de cada plan\n" +
                      "2)Dado un valor, mostrar codigo, modelo y version\n" +
                      "3)Mostrar monto que se debe pagar para licitar el vehiculo\n" +
                      "4)Modificar la cantidad de cuotas que se debe tener pagas para licitar\n" +
                      "5)Finalizar\n"+
                      "Elija una opcion\n"))
        return opc
    while opcion!=5:
        opcion=menu()
        if opcion == 1:
            objetoManejador.opcion1()

        if opcion == 2:
            print("Ingresar un valor ") #para que funcione debe ser mayor al valor de la cuota
            valor=int (input())
            objetoManejador.opcion2(valor)

        if opcion == 3:
            objetoManejador.opcion3()


        if opcion == 4:
            print ("Ingresar codigo de plan")
            cod=int(input())
            objetoManejador.opcion4(cod)




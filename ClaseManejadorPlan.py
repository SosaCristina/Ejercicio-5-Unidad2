import csv
from ClasePlanAhorro import PlanAhorro

class Manejador:

    def __init__(self):
        self.__listaPlan=[]

    def agregar (self, unPlan):
        self.__listaPlan.append(unPlan)

    def testPlan (self):
        archivo = open("planes.csv")
        reader=csv.reader(archivo, delimiter=";")
        for fila in reader:
            cod = int (fila[0])
            modelo = fila[1]
            version = fila[2]
            valor = fila[3]

            unPlan=PlanAhorro(cod,modelo,version,valor)
            self.agregar(unPlan)



        archivo.close()

    def __str__(self):
        s =""
        for plan in self.__listaPlan:
            s += str(plan) + '\n'
        return s


    def opcion1 (self):
        for plan in self.__listaPlan:
           print("Codigo de plan:{}.Modelo:{}. Version{}".format(plan.getCodigo(), plan.getModelo(), plan.getVersion()))
           print("Ingresar nuevo valor:")
           nuevo=float (input())
           plan.modificarValor (nuevo)


    def opcion2 (self, valor):
        for plan in self.__listaPlan:

            if(plan.calcularcuota() < int(valor)):
                print("Codigo de plan:{}.Modelo:{}. Version{}".format(plan.getCodigo(), plan.getModelo(), plan.getVersion()))

    def opcion3 (self):
        for plan in self.__listaPlan:
            licitar=int (plan.calcularcuota()) * (PlanAhorro.getCant_cuotasLicitar())
            print("Se debe pagar para licitar el vehiculo con codigo {}: {}".format(plan.getCodigo(),licitar))


    def opcion4 (self, cod):
        for plan in self.__listaPlan:
            if (plan.getCodigo() == cod):
                plan.modificarCuota_l()

    def buscar (self, cod):
        indice = 0
        while indice < len(self.__listaPlan) and (cod!=self.__listaPlan.getCodigo()):
            indice+=1

        if(indice -1 < len(self.__listaPlan)):
            self.__listaPlan[indice-1].modificarCuota_l()






















class PlanAhorro:
    __Codigo_plan = int
    __Modelo= ""
    __Version= ""
    __Valor_vehiculo= int
    cant_cuotas_plan = 50 #igual para todos los planes
    cant_cuotas_licitar = 20 #igual para todos los planes

    def __init__ (self, cod, modelo, version, precio):
        self.__Codigo_plan = cod
        self.__Modelo = modelo
        self.__Version = version
        self.__Valor_vehiculo = precio


    def getCodigo (self):
         return self.__Codigo_plan

    def getModelo (self):
        return self.__Modelo

    def getVersion (self):
        return self.__Version

    @classmethod
    def getCant_cuotasPlan(cls):
      return cls.cant_cuotas_plan
    @classmethod
    def getCant_cuotasLicitar(cls):
       return cls.cant_cuotas_licitar

    def __str__(self):
        return "%s %s %s %s %s  %s" % (self.__Codigo_plan, self.__Modelo, self.__Version, self.__Valor_vehiculo, PlanAhorro.getCant_cuotasPlan(), PlanAhorro.getCant_cuotasLicitar())

    def modificarValor (self, valor):
        self.__Valor_vehiculo=valor
        print("Valor modificado:{}".format(self.__Valor_vehiculo))

    def modificarCuota_l (self):
        print("Ingresar nueva cantidad de cuotas")
        nueva_cant=int(input())
        PlanAhorro.cant_cuotas_licitar = nueva_cant
        print("Nueva cantidad  de cuota para licitar:{}".format(PlanAhorro.getCant_cuotasLicitar())) ##esta bien????

    def calcularcuota (self):
        importe= int (self.__Valor_vehiculo)
        cuotasp=  (PlanAhorro.cant_cuotas_plan)
        porcentaje= int (importe*0.10)
        cuota=(importe/cuotasp) + porcentaje
        return cuota









    

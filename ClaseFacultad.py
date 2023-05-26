from ClaseCarrera import Carrera

class Facultad:
    __codigoF=int
    __nombre=""
    __direccion=""
    __localidad=""
    __telefono=""
    __carrera=None

    def __init__(self,c,n,d,l,t):
        self.__codigoF=c
        self.__nombre=n
        self.__direccion=d
        self.__localidad=l
        self.__telefono=t
        self.__carrera=[]

    def __str__(self):
        return "CODIGO FACULTAD:{} - NOMBRE:{} - DIRECCION:{} - LOCALIDAD:{}".format(self.__codigoF,self.__nombre,self.__direccion,self.__localidad,self.__telefono)

    def agregar_Carrera(self,cod,nom,fecha,dur,titulo):
        unaCarrera=Carrera(cod,nom,fecha,dur,titulo)
        self.__carrera.append(unaCarrera)

    def get_nombre (self):
        return self.__nombre
    def get_codigoF(self):
        return self.__codigoF
    def get_localidad(self):
        return self.__localidad
    def mostrar_carrera (self):
        for lista in self.__carrera:
            print(lista)

    def buscar_carrera(self,nombre):
        
        i=0
        indice=0
        bandera=False
        while i< len(self.__carrera) and not bandera:
            
            if (str(nombre) != str(self.__carrera[i].get_nombreC())):
                print("CARRERA DENTRO DEL BUSCAR:",self.__carrera[i].get_nombreC())
                i+=1
                
            else:
                indice=i
                bandera= True
        if bandera == True:
            return self.__carrera[indice]


        


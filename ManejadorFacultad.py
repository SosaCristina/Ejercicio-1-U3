from ClaseFacultad import Facultad
from ClaseCarrera import Carrera
import csv

class ManejadorF:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def agregar (self,unaFacultad):
        self.__lista.append(unaFacultad)

    def crear_facultad (self):
        archivo=open("C:\\Users\\chili\\POO archivos\\facultades.csv")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            if len(fila)==5:
                cod=fila[0]
                nom=fila[1]
                direc=fila[2]
                loc=fila[3]
                tel=fila[4]        
                unaFacultad=Facultad(cod,nom,direc,loc,tel)
                self.agregar(unaFacultad)
            else:
                codC=fila[1]
                nom=fila[2]
                fecha=fila[3]
                dur=fila[4]
                titulo=fila[5]
                self.__lista[int(cod)-1].agregar_Carrera(codC,nom,fecha,dur,titulo)
        archivo.close

    def __str__(self):
        s=""
        for lista in self.__lista:
            s+= str(lista) + "\n"
        return s

    def obtener_datos(self,cod):
        indice=0
        bandera=False
        
        while indice<len (self.__lista) and not bandera:
            if int(cod)==int(self.__lista[indice].get_codigoF()):
                facultad=self.__lista[indice]
                print("Nombre de la Facultad:{}".format(self.__lista[indice].get_nombre()))
                bandera=True
                facultad.mostrar_carrera ()
            else:
                indice+=1    

    def mostrar_todo(self):
        for lista in self.__lista:
            print(lista.mostrar_carrera())

    def datos_facultad(self,nombre):
        
        i=0
        bandera=False
        while i< len(self.__lista) and not bandera:
            
            carrera=self.__lista[i].buscar_carrera(nombre)
            
            if carrera!=None :
                bandera=True
            
                print("Codigo:{}{} Nombre Facultad:{} - Localidad:{}".format(carrera.get_codigoC(),self.__lista[i].get_codigoF(),self.__lista[i].get_nombre(),self.__lista[i].get_localidad()))
            else: 
                i+=1
from ManejadorFacultad import ManejadorF
from ClaseCarrera import Carrera
from ClaseFacultad import Facultad
import csv

if __name__=="__main__":
    unaFacultad=ManejadorF()
    unaFacultad.crear_facultad()
    #print(unaFacultad)
    cod=int(input("Ingresar codigo de Facultad: "))
    unaFacultad.obtener_datos(cod)

    nom=input("Ingresar nombre de Carrera: ")
    unaFacultad.datos_facultad(nom)

    

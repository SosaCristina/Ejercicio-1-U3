
class Carrera:
    __codigoC=int
    __nombreC=""
    __fecha=""
    __duracion=""
    __titulo=""

    def __init__(self,c,n,f,d,t):
        self.__codigoC=c
        self.__nombreC=n
        self.__fecha=f
        self.__duracion=d
        self.__titulo=t

    def __str__(self):
        return "CODIGO CARRERA:{} - NOMBRE:{} - FECHA:{} - DURACION:{} - TITULO:{}".format(self.__codigoC,self.__nombreC,self.__fecha,self.__duracion,self.__titulo)

    def get_codigoC(self):
        return self.__codigoC
    def get_nombreC(self):
        return self.__nombreC
    def get_duracion(self):
        return self.__duracion    
    
        
class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __password = ''
    def __init__(self,idCuenta='',dominio='',tipoDominio='',password=''):
        self.__idCuenta= idCuenta
        self.__dominio= dominio
        self.__tipoDominio= tipoDominio
        self.__password = password

    def retornaEmail(self):
        return '{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipoDominio)
    
    def getContraseña(self):
        return self.__password
    def getDominio(self):
        return self.__dominio
    def setContraseña(self,contra):
        self.__password=contra

    def __str__(self):
        return ('( {}, {}, {}, {})').format(self.__idCuenta,self.__dominio,self.__tipoDominio,self.__password)
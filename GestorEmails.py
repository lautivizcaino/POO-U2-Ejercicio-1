import csv
from email import Email

class gestorEmails:
    def __init__(self):
         self.__listaEmails= []
    def agregarEmail(self,unEmail):
        self.__listaEmails.append(unEmail)
    def __str__(self) -> str:
        s=''
        for e in self.__listaEmails:
            s+= str(e) + '\n'
        return s

    def crearCuenta(self,mail):
        id=mail.split("@",1)
        dom=id[1].split(".",1)
        unEmail= Email(id[0],dom[0],dom[1],input('Contraseña: '))
        self.agregarEmail(unEmail)

    def modificarContraseña(self,unMail):
            c= input('Contraseña actual: ')
            if c==unMail.getContraseña():
                unMail.setContraseña(input('Contraseña nueva: '))
    def testEmail(self):
            i=1
            file=open('archivo.csv')
            reader= csv.reader(file,delimiter=',')
            for fila in reader:
                id=fila[0].split("@",1)
                dom=id[1].split(".")
                if id[0]=='' or dom[0]=='' or dom[1]=='':
                    print("El email {} es incorrecto".format(fila[0]))
                else:
                    OtroMail = Email(id[0],dom[0],dom[1],input('Contraseña del email {}: '.format(i)))
                    print(OtroMail)
                    self.agregarEmail(OtroMail)
                    i+=1
    def obtenerIgualDominio(self,dom):
        i=0
        for e in self.__listaEmails:
            if e.getDominio()== dom:
                i+=1
        return i
        

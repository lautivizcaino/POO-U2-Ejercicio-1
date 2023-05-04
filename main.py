import csv
from email import Email
from GestorEmails import gestorEmails
if __name__ == '__main__':
    gE= gestorEmails()
    print('PUNTO 1')
    print('Ingrese su nombre y direccion de email')
    persona= input('Nombre: ')
    unMail = Email(input('ID de Cuenta: '),input('Dominio: '),input('Tipo de Dominio: '),input('Contraseña: '))
    gE.agregarEmail(unMail)
    print('Estimado {} te enviaremos tus mensajes a la direccion {}'.format(persona,unMail.retornaEmail()))


    print('PUNTO 2')
    gE.modificarContraseña(unMail)

    print('PUNTO 3')
    gE.crearCuenta(input('Direccion de Email: '))

    print('PUNTO 4')
    gE.testEmail()
    print(gE.obtenerIgualDominio(input('Ingresar un dominio :')))
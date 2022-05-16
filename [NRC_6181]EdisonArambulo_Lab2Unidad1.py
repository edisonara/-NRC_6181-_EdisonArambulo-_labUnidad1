# ubicandonos desde  un angulo que no sea 90 grados

def caratula():
    #mensaje en pantalla 
    print("\nUNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE \n\n" +
    "viembenido, clacularas la hipotenusa de un triangulo rectangulo.\n autor: edison arambulo\n curso: POO, 2do 'a'")


def hipotenusa(datOp, datAdya):
    # calcular la hipotenusa con la formula de pitagoras (utiliza str)
    return(str((datOp**2 + datAdya**2)**1/2))

def cateto():
    #calculo de cateto (utiliza str)
    hipotenusa = int(input("ingrese la hipotenusa: "))
    dat = int(input("ingrese el cateteto: "))
    print("el valor del cateto es: " + str((hipotenusa**2 - dat**2)**1/2))

caratula()
#menu de 4 pociones   %%%
while True: # repetir infinita veses, con el exit() de la opcion salir termina.
    #presentaar en pantalla el menu disponible (4 opciones)
    print('\n------- eliga opcion ----------')
    print('op 1: calculo de hipotenusa.')
    print('op 2: calculo de cateto opuesto.')
    print('op 3: calculo de cateto adyasente.')
    print('op 4: salir.')
    opMenu = int(input('la opcion es? : '))
    if opMenu==1:
        catetOpDato = int(input("ingrese el cateto opuesto: "))
        catetAdDato = int(input("ingrese el cateteto adyasente: "))
        print("la hipotenusa es: " + hipotenusa(catetOpDato,catetAdDato))

    elif opMenu==2:
        #repite el mismo proceso con opcion 3
        cateto()  
    elif opMenu==3:
        cateto()
    elif opMenu==4:
        #salir con exit()
        print('usted salio mi pana ;) ')
        exit()
    else:
        print('error ;)')


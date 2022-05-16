# ubicandonos desde  un angulo que no sea 90 grados
def caratula():
    #mensaje
    print("UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE \n" +"viembenido, clacularas la hipotenusa de un triangulo rectangulo.\n autor: edison arambulo\n curso: POO, 2do 'a'")


def hipotenusa(datOp, datAdya):
    # calcular la hipotenusa con la formula de pitagoras
    return((datOp**2 + datAdya**2)**1/2)

caratula()
catetOpDato = int(input("ingrese el cateto opuesto: "))
catetAdDato = int(input("ingrese el cateteto adyasente: "))
print("la hipotenusa del triangulo es: " + str(hipotenusa(catetOpDato, catetAdDato)))
#modificacion  adicional, no va a quedar asi
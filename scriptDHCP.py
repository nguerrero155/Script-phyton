contador=10
archivo=open ('IP_Fijas_19102022.txt', mode='r')
for dispositivo in archivo:
    dispositivo_coma = dispositivo.replace ('---------', ';')
    elementos=dispositivo_coma.split(';')
    nombre_dispositivo=elementos[0].replace('.', '_')

    print ("host ", nombre_dispositivo, "{")
    print ("#Asignacion estatica")
    print ("hardsare ethernet ", elementos[1], "; #Direccion MAC del host")
    print ('fixed-address 192.168.0.%d'%contador, "; #IP a asignar al host")
    print ("}")

    contador=contador+1



import os

import datetime

from ftplib import FTP_TLS

import ssl

import smtplib

#from knockknock import email_sender



now = datetime.datetime.now()

tiempo = now.strftime("%Y%m%d_%H-%M")

#tiempo = now.strftime("%Y%m%d")



cmd= "tar -czf backup"+tiempo+".tgz /var/www"

os.system(cmd)



#Función para conectarse

def connect():

    ftp = FTP_TLS()

    #ftp.debugging = 2

    ftp.connect('192.168.206.120')

    #ftp.connect('192.168.1.32')

    ftp.login('ftpUser1', '1e2f3m-A')

    #para proteger y usar TLS

    ftp.prot_p()

    print ("Bien")

    return ftp



ftp = connect()



#Enviar fichero

fichero="backup"+tiempo+".tgz"

file = open(fichero, 'rb')

ftp.storbinary('STOR '+fichero, file)

file.close() 



#NLST muestra solo los nombres de los ficheros, LIST muestra nombres e info (como ls -l)

print ("Contenido de la carpeta antes de borrar:")

ftp.retrlines('NLST')



#Recuperamos lista ficheros y ordenamos la lista por si el server no la devuelve ordenada

listaFich=ftp.nlst()

listaFichOrdenada= sorted(listaFich, reverse=False)

#print (listaFich)

#print (listaFichOrdenada)



#Muestra el numero de filas/ficheros que hay

print (len(listaFich))





if (len(listaFich) > 10):

	print ("Hay más de 10 copias... Hay que borrar una")

	ftp.delete(listaFichOrdenada[0])

	print ("Contenido de la carpeta despues de borrar:")

	ftp.retrlines('NLST')





#Borrar fichero local

borrar="rm "+fichero

os.system(borrar)





#Enviar correo 2

remitente = 'pruebaftp03@gmail.com'

destinatario = ['jgalmansa184@ieszaidinvergeles.org', 'pedro@andared.com']

asunto = 'Copia de seguridad ftp'

mensaje = 'Se ha hecho la copia de seguridad ftp'



email = """\

From: %s

To: %s

Subject: %s



%s

""" % (remitente, ", ".join(destinatario), asunto, mensaje)



try:

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.login('pruebaftp03@gmail.com', 'antbddwmcvqlhatt')

    

    server.sendmail(remitente, destinatario, email)

    server.close()

    print ('Correo enviado!')

    # ...send emails

except:

    print ('Algo ha salido mal')



















#-------------------------



#Enviar correo

#remitente = "julia.almansa.garcia@gmail.com"  

#destinatario = "naddiaa27@gmail.com" 

#asunto = "Copia de seguridad - TFP" 

#mensaje = """Hola!<br/> <br/> 

#La copia de seguridad se ha completado.

#"""

#email = """From: %s 

#To: %s 

#MIME-Version: 1.0 

#Content-type: text/html 

#Subject: %s 

#

#%s

#""" % (remitente, destinatario, asunto, mensaje) 

#try: 

#    smtp = smtplib.SMTP('localhost') 

#    #smtp.set_debuglevel(1)

#    smtp.sendmail(remitente, destinatario, email) 

#    print ("Correo enviado") 

#except: 

#    print ("Error: el mensaje no pudo enviarse. Compruebe que sendmail se encuentra instalado en su sistema")



#-------------------------





#@email_sender(recipient_emails="nguerrero155@ieszaidinvergeles.org", sender_email="jgalmansa184@ieszaidinvergeles.org")

#def train_your_nicest_model(your_nicest_parameters):

#    import time

#    time.sleep(10000)

#    return {'loss': 0.9} # Optional return value















#Viejo

#Hostname = "192.168.1.32"

#Username = "julia"

#Password = "1234"

#with pysftp.Connection(host=Hostname, username=Username, password=Password) as sftp:

#	print("Connection successfully established ... ")
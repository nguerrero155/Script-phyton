#Script para acrear un fichero .htaccess

import sys
import os
import hashlib

password = sys.argv[4]
passwordCifrado = password.encode('utf-8')
md5 = hashlib.md5(passwordCifrado).hexdigest()
print(md5)

if len(sys.argv) != 6:
    print("El programa encesita 6 argumentos.")
    sys.exit(1) #1 es salida con error
else:
    #print(sys.argv[0]) #muestra el argumento 1, el nombre del programa
    #print(sys.argv[1]) #muestra el argumento 2, la ruta
    #print(sys.argv[2])
    #print(sys.argv[3])
    #print(sys.argv[4])
    #print(sys.argv[5])
    
    file = open(sys.argv[1] + "\.htpasswd", "w")
    file.write(f"{sys.argv[3]}:{md5}")

    #Generar .htaccess en el direcotrio que indicamos
    file = open(sys.argv[1]+"\.htaccess","w") # \ en winndows y / en linux, la ruta de hdocs/asir debe existir
    file.write("DirectoryIndex "+sys.argv[2]+'\n')    
    
    file.write("AuthName \"Dialog prompt\"\n")
    file.write("AuthType Basic\n")
    file.write(sys.argv[1] + "\.htpasswd\n")

    #Optionss - Indexes
    if (sys.argv[5]) == 'S':
        file.write("Options -Indexes\n")





    
import urllib.request, urllib.parse, urllib.error
###Creando un web Browser###

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #Crea la conexion, encode automatico y recoge la cabecera y la guarda dejando solo un file handle 'fichero temporal'
for line in fhand:
    print( line.decode().strip() )#Strip quita los espacios



#Manera antigua
"""
import socket
mysock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
try:
    mysock.connect( ('data.pr4e.org', 80) ) #Primer parametro es el host y segundo el puerto
except:
    print('No se ha podido crear una conexión con ese host')
    quit()
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() #El mensaje enviado es el get del protocolo HTTP. El salto de linea doble se pone siempre.
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ):
        break #Significa que el servidor ha terminado la conexión ya que no envia más datos
    print( data.decode() )
mysock.close()
"""

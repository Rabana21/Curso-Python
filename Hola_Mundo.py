import re

print ('Introduce el nombre del archivo: ')
narchivo = input()
try:
    archivo = open(narchivo)
except:
    print('El archivo no exixte')
    quit()

diccionario = dict()
for linea in archivo:
    correo = re.findall( '^From (\S+@\S+)',linea )
    palabras = linea.split()
    for palabra in palabras:
        diccionario[palabra] = diccionario.get(palabra,0) + 1
"""
palabra_mas_repetida = None
numero_veces = None
lista = list()
for palabra,veces in diccionario.items():
    if palabra_mas_repetida == None or numero_veces < veces:
        palabra_mas_repetida = palabra
        numero_veces = veces
    lista.append( (veces,palabra) ) #Utilizo el valor primero para despues ordenarlo

lista = sorted(lista, reverse = True)
"""
#Manera cool de hacer lo de arriba
lista = sorted( [ (v,p) for p,v in diccionario.items() ], reverse = True )

print('El top 10 de palabras repetidas en le texto es: ') 
for v,p in lista[:10]:
    print(p, str(v))
    
#print('La palabra más repetida ha sido: \'' + palabra_mas_repetida + '\' la cual se ha repetido ' + str(numero_veces) + ' veces')
if correo[0] is not None:
    print('El correo del archivo es: \'' + correo[0] + '\'')






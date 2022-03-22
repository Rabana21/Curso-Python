import xml.etree.ElementTree as ET

data = '''<people>
    <person x="1">
        <name>Chuck</name>
        <phone type="intl">
            +34 655 00 00 00
        </phone>
        <email hide="yes"/>
    </person>
    <person x="2">
        <name>Bob</name>
        <phone type="intl">
            +34 656 00 00 00
        </phone>
        <email hide="yes"/>
    </person>
</people>'''

try:
    tree = ET.fromstring(data) #Puede porducir fallo por la sintaxis
except:
    print('El xml está mal escrito')
    quit()
lst = tree.findall('person')
print('Numero de personas:', len(lst) )
for tag in lst:
    print('Attribute:', tag.get( 'x' ))#get es por si tiene un atributo el tag
    print('Name:', tag.find( 'name' ).text)
    print('Attr:', tag.find( 'email' ).get( 'hide' ),'\n') 

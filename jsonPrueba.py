import json

data = '''[
    {   "x" : "1",
        "name" : "Chuck",
        "phone" : "+34 655 00 00 00",
        "email" : { "hide" : "yes" }
    },
    {   "x" : "2",
        "name" : "Bob",
        "phone" : "+34 656 00 00 00",
        "email" : { "hide" : "no" }
    }
]'''
info = json.loads(data) #Devuelve una lista de diccionarios

for item in info:
    print('Attribute:', item['x'])
    print('Name:', item['name'])
    print('Phone:', item['phone'])
    print('Email', item['email']['hide'], '\n')
     

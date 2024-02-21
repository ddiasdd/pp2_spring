import json
with open('sample-data.json','r') as file:data = json.load(file)
print("Interface Status\n================================================================================\nDN                                                 Description           Speed    MTU\n-------------------------------------------------- --------------------  ------  ------ ")
st = 0
for i in data['imdata']:
    size = 0
    for key in i['l1PhysIf']['attributes']['dn']:size += 1
    for key in i['l1PhysIf']['attributes']['dn']:print(key,end = '')
    if size > st:st = size
    if size != st : print(' ' * (st - size),end = "")
    print(' ' * (12) ,end = ' ') 
    for key in i['l1PhysIf']['attributes']['descr']: print(key, end = '')
    print(' ' * (16),end = ' ')
    for key in i['l1PhysIf']['attributes']['speed']:print(key,end ='')
    print(' ' * (3),end = "")
    for key in i['l1PhysIf']['attributes']['mtu']: print(key,end = '')
    print()
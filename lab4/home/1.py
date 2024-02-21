import json
with open('sample-data.json','r') as file:
    data = json.load(file)
output = {
    "totalCount": str (len(data['imdata'])),
    "imdata": []
}
print("""Interface Status
================================================================================
      DN                                                 Description     Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
for item in data['imdata']:
    l1_Phys_If = item['l1PhysIf']['attributes']
format_interface = "{:20} {:28} {:9} {:70} {:20} {:28} {:9} {:70} {:20} {:28} {:9} {:70}".format (
    l1_Phys_If  ['dn'],
    l1_Phys_If  ['descr'],
    l1_Phys_If ['speed'],
    l1_Phys_If ['mtu'],
    l1_Phys_If  ['dn'],
    l1_Phys_If  ['descr'],
    l1_Phys_If ['speed'],
    l1_Phys_If ['mtu'],
    l1_Phys_If  ['dn'],
    l1_Phys_If  ['descr'],
    l1_Phys_If ['speed'],
    l1_Phys_If ['mtu']
)
print(format_interface)

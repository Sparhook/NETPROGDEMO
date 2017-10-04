inventory=[]
file=open("inventory.txt","r")
for item in file:
    item=item.strip()
    inventory.append(item)
file.close()
for item2 in inventory:
    print(item2)
    

import time
file=open("inventory2.txt","a")
print("TYPE in 'exit' to list current contents...")
while True:
    newItem=input("Enter new inventory item: ")
    if newItem == "exit":
        print ("All Done!!")
        break
    file.write(newItem + "\n")
file.close()
file=open("inventory2.txt","r")
invent=[]
for item in file:
    item=item.strip()
    invent.append(item)
file.close()
print ("<-- START OF LIST -->")
print ("\n")
for item2 in invent:
    print(item2)
else:
    print("\n")
    print("<-- END OF LIST -->")
    time.sleep(3)
while True:
    resetFile=input("Do you want to reset the file?")
    if resetFile != "yes":
        print ("Exiting Script.....")
        time.sleep(3)
        break
    else:
        print("Resetting file contents please wait....")
        time.sleep(3)
        file=open("inventory2.txt","w")
        file.close()
        print("FILE BLANKED.....")
        break
    

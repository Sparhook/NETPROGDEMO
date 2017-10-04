dscp=input("Enter the DSCP value please: ")
if dscp=="46":
    print ("This is a VOICE MEDIA packet...")
elif dscp=="24":
    print ("This is a VOICE SIGNALING packet...")
else:
    print ("This is not a VOICE packet....")

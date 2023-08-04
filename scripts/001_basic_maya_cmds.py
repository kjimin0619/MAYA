from maya import cmds
a = 182
b = 185

if a == b :
    print("같음!")
    for i in range(10) :
        cmds.polyCube(name = "pc{}".format(i+1))
    # cmds.polyCone()
else :
    print("다름!")
    for i in range(10):
        cmds.polySphere(name = "ps".format(i+1))
    # cmds.polyCylinder()
    

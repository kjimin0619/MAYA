from maya import cmds
import random

cmds.polyCylinder(name="myCylinder")
cmds.setAttr("myCylinder.translate", 3,4,5)
cmds.setAttr("myCylinder.rotate", 30,30,30)
cmds.setAttr("myCylinder.scale", 2,4,1)

mode = "Cone"

for i in range(3):
    if mode == "Cube" :
        obj = cmds.polyCube(name="myObj_%d" %(i))
    elif mode == "Cone" :
        obj = cmds.polyCone(name="myObj_%d" %(i))
    else :
        cmds.error("I don't know..")

    cmds.setAttr(obj[0]+".translate", random.randint(0,20),random.randint(0,20),random.randint(0,20))

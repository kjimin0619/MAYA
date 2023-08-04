from maya import cmds
import random

i = 0
while i < 10 :
    print(i)
    cmds.polyCube(name = "myCube_{}".format(i+1))
    cmds.setAttr("myCube_{}.translate".format(i+1) , i*5, i*5, i*5)
    
    cmds.polySphere(name = "mySphere_{}".format(i+1))
    cmds.setAttr("mySphere_{}.translate".format(i+1), random.randint(0,10),random.randint(0,10),random.randint(0,10))
    
    i+= 1
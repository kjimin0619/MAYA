from maya import cmds

cmds.polyCube(name="bottom")
cmds.setAttr("bottom.scale", 4, 1, 10)

for i in range(1,5):
    cmds.polyCylinder(name="wheel_%d" %(i))
    cmds.setAttr("wheel_{}.scale".format(i), 2,0.3,2)
    cmds.setAttr("wheel_{}.rotateZ".format(i), 90)
    

cmds.setAttr("wheel_1.translate", -2.25,-0.1,5)
cmds.setAttr("wheel_2.translate", -2.25,-0.1,-5)
cmds.setAttr("wheel_3.translate", 2.25,-0.1,5)
cmds.setAttr("wheel_4.translate", 2.25,-0.1,-5)


cmds.polyCone(name="pCone")
cmds.setAttr("pCone.scale", 0.5,1.8,0.5)
cmds.setAttr("pCone.translate", 0,1.7,5)
cmds.setAttr("pCone.rx",25)
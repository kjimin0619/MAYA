from maya import cmds

cmds.polyCube(name = "pC1")
cmds.setAttr("pC1.sz", 10)

cmds.polyCube(name = "pC2")
cmds.setAttr("pC2.sz", 10)
cmds.setAttr("pC2.tx", -10)

cmds.polyCube(name = "pC3")
cmds.setAttr("pC3.sx", 10)
cmds.setAttr("pC3.translate", -5,0,4.5)

cmds.polyCube(name = "pC4")
cmds.setAttr("pC4.sx", 10)
cmds.setAttr("pC4.translate", -5,0,-4.5)
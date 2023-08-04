from maya import cmds

## translate
print(cmds.getAttr("pCube1.translate"))

cmds.setAttr("pCube1.translateX", 7) # x축 위치 변경
print(cmds.getAttr("pCube1.translate"))



cmds.setAttr("pCube1.translateY", 10) # y축 위치 변경
print(cmds.getAttr("pCube1.translate"))

cmds.setAttr("pCube1.translate", 10, 10, 10) # x y z축 위치 변경
print(cmds.getAttr("pCube1.translate"))

## rotate
cmds.setAttr("pCube1.rotate", 15,15,15)

## scale
cmds.setAttr("pCube1.scale", 1,2,1)
from maya import cmds
import random 

def randObj(mode, num, minP = 0, maxP = 20) :
    objList = []
    for i in range(num) :
        if mode == "cube" :
            obj = cmds.polyCube()
        elif mode == "cone" :
            obj = cmds.polyCone()
        elif mode == "sphere" :
            obj = cmds.polySphere()
        else :
            cmds.error("i dont know")
            
        objList.append(obj[0])
    
    for obj in objList :
        cmds.setAttr(obj+".tx", random.randint(minP, maxP))
        cmds.setAttr(obj+".ty", random.randint(minP, maxP))
        cmds.setAttr(obj+".tz", random.randint(minP, maxP))
   
    return objList
            
temp = randObj("cube", 5)
print(temp)
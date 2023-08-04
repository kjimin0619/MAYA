from maya import cmds
myObj = [cmds.polyCube,cmds.polySphere,cmds.polyCone, cmds.polyCylinder]

for item in myObj:
    #item()
    pass
    
# 구구단
for i in range(2,10):
    for j in range(1,10):
        print("%2d * %2d  = %2d " %(i,j,i*j), end=" ")
    print()
        
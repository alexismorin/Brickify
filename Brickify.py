import maya.cmds as cmds
import random

selected_items = cmds.ls(selection=True)
if selected_items:
    shapes = cmds.listRelatives(selected_items[0], shapes=True)
    
for shape in shapes:
    
    smoothnode = cmds.polySmooth( shape )
    cmds.polyBevel( shape, offset=0.040,worldSpace=True )
    
    vertexPositionList = cmds.getAttr( shape+".vrts", multiIndices=True )
    for i in vertexPositionList :
        if random.random() > 0.8:
            brick = cmds.polyCube( w=0.2+(random.random()*0.4), h=0.3, d=0.2+(random.random()*0.4) )
            vtxPos = cmds.xform( str(shape)+".pnts["+str(i)+"]", query=True, translation=True, worldSpace=True )
            cmds.move(vtxPos[0]+(random.random()-0.5)*0.1,vtxPos[1]+(random.random()-0.5)*0.05,vtxPos[2]+(random.random()-0.5)*0.1, brick, absolute=True)
            cmds.rotate((random.random()-0.5)*5.0,(random.random()-0.5)*5.0,(random.random()-0.5)*5.0,brick)
            
            brickShape = cmds.listRelatives(brick, shapes=True)
            for brickVertices in brickShape:
                vertexNormalList = cmds.ls(brickVertices+'.e[*]', fl=True)
                for vertexRotation in vertexNormalList :
                    cmds.polyMoveVertex(vertexRotation, t=(0.0, 0.0, 0.0), random=0.1)
                    if random.random() > 0.4:
                        cmds.polyBevel( vertexRotation, offset=0.05,worldSpace=True )
                    
    cmds.delete( smoothnode )
            
            

            
            


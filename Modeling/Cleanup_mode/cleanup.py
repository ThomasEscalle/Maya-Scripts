### Maya script that clean the scene, delete history, freeze transforms, and optimize the scene size.
### Copyright (c) 2023, Thomas Escalle

import maya.cmds as cmds
import maya.mel as mel

def cleanScene():
    ### Delete all by type history.
    cmds.delete(ch=True, all=True)

    ### Loop through all the objects in the scene and freeze the transforms.
    for obj in cmds.ls():
        cmds.makeIdentity(obj, apply=True, t=1, r=1, s=1, n=0)
    
    ### Optimize the scene size.
    ### run the mel command "OptimizeScene;" in python.
    mel.eval('OptimizeScene;')

cleanScene()
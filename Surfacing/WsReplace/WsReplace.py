### Maya scrip that get all the PxrTexture nodes in the scene
### and make their path relative to the /sourceimages/ folder
### Replace everything before /sourceimages/ by '<ws>'

import maya.cmds as cmds

def replacePath():
    # get all the PxrTexture nodes in the scene
    nodes = cmds.ls(type='PxrTexture')
    for node in nodes:

        # get the file name
        fileName = cmds.getAttr(node+'.filename')
		

        # replace everything before /sourceimages/ by '<ws>'
        fileName = fileName.replace(fileName[:fileName.find('/sourceimages/')], '<ws>')

        # Set the new file name
        cmds.setAttr(node+'.filename', fileName, type='string')


### Replace the paths
replacePath()
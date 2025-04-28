###
### /!\ This is not used anymore, but it is kept for reference.
###
### Maya Python script to save the current scene as a new file
### This script will save the current scene as a "publish" version

import maya.cmds as cmds

def saveSceneAs():
    ### Save the current scene
    cmds.file(save=True, type='mayaAscii')

    ### Get the name of the scene
    sceneName = cmds.file(q=True, sn=True)
    sceneName = sceneName.replace('\\', '/')
    sceneName = sceneName.split('/')[-1]

    ### Remove the .ma or .mb extension
    sceneName = sceneName.replace('.ma', '').replace('.mb', '')
    
    splitedSceneName = sceneName.split('.')
    ### If the scene name has a version number, remove it
    if len(splitedSceneName) > 1:
        ### Remove the last element of the list
        splitedSceneName.pop()
        ### Join the list back together
        sceneName = '.'.join(splitedSceneName)
    

    ### Get the name of the scene directory
    sceneDir = cmds.workspace(q=True, rd=True)
    sceneDir = sceneDir.replace('\\', '/')
    sceneDir += 'scenes/'

    ### Export the scene
    oldSceneName = cmds.file(q=True, sn=True)
    savePath = sceneDir + sceneName + '.ma'
    cmds.file(rename=savePath)
    cmds.file(save=True, type='mayaAscii')
    cmds.file(rename=oldSceneName)

    ### Print in green
    print('Scene saved as: ' + savePath)
    



saveSceneAs()
### Maya script used to open a window to ask the user what type of objects to delete
### and then delete them
### Very usefull when a specific type of node crashes Maya, for example when a plugin is not loaded 

import maya.cmds as cmds


# Create a window
def CreateWindow():
    # Create a window
    window = cmds.window(title="Delete by Type", iconName='Short Name', widthHeight=(300, 100))

    cmds.columnLayout()
    cmds.text(label = 'Delete all the objects of a specific type')
    cmds.separator(height = 10, style = 'none')
    ### Ask the user what type of objects to delete as a text field
    cmds.textField('type',  text = '', width = 300)
    
    cmds.separator(height = 10, style = 'none')
    cmds.button(label = 'Delete', command = 'deleteAll()', width = 300)
    cmds.showWindow(window)


def deleteAll():
    # Delete all the objects of a specific type
    pType = cmds.textField('type', query = True, text = True)
    ### Get all the obejcts
    allObjects = cmds.ls()
    ### Loop through all the objects
    for obj in allObjects:
        ### Get the type of the current object
        objType = cmds.objectType(obj)
        ### If the type of the current object is the same as the type asked by the user
        if objType == pType:
            ### Delete the object
            cmds.delete(obj)



CreateWindow()
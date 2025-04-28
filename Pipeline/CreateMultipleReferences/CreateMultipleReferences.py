### Maya script that open a window where you can choose a file and create multiple reference of it in the scene
import maya.cmds as cmds

## Create a window
def create_window():
    window = cmds.window(title = 'Create multiple reference', widthHeight = (450, 160))
    cmds.columnLayout()
    cmds.text(label = 'Choose a file to create multiple reference of it')
    cmds.separator(height = 10, style = 'none')
    cmds.textFieldButtonGrp('file', label = 'File', buttonLabel = 'Browse', buttonCommand = 'browse_file()')
    cmds.textFieldGrp('namespace' ,label='namespace', text='default' )
    cmds.intFieldGrp('number', label = 'Number of reference', numberOfFields = 1, value1 = 1)
    
    cmds.separator(height = 10, style = 'none')
    cmds.button(label = 'Create', command = 'create_reference()', width = 450)
    cmds.showWindow(window)


## Browse a file
def browse_file():
    file = cmds.fileDialog2(fileMode = 1, caption = 'Choose a file')
    cmds.textFieldButtonGrp('file', edit = True, text = file[0])


## Create multiple reference
def create_reference():
    file = cmds.textFieldButtonGrp('file', query = True, text = True)
    anamespace = cmds.textFieldGrp('namespace', query=True, text= True)
    number = cmds.intFieldGrp('number', query = True, value1 = True)
    for i in range(number):
        cmds.file(file, reference = True, namespace = anamespace)


## Run the script
create_window()
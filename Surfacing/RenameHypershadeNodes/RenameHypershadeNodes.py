# Litle maya script to open a rename window

from distutils.log import debug
from sys import prefix
from unicodedata import name
import maya.cmds as cmds


def renameWindow():
    global RenameText
    global ObjectName
    

    if cmds.window('renameWindow', exists=True):
        cmds.deleteUI('renameWindow')
    cmds.window('renameWindow', title='Rename nodes', widthHeight=(250, 200), resizeToFitChildren=True)
    cmds.columnLayout()

    #
    # Text
    #
    cmds.separator(h=10)
    cmds.text(label="  Texts", font = "boldLabelFont" , w = 60, align = "left")

    #Rename Field in a row
    cmds.rowLayout(numberOfColumns=2, w = 240)
    cmds.text(label="  Text:" , ann="Write the prefix you want to add to the objects selected." , w = 70, align = "left")
    RenameText = cmds.textField( w = 165 )
    cmds.setParent('..')

    #Object name Field in a row
    cmds.rowLayout(numberOfColumns=2, w = 240)
    cmds.text(label="  Object name:", ann="Write the object name of what you are working on." , w = 70, align = "left")
    ObjectName = cmds.textField( w = 165 )
    cmds.setParent('..')

    cmds.separator(h=10, style='double',w = 240)


    #
    # Number 
    #
    cmds.text(label="  Number", font = "boldLabelFont" , w = 60, align = "left")
    cmds.separator(h=3)
    cmds.checkBox("showNumber_cb",label="Show index", value=False, ann="Show the type of the object in the name, ex: pxrRamp_")
    cmds.rowLayout(numberOfColumns=2, w = 240)
    cmds.text(label="  Start number",w = 80, align = "left")
    cmds.intField('startNumber', value=1, w = 40)
    cmds.setParent('..')
    cmds.separator(h=10, style='double',w = 240)

    #
    # Options in a row
    #
    cmds.text(label="  Options", font = "boldLabelFont" , w = 60, align = "left")
    cmds.separator(h=3)
    # If we want to show the type of the object
    cmds.checkBox("objectType_cb",label="Show type", value=True, ann="Show the type of the object in the name, ex: pxrRamp_")
    cmds.separator(h=5)

    cmds.rowLayout(numberOfColumns=3, w = 240)
    cmds.checkBox("vertical_cb",label="Vertical", ann="Add the '_vertical' attribute to your text.", w=75)
    cmds.checkBox("horizontal_cb",label="Horizontal", ann="Add the '_horizontal' attribute to your text.", w=75)
    cmds.checkBox("radial_cb",label="Radial", ann="Add the '_radial' attribute to your text.", w=75)
    cmds.setParent('..')

    cmds.separator(h=5)
    cmds.rowLayout(numberOfColumns=3, w = 240)
    cmds.checkBox("mask_cb", label="Mask", ann="Add the '_mask' attribute to your text.", w=75)
    cmds.checkBox("coloc_cb",label="Color", ann="Add the '_col' attribute to your text.", w=75)
    cmds.checkBox("dif_color_cb", label="Dif Color", ann="Add the '_difCol' attribute to your text.", w=75)
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns=3, w = 240)
    cmds.checkBox("specular_cb" , label="Specular", ann="Add the '_spec' attribute to your text.", w=75)
    cmds.checkBox("rough_cb" , label="Rough", ann="Add the '_rough' attribute to your text.", w=75)
    cmds.checkBox("refraction_cb",label="Refraction", ann="Add the '_refr' attribute to your text.", w=75)
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns=3, w = 240)
    cmds.checkBox("reflection_cb", label="Reflection", ann="Add the '_refl' attribute to your text.", w=75)
    cmds.checkBox("bump_cb" , label="Bump", ann="Add the '_bump' attribute to your text.", w=75)
    cmds.checkBox("displacement_cb" , label="Displacement", ann="Add the '_displ' attribute to your text.", w=75)
    cmds.setParent('..')
    
    cmds.separator(h=10, style='double',w = 240)



    cmds.separator(h=20)

    # Rename button at the bottom of the window filled on width
    cmds.button(label='Rename', command='rename()', width=240, bgc=[0.1884, 0.4513, 0.1428])

    cmds.separator(h=8)

    cmds.rowLayout(numberOfColumns=3, w = 240)
    cmds.button(label='Select Left', command='selectLeft()', width=120)
    cmds.button(label='Select Right', command='selectRight()', width=120)
    cmds.setParent('..')    

    cmds.showWindow('renameWindow')
    

def selectRight():
    print("selectRight")

def selectLeft():
    print("selectLeft")


def rename():
    numberIndex = cmds.intField('startNumber', query=True, value=True)

    # Loop through all selected objects
    for obj in cmds.ls(selection=True):
        text = ""
        text =  cmds.textField(RenameText, query=True, text=True)
        objectName = cmds.textField(ObjectName, query=True, text=True)
        pType = ""
        options = ""
        number = ""

        if(cmds.checkBox("objectType_cb", query=True, value=True)):
            pType = getObjectType(obj);

        # Get the options
        options = getOptions()



        ## Convert the number to a string
        number = str(numberIndex)
        numberIndex += 1

        # Create the new name
        GoodName = ""

        # iF there is a type   type_objectName_options_text_number
        if(pType != ""):
            GoodName = pType + "_"

        if(objectName != ""):
            GoodName += objectName + "_"
        
        if(options != ""):
            GoodName += options + "_"
        
        if(text != ""):
            GoodName += text + "_"
        
        if(number != "" and cmds.checkBox("showNumber_cb", query=True, value=True)):
            GoodName += number

        # If the name finish with an underscore, remove it
        if(GoodName.endswith("_")):
            GoodName = GoodName[:-1]
        
        # Rename the object
        finalName = ""
        finalName = cleanName(GoodName)

        if(finalName== ""):
            finalName = "NoName"
        cmds.rename(obj, finalName)
        


def cleanName(namea):
    # Replace all which is not a letter or a number with an underscore
    return ''.join(c if c.isalnum() else '_' for c in namea)



def getObjectType(obj):
    text = ""
    # Get the type of the object
    objType = cmds.objectType(obj)
    # If the type is PxrRamp 
    if objType == 'PxrRamp':
        text += 'pxrRamp'
    # If the type is PxrTexture
    elif objType == 'PxrTexture':
        text += 'pxrText'
    # If the type is PxrNormalMap
    elif objType == 'PxrNormalMap':
        text += 'pxrNorm'
    # If the type is PxrLayeredTexture
    elif objType == 'PxrLayeredTexture':
        text += 'pxrLayer'
    # If the type is PxrRemap
    elif objType == 'PxrRemap':
        text += 'pxrRemap'
    # If the type is PxrBump
    elif objType == 'PxrBump':
        text += 'pxrBump'
    # If the type is PxrDisplace
    elif objType == 'PxrDisplace':
        text += 'pxrDispl'
    # If the type is PxrDirt
    elif objType == 'PxrDirt':
        text += 'pxrDirt'
    # If the type is noise
    elif objType == 'noise':
        text += 'noise'
    # If the type is ramp
    elif objType == 'ramp':
        text += 'ramp'
    # If the type is file
    elif objType == 'file':
        text += 'file'
    # If the type is a fractal
    elif objType == 'fractal':
        text += 'fractal'
    else:
        text += objType
    return text

def getOptions():
    options = ""
    if(cmds.checkBox("vertical_cb", query=True, value=True)):
        options += "_vert"
    if(cmds.checkBox("horizontal_cb", query=True, value=True)):
        options += "_hor"
    if(cmds.checkBox("radial_cb", query=True, value=True)):
        options += "_rad"
    if(cmds.checkBox("mask_cb", query=True, value=True)):
        options += "_mask"
    if(cmds.checkBox("coloc_cb", query=True, value=True)):
        options += "_col"
    if(cmds.checkBox("dif_color_cb", query=True, value=True)):
        options += "_difCol"
    if(cmds.checkBox("specular_cb", query=True, value=True)):
        options += "_spec"
    if(cmds.checkBox("rough_cb", query=True, value=True)):
        options += "_rough"
    if(cmds.checkBox("refraction_cb", query=True, value=True)):
        options += "_refr"
    if(cmds.checkBox("reflection_cb", query=True, value=True)):
        options += "_refl"
    if(cmds.checkBox("bump_cb", query=True, value=True)):
        options += "_bump"
    if(cmds.checkBox("displacement_cb", query=True, value=True)):
        options += "_displ"
    return options


renameWindow()
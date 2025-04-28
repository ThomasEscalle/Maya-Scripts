# Litle maya script to open a rename window for the objects selected in the scene.

from distutils.log import debug
from sys import prefix
from unicodedata import name
import maya.cmds as cmds


def renameWindow():
    global RenameText
    global ObjectName
    global Prefix
    global Suffix
    

    if cmds.window('renameWindow', exists=True):
        cmds.deleteUI('renameWindow')
    cmds.window('renameWindow', title='Rename Geos', widthHeight=(250, 200), resizeToFitChildren=True)
    cmds.columnLayout()


    ### Add a text to explain the format of the name : prefix_objectName_options_text_number_suffix
    cmds.separator(h=10)
    cmds.text(label="  Format of the name:", font = "boldLabelFont" , w = 240, align = "left")
    cmds.text(label="  prefix_objectName_options_text_number_suffix", w = 240, align = "left")
    cmds.separator(h=10, style='double',w = 240)

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

    # Prefix Field in a row
    cmds.rowLayout(numberOfColumns=2, w = 240)
    cmds.text(label="  Prefix:", ann="Write the prefix you want to add to the objects selected." , w = 70, align = "left")
    Prefix = cmds.textField( w = 165 )
    cmds.setParent('..')

    # Suffix Field in a row
    cmds.rowLayout(numberOfColumns=2, w = 240)
    cmds.text(label="  Suffix:", ann="Write the suffix you want to add to the objects selected." , w = 70, align = "left")
    Suffix = cmds.textField( w = 165 )
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

    cmds.rowLayout(numberOfColumns=2, w = 240)
    cmds.checkBox("right_cb",label="Right", ann="Add the '_R' attribute to your text.", w=75)
    cmds.checkBox("left_cb",label="Left", ann="Add the '_L' attribute to your text.", w=75)
    cmds.setParent('..')

    cmds.separator(h=5)
    cmds.rowLayout(numberOfColumns=3, w = 240)
    cmds.checkBox("front_cb", label="Front", ann="Add the '_F' attribute to your text.", w=75)
    cmds.checkBox("middle_cb",label="Middle", ann="Add the '_M' attribute to your text.", w=75)
    cmds.checkBox("back_cb", label="Back", ann="Add the '_B' attribute to your text.", w=75)
    cmds.setParent('..')

    cmds.separator(h=10, style='double',w = 240)

    cmds.separator(h=20)

    # Rename button at the bottom of the window filled on width
    cmds.button(label='Rename', command='rename()', width=240, bgc=[0.1884, 0.4513, 0.1428])

    cmds.separator(h=8)

    cmds.showWindow('renameWindow')
    


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


        ### The format of the name is: prefix_objectName_options_text_number_suffix



        # Get the options
        options = getOptions()



        ## Convert the number to a string
        number = str(numberIndex)
        numberIndex += 1

        # Create the new name
        GoodName = ""

        ### Add the prefix
        if(cmds.textField(Prefix, query=True, text=True) != ""):
            GoodName += cmds.textField(Prefix, query=True, text=True) + "_"

        if(objectName != ""):
            GoodName += objectName + "_"
        
        if(options != ""):
            GoodName += options + "_"
        
        if(text != ""):
            GoodName += text + "_"
        
        if(number != "" and cmds.checkBox("showNumber_cb", query=True, value=True)):
            GoodName += number

        ### Add the suffix
        if(cmds.textField(Suffix, query=True, text=True) != ""):
            ### Check if the good name finish with an underscore
            if(GoodName.endswith("_")):
                GoodName += cmds.textField(Suffix, query=True, text=True)
            else:
                GoodName += "_" + cmds.textField(Suffix, query=True, text=True)

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



def getOptions():
    options = ""
    if(cmds.checkBox("front_cb", query=True, value=True)):
        # Check if the good name finish with an underscore
        if(options.endswith("_") or options == ""):
            options += "F"
        else:
            options += "_F"
    if(cmds.checkBox("middle_cb", query=True, value=True)):
        # Check if the good name finish with an underscore
        if(options.endswith("_") or options == ""):
            options += "M"
        else:
            options += "_M"
    if(cmds.checkBox("back_cb", query=True, value=True)):
        # Check if the good name finish with an underscore
        if(options.endswith("_") or options == ""):
            options += "B"
        else:
            options += "_B"
    if(cmds.checkBox("right_cb", query=True, value=True)):
        # Check if the good name finish with an underscore
        if(options.endswith("_") or options == ""):
            options += "R"
        else:
            options += "_R"
    if(cmds.checkBox("left_cb", query=True, value=True)):
        # Check if the good name finish with an underscore or if it's empty
        if(options.endswith("_") or options == "" ):
            options += "L"
        else:
            options += "_L"

    return options


renameWindow()
### Maya script that enable or not my lookdev scene
### This script will create a PxrDomeLight with the name "LOOKDEV_DomeLight" in Renderman

import maya.cmds as cmds

hdriPath = "<ws>/sourceimages/Env_StinsonBeach_1700PM_2k.20.tex"
hdriExposure = 0.42

def enableLookdev():
    ### Create a PxrDomeLight
    domeLight = cmds.shadingNode('PxrDomeLight', asLight=True)
    ### Rename the DomeLight to "LOOKDEV_DomeLight"
    cmds.rename(domeLight, "LOOKDEV_DomeLight")
    ### Set the Outliner color of the domeLight to yellow
    cmds.setAttr("LOOKDEV_DomeLight.useOutlinerColor", 1)
    cmds.setAttr("LOOKDEV_DomeLight.outlinerColor", 1, 1, 0)
    
    ### Set the lightColorMap to '<ws>/sourceimages/Env_StinsonBeach_1700PM_2k.20.tex'
    cmds.setAttr("LOOKDEV_DomeLight.lightColorMap", hdriPath, type="string")
    ### Set the exposure to 0.42
    cmds.setAttr("LOOKDEV_DomeLight.exposure", hdriExposure)


def run():

    ### Check if there is a LOOKDEV_DomeLight in the scene
    if cmds.objExists("LOOKDEV_DomeLight"):
        ### If there is a LOOKDEV_DomeLight in the scene, delete it
        cmds.delete("LOOKDEV_DomeLight")
    else:
        ### If there is no LOOKDEV_DomeLight in the scene, run the enableLookdev function
        enableLookdev()

run()
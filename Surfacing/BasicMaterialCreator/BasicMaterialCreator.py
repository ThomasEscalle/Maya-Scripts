### Maya script that creates a PxrSurface shader
### Create a PxrTextureNode and connect it to the PxrSurface shader in the diffuse slot


import maya.cmds as cmds
import maya.mel as mel

name = 'test'

### Create a window that ask for the name of the shader and a button to create the shader
def createWindow():
    window = cmds.window(title='Substance to PxrSurface', widthHeight=(300, 170))
    cmds.columnLayout(adjustableColumn=True)

    ### Ask for the name of the shader
    cmds.text(label='Name of the shader')
    global nameField
    nameField = cmds.textField()

    cmds.separator(height=10, style='none')

    ### Ask if we want to create a the diffuse color into a checkbox
    global diffuseColorEnabled
    diffuseColorEnabled = cmds.checkBox(label='Diffuse Color', value=True)

    ### Ask if we want to create a the roughness into a checkbox
    global roughnessEnabled
    roughnessEnabled = cmds.checkBox(label='Roughness', value=True)

    ### Ask if we want to create the bump into a checkbox
    global bumpEnabled
    bumpEnabled = cmds.checkBox(label='Bump', value=True)

    ### Ask if we want to create displacement into a checkbox
    global displacementEnabled
    displacementEnabled = cmds.checkBox(label='Displacement', value=False)




    cmds.separator(height=10, style='none')
    cmds.button(label='Create PxrSurface', command='createPxrSurface()')
    cmds.showWindow(window)




def createPxrSurface():
    ### Get the name of the shader from the text field
    name = cmds.textField(nameField, query=True, text=True)
    ### Clean the name (remove spaces and special characters)
    name = name.replace(' ', '')



    ### Create the PxrSurface shader
    shader = cmds.shadingNode('PxrSurface', asShader=True)
    ### Rename the shader to PxrS_'name'
    shader = cmds.rename(shader, 'PxrS_' + name)

    ####################
    ### DIFUSE COLOR ###
    ####################
    ### Check if the diffuse color checkbox is checked
    if cmds.checkBox(diffuseColorEnabled, query=True, value=True):
        ### Create the PxrTexture node
        texture = cmds.shadingNode('PxrTexture', asTexture=True)
        ### Set the texture's linearise to 1
        cmds.setAttr(texture + '.linearize', 1)
        ### Rename the PxrTexture node to PxrT_'name'
        texture = cmds.rename(texture, 'PxrT_' + name + '_diffColor')
        ### Connect the PxrTexture node to the PxrSurface shader
        cmds.connectAttr(texture + '.resultRGB', shader + '.diffuseColor')



    ##################
    ### ROUGHNESS  ###
    ##################
    ### Check if the roughness checkbox is checked
    if cmds.checkBox(roughnessEnabled, query=True, value=True):
        ### Create the PxrTexture node
        texture = cmds.shadingNode('PxrTexture', asTexture=True)
        ### Rename the PxrTexture node to PxrT_'name'_roughness
        texture = cmds.rename(texture, 'PxrT_' + name + '_roughness')
        ### Set the texture's linearise to 1
        cmds.setAttr(texture + '.linearize', 1)
        ### Create a PxrRemap node
        remap = cmds.shadingNode('PxrRemap', asUtility=True)
        ### Rename the PxrRemap node to PxrR_'name'_roughness
        remap = cmds.rename(remap, 'PxrR_' + name + '_roughness')
        ### Connect the PxrTexture node to the PxrRemap node
        cmds.connectAttr(texture + '.resultRGB', remap + '.inputRGB')
        ### Connect the PxrRemap node to the PxrSurface shader
        cmds.connectAttr(remap + '.resultRGBR', shader + '.specularRoughness')


    ##################
    ### SPECULAR  ###
    ##################
    ### Set the specular fresnel mode to 1
    cmds.setAttr(shader + '.specularFresnelMode', 1)
    ### Set the specularEdgeColor to white
    cmds.setAttr(shader + '.specularEdgeColor', 1, 1, 1, type='double3')
    ### Set the specular model type to 1
    cmds.setAttr(shader + '.specularModelType', 1)



    ############
    ### BUMP ###
    ############
    ### Check if the bump checkbox is checked
    if cmds.checkBox(bumpEnabled, query=True, value=True):
        ### Create the PxrTexture node
        texture = cmds.shadingNode('PxrTexture', asTexture=True)
        ### Rename the PxrTexture node to PxrT_'name'_bump
        texture = cmds.rename(texture, 'PxrT_' + name + '_bump')
        ### Set the texture's linearise to 1
        cmds.setAttr(texture + '.linearize', 1)
        ### Create a PxrRemap node
        remap = cmds.shadingNode('PxrRemap', asUtility=True)
        ### Rename the PxrRemap node to PxrR_'name'_bump
        remap = cmds.rename(remap, 'PxrR_' + name + '_bump')
        ### Create the PxrBump node
        bump = cmds.shadingNode('PxrBump', asUtility=True)
        ### Rename the PxrBump node to PxrB_'name'_bump
        bump = cmds.rename(bump, 'PxrB_' + name + '_bump')
        ### Connect the PxrTexture node to the PxrRemap node
        cmds.connectAttr(texture + '.resultRGB', remap + '.inputRGB')
        ### Connect the PxrRemap node to the PxrBump node
        cmds.connectAttr(remap + '.resultRGBR', bump + '.inputBump')
        ### Connect the PxrBump node to the PxrSurface shader
        cmds.connectAttr(bump + '.resultN', shader + '.bumpNormal')


    ###  SHADER GROUP  ###
    shaderSG = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)
    shaderSG = cmds.rename(shaderSG, 'PxrSG_' + name)
    cmds.connectAttr(shader + '.outColor', shaderSG + '.rman__surface')

    ### LAMBERT ###
    lambert = cmds.shadingNode('lambert', asShader=True)
    lambert = cmds.rename(lambert, 'lambert_' + name)
    cmds.connectAttr(lambert + '.outColor', shaderSG + '.surfaceShader')


    ####################
    ### DISPLACEMENT ###
    ####################
    ### Check if the displacement checkbox is checked
    if cmds.checkBox(displacementEnabled, query=True, value=True):
        ### Create the PxrTexture node
        texture = cmds.shadingNode('PxrTexture', asTexture=True)
        ### Rename the PxrTexture node to PxrT_'name'_displacement
        texture = cmds.rename(texture, 'PxrT_' + name + '_displacement')
        ### Set the texture's linearise to 1
        cmds.setAttr(texture + '.linearize', 1)
        ### Create a PxrRemap node
        remap = cmds.shadingNode('PxrRemap', asUtility=True)
        ### Rename the PxrRemap node to PxrR_'name'_displacement
        remap = cmds.rename(remap, 'PxrR_' + name + '_displacement')
        ### Create the PxrDispTransform node
        dispTransform = cmds.shadingNode('PxrDispTransform', asUtility=True)
        ### Rename the PxrDispTransform node to PxrDT_'name'_displacement
        dispTransform = cmds.rename(dispTransform, 'PxrDT_' + name + '_displacement')
        ### Create the PxrDisplace node
        displace = cmds.shadingNode('PxrDisplace', asUtility=True)
        ### Rename the PxrDisplace node to PxrD_'name'_displacement
        displace = cmds.rename(displace, 'PxrD_' + name + '_displacement')
        ### Connect the PxrTexture node to the PxrRemap node
        cmds.connectAttr(texture + '.resultRGB', remap + '.inputRGB')
        ### Connect the PxrRemap node to the PxrDispTransform node
        cmds.connectAttr(remap + '.resultRGBR', dispTransform + '.dispScalar')
        ### Connect the PxrDispTransform node to the PxrDisplace node
        cmds.connectAttr(dispTransform + '.resultF', displace + '.dispScalar')
        ### Connect the PxrDisplace node to the shading group
        cmds.connectAttr(displace + '.outColor', shaderSG + '.rman__displacement')





createWindow()
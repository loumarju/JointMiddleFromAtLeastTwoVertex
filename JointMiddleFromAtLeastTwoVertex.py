import maya.cmds as cmds

# Get the current selection
selVert = cmds.ls(selection=True, flatten=True)

# Check if there are at least two vertices selected
if len(selVert) < 2:
    cmds.warning('Please select at least two vertices.')
else:
    # Create a cluster
    cl = cmds.cluster(selVert, rel=True, en=True)

    # Get the position of the cluster
    cl_pos = cmds.xform(cl, query=True, worldSpace=True, rotatePivot=True)

    # Create a world joint at the cluster position
    cmds.select(clear=True)
    jnt = cmds.joint(p=cl_pos)

    # Delete the cluster
    cmds.delete(cl)

    # Select the joint
    cmds.select(clear=True)
    cmds.select(jnt)

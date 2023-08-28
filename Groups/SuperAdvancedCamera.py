import bpy
from bpy.types import NodeTree
from .. import SID_Settings
from .Colorgrading import (
    create_temperature_group,
    create_tint_group
)
def create_main_group() -> NodeTree:

    # Create the group
    sac_group: NodeTree = bpy.data.node_groups.new(name="Super Advanced Camera (2)",type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_group.nodes.new("NodeGroupInput")
    output_node = sac_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_group.inputs.new("NodeSocketColor","Image")
    sac_group.outputs.new("NodeSocketColor","Image")

    # Create the nodes
    # Temperature
    sac_temperature_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_temperature_group.node_tree = create_temperature_group()
    # Tint
    sac_tint_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_tint_group.node_tree = create_tint_group()

    # Create the links
    # link the input node to the temperature node
    sac_group.links.new(input_node.outputs[0], sac_temperature_group.inputs[0])
    # link the temperature node to the tint node
    sac_group.links.new(sac_temperature_group.outputs[0], sac_tint_group.inputs[0])

    # return
    return(sac_group)
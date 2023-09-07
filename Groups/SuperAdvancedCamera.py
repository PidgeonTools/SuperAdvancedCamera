# ##### BEGIN GPL LICENSE BLOCK #####
#
#  <Adds plenty of new features to Blenders camera and compositor>
#    Copyright (C) <2023>  <Kevin Lorengel>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#  Alternatively, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.types import NodeTree

from .Colorgrading.WhiteLevel import create_whitelevel_group
from .Colorgrading.Temperature import create_temperature_group
from .Colorgrading.Tint import create_tint_group
from .Colorgrading.Saturation import create_saturation_group
from .Colorgrading.Exposure import create_exposure_group
from .Colorgrading.Contrast import create_contrast_group
from .Colorgrading.Highlights import create_highlights_group
from .Colorgrading.Shadows import create_shadows_group
from .Colorgrading.Whites import create_whites_group
from .Colorgrading.Darks import create_darks_group
from .Colorgrading.Sharpen import create_sharpen_group
from .Colorgrading.Vibrance import create_vibrance_group
from .Colorgrading.HighlightTint import create_highlighttint_group
from .Colorgrading.ShadowTint import create_shadowtint_group
from .Colorgrading.Curves import create_curves_group
from .Colorgrading.Colorwheels import create_colorwheel_group
from .Effects.Duotone import create_duotone_group
from .Effects.FogGlow import create_fogglow_group
from .Effects.Streaks import create_streaks_group
from .Effects.Ghost import create_ghost_group
from .Effects.Emboss import create_emboss_group
from .Effects.Posterize import create_posterize_group
from .Effects.Overlay import create_overlay_group
from .Effects.Pixelate import create_pixelate_group
from .Effects.ChromaticAberration import create_chromatic_group
from .Effects.Viginette import create_viginette_group
from .Effects.Infrared import create_infrared_group
from .Effects.Negative import create_negative_group
from .Effects.Warp import create_warp_group
from .Effects.Fisheye import create_fisheye_group
from .Effects.PerspectiveShift import create_perspectiveshift_group
from .Effects.ISO import create_iso_group
from .Effects.FilmGrain import create_filmgrain_group
from .Effects.Halftone import create_halftone_group
from .Effects.GradientMap import create_gradientmap_group


def create_main_group() -> NodeTree:

    # Delete the group if it already exists
    try:
        if bpy.data.node_groups["Super Advanced Camera"]:
            bpy.data.node_groups.remove(bpy.data.node_groups["Super Advanced Camera"])
    except:
        pass

    # Create the group
    sac_group: NodeTree = bpy.data.node_groups.new(name="Super Advanced Camera", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_group.nodes.new("NodeGroupInput")
    output_node = sac_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_group.inputs.new("NodeSocketColor", "Image")
    sac_group.outputs.new("NodeSocketColor", "Image")

    def create_and_link_colorgrade_group(sac_group, previous_node, node_name, node_key, creation_function, *args):
        new_group = sac_group.nodes.new("CompositorNodeGroup")
        try:
            if bpy.data.node_groups[node_key]:
                new_group.node_tree = bpy.data.node_groups[node_key]
        except:
            new_group.node_tree = creation_function(*args)
        new_group.name = node_name
        new_group.mute = True

        sac_group.links.new(previous_node.outputs[0], new_group.inputs[0])
        return new_group

    # Create and link groups
    node_configurations = [
        ("SAC WhiteLevel", ".SAC WhiteLevel", create_whitelevel_group),
        ("SAC Temperature", ".SAC Temperature", create_temperature_group),
        ("SAC Tint", ".SAC Tint", create_tint_group),
        ("SAC Saturation", ".SAC Saturation", create_saturation_group, "SAC Colorgrade_Color_Saturation", ".SAC Saturation"),
        ("SAC Exposure", ".SAC Exposure", create_exposure_group),
        ("SAC Contrast", ".SAC Contrast", create_contrast_group),
        ("SAC Highlights", ".SAC Highlights", create_highlights_group),
        ("SAC Shadows", ".SAC Shadows", create_shadows_group),
        ("SAC Whites", ".SAC Whites", create_whites_group),
        ("SAC Darks", ".SAC Darks", create_darks_group),
        ("SAC Sharpen", ".SAC Sharpen", create_sharpen_group),
        ("SAC Vibrance", ".SAC Vibrance", create_vibrance_group),
        ("SAC Saturation2", ".SAC Saturation2", create_saturation_group, "SAC Colorgrade_Presets_Saturation", ".SAC Saturation2"),
        ("SAC HighlightTint", ".SAC HighlightTint", create_highlighttint_group),
        ("SAC ShadowTint", ".SAC ShadowTint", create_shadowtint_group),
        ("SAC Curves", ".SAC Curves", create_curves_group),
        ("SAC Colorwheel", ".SAC Colorwheel", create_colorwheel_group)
    ]

    previous_node = input_node
    for node_name, node_key, creation_function, *args in node_configurations:
        previous_node = create_and_link_colorgrade_group(sac_group, previous_node, node_name, node_key, creation_function, *args)

    # Effects

    # Delete the group tree if it already exists
    try:
        if bpy.data.node_groups[".SAC Effects"]:
            bpy.data.node_groups.remove(bpy.data.node_groups[".SAC Effects"])
    except:
        pass

    # Create the group
    effects_node = sac_group.nodes.new("CompositorNodeGroup")
    effects_group: NodeTree = bpy.data.node_groups.new(name=".SAC Effects", type="CompositorNodeTree")
    effects_node.node_tree = effects_group

    # Create the input and output nodes
    effects_input_node = effects_group.nodes.new("NodeGroupInput")
    effects_output_node = effects_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    effects_group.inputs.new("NodeSocketColor", "Image")
    effects_group.outputs.new("NodeSocketColor", "Image")

    sac_group.links.new(previous_node.outputs[0], effects_node.inputs[0])

    def create_and_link_group(effects_group, previous_node, node_name, creation_function, unique_id):
        new_group = effects_group.nodes.new("CompositorNodeGroup")
        try:
            if bpy.data.node_groups[f".{node_name}_{unique_id}"]:
                new_group.node_tree = bpy.data.node_groups[f".{node_name}_{unique_id}"]
        except:
            new_group.node_tree = creation_function()

        # Rename the node_tree to include the unique_id
        new_group.node_tree.name = f".{node_name}_{unique_id}"

        new_group.name = f"{node_name}_{unique_id}"

        effects_group.links.new(previous_node.outputs[0], new_group.inputs[0])
        return new_group

    node_mapping = {
        "SAC_CHROMATICABERRATION": create_chromatic_group,
        "SAC_DUOTONE": create_duotone_group,
        "SAC_EMBOSS": create_emboss_group,
        "SAC_FILMGRAIN": create_filmgrain_group,
        "SAC_FISHEYE": create_fisheye_group,
        "SAC_FOGGLOW": create_fogglow_group,
        "SAC_GHOST": create_ghost_group,
        "SAC_GRADIENTMAP": create_gradientmap_group,
        "SAC_HALFTONE": create_halftone_group,
        "SAC_INFRARED": create_infrared_group,
        "SAC_ISONOISE": create_iso_group,
        "SAC_NEGATIVE": create_negative_group,
        "SAC_OVERLAY": create_overlay_group,
        "SAC_PERSPECTIVESHIFT": create_perspectiveshift_group,
        "SAC_MOSAIC": create_pixelate_group,
        "SAC_POSTERIZE": create_posterize_group,
        "SAC_STREAKS": create_streaks_group,
        "SAC_VIGNETTE": create_viginette_group,
        "SAC_WARP": create_warp_group,
    }

    effect_array = []

    for item in bpy.context.scene.sac_effect_list:
        # add (effect, unique_id) to the effect_array
        effect_array.append((item.EffectGroup, item.ID))

    previous_node = effects_input_node
    for effect, unique_id in effect_array:
        creation_function = node_mapping.get(effect)
        if creation_function:
            previous_node = create_and_link_group(effects_group, previous_node, effect, creation_function, unique_id)

    for item in bpy.context.scene.sac_effect_list:
        # set the mute stage of the node based on the mute property
        effects_group.nodes[f"{item.EffectGroup}_{item.ID}"].mute = item.mute

    # Create the links
    effects_group.links.new(previous_node.outputs[0], effects_output_node.inputs[0])

    # link the effects node to the output node
    sac_group.links.new(effects_node.outputs[0], output_node.inputs[0])

    # return
    return (sac_group)


def connect_renderLayer_node():
    # Make sure the compositor is enabled for the active scene
    bpy.context.scene.use_nodes = True
    # bpy.context.space_data.shading.use_compositor = 'ALWAYS'
    tree = bpy.context.scene.node_tree

    # Loop through all nodes to find Render Layer nodes
    render_layer_nodes = [node for node in tree.nodes if node.type == 'R_LAYERS']
    super_denoiser_nodes = [node for node in tree.nodes if node.name == 'sid_node']

    # Exit if no Render Layer nodes are found
    if not render_layer_nodes:
        print("No Render Layer nodes found.")
        return

    # Process each Render Layer node
    for render_layer_node in render_layer_nodes:
        # Check if SuperImageDenoiser is connected to this Render Layer node
        connect_to_node = render_layer_node
        for link in tree.links:
            if link.from_node == render_layer_node and link.to_node in super_denoiser_nodes:
                connect_to_node = link.to_node
                break
        # Check if Super Advanced Camera node exists in the compositor, if it does, update the node tree, if not, create it
        sac_node = None
        for node in tree.nodes:
            if node.name == "Super Advanced Camera":
                sac_node = node
                break
        if not sac_node:
            sac_node = tree.nodes.new("CompositorNodeGroup")
            sac_node.name = "Super Advanced Camera"
            sac_node.node_tree = create_main_group()
            sac_node.location = (render_layer_node.location.x + 300, render_layer_node.location.y)
            tree.links.new(connect_to_node.outputs[0], sac_node.inputs[0])
            tree.links.new(sac_node.outputs[0], tree.nodes["Composite"].inputs[0])
        else:
            sac_node.node_tree = create_main_group()

        # Collect links to be rerouted
        to_disconnect = []
        to_connect = []
        for link in tree.links:
            if link.from_node == connect_to_node:
                # Save the links to be disconnected
                to_disconnect.append(link)

                # Save the information needed to make new connections
                to_connect.append((sac_node.outputs[0], link.to_socket, connect_to_node.outputs[link.from_socket.name]))

        # Disconnect the original links
        for link in to_disconnect:
            tree.links.remove(link)

        # Make new connections
        for mix_output, to_socket, from_socket in to_connect:
            # Connect the mix node to where the connect_to_node was connected
            tree.links.new(mix_output, to_socket)

            # Connect the connect_to_node to the mix node
            tree.links.new(from_socket, sac_node.inputs[0])

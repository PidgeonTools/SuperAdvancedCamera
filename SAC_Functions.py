import bpy


def link_nodes(node_tree, node1, node1_output, node2, node2_input):
    node_tree.links.new(node1.outputs[node1_output], node2.inputs[node2_input])


def load_image_once(image_path, image_name):
    image = bpy.data.images.get(image_name)
    if image is None:
        image = bpy.data.images.load(image_path)
    return image


def create_dot_texture():
    texture = bpy.data.textures.get(".SAC Dot Screen")
    if texture is None:
        texture = bpy.data.textures.new(name=".SAC Dot Screen", type='MAGIC')
    texture.noise_depth = 1  # Depth
    texture.turbulence = 6.0  # Turbulence
    texture.use_color_ramp = True
    texture.color_ramp.interpolation = 'CONSTANT'
    texture.color_ramp.elements[1].position = 0.65


def active_effect_update(self, context):
    settings = context.scene.sac_settings
    item = context.scene.sac_effect_list[self.sac_effect_list_index]
    node_name = f"{item.EffectGroup}_{item.ID}"
    node_group_name = f".{node_name}"
    # Bokeh
    if item.EffectGroup == "SAC_BOKEH":
        settings.Effects_Bokeh_MaxSize = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Blur"].blur_max
        settings.Effects_Bokeh_Range = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Range"].inputs[1].default_value
        settings.Effects_Bokeh_Offset = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Offset"].inputs[1].default_value
        settings.Effects_Bokeh_Rotation = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Rotation"].inputs[1].default_value
        settings.Effects_Bokeh_Procedural_Flaps = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Procedural"].flaps
        settings.Effects_Bokeh_Procedural_Angle = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Procedural"].angle
        settings.Effects_Bokeh_Procedural_Rounding = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Procedural"].rounding
        settings.Effects_Bokeh_Procedural_Catadioptric = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Procedural"].catadioptric
        settings.Effects_Bokeh_Procedural_Shift = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Procedural"].shift

        if bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Switch"].check == True:
            settings.Effects_Bokeh_Type = "PROCEDURAL"
        else:
            if bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_ImageSwitch"].check == True:
                settings.Effects_Bokeh_Type = "CUSTOM"
            else:
                settings.Effects_Bokeh_Type = "CAMERA"

    # Chromatic Aberration
    elif item.EffectGroup == "SAC_CHROMATICABERRATION":
        settings.Effects_ChromaticAberration_Amount = bpy.data.node_groups[node_group_name].nodes["SAC Effects_ChromaticAberration"].inputs[2].default_value
    # Duotone
    elif item.EffectGroup == "SAC_DUOTONE":
        # Color 1
        settings.Effects_Duotone_Color1[0] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[0]
        settings.Effects_Duotone_Color1[1] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[1]
        settings.Effects_Duotone_Color1[2] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[2]
        # Color 2
        settings.Effects_Duotone_Color2[0] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[0]
        settings.Effects_Duotone_Color2[1] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[1]
        settings.Effects_Duotone_Color2[2] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[2]
        # Blend
        settings.Effects_Duotone_Blend = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Blend"].inputs[0].default_value
    # Emboss
    elif item.EffectGroup == "SAC_EMBOSS":
        settings.Effects_Emboss_Strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Emboss"].inputs[0].default_value
    # Film Grain
    elif item.EffectGroup == "SAC_FILMGRAIN":
        settings.Filmgrain_strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FilmGrain_Strength"].inputs[0].default_value
        settings.Filmgrain_dustproportion = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FilmGrain_Blur"].sigma_color
        settings.Filmgrain_size = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FilmGrain_Blur"].iterations
    # Fish Eye
    elif item.EffectGroup == "SAC_FISHEYE":
        settings.Effects_Fisheye = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Fisheye"].inputs[1].default_value
    # Fog Glow
    elif item.EffectGroup == "SAC_FOGGLOW":
        settings.Effects_FogGlow_Strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FogGlowStrength"].inputs[0].default_value
        settings.Effects_FogGlow_Threshold = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FogGlow"].threshold
        settings.Effects_FogGlow_Size = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FogGlow"].size
    # Ghost
    elif item.EffectGroup == "SAC_GHOST":
        settings.Effects_Ghosts_Strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_GhostsStrength"].inputs[0].default_value
        settings.Effects_Ghosts_Threshold = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Ghosts"].threshold
        settings.Effects_Ghosts_Count = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Ghosts"].iterations
        settings.Effects_Ghosts_Distortion = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Ghosts"].color_modulation
    # Gradient Map
    elif item.EffectGroup == "SAC_GRADIENTMAP":
        settings.Effects_GradientMap_blend = bpy.data.node_groups[node_group_name].nodes["SAC Effects_GradientMap_Mix"].inputs[0].default_value
    # Halftone
    elif item.EffectGroup == "SAC_HALFTONE":
        settings.Effects_Halftone_value = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_Value"].outputs[0].default_value
        settings.Effects_Halftone_delta = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_Delta"].outputs[0].default_value
        settings.Effects_Halftone_size = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_SizeSave"].outputs[0].default_value
    # Infrared
    elif item.EffectGroup == "SAC_INFRARED":
        settings.Effects_Infrared_Blend = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Infrared_Mix"].inputs[0].default_value
        settings.Effects_Infrared_Offset = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Infrared_Add"].inputs[1].default_value
    # ISO Noise
    elif item.EffectGroup == "SAC_ISONOISE":
        settings.ISO_strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_ISO_Add"].inputs[0].default_value
        settings.ISO_size = bpy.data.node_groups[node_group_name].nodes["SAC Effects_ISO_Despeckle"].inputs[0].default_value
    # Mosaic
    elif item.EffectGroup == "SAC_MOSAIC":
        settings.Effects_Pixelate_PixelSize = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Pixelate_Size"].inputs[0].default_value
    # Negative
    elif item.EffectGroup == "SAC_NEGATIVE":
        settings.Effects_Negative = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Negative"].inputs[0].default_value
    # Overlay
    elif item.EffectGroup == "SAC_OVERLAY":
        settings.Effects_Overlay_Strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Overlay"].inputs[0].default_value
    # Perspective Shift
    elif item.EffectGroup == "SAC_PERSPECTIVESHIFT":
        if bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[1].default_value[0] > 0:
            settings.Effects_PerspectiveShift_Horizontal = bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[1].default_value[0] * 2
        else:
            settings.Effects_PerspectiveShift_Horizontal = -bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[3].default_value[0] * 2

        if bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[3].default_value[1] > 0:
            settings.Effects_PerspectiveShift_Vertical = bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[3].default_value[1] * 2
        else:
            settings.Effects_PerspectiveShift_Vertical = -bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[4].default_value[1] * 2
    # Posterize
    elif item.EffectGroup == "SAC_POSTERIZE":
        settings.Effects_Posterize_Steps = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Posterize"].inputs[1].default_value
    # Streaks
    elif item.EffectGroup == "SAC_STREAKS":
        settings.Effects_Streaks_Strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_StreaksStrength"].inputs[0].default_value
        settings.Effects_Streaks_Threshold = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].threshold
        settings.Effects_Streaks_Count = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].streaks
        settings.Effects_Streaks_Length = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].iterations
        settings.Effects_Streaks_Fade = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].fade
        settings.Effects_Streaks_Angle = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].angle_offset
        settings.Effects_Streaks_Distortion = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].color_modulation
    # Vignette
    elif item.EffectGroup == "SAC_VIGNETTE":
        settings.Effects_Vignette_Intensity = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Intensity"].inputs[0].default_value
        settings.Effects_Vignette_Roundness = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Roundness"].inputs[0].default_value
        settings.Effects_Vignette_Feather = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Directional_Blur"].zoom
        settings.Effects_Vignette_Midpoint = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Midpoint"].inputs[0].default_value
    # Warp
    elif item.EffectGroup == "SAC_WARP":
        settings.Effects_Warp = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Warp"].zoom

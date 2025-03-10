import bpy
all_materials = bpy.data.materials

for material in all_materials:
    color = material.diffuse_color
    print(color)
    material.use_nodes = True
    node_tree = material.node_tree
    for node in node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            node_tree.nodes.remove(node)
    RGB = node_tree.nodes.new('ShaderNodeRGB')
    RGB.outputs['Color'].default_value = color
    node_tree.links.new(node_tree.nodes["Material Output"].inputs[0], RGB.outputs['Color'])
import bpy
d = bpy.context.active_object.data.archipack_floor[0]
d.add_grout = True
d.bevel = True
d.bevel_amount = 0.0015
d.board_length = 2.0
d.board_width = 0.2
d.boards_in_group = 5
d.length_spacing = 0.002
d.length_variance = 50
d.matid = 7
d.max_boards = 20
d.mortar_depth = 0.0015
d.offset = 0.0
d.offset_variance = 50
d.pattern = 'hexagon'
d.random_offset = False
d.random_uvs = True
d.short_board_length = 0.15
d.spacing = 0.005
d.thickness = 0.1
d.thickness_variance = 25.0
d.tile_length = 0.3
d.tile_width = 0.1
d.vary_length = False
d.vary_materials = False
d.vary_thickness = False
d.vary_width = False
d.width_spacing = 0.002
d.width_variance = 50.0

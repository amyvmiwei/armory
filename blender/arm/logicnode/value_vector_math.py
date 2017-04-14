import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class VectorMathNode(Node, ArmLogicTreeNode):
    '''Vector math node'''
    bl_idname = 'LNVectorMathNode'
    bl_label = 'Vector Math'
    bl_icon = 'CURVE_PATH'
    property0 = EnumProperty(
        items = [('Add', 'Add', 'Add'),
                 ('Dot Product', 'Dot Product', 'Dot Product'),
                 ('Multiply', 'Multiply', 'Multiply'),
                 ('Normalize', 'Normalize', 'Normalize')],
        name='', default='Add')
    
    def init(self, context):
        self.inputs.new('NodeSocketVector', 'Vector')
        self.inputs.new('NodeSocketVector', 'Vector')
        self.outputs.new('NodeSocketVector', 'Vector')
        self.outputs.new('NodeSocketFloat', 'Value')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

add_node(VectorMathNode, category='Value')

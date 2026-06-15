import bpy


def draw_settings(layout, prefs):
    layout.prop(prefs, "blendermcp_port")
    layout.prop(prefs, "blendermcp_autostart")


class BlenderMCPPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    blendermcp_port: bpy.props.IntProperty(
        name="Port",
        description="Port for the BlenderMCP server",
        default=9876,
        min=1024,
        max=65535,
    )
    blendermcp_autostart: bpy.props.BoolProperty(
        name="Auto-connect on Blender launch",
        description="Start the MCP server automatically when the addon loads",
        default=True,
    )

    def draw(self, context):
        draw_settings(self.layout, self)

import bpy

from . import state
from .common import get_prefs
from .server import BlenderMCPServer


class BLENDERMCP_OT_StartServer(bpy.types.Operator):
    bl_idname = "blendermcp.start_server"
    bl_label = "Connect to Claude"
    bl_description = "Start the BlenderMCP server to connect with Claude"

    def execute(self, context):
        if state.server is None:
            state.server = BlenderMCPServer(port=get_prefs().blendermcp_port)
        state.server.start()
        return {'FINISHED'}


class BLENDERMCP_OT_StopServer(bpy.types.Operator):
    bl_idname = "blendermcp.stop_server"
    bl_label = "Stop the connection to Claude"
    bl_description = "Stop the connection to Claude"

    def execute(self, context):
        if state.server is not None:
            state.server.stop()
            state.server = None
        return {'FINISHED'}

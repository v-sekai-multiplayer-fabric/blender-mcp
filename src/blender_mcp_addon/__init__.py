"""Blender MCP addon — connects Blender to Claude via the Model Context Protocol.

Originally created by Siddharth Ahuja (https://github.com/ahujasid/blender-mcp).
Forked and maintained by K. S. Ernest (iFire) Lee.
"""

import bpy

from . import state
from .operators import (
    BLENDERMCP_OT_SetFreeTrialHyper3DAPIKey,
    BLENDERMCP_OT_StartServer,
    BLENDERMCP_OT_StopServer,
)
from .panel import BLENDERMCP_PT_Panel
from .preferences import BlenderMCPPreferences
from .server import BlenderMCPServer

# Legacy bl_info for Blender 3.x/4.0/4.1 installs that pre-date the manifest.
# Blender 4.2+ reads blender_manifest.toml instead and ignores this dict.
bl_info = {
    "name": "Blender MCP",
    "author": "BlenderMCP",
    "version": (2, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > BlenderMCP",
    "description": "Connect Blender to Claude via MCP",
    "category": "Interface",
}

_CLASSES = (
    BlenderMCPPreferences,
    BLENDERMCP_PT_Panel,
    BLENDERMCP_OT_SetFreeTrialHyper3DAPIKey,
    BLENDERMCP_OT_StartServer,
    BLENDERMCP_OT_StopServer,
)


def _autostart():
    try:
        prefs = bpy.context.preferences.addons[__package__].preferences
    except (KeyError, AttributeError):
        return None
    if not prefs.blendermcp_autostart:
        return None
    if state.server is None:
        state.server = BlenderMCPServer(port=prefs.blendermcp_port)
    state.server.start()
    return None


def register():
    for cls in _CLASSES:
        bpy.utils.register_class(cls)
    bpy.app.timers.register(_autostart, first_interval=0.5)
    print("BlenderMCP addon registered")


def unregister():
    if state.server is not None:
        state.server.stop()
        state.server = None

    for cls in reversed(_CLASSES):
        bpy.utils.unregister_class(cls)

    print("BlenderMCP addon unregistered")

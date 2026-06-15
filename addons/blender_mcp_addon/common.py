import bpy
import requests

REQ_HEADERS = requests.utils.default_headers()
REQ_HEADERS.update({"User-Agent": "blender-mcp"})


def get_prefs():
    return bpy.context.preferences.addons[__package__].preferences

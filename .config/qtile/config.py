
#   ▄▄█▀▀██▄                               ▀███▀▀▀██▄ ▀███▀▀▀███
# ▄██▀    ▀██▄                               ██    ▀██▄ ██    ▀█
# ██▀      ▀██ ▄█▀██▄ ▀██▀   ▀██▀███  ▀███   ██     ▀██ ██   █
# ██        ████   ██   ██   ▄█   ██    ██   ██      ██ ██████
# ██▄      ▄██ ▄█████    ██ ▄█    ██    ██   ██     ▄██ ██   █  ▄
# ▀██▄    ▄██▀██   ██     ███     ██    ██   ██    ▄██▀ ██     ▄█
#   ▀▀████▀▀  ▀████▀██▄   ▄█      ▀████▀███▄████████▀ ▄██████████
#       ███             ▄█
#        ▀████▀       ██▀

# Qtile config for Jahns Michael's desktop.

# Inpired by Ayu Colorschemes https://github.com/ayu-theme/ayu-colors.

from typing import List  # noqa: F401

from libqtile import hook

from lib.scripts import xrandr, get_monitors
from lib.screens import get_screens
from lib.keys import get_keys
from lib.groups import get_groups
from lib.layouts import get_floating_layout, get_layouts
from lib.mouse import get_mouse
from lib.const import colors, fonts

import os
import subprocess


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/lib/scripts/autostart')
    subprocess.call([home])
    xrandr()


groups = get_groups()
keys = get_keys()
layouts = get_layouts()

widget_defaults = dict(
    font=fonts.MAIN,
    fontsize=10,
    # background=colors.common["bg"]
)
extension_defaults = widget_defaults.copy()
screens = get_screens()


@hook.subscribe.startup
def every_start():
    xrandr()


# Drag floating layouts.
mouse = get_mouse()

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = get_floating_layout()
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

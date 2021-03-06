# Qtile config for Jahns Michael's desktop.

from typing import List  # noqa: F401

from libqtile import hook, qtile
from libqtile.log_utils import logger

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

# @hook.subscribe.float_change
# def float_change():
    # try:
        # if qtile.current_window.floating:
            # qtile.config.follow_mouse_focus = False
            # qtile.config.cursor_warp = False
        # else:
            # qtile.config.follow_mouse_focus = True
            # qtile.config.cursor_warp = True
    # except AttributeError:
        # pass

@hook.subscribe.focus_change
def focus_change():
    # turn off follow_mouse_focus if float
    # try:
        # if qtile.current_window.floating:
            # qtile.config.follow_mouse_focus = False
            # qtile.config.cursor_warp = False
        # else:
            # qtile.config.follow_mouse_focus = True
            # qtile.config.cursor_warp = True
    # except AttributeError:
        # pass

    # pinned windows
    if not getattr(qtile.config, "pinned", False):
        return

    pinned = qtile.config.pinned
    screen = qtile.current_screen.index

    if screen not in pinned.keys():
        return

    for window in pinned[screen]:
        window.toscreen(screen)
        window.cmd_bring_to_front()

@hook.subscribe.client_killed
def client_killed(killed_window):
    # remove from pinned windows
    if not getattr(qtile.config, "pinned_windows", False):
        return

    if killed_window in qtile.config.pinned_windows:
        qtile.config.pinned_windows.remove(killed_window)


# Drag floating layouts.
mouse = get_mouse()

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = get_floating_layout()
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

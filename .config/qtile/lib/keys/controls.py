from libqtile.config import Key
from libqtile.lazy import lazy

def toggle_cursor_warp(qtile):
    qtile.config.cursor_warp = not qtile.config.cursor_warp
    qtile.cmd_spawn(f'notify-send "Qtile Config" "cursor_warp set to {qtile.config.cursor_warp}"', shell=True)

def toggle_follow_mouse_focus(qtile):
    qtile.config.follow_mouse_focus = not qtile.config.follow_mouse_focus
    qtile.cmd_spawn(f'notify-send "Qtile Config" "follow_mouse_focus set to {qtile.config.follow_mouse_focus}"', shell=True)

def resize_layout_margin(qtile, amount):
    if qtile.current_layout.margin + amount >= 0:
       qtile.current_layout.margin += amount

CONTROL_KEYS = [
    Key(["control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key(["control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(["control"], "l", lazy.spawn(["betterlockscreen", "-l"]),
        desc="Lock Screen with betterlockscreen"),
    Key(["control"], "s", lazy.spawn(["betterlockscreen", "-s"]),
        desc="Suspend with betterlockscreen"),
    Key(["control"], "Home", lazy.hide_show_bar(position="top"),
        desc="Toggle top bar"),
    Key(["control"], "End", lazy.hide_show_bar(position="bottom"),
        desc="Toggle bottom bar"),
    Key(["control"], "equal", lazy.function(toggle_cursor_warp),
        desc="Toggle bottom cursor warp"),
    Key(["control"], "minus", lazy.function(toggle_follow_mouse_focus),
        desc="Toggle bottom follow_mouse_focus"),
    Key([], "equal", lazy.function(resize_layout_margin, 3),
        desc="Increase layout margin"),
    Key([], "minus", lazy.function(resize_layout_margin, -3),
        desc="Decrease layout margin"),
    Key([], "BackSpace", lazy.spawn("dunstctl close"),
        desc="Close the last notification"),
    Key(["control"], "BackSpace", lazy.spawn("dunstctl close-all"),
        desc="Close all notifications"),
    Key(["mod1"], "BackSpace", lazy.spawn("dunstctl history-pop"),
        desc="Pop one notification from history"),
    # Key(["shift"], "BackSpace", lazy.spawn("dunstctl context"),
        # desc="Open notification context menu"),
]

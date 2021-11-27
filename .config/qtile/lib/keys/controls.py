from libqtile.config import Key
from libqtile.lazy import lazy


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
    Key([], "BackSpace", lazy.spawn("dunstctl close"),
        desc="Close the last notification"),
    Key(["control"], "BackSpace", lazy.spawn("dunstctl close-all"),
        desc="Close all notifications"),
    Key(["mod1"], "BackSpace", lazy.spawn("dunstctl history-pop"),
        desc="Pop one notification from history"),
    # Key(["shift"], "BackSpace", lazy.spawn("dunstctl context"),
        # desc="Open notification context menu"),
]

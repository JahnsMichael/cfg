from libqtile.config import Key
from libqtile.lazy import lazy

SCREEN_KEYS = [
    Key(["control"], "Left", lazy.next_screen(),
        desc="Move Focus to next screen"),
    Key(["control"], "Right", lazy.prev_screen(),
        desc="Move Focus to next screen"),
]
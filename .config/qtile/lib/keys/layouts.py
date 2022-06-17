from libqtile.config import Key
from libqtile.lazy import lazy

LAYOUT_KEYS = [
    Key(["mod1"], "Return", lazy.next_layout(), desc="Toggle between layouts"),
]

from libqtile.config import Key
from libqtile.lazy import lazy

LAYOUT_KEYS = [
    Key(["shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
]
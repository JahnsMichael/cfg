from libqtile.config import Key
from libqtile.lazy import lazy

VIM_DICT = {
    "Left": "h",
    "Right": "l",
    "Down": "j",
    "Up": "k",
}

WINDOW_FOCUS_KEYS = [
    *[
        Key([], direction, getattr(lazy.layout, direction.lower())(),
            desc=f"Move focus to {direction.lower()}" ) 
        for direction in ["Left", "Right", "Up", "Down"]
    ],
    *[
        Key([], VIM_DICT[direction], getattr(lazy.layout, direction.lower())(),
            desc=f"Move focus to {direction.lower()}" ) 
        for direction in ["Left", "Right", "Up", "Down"]
    ],
    Key([], "Next", lazy.group.next_window(), desc="Move focus to next window"),
    Key([], "Prior", lazy.group.prev_window(), desc="Move focus to previous window"),
]

def grow(qtile, direction):
    if direction not in ["Left", "Right", "Up", "Down"] :
        pass
    if qtile.current_window.floating:
        x_y_direction = {
            "Left": (-15,0),
            "Right": (15,0),
            "Up": (0,-15),
            "Down": (0,15),
        }
        qtile.current_window.cmd_resize_floating(*x_y_direction[direction])
    else :
        getattr(qtile.current_layout, f"cmd_grow_{direction.lower()}")()

WINDOW_SIZE_KEYS = [
    *[
        Key(["shift"], direction, lazy.function(grow, direction),
            desc=f"Grow window to the {direction.lower()}" ) 
        for direction in ["Left", "Right", "Up", "Down"]
    ],
    *[
        Key(["shift"], VIM_DICT[direction], lazy.function(grow, direction),
            desc=f"Grow window to the {direction.lower()}" ) 
        for direction in ["Left", "Right", "Up", "Down"]
    ],
    Key([], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    Key(["mod1"], "Return", lazy.window.toggle_maximize(),
        desc="Toggle maximize window"),
]

def move(qtile, direction):
    if direction not in ["Left", "Right", "Up", "Down"] :
        pass
    if qtile.current_window.floating:
        x_y_direction = {
            "Left": (-15,0),
            "Right": (15,0),
            "Up": (0,-15),
            "Down": (0,15),
        }
        qtile.current_window.cmd_move_floating(*x_y_direction[direction])
    else :
        getattr(qtile.current_layout, f"cmd_shuffle_{direction.lower()}")()

WINDOW_MOVE_KEYS = [
    *[
        Key(["mod1"], direction, lazy.function(move, direction),
            desc=f"Move window to the {direction.lower()}" ) 
        for direction in ["Left", "Right", "Up", "Down"]
    ],
    *[
        Key(["mod1"], VIM_DICT[direction], lazy.function(move, direction),
            desc=f"Move window to the {direction.lower()}" ) 
        for direction in ["Left", "Right", "Up", "Down"]
    ],
    *[
        Key(["mod1", "shift"], direction, 
            getattr(lazy.layout, f"swap_column_{direction.lower()}")(),
            desc=f"Swap column {direction.lower()}" ) 
        for direction in ["Left", "Right"]
    ],
    *[
        Key(["mod1", "shift"], VIM_DICT[direction], 
            getattr(lazy.layout, f"swap_column_{direction.lower()}")(),
            desc=f"Swap column {direction.lower()}" ) 
        for direction in ["Left", "Right"]
    ],
    Key(["shift"], "backslash", lazy.layout.toggle_split()),
]

WINDOW_TOGGLE_FLOATING_KEYS = [
    Key(["shift"], "f", lazy.window.toggle_floating(),
        desc="Toggle floating"),
]

WINDOW_KILL_KEYS = [
    Key([], "c", lazy.window.kill(), desc="Kill focused window"),
]

WINDOW_KEYS = [
    *WINDOW_FOCUS_KEYS,
    *WINDOW_KILL_KEYS,
    *WINDOW_MOVE_KEYS,
    *WINDOW_SIZE_KEYS,
    *WINDOW_TOGGLE_FLOATING_KEYS
]

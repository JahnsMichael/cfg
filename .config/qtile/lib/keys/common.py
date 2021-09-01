from lib.keys.screens import SCREEN_KEYS
from lib.keys.controls import CONTROL_KEYS
from lib.keys.layouts import LAYOUT_KEYS
from lib.keys.functional import (
    ROFI_KEYS, 
    UTIL_KEYS,
    APP_KEYS
)
from lib.keys.windows import (
    WINDOW_KEYS,
    WINDOW_FOCUS_KEYS,
    WINDOW_KILL_KEYS,
)
from lib.keys.groups import (
    GROUP_CYCLE_KEYS,
    GROUP_KEYS
)

NEED_MOD_KEYS = [
    *GROUP_KEYS,
    *SCREEN_KEYS,
    *WINDOW_KEYS,
    *CONTROL_KEYS,
    *LAYOUT_KEYS,
    *ROFI_KEYS,
    *APP_KEYS
]

DONT_NEED_MOD_KEYS = [
    *UTIL_KEYS
]

NAV_KEYS = [
    *GROUP_CYCLE_KEYS,
    *WINDOW_FOCUS_KEYS,
    *WINDOW_KILL_KEYS
]
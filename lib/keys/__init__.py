from lib.keys.common import (
    NEED_MOD_KEYS,
    DONT_NEED_MOD_KEYS
)
from lib.keys.modes import MODES_KEYCHORDS
from lib.keys.utils import get_keys_with_mod

def get_keys():
    return [
        *get_keys_with_mod(NEED_MOD_KEYS),
        *DONT_NEED_MOD_KEYS,
        *MODES_KEYCHORDS,
    ]
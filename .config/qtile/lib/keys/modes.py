from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from lib.groups import get_groups
from lib.const import MOD
from lib.keys.common import (
    NAV_KEYS,
    NEED_MOD_KEYS
)

def get_keepmod_mod_keys():
    keys = []
    keychords = NEED_MOD_KEYS.copy()
    keys.append(KeyChord([MOD, 'control'], "m", keychords, mode="keepmod"))
    return keys


def get_move_mode_keys():
    keys = []
    keychords = NAV_KEYS.copy()

    for group in get_groups():
        keychords.append(
            Key(
                [], group.name[0],
                lazy.window.togroup(group.name),
                desc="move focused window to group {}".format(group.name)
            )
        )
        keychords.append(
            Key(
                ['mod1'], group.name[0],
                lazy.window.togroup(group.name, switch_group=True),
                desc="move focused window and jump to group {}".format(
                    group.name)
            )
        )

    keys.append(KeyChord([MOD], "m", keychords))

    return keys


def get_manage_mode_keys():
    keys = []
    keychords = NAV_KEYS.copy()

    keychords.append(
        Key([], "c", lazy.window.kill(), desc="Kill focused window"),
    )

    for group in get_groups():
        keychords.append(
            Key(
                [], group.name[0],
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name)
            )
        )
        keychords.append(
            Key(
                ['mod1'], group.name[0],
                lazy.window.togroup(group.name, switch_group=True),
                desc="move focused window and jump to group {}".format(
                    group.name)
            )
        )
        keychords.append(
            Key(
                ['shift'], group.name[0],
                lazy.window.togroup(group.name),
                desc="move focused window to group {}".format(group.name)
            )
        )

    keys.append(KeyChord([MOD, "shift"], "m", keychords, mode="manage"))

    return keys


def get_kill_mode_keys():
    keys = []
    keychords = NAV_KEYS.copy()
    keychords.append(
        Key([], "Return", lazy.window.kill(), desc="Kill focused window"),
    )

    keys.append(KeyChord([MOD, "shift"], "c", keychords, mode="kill"))

    return keys


MODES_KEYCHORDS = [
    *get_move_mode_keys(),
    *get_manage_mode_keys(),
    *get_kill_mode_keys(),
    *get_keepmod_mod_keys(),
]

from libqtile.config import Key
from libqtile.lazy import lazy
from lib.groups import get_groups
from lib.const import apps

SCRATCHPAD_KEYS = [
    Key([], "Return", lazy.group["scratchpad"].dropdown_toggle('term'),
        desc="Launch terminal"),
]

GROUP_CYCLE_KEYS = [
    Key([], "period", lazy.screen.next_group(),
            desc="Move to the group on the right"),
    Key([], "comma", lazy.screen.prev_group(),
        desc="Move to the group on the left"),
]

GROUP_KEYS = [*SCRATCHPAD_KEYS, *GROUP_CYCLE_KEYS]


for group in get_groups():

    if (group.name == "scratchpad"):
        continue

    GROUP_KEYS.extend([
        Key([], group.name[0], lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),
        Key(["shift"], group.name[0], lazy.window.togroup(group.name),
            desc="move focused window to group {}".format(group.name)),
        Key(["mod1"], group.name[0], lazy.window.togroup(group.name),
            desc="move focused window to group {}".format(group.name)),
    ])

APP_MAPPING = {
    '1': [apps.CODE],
    '2': [apps.WEB],
    '3': [apps.WEB],
    '4': [apps.WEB],
    '5': [apps.WEB],
    '6': [apps.FILE],
    '7': [apps.INKSCAPE],
    '8': [apps.WEB],
    '9': [
        apps.WHATSAPP,
        apps.LINE
    ],
    '0': [apps.PAMAC]
}


def spawn_group_apps(qtile):
    for app in APP_MAPPING[qtile.current_group.name]:
        qtile.cmd_spawn(app)


GROUP_KEYS.append(
    Key(["control"], "Return",
        lazy.function(spawn_group_apps),
        desc="Spawn app according to the mapping"
        )
)

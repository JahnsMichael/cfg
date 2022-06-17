from libqtile.config import Key
from libqtile.lazy import lazy
from lib.groups import get_groups
from lib.const import apps

SCRATCHPAD_KEYS = [
    Key([], "Return", lazy.group["scratchpad"].dropdown_toggle('term'),
        desc="Launch terminal"),
    # Key([], "space", lazy.group["scratchpad"].dropdown_toggle('run'),
        # desc="Launch CLI run launcher inside a terminal"),
]

def send_window_to_next_group(qtile):
    current_group = int(qtile.current_group.name)
    next_group = current_group + 1
    if (next_group == 10):
        next_group = 0
    qtile.current_window.togroup(str(next_group))

def send_window_to_previous_group(qtile):
    current_group = int(qtile.current_group.name)
    prev_group = current_group - 1
    if (prev_group == -1):
        prev_group = 9
    qtile.current_window.togroup(str(prev_group))


GROUP_CYCLE_KEYS = [
    Key([], "period", lazy.screen.next_group(),
            desc="Move to the group on the right"),
    Key([], "comma", lazy.screen.prev_group(),
        desc="Move to the group on the left"),
    Key(["shift"], "period", lazy.function(send_window_to_next_group),
            desc="Send window to the group on the right"),
    Key(["shift"], "comma", lazy.function(send_window_to_previous_group),
        desc="Send window to the group on the left"),
]

GROUP_KEYS = [*SCRATCHPAD_KEYS, *GROUP_CYCLE_KEYS]


for group in get_groups():

    if (group.name == "scratchpad"):
        continue

    GROUP_KEYS.extend([
        Key([], group.name[0], lazy.group[group.name].toscreen(toggle=True),
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

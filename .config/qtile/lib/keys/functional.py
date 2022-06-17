from libqtile.config import Key
from libqtile.lazy import lazy
from lib.const import MOD, apps
from lib.scripts import (
    screenshot,
)

UTIL_KEYS = [
    Key([], "XF86MonBrightnessDown", lazy.spawn(["xbacklight", "-dec", "5"]),
            desc="Set brightness down"),
    Key([], "XF86MonBrightnessUp", lazy.spawn(["xbacklight", "-inc", "5"]),
        desc="Set brightness up"),
    Key([], "Print", lazy.function(screenshot),
            desc="Take a screenshot, select region"),
]

ROFI_KEYS = [
    Key([], "space", lazy.spawn(["rofi", "-show", "drun"]),
            desc="rofi -show drun"),
    Key(['mod1'], "space", lazy.spawn(["rofi", "-show", "file-browser-extended"]),
        desc="rofi -show file-browser-extended"),
    Key([], "slash", lazy.spawn(["rofi", "-show", "window"]),
        desc="rofi -show window"),
    Key(['control'], "b", lazy.spawn(["rofi-bluetooth"]),
        desc="rofi-bluetooth"),
]

def sosmed(qtile):
    qtile.cmd_spawn('/usr/bin/brave --app=https://web.whatsapp.com')
    qtile.cmd_spawn('/usr/bin/brave --app=chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html')

APP_KEYS = [
    Key(['control'], "1", lazy.spawn(apps.CODE),
        desc="Spawn text editor."),
    Key(['control'], "3", lazy.spawn(apps.WEB),
        desc="Spawn web browser."),
    Key(['control'], "6", lazy.spawn(apps.FILE),
        desc="Spawn file browser."),
    Key(['control'], "9", lazy.function(sosmed),
        desc="Spawn social media's apps."),
    Key(['shift'], "Return", lazy.spawn(apps.TERM),
        desc="Spawn terminal."),
    Key([], "f", lazy.spawn(apps.FILE),
        desc="Spawn file browser."),
    Key([], "b", lazy.spawn(apps.WEB),
        desc="Spawn web browser."),
    Key([], "t", lazy.spawn(apps.TERM),
        desc="Spawn terminal."),
]

# def show_keys_key(keys):
#     return Key(
#         [mod, "shift"], "slash",
#         lazy.spawn(
#             "sh -c 'echo \"" +
#             show_keys(keys) +
#             "\" | rofi -columns 1 -width 45 -dmenu -i -mesg \"Keyboard shortcuts\"'"
#         ),
#         desc="Print keyboard bindings"
#     )

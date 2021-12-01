from libqtile.config import (
    Group,
    Match,
    ScratchPad,
    DropDown
)
from lib.const.apps import ( 
  WHATSAPP,
  LINE,
  WEB
)

GROUPS = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8", matches=[
        Match(wm_class="zoom"),
    ]),
    Group("9", matches=[
        Match(wm_class="web.whatsapp.com"),  # Whatsapp Web
        Match(wm_class="ophjlpahpchlmihnnnihgmmeilfjmjjc__index.html"), # LINE Browser Extension
    ]),
    Group("0")
]

cmd = "kitty"

GROUPS.append(
    ScratchPad("scratchpad", [
        DropDown(
            "term",
            cmd,
            opacity=1.0,
            x=0.05, y=0.05,
            width=0.9, height=0.9,
        ),
    ]))


def get_groups():
    return GROUPS

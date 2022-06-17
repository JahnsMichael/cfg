from libqtile.config import (
    Group,
    Match,
    ScratchPad,
    DropDown,
)

GROUPS = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7", matches=[
        Match(wm_class="libreoffice"),
    ]),
    Group("8", matches=[
        Match(wm_class="zoom"),
    ]),
    Group("9", matches=[
        Match(wm_class="web.whatsapp.com"),  # Whatsapp Web
        Match(wm_class="ophjlpahpchlmihnnnihgmmeilfjmjjc__index.html"), # LINE Browser Extension
    ]),
    Group("0", matches=[
        Match(wm_class="discord")
    ])
]

GROUPS.append(
    ScratchPad("scratchpad", [
        DropDown(
            "term",
            "alacritty",
            opacity=1.0,
            x=0, y=0,
            width=0.7, height=0.7,
        ),
        DropDown(
            "run",
            "alacritty -e fmenu --hold",
            opacity=1.0,
            x=-0.015, y=0.25,
            width=0.2, height=0.5,
        ),
    ]))


def get_groups():
    return GROUPS

from libqtile import qtile, bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from lib.scripts import get_monitors, xrandr

from lib.const import colors
from lib.screens.widgets import (
    get_top_widgets,
    get_bottom_widgets
)


def get_default_screen(systray=False):
    attrs = {"size": 30, "background": colors.common["bg"] + "00"}
    return Screen(
        top=bar.Bar(
            get_top_widgets(systray),
            margin=[5,5,2,5],
            **attrs
        ),
        bottom=bar.Gap(3),
        right=bar.Gap(3),
        left=bar.Gap(3),
    )


def get_screens():
    screens = [get_default_screen(systray=True),]
    for i in range(len(get_monitors())-1):
        screens.append(get_default_screen())
    return screens

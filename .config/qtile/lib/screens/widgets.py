from libqtile import qtile
from libqtile import widget as default_widget
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, BorderDecoration
from lib.const import colors, fontawesome, fonts, apps
from lib.screens.custom_widgets.tasklist import CustomTaskList
from lib.screens.custom_widgets.window_control import WindowControl
from os.path import exists
from os import walk

SEP_S = widget.TextBox(
    text=" ",
    font=fonts.POWERLINE,
    padding=0,
    fontsize=10
)

SEP_M = widget.TextBox(
    text=" ",
    font=fonts.POWERLINE,
    padding=0,
    fontsize=15
)

SEP_L = widget.TextBox(
    text=" ",
    font=fonts.POWERLINE,
    padding=0,
    fontsize=20
)


SEP_S_DARK = widget.Sep(
    foreground=colors.black[4],
    background=colors.black[4],
    linewidth=5
)
SEP_M_DARK = widget.Sep(
    foreground=colors.black[4],
    background=colors.black[4],
    linewidth=5
)
SEP_L_DARK = widget.Sep(
    foreground=colors.black[4],
    background=colors.black[4],
    linewidth=5
)

def decorations(
        color=colors.blue[0],
        position="single",
        filled=True,
        pad=5,
        rad=10
    ):
    pad_y = pad if filled else pad+1
    attrs_map = {
        "single": { "filled": filled, "radius": rad, "padding_y": pad_y },
        "center": { "filled": filled, "radius": 0, "padding_y": pad_y },
        "left": { "filled": filled, "radius": [rad, 0, 0, rad], "padding_y": pad_y },
        "right": { "filled": filled, "radius": [0, rad, rad, 0], "padding_y": pad_y },
    }

    position = "single" if position not in attrs_map else position
    attr = attrs_map[position]

    return {
        "decorations": [
            RectDecoration(colour=color, **attr),
            # BorderDecoration(colour=color, border_width=[3, 0, 0, 0]),
        ],
    }

def widget_with_icon(main_widget, icon, color):
    setattr(
        main_widget,
        "decorations",
        decorations(color, position="right")["decorations"]
    )
    return [
        widget.TextBox(
            text=f' {icon} ',
            font=fonts.ICON,
            foreground=color,
            **decorations(color, position="left", filled=False)
        ),
        main_widget
    ]

def get_top_widgets(systray=False):

    def get_app_btn(text, color, cmd, position="center"):
        return widget.TextBox(
            text=" " + text + " ",
            font=fonts.ICON,
            foreground=color,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(cmd)
            },
            # **decorations(colors.common["bg"], position)
        )

    APP_BTN = widget.WidgetBox(
        widgets=[
            get_app_btn(fontawesome.SEARCH, colors.red[0], "rofi -show drun", "left"),
            get_app_btn(fontawesome.CODE, colors.brown[0], "/usr/bin/codium -n"),
            get_app_btn(fontawesome.WEB, colors.blue[0], "/usr/bin/brave"),
            get_app_btn(fontawesome.FOLDER, colors.green[0], "/usr/bin/pcmanfm", "right"),
        ],
        text_closed="  " + fontawesome.ARROW_RIGHT + " ",
        text_open="  "+ fontawesome.ARROW_LEFT + "\t",
        font=fonts.ICON,
        foreground=colors.blue[0],
    )

    GROUPBOX = widget.GroupBox(
        other_current_screen_border=colors.common['ui'],
        other_screen_border=colors.common['ui'],
        inactive=colors.black[2],
        urgent_border=colors.red[2],
        padding=5,
        # rounded=False,
        highlight_method="block",
        this_screen_border=colors.brown[3],
        this_current_screen_border=colors.blue[1],
        # hide_unused=True,
        center_aligned=True,
        **decorations(colors.common["bg"], "single")
    )

    CURRENT_WINDOW = [
        *[WindowControl(
            action_type=attrs["action"],
            font=fonts.ICON,
            fontsize=10,
            padding=5,
            # **decorations(colors.black[2], attrs["position"])
        ) for attrs in [
            {"action": "KILL", "position": "left"},
            {"action": "MAX", "position": "center"},
            {"action": "MIN", "position": "center"},
            {"action": "FLOAT", "position": "right"},
        ]],
        SEP_S,
        CustomTaskList(
            border=colors.brown[2],
            rounded=False,
            highlight_method='block',
            txt_floating=f"{fontawesome.FLOAT} ",
            txt_maximized=f"{fontawesome.MAXIMIZE} ",
            txt_minimized=f"{fontawesome.MINIMIZE} ",
            spacing=5,
            padding=8,
            icon_size=15,
            title_width_method="uniform",
            # max_title_width=200,
            urgent_border=colors.red[0],
        ),
    ]


    MEMORY = widget_with_icon(
        main_widget=widget.Memory(
            format='{MemPercent}% ',
            foreground=colors.common['bg']
        ),
        icon=fontawesome.MEMORY,
        color=colors.magenta[0]
    )

    CPU = widget_with_icon(
        main_widget=widget.CPU(
            format='{load_percent}% ',
            foreground=colors.common['bg']
        ),
        icon=fontawesome.CPU,
        color=colors.green[0]
    )

    CLOCK = widget.Clock(
        format='%a, %d %b %Y   %H:%M:%S',
        foreground="#ffffff",
        font=fonts.BOLD
    )

    SYSTRAY = widget.Systray(
        icon_size=15
    )

    def get_power_btn(text, cmd, position="center"):
        return widget.TextBox(
            text=" " + text + " ",
            font=fonts.ICON,
            mouse_callbacks={
                'Button1': cmd
            },
            **decorations(colors.red[0], position)
        )

    POWER = widget.WidgetBox(
        widgets=[
            get_power_btn(fontawesome.POWER, lambda:  qtile.cmd_spawn('shutdown now'), "left"),
            get_power_btn(fontawesome.REBOOT, lambda:  qtile.cmd_spawn('reboot')),
            get_power_btn(fontawesome.LOGOUT, lambda:  qtile.cmd_shutdown()),
            get_power_btn(fontawesome.SLEEP, lambda:  qtile.cmd_spawn("betterlockscreen -s")),
            get_power_btn(fontawesome.LOCK, lambda:  qtile.cmd_spawn("betterlockscreen -l"), "right"),
        ],
        text_closed="  " + fontawesome.POWER + "  ",
        text_open="  " + fontawesome.CLOSE + "  ",
        font=fonts.ICON,
        foreground=colors.red[0]
    )

    WORD_CLOCK = widget.WordClock(
        background=colors.common['bg'],
        active=colors.blue[0],
        font=fonts.MAIN
    )

    LAYOUT_ICON = widget.CurrentLayoutIcon(
        padding=0,
        scale=0.4,
        **decorations(colors.blue[0], "single")
    )

    TOP_WIDGETS = [
        SEP_S, CLOCK, SEP_S,
        *CURRENT_WINDOW, SEP_M,
        LAYOUT_ICON, SEP_M,
        GROUPBOX, SEP_M,
        widget.Chord(), SEP_M,
        *MEMORY, SEP_M,
        *CPU, SEP_M,
        POWER, SEP_S,
    ]

    TOP_WIDGETS_SYSTRAY = TOP_WIDGETS.copy()
    TOP_WIDGETS_SYSTRAY.insert(-2, SYSTRAY)
    TOP_WIDGETS_SYSTRAY.insert(-2, SEP_M)

    if systray:
        return TOP_WIDGETS_SYSTRAY
    return TOP_WIDGETS

def get_left_widgets():

    def get_app_btn(icon_name, cmd, icon_theme="/usr/share/icons/hicolor/128x128/apps/", spawn=True):

        fallback_icon_dir = "/usr/share/icons"
        filename = ""

        if exists(f"{icon_theme}{icon_name}.png"):
            filename = f"{icon_theme}{icon_name}.png"
        elif exists(f"{icon_theme}{icon_name}.svg"):
            filename = f"{icon_theme}{icon_name}.svg"
        else:
            for root, dirs, files in walk(fallback_icon_dir):
                if len(filename) != 0:
                    break
                for file in files:
                    if len(filename) != 0 :
                        break
                    if (icon_name in file) and (".png" in file or ".svg" in file):
                        filename = f"{root}/{str(file)}"
                        break
        
        func = cmd
        if spawn:
            func = lambda: qtile.cmd_spawn(cmd)

        return widget.Image(
            filename=filename,
            mouse_callbacks={
                'Button1': func
            },
            margin=5,
        )

    icon_theme = "/usr/share/icons/Yaru++-Dark/apps/48/"
    icon_theme_places = "/usr/share/icons/Yaru++/places/scalable/"

    LEFT_WIDGETS = [
            get_app_btn("ubuntu-logo-icon", "rofi -show drun", icon_theme_places),
            get_app_btn("window-duplicate", "rofi -show window", icon_theme),
            get_app_btn("workspace-switcher-left-top", lambda : qtile.groups_map["scratchpad"].cmd_dropdown_toggle('term'), icon_theme, spawn=False),
            widget.Sep(padding=10),
            get_app_btn("brave-desktop", apps.WEB, icon_theme),
            get_app_btn("file-manager", apps.FILE, icon_theme),
            get_app_btn("terminal", apps.TERM, icon_theme),
            get_app_btn("logseq", "/usr/bin/logseq", icon_theme),
            get_app_btn("code", "/usr/bin/code", icon_theme),
    ]

    return LEFT_WIDGETS

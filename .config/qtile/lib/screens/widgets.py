from libqtile import qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, BorderDecoration
from lib.const import colors, fontawesome, fonts
from lib.screens.custom_widgets.tasklist import CustomTaskList
from lib.screens.custom_widgets.window_control import WindowControl

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
        rad=3
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
            text=icon,
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
        inactive=colors.common['bg'],
        urgent_border=colors.red[2],
        padding=5,
        # rounded=False,
        highlight_method="block",
        this_screen_border=colors.brown[3],
        this_current_screen_border=colors.blue[1],
        hide_unused=True,
        center_aligned=True,
        **decorations(colors.common["bg"], "single")
    )

    CURRENT_WINDOW = [
        *[WindowControl(
            action_type=action,
            font=fonts.ICON,
            fontsize=10,
            padding=5
        ) for action in ["KILL","MAX", "MIN", "FLOAT"]],
        SEP_S,
        CustomTaskList(
            border=colors.brown[2],
            rounded=True,
            highlight_method='block',
            txt_floating=f"{fontawesome.FLOAT} ",
            txt_maximized=f"{fontawesome.MAXIMIZE} ",
            txt_minimized=f"{fontawesome.MINIMIZE} ",
            spacing=5,
            padding=5,
            icon_size=0,
            max_title_width=200,
            urgent_border=colors.red[0],
        ),
    ]


    MEMORY = widget_with_icon(
        main_widget=widget.Memory(
            format='RAM {MemPercent}%{MemUsed: .0f}M',
            foreground=colors.common['bg']
        ),
        icon=fontawesome.MEMORY,
        color=colors.magenta[0]
    )

    CPU = widget_with_icon(
        main_widget=widget.CPU(
            format='{load_percent}% {freq_current}GHz',
            foreground=colors.common['bg']
        ),
        icon=fontawesome.CPU,
        color=colors.green[0]
    )

    CLOCK = widget_with_icon(
        main_widget=widget.Clock(
            format='%a, %d %b %Y | %H:%M:%S',
            foreground=colors.common['bg']
        ),
        icon=fontawesome.CLOCK,
        color=colors.blue[0]
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

    TOP_WIDGETS = [
        APP_BTN, SEP_M,
        GROUPBOX, SEP_M,
        *CURRENT_WINDOW,
        widget.Chord(),
        *MEMORY, SEP_M,
        *CPU, SEP_M,
        *CLOCK, SEP_M,
        POWER, SEP_S,
        # WORD_CLOCK
    ]

    TOP_WIDGETS_SYSTRAY = [
        APP_BTN, SEP_M,
        GROUPBOX, SEP_M,
        *CURRENT_WINDOW,
        widget.Chord(),
        *MEMORY, SEP_M,
        *CPU, SEP_M,
        *CLOCK, SEP_M,
        SYSTRAY, SEP_M,
        POWER, SEP_S,
        # WORD_CLOCK
    ]

    if systray:
        return TOP_WIDGETS_SYSTRAY
    return TOP_WIDGETS


def get_bottom_widgets(systray=False):
    def get_app_btn(text, color, cmd):
        return widget.TextBox(
            text=text,
            font=fonts.ICON,
            foreground=color,
            background=colors.black[4],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(cmd)
            }
        )

    APP_BTN = [
        get_app_btn(fontawesome.SEARCH, colors.red[0], "rofi -show drun"),
        get_app_btn(fontawesome.CODE, colors.brown[0], "/usr/bin/codium -n"),
        get_app_btn(fontawesome.WEB, colors.blue[0], "/usr/bin/brave"),
        get_app_btn(fontawesome.FOLDER, colors.green[0], "/usr/bin/pcmanfm"),
    ]

    APP_LIST = CustomTaskList(
        border=colors.brown[2],
        rounded=False,
        highlight_method='block',
        txt_floating=f"{fontawesome.FLOAT} ",
        txt_maximized=f"{fontawesome.MAXIMIZE} ",
        txt_minimized=f"{fontawesome.MINIMIZE} ",
        padding=4,
        margin=0,
        icon_size=15,
        max_title_width=200,
        urgent_border=colors.red[0]
    )

    MUSIC = widget.Moc(
        foreground=colors.brown[1],
        play_color=colors.brown[1],
        noplay_color=colors.brown[0],
    )

    SYSTRAY = widget.Systray(
        foreground=colors.black[5],
        background=colors.black[4]
    )
    POWER = widget.QuickExit(
        default_text=fontawesome.POWER,
        foreground=colors.red[0],
        font=fonts.ICON,
        background=colors.black[4]
    )

    BOTTOM_WIDGETS_SYSTRAY = [
        SEP_S_DARK,
        *APP_BTN,
        SEP_L_DARK,
        APP_LIST, SEP_S,
        MUSIC, SEP_S,
        SEP_S_DARK,
        SYSTRAY,
        SEP_L_DARK,
        POWER,
        SEP_L_DARK
    ]

    BOTTOM_WIDGETS = [
        SEP_S_DARK,
        *APP_BTN,
        SEP_L_DARK,
        APP_LIST, SEP_S,
        MUSIC, SEP_S,
        SEP_L_DARK,
        POWER,
        SEP_L_DARK
    ]

    if systray:
        return BOTTOM_WIDGETS_SYSTRAY
    return BOTTOM_WIDGETS

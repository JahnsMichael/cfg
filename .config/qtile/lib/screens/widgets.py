from libqtile import qtile, widget
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

def powerlined(main_widget, color=None, margin_left=3, margin_right=3):

    if not color:
        if isinstance(main_widget, list) or not main_widget.background:
            color = colors.common["bg"]
        else:
            color = main_widget.background

    left = [
        widget.TextBox(
            text=" ",
            font=fonts.POWERLINE,
            padding=0,
            fontsize=margin_left,
            foreground=color
        ),
        widget.TextBox(
            text=fontawesome.SEP_ROUNDED_LEFT,
            font=fonts.POWERLINE,
            padding=0,
            foreground=color,
            fontsize=18
        ),
    ]
    right = [
        widget.TextBox(
            text=fontawesome.SEP_ROUNDED_RIGHT,
            font=fonts.POWERLINE,
            padding=0,
            fontsize=18,
            foreground=color
        ),
        widget.TextBox(
            text=" ",
            font=fonts.POWERLINE,
            padding=0,
            fontsize=margin_right
        ),
    ]
    if isinstance(main_widget, list):
        return [*left, *main_widget, *right]
    return [*left, main_widget, *right]

def get_top_widgets(systray=False):

    def _get_text_with_callback(text, fg, bg, cmd):
        return widget.TextBox(
            text=text,
            font=fonts.ICON,
            foreground=fg,
            background=bg,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(cmd)
            }
        )

    def get_app_btn(text, color, cmd, bg=colors.common["bg"]):
        return _get_text_with_callback(text, color, bg, cmd)

    APP_BTN = powerlined(widget.WidgetBox(
        widgets=[
            get_app_btn(fontawesome.SEARCH, colors.red[0], "rofi -show drun"),
            get_app_btn(fontawesome.CODE, colors.brown[0], "/usr/bin/codium -n"),
            get_app_btn(fontawesome.WEB, colors.blue[0], "/usr/bin/brave"),
            get_app_btn(fontawesome.FOLDER, colors.green[0], "/usr/bin/pcmanfm"),
        ],
        text_closed=fontawesome.ARROW_RIGHT,
        text_open=fontawesome.ARROW_LEFT + "\t",
        font=fonts.ICON,
        foreground=colors.blue[0],
        background=colors.common["bg"],
    ))

    GROUPBOX = powerlined(widget.GroupBox(
        other_current_screen_border=colors.common['ui'],
        other_screen_border=colors.common['ui'],
        inactive=colors.common['ui'],
        urgent_border=colors.red[2],
        padding=5,
        rounded=True,
        highlight_method="line",
        this_screen_border=colors.brown[3],
        this_current_screen_border=colors.blue[1],
        hide_unused=True,
        background=colors.common["bg"],
        center_aligned=True,
    ))

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
            borderwidth=0,
            rounded=True,
            title_width_method="uniform",
            highlight_method='block',
            txt_floating=f"{fontawesome.FLOAT} ",
            txt_maximized=f"{fontawesome.MAXIMIZE} ",
            txt_minimized=f"{fontawesome.MINIMIZE} ",
            margin=0,
            spacing=5,
            icon_size=12,
            max_title_width=200,
            urgent_border=colors.red[0],
        ),
    ]

    def get_icon(text, color, cmd):
        return _get_text_with_callback(text, color, None, cmd)

    MEMORY = powerlined([
        widget.TextBox(
            text=fontawesome.MEMORY,
            font=fonts.ICON,
            background=colors.magenta[0],
            foreground=colors.common["bg"],
        ),
        widget.Memory(
            format='{MemPercent}%{MemUsed: .0f}M',
            background=colors.magenta[0],
            foreground=colors.common["bg"],
            font=fonts.MAIN
        )
    ], color=colors.magenta[0])

    CPU = powerlined([
        widget.TextBox(
            text=fontawesome.CPU,
            font=fonts.ICON,
            background=colors.green[0],
            foreground=colors.common["bg"],
        ),
        widget.CPU(
            format='{load_percent}% {freq_current}GHz',
            background=colors.green[0],
            foreground=colors.common["bg"],
            font=fonts.MAIN
        )
    ], color=colors.green[0])

    # CPUGRAPH = powerlined(widget.CPU())

    CLOCK = powerlined([
        widget.TextBox(
            text=fontawesome.CLOCK,
            font=fonts.ICON,
            background=colors.blue[0],
            foreground=colors.common["bg"],
        ),
        widget.Clock(
            format='%a, %d %b %Y | %H:%M:%S',
            background=colors.blue[0],
            foreground=colors.common["bg"],
            font=fonts.MAIN
        )
    ], color=colors.blue[0])

    POMODORO = powerlined(widget.Pomodoro(
        color_active=colors.common['accent'],
        color_break=colors.green[0],
        color_inactive=colors.common['fg'],
        background=colors.common['bg'],
    ))

    SYSTRAY = widget.Systray(
        icon_size=15
    )

    def get_power_btn(text, cmd):
        return widget.TextBox(
            text=text,
            font=fonts.ICON,
            background=colors.red[0],
            mouse_callbacks={
                'Button1': cmd
            }
        )

    POWER = powerlined(widget.WidgetBox(
        widgets=[
            get_power_btn(fontawesome.POWER, lambda:  qtile.cmd_spawn('shutdown now')),
            get_power_btn(fontawesome.REBOOT, lambda:  qtile.cmd_spawn('reboot')),
            get_power_btn(fontawesome.LOGOUT, lambda:  qtile.cmd_shutdown()),
            get_power_btn(fontawesome.SLEEP, lambda:  qtile.cmd_spawn("betterlockscreen -s")),
            get_power_btn(fontawesome.LOCK, lambda:  qtile.cmd_spawn("betterlockscreen -l")),
        ],
        text_closed=fontawesome.POWER,
        text_open=fontawesome.CLOSE + "   ",
        background=colors.red[0],
        font=fonts.ICON,
    ))

    TOP_WIDGETS = [
        *APP_BTN,
        *GROUPBOX, SEP_M,
        *CURRENT_WINDOW,
        widget.Chord(),
        # *POMODORO,
        *MEMORY,
        *CPU,
        *CLOCK,
        *POWER,
    ]

    TOP_WIDGETS_SYSTRAY = [
        *APP_BTN,
        *GROUPBOX, SEP_M,
        *CURRENT_WINDOW,
        widget.Chord(),
        # *POMODORO,
        *MEMORY,
        *CPU,
        *CLOCK, SEP_M,
        SYSTRAY, SEP_M,
        *POWER,
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

from libqtile import qtile, widget
from lib.const import colors, fontawesome, fonts
from lib.screens.custom_widgets.tasklist import CustomTaskList
from lib.screens.custom_widgets.window_control import WindowControl

SEP_S = widget.Sep(
    foreground=colors.common['bg'],
    linewidth=5
)
SEP_M = widget.Sep(
    foreground=colors.common['bg'],
    linewidth=10
)
SEP_L = widget.Sep(
    foreground=colors.common['bg'],
    linewidth=20
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

def get_top_widgets(systray=False):

    group_box_attr = {
        "rounded": False,
        "highlight_method": "line",
        "other_current_screen_border": colors.common['ui'],
        "other_screen_border": colors.common['ui'],
        "inactive": colors.common['ui'],
        "urgent_border": colors.red[2],
        "padding": 5,
    }

    def get_groupbox(text, scheme, groups):
        return [
            # widget.TextBox(
                # text=text,
                # font=fonts.ICON,
                # foreground=scheme[0],
            # ),
            widget.GroupBox(
                **group_box_attr,
                highlight_color=[colors.common['bg'], scheme[0]],
                this_screen_border=scheme[0],
                this_current_screen_border=scheme[1],
                visible_groups=groups[0],
            ),
            widget.GroupBox(
                **group_box_attr,
                highlight_color=[colors.common['bg'], scheme[0]],
                this_screen_border=scheme[0],
                this_current_screen_border=scheme[1],
                visible_groups=groups[1:],
                hide_unused=True
            )
        ]

    def get_app_btn(text, color, cmd):
            return widget.TextBox(
                text=text,
                font=fonts.ICON,
                foreground=color,
                fontshadow=colors.black[4],
                mouse_callbacks={
                    'Button1': lambda: qtile.cmd_spawn(cmd)
                }
            )
    
    APP_BTN = [
        get_app_btn(fontawesome.CODE, colors.brown[0], "/usr/bin/codium -n"),
        get_app_btn(fontawesome.WEB, colors.blue[0], "/usr/bin/brave"),
        get_app_btn(fontawesome.FOLDER, colors.green[0], "/usr/bin/pcmanfm"),
    ]

    START_MENU = widget.Image(
        filename="~/.config/qtile/assets/mirage-logo.png",
        margin_x=7,
        margin_y=5,
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn("rofi -show drun")
        }
    )

    # Split GroupBox into sections
    CODE_GROUPBOX = get_groupbox(
        fontawesome.CODE, [colors.brown[0], colors.brown[2]], ["1", "2"])
    WEB_GROUPBOX = get_groupbox(
        fontawesome.WEB, [colors.blue[0], colors.blue[1]], ["3", "4", "5"])
    DOCS_GROUPBOX = get_groupbox(
        fontawesome.FOLDER, [colors.green[0], colors.green[1]], ["6", "7"])
    MEET_GROUPBOX = get_groupbox(
        fontawesome.CAMERA, [colors.red[0], colors.red[1]], ["8", "9", "0"])
    GROUPBOXES = [
        *CODE_GROUPBOX,
        SEP_S,
        *WEB_GROUPBOX,
        SEP_S,
        *DOCS_GROUPBOX,
        SEP_S,
        *MEET_GROUPBOX
    ]
    GROUPBOX = widget.GroupBox(
        **group_box_attr,
        highlight_color=colors.common["bg"],
        this_screen_border=colors.brown[3],
        this_current_screen_border=colors.blue[1],
        hide_unused=True
    )

    CURRENT_WINDOW = [
        SEP_S,
        *[WindowControl(
            action_type=action, 
            font=fonts.ICON,
            fontshadow=colors.black[4],
            padding=5
        ) for action in ["KILL","MAX", "MIN", "FLOAT"]],
        SEP_S,
        CustomTaskList(
            border=colors.brown[2],
            rounded=False,
            highlight_method='block',
            txt_floating=f"{fontawesome.FLOAT} ",
            txt_maximized=f"{fontawesome.MAXIMIZE} ",
            txt_minimized=f"{fontawesome.MINIMIZE} ",
            padding=7,
            margin=0,
            icon_size=15,
            max_title_width=200,
            urgent_border=colors.red[0]
        ),
        SEP_S
    ]

    MEMORY = [
        # widget.TextBox(
        #     text=fontawesome.MEMORY,
        #     font=fonts.ICON,
        #     foreground=colors.blue[0],
        # ),
        widget.Memory(
            foreground=colors.blue[0],
            format='{MemPercent}%{MemUsed: .0f}M/{MemTotal: .0f}M',
            font=fonts.MAIN
        ),
    ]

    BATTERY = [
        # widget.TextBox(
        #     text=fontawesome.BATTERY,
        #     font=fonts.ICON,
        #     foreground=colors.brown[5],
        # ),
        # widget.BatteryIcon(
        #     theme_path="/home/jahnsmichael/.config/qtile/assets/battery",
        #     padding=8,
        # ),
        widget.Battery(
            foreground=colors.brown[5],
            format='{char} {percent:2.0%}',
            discharge_char='',
            low_percentage=0.1,
            low_foreground=colors.red[0],
            notify_below=20,
            show_sort_text=False,
            font=fonts.MAIN
        )
    ]
    CLOCK = [
        # widget.TextBox(
        #     text=fontawesome.CLOCK,
        #     font=fonts.ICON,
        #     foreground=colors.green[0],
        # ),
        widget.Clock(
            format='%a, %d %b %Y | %H:%M:%S',
            foreground=colors.green[0],
            font=fonts.MAIN
        ),
    ]
    
    SYSTRAY = widget.Systray(
        foreground=colors.black[5],
        icon_size=15
    )

    POWER = widget.QuickExit(
        default_text=fontawesome.POWER,
        foreground=colors.red[0],
        font=fonts.ICON,
    )

    TOP_WIDGETS = [
        START_MENU,
        *APP_BTN,
        *CURRENT_WINDOW,
        GROUPBOX,
        widget.Chord(), SEP_S,
        *MEMORY, SEP_S,
        *BATTERY, SEP_S,
        *CLOCK, SEP_L
    ]

    TOP_WIDGETS_SYSTRAY = [
        START_MENU,
        *APP_BTN,
        *CURRENT_WINDOW,
        GROUPBOX,
        widget.Chord(), SEP_S,
        *MEMORY,
        *BATTERY,
        *CLOCK,
        SYSTRAY, SEP_S,
        POWER, SEP_S
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

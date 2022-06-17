from libqtile import layout
from lib.layouts.custom_bsp import BorderOnSingleBSP
from libqtile.config import Match
from lib.const import colors, fonts

layout_theme = {
    "border_width": 2,
    "font": fonts.MAIN,
    # "margin": 2,
    "border_focus": colors.brown[2],
    "border_normal": colors.common['bg']
}


def get_layouts():
    return [
        layout.Columns(
            **layout_theme,
            border_normal_stack=colors.black[3],
            border_focus_stack=colors.blue[1],
            insert_position=1,
            num_columns=2,
            # border_on_single=True,
        ),
        layout.Max(),
        # BorderOnSingleBSP(
            # **layout_theme,
            # border_on_single=True,
            # fair=False,
            # grow_amount=5,
        # )
    ]


def get_floating_layout():
    floating_layout = layout.Floating(float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry

        # Match(wm_class='pamac-manager'),
        Match(wm_class='pavucontrol'),
        Match(wm_class='Conky'),
        Match(wm_class='pentablet'),
        Match(wm_class='Unity'),
    ], **layout_theme)
    return floating_layout

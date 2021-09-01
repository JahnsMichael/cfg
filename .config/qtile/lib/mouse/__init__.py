from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from lib.const import MOD

def get_mouse():
    return [
        Click([MOD], "Button1", lazy.window.bring_to_front()),
        Drag([MOD], "Button1", lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        Drag([MOD, "shift"], "Button1", lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
        Drag([MOD], "Button3", lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
        Click([MOD], "Button2", lazy.window.toggle_floating()),
        Click([MOD, "control"], "Button2", lazy.window.kill())
    ]

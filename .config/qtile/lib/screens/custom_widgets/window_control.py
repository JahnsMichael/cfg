from qtile_extras import widget
from libqtile import hook
from lib.const import fontawesome, colors
from libqtile.widget import base

class WindowControl(widget.TextBox):

    action_type = None

    def __init__(self, action_type="KILL", **config):
        self.action_type = action_type

        super().__init__(text="", foreground=self.get_color(), **config)

        self.add_callbacks({
            'Button1': self.action
        })

    def _configure(self, qtile, bar):
        super()._configure(qtile, bar)
        self.setup_hooks()

    def setup_hooks(self):
        hook.subscribe.client_name_updated(self.hook_response)
        hook.subscribe.focus_change(self.hook_response)
        hook.subscribe.float_change(self.hook_response)

    def hook_response(self, *args):
        if not self.bar.screen.group.current_window:
            self.update("")
        else:
            self.update(self.get_text())

    def action(self):
        current_win = self.bar.screen.group.current_window
        action_map = {
            "KILL": current_win.cmd_kill,
            "MIN": current_win.cmd_toggle_minimize,
            "MAX": current_win.cmd_toggle_maximize,
            "FLOAT": current_win.cmd_toggle_floating,
        }
        if self.action_type:
            action_map[self.action_type]()

    def get_text(self):
        text_map = {
            "KILL": fontawesome.CLOSE,
            "MIN": fontawesome.MINIMIZE,
            "MAX": fontawesome.MAXIMIZE,
            "FLOAT": fontawesome.FLOAT,
        }
        if self.action_type:
            return text_map[self.action_type]
        return fontawesome.CLOSE

    def get_color(self):
        color_map = {
            "KILL": colors.red[0],
            "MIN": colors.blue[0],
            "MAX": colors.brown[0],
            "FLOAT": colors.green[0],
        }
        if self.action_type:
            return color_map[self.action_type]
        return colors.red[0]

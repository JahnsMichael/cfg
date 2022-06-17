from libqtile import qtile
from libqtile.widget.tasklist import TaskList

class CustomTaskList(TaskList):

    def __init__(self, **config):
        super().__init__(**config)

        self.add_callbacks({
            'Button1': self.select_window,
            'Button2': self.kill_window,
            'Button3': self.maximize_window,
            "Button4": self.prev_window,
            "Button5": self.next_window,
        })

    def next_window(self):
        qtile.current_group.cmd_next_window()    
    
    def prev_window(self):
        qtile.current_group.cmd_prev_window()

    def kill_window(self):
        if self.clicked:
            window = self.clicked
            window.group.focus(window, False)
            window.cmd_kill()

    def maximize_window(self):
        if self.clicked:
            window = self.clicked
            window.group.focus(window, False)
            window.cmd_toggle_maximize()

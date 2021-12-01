from libqtile.lazy import lazy

import os
import subprocess
import datetime

HOME = os.path.expanduser('~')
SCRIPTS_DIR = f'{HOME}/.config/qtile/scripts/'

def screenshot(qtile):
    date = datetime.datetime.now().strftime("%m%d%Y-%H%M%S")
    filename = os.path.expanduser(f'~/Pictures/Screenshots/{date}.png')
    qtile.cmd_spawn(f'maim -s | tee {filename} | xclip -selection clipboard -t image/png', shell=True)
    
def xrandr():
    active_monitors = get_monitors()
    all_monitors = get_monitors(all=True)
    cmd = "xrandr "
    if (len(active_monitors) > 1):
        for i in range(1, len(active_monitors)):
            cmd += f"--output {active_monitors[i]} --auto --right-of {active_monitors[i-1]} "
    else:
        for i in range(1, len(all_monitors)):
            cmd += f"--output {all_monitors[i]} --off "
    subprocess.call(cmd, shell=True)


def get_monitors(all=False):
    if (all):
        cmd = "xrandr | grep 'connected ' | awk '{ print$1 }'"
    else:
        cmd = "xrandr | grep ' connected ' | awk '{ print$1 }'"
    monitors = subprocess.check_output(
        cmd, shell=True).decode("utf8").splitlines()
    return monitors

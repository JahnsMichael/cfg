from lib.const import MOD
from copy import deepcopy

def get_keys_with_mod(need_mod_keys):
    keys = []
    for need_mod_key in need_mod_keys:
        key = deepcopy(need_mod_key)
        key.modifiers.append(MOD)
        keys.append(key)
    return keys
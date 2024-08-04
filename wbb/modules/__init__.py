import glob
import importlib
import sys
from os.path import basename, dirname, isfile

def __list_all_modules():
    # Only load the feds module
    mod_paths = glob.glob(dirname(__file__) + "/feds.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f)
        and f.endswith(".py")
        and not f.endswith("__init__.py")
        and not f.endswith("__main__.py")
    ]
    return all_modules

print("[INFO]: IMPORTING MODULES")
importlib.import_module("wbb.modules.__main__")
ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]

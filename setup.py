import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
executables = [
    Executable("Criptografando.py", base = base)
]

buildOptions = dict(
    packages = [],
    includes = ["Tkinter"],
    include_files = [],
    excludes = []
)

setup (
    name = "Criptografia Blkz",
    version = "1.0",
    description = "Criptografador 1.0",
    options = dict (build_exe = buildOptions),
    executables = executables
)

from windows_pathlib import WindowsPathlib as Path
import os


a = Path(os.path.expanduser("~/Desktop"))

print(Path.appdata())
print(Path.cache())
print(Path.cookies())
print(Path.desktop())

print(Path("%APPDATA%/Microsoft"))

Path.close()

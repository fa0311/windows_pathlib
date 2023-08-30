# windows_pathlib

Best Practices for Handling Paths in Windows.

Have you written code like this?

```python
import os
import pathlib as Path

# In Windows, the desktop can be changed to any location. The desktop is not necessarily located in the home directory.
print(Path(os.path.expanduser("~/Desktop")))

# This does not work.
print(Path("%APPDATA%/Microsoft"))

```

windows_pathlib can be used for concise writing.

```python
from windows_pathlib import WindowsPathlib as Path

# C:\Users\username\Desktop
print(Path.desktop())

# C:\Users\username\AppData\Roaming\Microsoft
print(Path("%APPDATA%/Microsoft"))
```

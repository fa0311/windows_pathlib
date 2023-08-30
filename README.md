# windows_pathlib

Best Practices for Handling Paths in Windows.

Have you written code like this?

```python
import os
import pathlib as Path
# In Windows, the desktop can be changed to any location. The desktop is not necessarily located in the home directory.
Path(os.path.expanduser("~/Desktop"))
```

```python
from windows_pathlib import WindowsPathlib as Path
print(Path.desktop()) # C:\Users\username\Desktop
print(Path("%APPDATA%/Microsoft")) # C:\Users\username\AppData\Roaming\Microsoft
```

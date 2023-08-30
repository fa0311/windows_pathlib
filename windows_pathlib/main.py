import pathlib
import winreg
import os


class WindowsPathlib(type(pathlib.Path()), pathlib.Path):
    _windowsFoldersRegistryKey = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders",
    )

    def __new__(cls, *args, **kwargs):
        for key, value in os.environ.items():
            if args[0].upper().startswith(f"%{key.upper()}%"):
                args = (f"{value}{args[0][len(key) + 2:]}", *args[1:])
        self = pathlib.Path(*args, **kwargs)
        return self

    @classmethod
    def _get_winreg_key(cls, key):
        return winreg.QueryValueEx(cls._windowsFoldersRegistryKey, key)[0]

    @classmethod
    def close(cls):
        winreg.CloseKey(cls._windowsFoldersRegistryKey)

    @classmethod
    def appdata(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("AppData"))

    @classmethod
    def cache(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Cache"))

    @classmethod
    def cookies(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Cookies"))

    @classmethod
    def desktop(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Desktop"))

    @classmethod
    def favorites(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Favorites"))

    @classmethod
    def history(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("History"))

    @classmethod
    def local_appdata(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Local AppData"))

    @classmethod
    def my_music(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("My Music"))

    @classmethod
    def my_pictures(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("My Pictures"))

    @classmethod
    def my_video(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("My Video"))

    @classmethod
    def nethood(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("NetHood"))

    @classmethod
    def personal(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Personal"))

    @classmethod
    def printhood(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("PrintHood"))

    @classmethod
    def programs(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Programs"))

    @classmethod
    def recent(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Recent"))

    @classmethod
    def sendto(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("SendTo"))

    @classmethod
    def startmenu(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Start Menu"))

    @classmethod
    def startup(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Startup"))

    @classmethod
    def templates(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("Templates"))

    @classmethod
    def downloads(cls) -> "pathlib.WindowsPath":
        return cls(cls._get_winreg_key("{374DE290-123F-4565-9164-39C4925E467B}"))

import mpris2
import subprocess

from time import sleep

SPOTIFY_URI = "org.mpris.MediaPlayer2.spotify"


class MprisInterfaces:
    def __init__(self, uri):
        dbus_interface_info = {"dbus_uri": uri}
        self.player = mpris2.Player(dbus_interface_info=dbus_interface_info)
        self.mediaPlayer2 = mpris2.MediaPlayer2(
            dbus_interface_info=dbus_interface_info
        )

    def is_ad(self) -> bool:
        return not bool(self.player.CanGoNext)

    def print_meta(self):
        print(self.player.Metadata)


def spawn_spotify() -> subprocess.Popen:
    spotify_process = subprocess.Popen("spotify")
    sleep(1)
    return spotify_process


def start_spotify() -> MprisInterfaces:
    _ = spawn_spotify()
    spotify_interfaces = MprisInterfaces(SPOTIFY_URI)
    spotify_interfaces.player.Play()
    return spotify_interfaces


def watch_spotify():
    spotify_interfaces = start_spotify()
    while True:
        if spotify_interfaces.is_ad():
            spotify_interfaces.mediaPlayer2.Quit()
            sleep(1)
            spotify_interfaces = start_spotify()
        else:
            sleep(3)


if __name__ == "__main__":
    watch_spotify()

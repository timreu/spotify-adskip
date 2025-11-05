import mpris2
import subprocess

from time import sleep

SPOTIFY_URI = "org.mpris.MediaPlayer2.spotify"


def spawn_spotify() -> subprocess.Popen:
    spotify_process = subprocess.Popen("spotify")
    sleep(1)
    return spotify_process


def get_spotify_player() -> mpris2.Player:
    dbus_interface_info = {"dbus_uri": SPOTIFY_URI}
    player = mpris2.Player(dbus_interface_info=dbus_interface_info)
    return player


def start_spotify() -> [subprocess.Popen, mpris2.Player]:
    spotify_process = spawn_spotify()
    player_interface = get_spotify_player()
    player_interface.Play()
    return spotify_process, player_interface


def print_meta(player):
    print(player.Metadata)


def is_ad(player: mpris2.Player) -> bool:
    return not bool(player.CanGoNext)


def watch_spotify():
    spotify_process, player_interface = start_spotify()
    while True:
        if is_ad(player_interface):
            spotify_process.kill()
            spotify_process = spawn_spotify()
            player_interface = get_spotify_player()
            player_interface.Play()
        else:
            sleep(3)


if __name__ == "__main__":
    watch_spotify()

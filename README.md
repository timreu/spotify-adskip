# Python-based spotify ad skipper
This script skips over spotify ads by restarting the spotify app. Works on Linux
using dbus/mpris2 interface.

## How to install:
Install Python version and dependancies specified in pyproject.toml. spotify
must be in your `PATH` and named `spotify`.

## How to use:
Start spotify by starting the script main.py.

## How it works:
On startup, spotify will never play an ad. Using dbus/mpris2 interface, you can
make spotify start playing after spawning the app. Ads cannot be skipped. 
dbus`s [mpris2.Player](https://mpris2.readthedocs.io/en/latest/interfaces.html#mpris2.Player)
has the property [CanGoNext](https://mpris2.readthedocs.io/en/latest/interfaces.html#mpris2.Player.CanGoNext)
, which is accessible through dbus. When realizing you cannot go next, the script
terminates the app and restarts it.  

### Ideas for improvement:
* make this into a Gnome extension
* The mpris2.Player interface has a dbus signal [PropertiesChanged](https://mpris2.readthedocs.io/en/latest/interfaces.html#mpris2.Player.PropertiesChanged) 
which is broadcasted, when e.g. the song changes. One could listen to this and 
check `CanGoNext` only, when this signal is broadcasted, instead of polling it
every few seconds.
* spotify starts in the foreground after an ad. Minimize it after spawning.

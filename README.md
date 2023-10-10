# Quod Libet Shuffling Repeat Plugin

A plugin for [Quod Libet](https://github.com/quodlibet/quodlibet) that shuffles and restarts the playlist every time it ends.

It uses a somewhat hacky way to accomplish this and while it worked fine for me, it may shuffle other playlists if they have the exact same content (including order), even if they have different names.

## How to install it

You can follow the [developer docs](https://quodlibet.readthedocs.io/en/latest/development/plugins.html) to add any plugin to Quod Libet.

For Flatpak the way to add a plugin is to add the python file (.py extention) to the `~/.var/app/io.github.quodlibet.QuodLibet/config/quodlibet/plugins/` directory (you may have to create the `plugins` directory yourself).

When installing, you should try [shufflingrepeat1.py](shufflingrepeat1.py) first and if it doesn't work, try [shufflingrepeat2.py](shufflingrepeat2.py). If neither work, you're out of luck here.

## Why are there 2 versions

I initially made [shufflingrepeat1.py](shufflingrepeat1.py) for my working Flatpak installation of Quod Libet, but after I found out it no longer worked, when the Flatpak installation started having weird problems (such as lacking font anti-aliasing, which occurred on both Quod Libet and all other GTK apps using Wayland), I created [shufflingrepeat2.py](shufflingrepeat2.py).

Now, after installing Quod Libet without Flatpak and having it work properly, [shufflingrepeat1.py](shufflingrepeat1.py) began working once more but [shufflingrepeat2.py](shufflingrepeat2.py) stopped working.

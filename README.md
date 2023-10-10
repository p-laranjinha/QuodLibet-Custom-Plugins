# Quod Libet Shuffling Repeat Plugin

A plugin for [Quod Libet](https://github.com/quodlibet/quodlibet) that shuffles and restarts the playlist every time it ends.

It uses a somewhat hacky way to accomplish this and while it worked fine for me, it shuffles other playlists if they have the exact same content (including order), even if they have different names.

## How to use it

You can follow the [developer docs](https://quodlibet.readthedocs.io/en/latest/development/plugins.html) to add any plugin to Quod Libet.

For Flatpak (the install method I use) the way to add a plugin is to add the python file (.py extention) to the `~/.var/app/io.github.quodlibet.QuodLibet/config/quodlibet/plugins/` directory (you may have to create the `plugins` directory yourself).

But you'll have to figure it out yourself for other operating systems or for any other install method there may be.

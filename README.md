# Quod Libet Custom Plugins

Some plugins for Quod Libet I wanted but couldn't find elsewhere.

Currently I only have 1 plugin, and I'm not really planning on adding more. Repo has this name/description just in case I find something else I want.

## How to use them

You can follow the [developer docs](https://quodlibet.readthedocs.io/en/latest/development/plugins.html) to add any plugin to Quod Libet.

For Flatpak (the install method I use) the way to add a plugin is to add the python file (.py extention) to the `~/.var/app/io.github.quodlibet.QuodLibet/config/quodlibet/plugins/` directory (you may have to create the `plugins` directory yourself).

But you'll have to figure it out yourself for other operating systems or for any other install method there may be.

## Plugins

### [Repeat Shuffle](repeatshuffle.py)

Shuffles and restarts the playlist every time it ends.

It uses a somewhat hacky way to accomplish this and while it worked fine for me, there exists the risk of it shuffling other playlists if they have the exact same content (I don't actually know because I barely know how Quod Libet works).

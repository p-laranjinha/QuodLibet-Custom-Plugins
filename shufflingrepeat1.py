from quodlibet.plugins.playorder import RepeatPlugin
from quodlibet.qltk import Icons
from quodlibet.util.dprint import print_d
from quodlibet.library.song import SongLibrary

class ShufflingRepeat(RepeatPlugin):
    PLUGIN_ID = "Shuffling Repeat"
    PLUGIN_NAME = "Shuffling Repeat"
    PLUGIN_ICON = Icons.MEDIA_PLAYLIST_REPEAT
    PLUGIN_DESC = "Shuffles and restarts the playlist every time it ends."
    display_name = "Shuffle and repeat all"
    accelerated_name = "Shuffle and repeat all"

    def next(self, playlist, iter):

        # If not at the end of the playlist, return
        next = self.wrapped.next(playlist, iter)
        if next:
            return next

        # Should shuffle all playlists with the same content, but only does the active one?
        # Good that it works but weird
        for other_playlist in SongLibrary.librarian.playlists._contents.values():
            if other_playlist.songs == playlist.get():
                other_playlist.shuffle()
    
        self.wrapped.reset(playlist)
        print_d("Shuffling and restarting song list")
        return playlist.get_iter_first()
from quodlibet.plugins.playorder import RepeatPlugin
from quodlibet.qltk import Icons
from quodlibet.util.dprint import print_d
from quodlibet.library.song import SongLibrary

class RepeatListShuffle(RepeatPlugin):
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
        
        # Shuffles all playlists with the same content (including order)
        # and saves the new first song of the shuffled playlist
        new_first_song = None
        for other_playlist in SongLibrary.librarian.playlists._contents.values():
            if other_playlist.songs == playlist.get():
                other_playlist.shuffle()
                new_first_song = other_playlist.songs[0]
        
        # Traverses backwards through GTK.TreeIter objects until it finds
        # the one corresponding to the new_first_song
        for song in reversed(playlist.get()):
            if song == new_first_song:
                self.wrapped.reset(playlist)
                return iter
            iter = self.wrapped.previous(playlist, iter)
        # playlist.get_iter_first() can't be used as it returns the
        # first song before shuffling instead of the new_first_song
        return None
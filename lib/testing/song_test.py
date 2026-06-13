#!/usr/bin/env python3

from song import Song

HALL_AND_OATES = "Hall and Oates"

Song.count = 0
Song.genre_count = {}
Song.artist_count = {}

class TestSong:
    '''Class "Song" in song.py'''

    Song("All eyes on Me", "2pac", "Rap")
    Song("Humble African", "Joseph Hill", "Reggae")
    Song("Smells Like Teen Spirit", "Nirvana", "Rock")

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", HALL_AND_OATES, "Pop")
        assert(out_of_touch.name == "Out of Touch")
        assert(out_of_touch.artist == HALL_AND_OATES)
        assert(out_of_touch.genre == "Pop")

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        assert(Song.count == 4)
        Song("Sara Smile", HALL_AND_OATES, "Pop")
        assert(Song.count == 5)

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        assert("Rap" in Song.genres)
        assert("Pop" in Song.genres)
        assert("Rock" in Song.genres)

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        assert("Nirvana" in Song.artists)
        assert("2pac" in Song.artists)
        assert(HALL_AND_OATES in Song.artists)
        
    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        assert(Song.genre_count["Rap"] == 1)
        assert(Song.genre_count["Pop"] == 2)
        assert(Song.genre_count["Rock"] == 1)

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        assert(Song.artist_count["2pac"] == 1)
        assert(Song.artist_count["Joseph Hill"] == 1)
        assert(Song.artist_count["Nirvana"] == 1)
        assert(Song.artist_count[HALL_AND_OATES] == 2)
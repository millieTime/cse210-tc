# Keeps track of the songs and levels available. Will have a collection of all the information
# on songs we have.

# Collection:
#  song:
#    bpm
#    albumImage
#    level
#    level
#    level
#  song:
#    bpm
#    albumImage
#    level
#    level
#  song:
#    bpm
#    albumImage
# etc.
from game import constants
from game.game_song import GameSong
import os


class Library():

    def __init__(self):
        """ the initializer.
        Populates self._song_dict with GameSong objects.
        """
        # Get the directory for the songs
        PATH = constants.DIRROOT + "/assets/songs/"
        self._song_dict = {}
        # Go through each folder in the songs folder
        for song in os.listdir(PATH):
            if song != ".DS_Store":
                song_path = PATH + song + "/"
                self._parse_folder(song_path)

    def _parse_folder(self, folder_path):
        # Get all the files in the song's folder
        file_list = os.listdir(folder_path)
        song_file = ""
        album_art = ""
        level_list = []
        # Check if each file is a level or the song
        for file in file_list:
            # If the last three characters are txt, it's a level
            if file[-3:] == "txt":
                level_list.append(file)
            # it might be an image though
            elif file[-3:] == "jpg" or file[-3:] == "png":
                album_art = file
            # it's probably a sound file.
            else:
                song_file = file
        if song_file and level_list:
            game_song = GameSong(folder_path, song_file, level_list, album_art)
            self._song_dict[game_song.get_song_name()] = game_song
        else:
            print("abandoned folder:", folder_path)

    def get_song_names(self):
        return list(self._song_dict)

    def get_song(self, key):
        return self._song_dict[key]


"""
lib = Library()
print(lib.get_song_names())
selection = input("which song? ")
song = lib.get_song(selection)
print(song.get_song())
print(song.get_song_name())
print(song.get_art())
print(song.get_level_names())
print(song.get_level_files())
print(song.get_level_file(0))
"""

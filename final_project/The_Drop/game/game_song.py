from game import constants
class GameSong:

    def __init__(self, folder_path = "", song_file = "", level_list = [], album_art = ""):
        self._base_path = folder_path
        self._audio = song_file
        self._level_list = level_list
        self._art = album_art
        self._difficulty = ""
        with open(self._base_path + self._level_list[0], 'r') as level_file:
            self._difficulty = int(level_file.readline().split(',')[2])


    def get_song(self):
        return self._base_path + self._audio

    def get_song_name(self):
        # we have an audio, so remove underscores and extension and add difficulty.
        return f'{self._audio[:-4].replace("_", " ")} ({constants.DIFFICULTY_NAMES[self._difficulty]})'

    def get_art(self):
        if not self._art:
            return None
        return self._base_path + self._art

    def get_level_names(self):
        name_list = []
        for level in self._level_list:
            # We want only the level part.
            #split will get a list of the stuff between underscores, and we want the
            #last bit. Then take off the file extension.
            name_list.append(level.split("_")[-1][:-4])
        return name_list
    
    def get_level_file(self, index):
        return self._base_path + self._level_list[index]

    def get_level_files(self):
        file_list = []
        for index in range(len(self._level_list)):
            file_list.append(self.get_level_file(index))
        return file_list

    def get_difficulty(self):
        return self._difficulty
    
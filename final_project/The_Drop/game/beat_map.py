#import os
from game import constants
from game.beat import Beat

# beat oject = (letterName/key, time when the beat hits)


class BeatMap:

    def __init__(self):
        self._beatList = []

    def get_beats(self):
        return self._beatList

    def get_max_score(self):
        return len(self._beatList) * constants.BEAT_POINTS

    def read_file(self, file, countdown):
        # file_name = os.path.basename(file)
        with open(file, "r") as f:
            imported_file = f.readlines()
            contents = imported_file.pop(0)
            # First line contains song data.
            metrics = contents.split(",")
            first_beat = float(metrics[0]) + countdown
            time_between_beats = float(metrics[1])
            time_in_measure = time_between_beats * 12

            for index in range(len(imported_file)):
                measure = imported_file[index].split(",")
                for spot, char in enumerate(measure):
                    if (char == "q" or char == "w" or char == "e" or char == "r"):
                        beat_timing = first_beat + time_between_beats * \
                            spot + (time_in_measure * index)
                        a_beat = Beat(char, beat_timing - time_in_measure)# IT WAS OUT OF SINK BY ONE BEAT. MIGHT NEED TO CHANGE THIS BACK ON FASTER COMPUTERS
                        self._beatList.append(a_beat)


""" b = Beat_Map()
b.read_file(os.path.basename(
    '/Users/matthewrapp/Documents/GitHub/School/Winter2021/cse210/cse210-tc/final_project/Believer.txt')) """
<<<<<<< HEAD
# Is given the name of a file, opens the file, reads the inputs from the file, and constructs a list of Beats from the inputs
# When called upon, will return the list of Beats
=======
import os
from game.beat import Beat

PATH = os.path.dirname(os.path.abspath(__file__))

# beat oject = (letterName/key, time when the beat hits)


class Beat_Map:

    def __init__(self):
        self._beatList = []

    def getBeats(self):
        return self._beatList

    def read_file(self, file):
        # file_name = os.path.basename(file)
        with open(file, "r") as f:
            imported_file = f.readlines()
            contents = imported_file.pop(0).split('\n')
            # First line contains song data.
            metrics = contents.pop(0).split(",")
            first_beat = float(metrics[0])
            time_between_beats = float(metrics[1])

            for index in range(len(imported_file)):
                measure = imported_file[index]
                for spot, char in enumerate(measure):
                    if (char == "q" or char == "w" or char == "e" or char == "r"):
                        time_in_measure = time_between_beats * 12
                        beat_timing = time_between_beats * \
                            spot + (time_in_measure * index)
                        a_beat = Beat(char, beat_timing)
                        self._beatList.append(a_beat)


b = Beat_Map()
b.read_file(os.path.basename(
    '/Users/matthewrapp/Documents/GitHub/School/Winter2021/cse210/cse210-tc/final_project/Believer.txt'))
>>>>>>> 6ab0924535e16aa9517fefee3f439e70699efd91

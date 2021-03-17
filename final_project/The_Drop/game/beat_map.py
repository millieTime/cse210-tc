import os
from game.beat import Beat

# beat oject = (letterName/key, time when the beat hits)


class BeatMap:

    def __init__(self):
        self._beatList = []

    def get_beats(self):
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


# b = Beat_Map()
# b.read_file(os.path.basename(
#     '/Users/matthewrapp/Documents/GitHub/School/Winter2021/cse210/cse210-tc/final_project/Believer.txt'))

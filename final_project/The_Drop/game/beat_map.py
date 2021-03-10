import os
# from game import constants
PATH = os.path.dirname(os.path.abspath(__file__))


class Beat_Map:

    def __init__(self):
        self._beatList = []

    def getBeats(self):
        return self._beatList

    def read_file(self, file):
        file_name = os.path.basename(file)
        with open(file, "r") as f:
            beat = f.read()
            beatInfo = {
                'beat_name': file_name,
                'beat': beat
            }
            self._beatList.append(beatInfo)
            print(self._beatList)


# b = Beat_Map()
# b.read_file(os.path.basename(
#     '/Users/matthewrapp/Documents/GitHub/School/Winter2021/cse210/cse210-tc/final_project/Believer.txt'))

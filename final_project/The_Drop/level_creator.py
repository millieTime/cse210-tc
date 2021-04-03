###    REQUIRES PIP INSTALL KEYBOARD!!
import keyboard
import time
import os

#Next step: keyboard is able to record time stamps, which may make recording levels even more accurate than it currently is!

PATH = os.path.dirname(os.path.abspath(__file__))
class LevelCreator():
    """ Used to create a text file holding the beat information
    for a song. That can then be used to create a level for our game.

    Attrs:
        _twelveth (float): how many seconds per 1/12 of a beat
        _folder (string): the location of the folder
        _file (string): the location of the file
        _delay (float): how many seconds between starting the audio and the first beat
        _string (string): the representation of the level in string format. Will be printed to a file.
        _started (boolean): whether the creator has been started
    """

    def __init__(self, name, level, difficulty, delay, twelveth):
        self._twelveth = twelveth
        self._folder = PATH + "\\assets\\songs\\" + name.replace(" ", "_")
        self._file = self._folder + f'\\{name.replace(" ", "_")}_{level.replace(" ", "_")}.txt'
        self._delay = delay
        self._difficulty = difficulty
        self._string = ""
        self._started = False

    def _start(self):
        """begins timing"""
        self._started = True
        self._covered_time = time.perf_counter()
    
    def key_pressed(self, key):
        """Logs that a key was pressed. Calculates the time since the 
        last key, and adds spaces to _string to account for that time.
        Then adds the key that was pressed.
        
        Args:
            key (string): a single character representing the key pressed.
        """
        if not self._started:
            self._start()
        elapsed = time.perf_counter() - self._covered_time
        # Subtract 1. That 1 represents the space for the key just pressed.
        spaces_to_add = round(elapsed / self._twelveth) - 1
        self._covered_time += (spaces_to_add + 1) * self._twelveth
        self._string += " " * spaces_to_add + key

    def stop(self):
        """Cease monitoring keys, format _string, and write to a file."""
        keyboard.unhook_all()
        self.key_pressed("s")

        os.makedirs(self._folder, exist_ok=True)
        with open(self._file, "w") as outfile:
            final_str = f"{self._delay},{self._twelveth},{self._difficulty}"
            for index, char in enumerate(self._string):
                # One beat per line, and we've split each beat into 12 parts.
                if index % 12 == 0:
                    final_str += "\n"
                final_str += char + ","
            outfile.write(final_str)
        print("File write complete.")

def get_float(prompt):
    float_response = -1
    accepted = False
    while not accepted:
        response = input(prompt)
        try:
            print(response)
            response = float(response)
            accepted = True
        except:
            print("Invalid input.")
    return float(response)

print(
"""\nThis program helps you build a level.
When instructed, start playing the song, return to this terminal,
and begin pressing Q, W, E, and R on the beats you want the arrows
to strike. When you're done, press 's' to stop.

You will need to find out how much time passes between the song starting and the first beat.
That way the first beat of the game will align with the first beat of the song.""")
input("\n press enter to begin entering preliminary information. . . ")
bpm = get_float("What is the BPM of the song? (helps with auto-aligning input to beats) ")
seconds_per_twelveth = 5 / bpm # 1/bpm * 60s/m * 1/12 (to catch triplets and 16ths)
name = input("What is the name of the song? ")
level = input("What level will this be? (1, 2, drums, drums 2, etc) ")
difficulty = input("What is the difficulty? (0-3) ")
delay = get_float("How long before the first beat? (in seconds, with decimal) ")
print("\nNow, we will build the level.")
print("Start the song, and press keys to begin recording.")

creator = LevelCreator(name, level, difficulty, delay, seconds_per_twelveth)
keyboard.on_press_key("q", lambda evt: creator.key_pressed(evt.name), True)
keyboard.on_press_key("w", lambda evt: creator.key_pressed(evt.name), True)
keyboard.on_press_key("e", lambda evt: creator.key_pressed(evt.name), True)
keyboard.on_press_key("r", lambda evt: creator.key_pressed(evt.name), True)

keyboard.wait('s', True)
creator.stop()
print(f"Your level file is in assets/songs/{name}")
from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 
""" The main file controls the flow from intro to game to outro.
It's not a class right now, but it definitely should be.

Stereotype: Controller
"""

def run():
    """Controls the flow of the game."""
    pre_game()
    Screen.wrapper(main)
    post_game()

def main(screen):
    """ sets up the interface with the screen, and starts the game.

    Args:
        screen (Screen): an instance of Screen to interact with.
    """
    input_service = InputService(screen)
    output_service = OutputService(screen)
    director = Director(input_service, output_service)
    director.start_game()

def pre_game():
    """Displays instructions"""
    print('''
  **********************************
          WELCOME TO SPEED!!
  **********************************
    
Type the words you see before they get
to the edge of the screen! Hit enter
after typing a word to send it back to
the start and increase your score. Did
you type a word wrong? Press enter to
clear it out. As you go, the game will
speed up; try to get the next high score!
    ''')
    input('press enter to continue')

def post_game():
    """Gets, displays, and updates the top 10 high scores."""
    scores = read_scores()
    if scores:
        scores = update_scores(scores)
        print_and_save(scores)

def read_scores():
    """Tries to read the high-scores file into a list.
    If something's wrong, it lets the user know.
    
    Returns:
        list: the contents of the file in list format.
    """
    scores = []
    backup = []
    try:
        with open("high-scores.txt", "r") as infile:
            backup = infile.readlines()
            for line in backup:
                scores.append(line.replace("\n", "").split(" "))
    except:
        pass
    # If there aren't 11 items in the list (top 10, and most recent score),
    # then there's been a problem.
    if len(scores) < 11:
        print("An error occured when reading high-scores.txt.")
        print("Are you in the correct directory (game)? Is the file formatted correctly?")
        with open("high-scores.txt", "w") as outfile:
            outfile.write("".join(backup))
        return
    return scores

def update_scores(scores):
    """Adds the user's score to the list in the correct spot.
    Removes the lowest score.

    Args:
        scores (List): the top ten scores, and the user's score.
    """
    score = int(scores.pop()[0])
    input("\n****\nGame Over, Press Enter to Continue: ")
    print("\nYour score: ", score)
    name = input("Enter your name: ").replace(" ", "_")
    rank = 10
    while rank > 0 and score > int(scores[rank - 1][1]):
        rank -= 1
    scores.insert(rank, [name, str(score)])
    return scores[:10]

def print_and_save(scores):
    """Displays the top ten scores and writes them to the file.
    
    Args:
        scores (List): a list of the top ten scores.
    """
    print("High Scores: ")
    for index, item in enumerate(scores):
        item = " ".join(item)
        print("\t", item)
        scores[index] = item
    with open("high-scores.txt", "w") as outfile:
        outfile.write("\n".join(scores))

response = input("***Is your directory set to the speed_project\\speed\\game folder? (y/n): ")
if response == "y":
    run()
else:
    print("Please use 'cd' to change your directory to the speed_project\\speed\\game folder.")
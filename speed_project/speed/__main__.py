from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):
    input_service = InputService(screen)
    output_service = OutputService(screen)
    director = Director(input_service, output_service)
    director.start_game()

def end_game():
    scores = []
    try:
        with open("high-scores.txt", "r") as infile:
            for line in infile.readlines():
                scores.append(line.replace("\n", "").split(" "))
    except:
        pass
    if not scores:
        print("An error occured when reading high-scores.txt. Is it empty?")
        return
    score = int(scores.pop()[0])
    input("Game Over, Press Enter to Continue: ")
    print("\nYour score: ", score)
    name = input("Enter your name: ").replace(" ", "_")
    
    rank = 10
    while rank > 0 and score > int(scores[rank - 1][1]):
        rank -= 1
    scores.insert(rank, [name, str(score)])
    scores.pop()
    print("High Scores: ")
    for index, item in enumerate(scores):
        item = " ".join(item)
        print("\t", item)
        scores[index] = item
    with open("high-scores.txt", "w") as outfile:
        outfile.write("\n".join(scores))

response = input("***Are you running this from the speed_project\\speed\\game folder? (y/n): ")
if response == "y":
    Screen.wrapper(main)
    end_game()
else:
    print("Please use cd to change your directory to the speed_project\\speed\\game folder.")
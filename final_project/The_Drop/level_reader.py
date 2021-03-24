import time
import os

PATH = os.path.dirname(os.path.abspath(__file__)) + "\\assets\\songs\\"

print("Here are the known songs:")
folder_list = os.listdir(PATH)
for folder in folder_list:
    if folder == ".DS_Store":
        folder_list.remove(folder)
print(" ** ".join(folder_list))
song = input("\nWhich would you like to use? ")
PATH += song + "\\"
print("\nHere are the known levels:")
file_list = os.listdir(PATH)
for file in file_list:
    if file[-3:] != "txt":
        file_list.remove(file)
print(" ** ".join(file_list))
level = input("\nWhich would you like to open? ")
file_name = PATH + level
contents = []
metrics = []
delay = 0
seconds_per_twelveth = 0
with open(file_name, "r") as infile:
    contents = infile.readlines()
    # First line contains song data.
    metrics = contents.pop(0).split(",")
    delay = float(metrics[0])
    seconds_per_twelveth = float(metrics[1])
    for index in range(len(contents)):
        # :-2 to leave off the \n at the end of each line.
        contents[index] = contents[index][:-2].split(",")
    print("Okay, have the audio ready to play.")
    input("Press enter to begin sync countdown!")
    print("Hit play in 4. . .")
    time.sleep(1)
    print("3. . .")
    time.sleep(1)
    print("2. . .")
    time.sleep(1)
    print("1. . ")
    time.sleep(1)
    print("Now!")
    time.sleep(delay)
    # Get the current computer time as accurately as possible.
    start_time = time.perf_counter()
    # keeps track of how many twelveths of a beat should have passed.
    counter = 0
    for line in contents[:-1]: # Last element is just a \n
        for char in line:
            counter+=1
            if not char == " ":
                print(char)
            # start_time + counter*seconds is what time we want to run the next cycle.
            # subtract the current time, and you're left with how much time you still need to wait.
            sleep_time = start_time + counter*seconds_per_twelveth - time.perf_counter()
            # If it's less than zero, skip the waiting! Otherwise, sleep.
            if sleep_time > 0:
                time.sleep(sleep_time)
import time

file_name = input("Which file to open? ")
print("Okay, have the audio ready to play.")
input("Press enter to begin sync countdown!")
with open(file_name, "r") as infile:
    contents = infile.readlines()
    # First line contains song data.
    metrics = contents.pop(0).split(",")
    delay = float(metrics[0])
    seconds_per_twelveth = float(metrics[1])
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
    for line in contents:
        # :-2 to leave off the \n at the end of each line.
        line = line[:-2].split(",")
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
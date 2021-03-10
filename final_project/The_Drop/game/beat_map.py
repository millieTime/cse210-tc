
def __init__(self):
    pass

def _set_map(self):
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
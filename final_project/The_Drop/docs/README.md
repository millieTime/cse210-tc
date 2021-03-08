# **Final Project Plan**
• _&#39; The Drop &#39;_

- What program are we going to create? Use your brainstorming from the solo checkpoint to answer this question together.
  - We are going to create a program, like &#39;Guitar Hero&#39;, where the user must press keys, to a song, at a certain time. If they hit the right key at the right time, they get points, if they don&#39;t, they lose points.
- What technologies will we use? The answer to this question is mostly already decided. Just take a minute to remind yourselves of the language, libraries and anything else you plan on using.
  - Python, Arcade, GitHub
- What is your timeline? The answer to this question is mostly already decided. Just take a minute to review the rest of the course schedule together.
  - Next week: complete super basic necessities. (Stuff comes down the screen, and if you press a button at a roughly-right time you get points. Else no points).
  - Week after: Make it work.
  - Last week: Make it EPIC.

**Feature List:**

- **Necessities**
  - 1 song
  - Simple Graphics &amp; timing
  - Correct key bindings
  - Scoring
    - Buffer Space
      - +5 on correct
      - -5 on missed
  - Board/Layout
    - X &amp; Y planes
    - Where to put score
    - Where to put user name
    - Are the notes coming down, going up?
    - Buffer of each note?
- **Stretch Goals**
  - Levels
    - Easy, Medium, Hard
  - 2 Players
  - Ok / good / perfect
  - Holding down notes/tapping notes
  - Golden Notes
  - Images/Graphics (RTX on)
  - THEME of game
  - NAME of game
  - High score
  - Unlock themes / songs
  - Star Power (wubzz?) from correct notes in a row (and Bonus Visuals)

**Class List:**

- **Main**
  - Description
    - Start the game
- **Beat**
  - Description
    - Generate the individual beat
    - Inherits from arcade.Sprite
    - Center\_y() &amp; Center\_x()
- **Beat Map/Board**
  - Description
    - Generating the board
    - Read the level file and create beats at the right time
- **Constants**
  - Description
    - Not necessarily a class, but just contains variables.
- **Player**
  - Description
    - Initialize each player
    - Has a name, and a score.
- **Input**
  - Description
    - Will handle the user input
- **Output**
  - Description
    - Will handle the output
    - Handle audio &amp; visuals
- **Score**
  - Description
    - Handles the score
    - Extra special scoring
    - Golden Notes, Whammy Bar, Streak (Star Power), etc.
- **High Scores**
  - Description
    - Handles the high scores
    - Reads the high scores file and returns
- **Library**
  - Description
    - Stores information on each song
    - Album art, bpm, difficulties and scores, length




## Project Structure
---
The project files and folders are organized as follows:
```
root                      (project root folder)
+-- docs                  (project documentation)
+-- rename                [rename this folder and description]
  +-- assets              (program asset files)
  +-- data                (program data files)
  +-- game                (program source code)
    +-- __init__.py       (python package file)
    +-- beat_map.py       (contains the Beat_Map class)
    +-- beat.py           (contains the Beat class)
    +-- constants.py      (contains important constants)
    +-- input.py          (contains the Input class)
    +-- library.py        (contains the Library class)
    +-- output.py         (contains the Output class)
    +-- player.py         (contains the Player class)
    +-- score_handler.py  (contains the Score_handler class)
    +-- score.py          (contains the Score class)
  +-- __init__.py         (python package file)
  +-- __main__.py         (entry point for program)
+-- LICENSE               (license file)
+-- README.md             (general info)
```
## Authors
---
Preston Millward - mil18037@byui.edu

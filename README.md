# SAISandbox
"Semi" artificial intelligence sandbox

# Challenge

Decide which team is the winning team and then just implement the code so that your team wins! Best solutions wins the ticket to Star Wars premiere on the 14th of December at Finnkino Tennispalatsi!

# Deadline

Deadline for the challenge is on the 8th of December 2016.

# How to apply?

Fill your contact information in [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdP5XzFXOa1vu61R_JwB0A5KopR4RRhUKA-QEwvzEZLZPh4nQ/viewform?c=0&w=1) and fork this repository. Create a pull request after you've finalized your code before deadline. You will be contacted on the 9th of December 2016.

# Factions

BrownRebelScumbagWithLaser aka Brown

WhiteManWithLazer aka White

# Rules

You can only modify challenge.py from this repository. Change the winning team of your choice by changing value of `WINNER` variable using enums defined TEAMS (WHITE or BROWN).

The run method from a chosen team will be run on every loop on the main loop.

The team that should lose will stay put for the whole game.

# Methods

You can check the methods from models.py for more information. Basic methods that you can use are:

* move_left
* move_right
* move_up
* move_down
* shoot

All of the move methods will return False if there is an obstacle.

# Setup

1. Install git
2. Install python 2.7.x
3. Install python pip
4. Install pygame
5. Clone repository
6. run command `cd SAISandbox ; pip install -r requirements.txt`

# Run game

Use following command `python game.py` and the game will automatically end after one of the teams are dead. The game will print to terminal "You win" or "You lose" depending if the team you decided to win actually won.
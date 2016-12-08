from models import ManWithLaser, DIRECTIONS
from colors import WHITE, RED, GREEN, BROWN
from enum import Enum

MAP_HEIGHT = 10
MAP_WIDTH = 10

TEAMS = Enum('WHITE', 'BROWN')
WINNER = TEAMS.WHITE #Define your team
class WhiteManWithLaser(ManWithLaser):
    color = WHITE
    beam = GREEN
    moves = 0
    stuckUp = False
    stuck = 0
    rightBlocks = 0
    
    def run(self):

        #If cannot get to the right go to Stuck mode
        if self.rightBlocks > 3:
            self.rightBlocks = 0
            self.stuck = 5
            self.stuckUp = not self.stuckUp
            print "Stuck"

        #Back up if stuck
        if self.stuck > 0:
            if self.stuckUp:
                self.move_left()
                self.move_up()
                self.stuck -= 1
                self.moves = 0
            else:
                self.move_left()
                self.move_down()
                self.stuck -= 1
                self.moves = 0
        else:
            #Kill enemies below
            if self.moves > MAP_WIDTH + MAP_HEIGHT:
                self.move_down()
                self.shoot()

            #Kill enemies above
            elif self.moves > MAP_WIDTH:
                self.move_up()
                self.shoot()
                self.moves += 1
            else:
                #Towards the enemies
                if self.move_right():
                    self.moves += 1
                else:
                    #Increase right blocked couter
                    self.rightBlocks += 1
                    #And try to move up and down
                    if not self.move_up():
                        if not self.move_down():
                            #Cannot move up or down: stuck
                            self.stuck = 5
                            self.stuckUp = not self.stuckUp
                            print "Stuck"

class BrownRebelScumbagWithLaser(ManWithLaser):
    color = BROWN
    beam = RED
    def run(self):
        self.move_left()

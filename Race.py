'''
#  Assignment 2 - A Horse Race
#  Name: JangHeon Yoo
#  uID: u1628436
'''
from graphics import *
from Dice import *
import time

#horse class to represent each racer and movement
class Horse:
    def __init__(self, speed, y, image, window):
        self.x_pos = 0
        self.speed =speed
        self.y_pos = y
        self.image = image
        self.window = window
        #for checking the horse's speed
        self.speed_dice = Dice(speed)

    #roll the dice when horse move
    def move(self):
        self.x_pos +=  self.speed_dice.roll()

    #redraw horse at its current location is changed
    def draw(self):
        self.image.undraw()
        self.image.draw_at_pos(self.window,self.x_pos,self.y_pos)

    # Check if the horse crossed or reached the finish line
    def crossed_finish_line(self,x):
        return self.x_pos >= x








def main():
    #set window
    win = GraphWin("horse Race",700,350)

    #making finising line and checking the x_pos of finishing line
    finishing_line_x = 600
    finish_line = Line(Point(finishing_line_x,0),Point(finishing_line_x,350))
    finish_line.setWidth(3)
    finish_line.draw(win)

    #every horse's image
    horse1 = Image(Point(0,0), "horse1.gif")
    horse2 = Image(Point(0,0), "horse2.gif")
    horse3 = Image(Point(0,0), "horse3.gif")

    # setting the status of the horse
    horse_1 = Horse(6,50,image=horse1,window=win)
    horse_2 = Horse(8, 120, image=horse2, window=win)
    horse_3 = Horse(10, 200, image=horse3, window=win)

    # draw all the horse at the starting position
    horse_list = [horse_1,horse_2,horse_3]
    for horse_check in horse_list:
        horse_check.draw()
    win.getMouse()

    #checking the all the race
    racing = True
    while racing:
        time.sleep(0.05)

        for horse in horse_list:
            horse.move()
            horse.draw()

            #checking the event if the horse arrived at the finising line
            if horse.crossed_finish_line(finishing_line_x):
                racing = False

        finish_line.undraw()
        finish_line.draw(win)

    #winning condition check
    win1 = horse_1.crossed_finish_line(finishing_line_x)
    win2 = horse_2.crossed_finish_line(finishing_line_x)
    win3 = horse_3.crossed_finish_line(finishing_line_x)

    #checking the winner and save the winner's name in the winner_check
    winner =[win1,win2,win3]
    winner_number = 1
    winner_check = []
    for check_winner in winner:
        if check_winner == True:
            winner_check.append(winner_number)
        winner_number += 1

    # print the winner's naem or Tie player's name
    if len(winner_check) == 1:
        print(f"Horse {winner_check[0]} is the winner")
    if len(winner_check) > 1:
        tie = f"Tie horse {winner_check[0]}"

        for num in winner_check[1:]:
            tie = tie + f" with Horse {num}"

        print(tie)

    #wiat for a final mouse click before closing the window
    win.getMouse()
    win.close()

#check the main function
if __name__ == "__main__":
    main()

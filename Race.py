from graphics import *
from Dice import *
import time

class Horse:
    def __init__(self, speed, y, image, window):
        self.x_pos = 10
        self.speed =speed
        self.y_pos = y
        self.image = image
        self.window = window

        self.speed_dice = Dice(speed)

    def move(self):
        self.x_pos +=  self.speed_dice.roll()

    def draw(self):
        self.image.undraw()
        self.image.draw_at_pos(self.window,self.horse_x,self.y)

    def crossed_finish_line(self,x):
        return self.x_pos >= x








def main():
    win = GraphWin("horse Race",700,350)

    finishing_line_x = 600
    finish_line = Line(Point(finishing_line_x,0),Point(finishing_line_x,350))
    finish_line.setWidth(3)
    finish_line.draw(win)

    horse1 = Image(Point(0,0), "horse1.gif")
    horse2 = Image(Point(0,0), "horse2.gif")
    horse3 = Image(Point(0,0), "horse3.gif")

    horse_1 = Horse(6,50,image=horse1,window=win)
    horse_2 = Horse(8, 120, image=horse2, window=win)
    horse_3 = Horse(10, 200, image=horse3, window=win)

    horse_list = [horse_1,horse_2,horse_3]

    for horse_check in horse_list:
        horse_check.draw()

    win.getMouse()

    racing = True
    while racing:
        time.sleep(0.05)

        for horse in horse_list:
            horse.move()
            horse.draw()

            if horse.crossed_finish_line(finishing_line_x):
                racing = False

        finish_line.undraw()
        finish_line.draw(win)

    win1 = horse_1.crossed_finish_line(finishing_line_x)
    win2 = horse_2.crossed_finish_line(finishing_line_x)
    win3 = horse_3.crossed_finish_line(finishing_line_x)

    winner =[win1,win2,win3]
    winner_number = 1
    winner_check = []
    for check_winner in winner:
        if check_winner == True:
            winner_check.append(winner_number)
        winner_number += 1


    if len(winner_check) == 1:
        print(f"Horse {winner_check[0]} is the winner")
    if len(winner_check) > 1:
        tie = f"Tie horse {winner_check[0]}"

        for num in winner_check[1:]:
            tie = tie + f" with Horse {num}"

        print(tie)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()

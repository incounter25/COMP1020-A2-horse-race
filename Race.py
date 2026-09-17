"""
Assignment by JangHeon YOO
U1628436
Assignment_A1

"""

from graphics import *


def draw_fun_shape(x,y,win):

    #draw the main case of x-box device
    device = Rectangle(Point(x+70,y+100),Point(x-70,y-70))
    device.setFill("black")
    device.draw(win)

    #This will be the body of x_box logo
    logo = Circle(Point(x,y),55)
    logo.setFill("limegreen")
    logo.setWidth(3)
    logo.draw(win)

    #draw the first crossline in logo
    f_line = Line(Point(x-40,y-40),Point(x+40,y+40))
    f_line.setFill("white")
    f_line.setWidth(12)
    f_line.draw(win)

    #draw the seconde crossline in logo
    s_line = Line(Point(x+40,y-40),Point(x-40, y+40))
    s_line.setFill("white")
    s_line.setWidth(12)
    s_line.draw(win)




def main():
    win = GraphWin("Assignment_1",600,600,autoflush=False) #draw the window
    win.setBackground("grey") # set the grey background.

    while True:

        #check the screen is while open
        if win.isClosed():
            break

        #re-draw the image of draw_fun_shape
        win.clear_win()

        #checking the location of mouse
        mouse_pos = win.getMousePosition()

        #checking the x,y position of mouse again
        if mouse_pos is not None:
            x_mouse = mouse_pos.getX()
            y_mouse = mouse_pos.getY()

            #draw the image, and cheaking the right location of image
            draw_fun_shape(x_mouse,y_mouse,win)

        #updating
        win.update()



if __name__ == "__main__":
    main()
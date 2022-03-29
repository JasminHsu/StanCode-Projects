"""
File: bouncing_ball.py
Name: Jasmin Hsu
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce
reduces y velocity to REDUCE of itself
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
counted = 1  # Calculate the number of runs


def main():
    """
    After create the ball in the right place, use campy
    mouse event to simulate bouncing process
    """

    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(bounce)


def bounce(mouse):
    global GRAVITY
    global counted
    vy = GRAVITY

    # To make sure that the bouncing process will not be affected by clicking mouse
    # Also make sure this game can only repeat 3 times
    if ball.x == START_X and ball.y == START_Y and counted < 4:
        while True:
            ball.move(VX, vy)
            # Before hitting the ground, the falling speed increases with gravity
            if ball.y + SIZE < window.height and ball.x < window.width:
                vy += GRAVITY

            # When the ball hits the ground, the ball bounces and its raising speed decreases with a constant REDUCE
            elif ball.y + SIZE >= 0 and ball.x < window.width:
                vy = -vy * REDUCE
                if vy > 0:
                    vy *= -1  # Ensure the number remains negative

            # When the ball hits the right wall, one run of game is finished
            elif ball.x >= window.width:
                break
            pause(DELAY)
        window.add(ball, START_X, START_Y)  # The ball returns to original position
        counted += 1


if __name__ == "__main__":
    main()

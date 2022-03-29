"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

When the player break all the bricks, he wins
But if he fails to catch the ball three times, he loses
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    speed_x = graphics.get_dx()
    speed_y = graphics.get_dy()
    lives = NUM_LIVES

    # Add animation loop here
    while True:
        pause(FRAME_RATE)
        if graphics.valid and lives > 0:
            pause(FRAME_RATE)
            graphics.ball.move(speed_x, speed_y)
            # The ball bounces when it hits the left and right walls
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                speed_x = -speed_x
            # The ball bounces when it hits the upper walls
            if graphics.ball.y <= 0:
                speed_y = -speed_y
            # When ball goes out and dies
            if graphics.ball.y >= graphics.window.height:
                graphics.window.remove(graphics.ball)
                lives -= 1
                graphics.valid = False
                if lives > 0:  # Reset the ball
                    graphics.random_speed()
                    speed_x = graphics.get_dx()
                    graphics.window.add(graphics.ball, x=(graphics.window_width-graphics.ball.width)/2,
                                        y=(graphics.window_height-graphics.ball.height)/2)
            # When player breaks all bricks
            if graphics.num_brick == 0:
                graphics.show_win()
                break
            if graphics.collision():
                speed_y = graphics.get_dy()
        # When player fails to break all bricks in limited attempts
        elif lives == 0:
            graphics.show_fail()
            break


if __name__ == '__main__':
    main()


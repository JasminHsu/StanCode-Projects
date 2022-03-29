"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).


INITIAL_Y_SPEED = 12   # Initial vertical speed for the ball.
MAX_X_SPEED = 7        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Initialize variable
        self.valid = False
        self.num_brick = brick_cols * brick_rows  # Calculate how many bricks do we have

        # Create a graphical window, with some extra space
        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle_exit = True

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window_width-ball_radius*2)/2,
                          y=(self.window_height-ball_radius*2)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j < 2:
                    self.brick.color = 'darkorange'
                    self.brick.fill_color = 'darkorange'
                elif j < 4:
                    self.brick.color = 'gold'
                    self.brick.fill_color = 'gold'
                elif j < 6:
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                elif j < 8:
                    self.brick.color = 'navajowhite'
                    self.brick.fill_color = 'navajowhite'
                else:
                    self.brick.color = 'lemonchiffon'
                    self.brick.fill_color = 'lemonchiffon'
                self.window.add(self.brick, x=i*(brick_width+brick_spacing),
                                y=brick_offset+j*(brick_height+brick_spacing))

        # Default initial velocity for the ball
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self._dx = -self._dx

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start_ball)

    # Valid click to start the game
    def start_ball(self, mouse):
        self.valid = True

    def move_paddle(self, mouse):
        if mouse.x <= self.paddle_width/2:
            self.window.add(self.paddle, x=0, y=self.window_height-self.paddle_offset-self.paddle_height)
        elif mouse.x >= self.window_width-self.paddle_width/2:
            self.window.add(self.paddle, x=self.window_width-self.paddle_width,
                            y=self.window_height-self.paddle_offset-self.paddle_height)
        else:
            self.window.add(self.paddle, mouse.x-self.paddle_width/2,
                            y=self.window_height-self.paddle_offset-self.paddle_height)
        if not self.paddle_exit:
            self.window.remove(self.paddle)

    # Create different velocity for the ball
    def random_speed(self):
        self._dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self._dx = -self._dx

    # Getter
    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    # Determine if the ball hits something
    def collision(self):
        # Upper left of the ball
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            self.bounce()
            return True
        # Upper right of the ball
        if self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y) is not None:
            self.bounce()
            return True
        # Bottom right of the ball
        if self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height) is not None:
            self.bounce()
            return True
        # Bottom left of the ball
        if self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height) is not None:
            self.bounce()
            return True

    # Determine what the ball hits and bounce
    def bounce(self):
        if self.ball.y >= self.window.height*0.5:  # Hit the paddle
            if self._dy > 0:
                self._dy = -self._dy

        if self.ball.y < self.window.height*0.5:  # Hit the bricks

            # Remove bricks and calculate how many bricks are left

            # Upper left of the ball
            if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
                self.num_brick -= 1
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
            # Upper right of the ball
            if self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y) is not None:
                self.num_brick -= 1
            self.window.remove(self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y))
            # Bottom right of the ball
            if self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height) is not None:
                self.num_brick -= 1
            self.window.remove(self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height))
            # Bottom left of the ball
            if self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height) is not None:
                self.num_brick -= 1
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height))

            self._dy = -self._dy

    def show_win(self):
        self.paddle_exit = False
        self.window.remove(self.paddle)
        # why can not remove paddle
        self.window.remove(self.ball)
        # self.paddle.color = 'white'
        # self.paddle.fill_color = 'white'
        win = GLabel('You Win')
        win.font = '-50'
        win.color = 'red'
        self.window.add(win, x=(self.window_width-win.width)/2, y=(self.window_height-win.height)/2)

    def show_fail(self):
        fail = GLabel('Game Over')
        fail.font = '-50'
        fail.color = 'red'
        self.window.add(fail, x=(self.window_width-fail.width)/2, y=(self.window_height-fail.height)/2)

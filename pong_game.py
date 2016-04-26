# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    rand_x = random.randrange(2,4)
    rand_y = random.randrange(1,3)
    if direction == RIGHT:
        ball_vel = [rand_x,-rand_y]
    else:
        ball_vel = [-rand_x,-rand_y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, RIGHT, LEFT  # these are ints
    spawn_ball(LEFT)
    
        
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle((ball_pos[0], ball_pos[1]), BALL_RADIUS, 3, "White", "White")        
    # update paddle's vertical position, keep paddle on the screen
    dist_vertical_ball_top = ball_pos[1] - BALL_RADIUS
    dist_vertiacl_ball_bottom = ball_pos[1] + BALL_RADIUS - HEIGHT
    if dist_vertical_ball_top == 0 or dist_vertiacl_ball_bottom == 0:
        ball_vel[1] *= -1
    # draw paddles
    
    # determine whether paddle and ball collide    
    dist_horizontal_ball_left_paddle = ball_pos[0] - PAD_WIDTH - 0.01
    dist_horizontal_ball_right_paddle = ball_pos[0] + PAD_WIDTH -WIDTH + 0.01
    if dist_horizontal_ball_left_paddle < 0 or dist_horizontal_ball_right_paddle > 0:
        ball_vel[0] = ball_vel[1] = 0
        new_game()
    # draw scores
        
'''def keydown(key):
    global paddle1_vel, paddle2_vel 
   
def keyup(key):
    global paddle1_vel, paddle2_vel'''

 
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
'''frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)'''


# start frame
new_game()
frame.start()
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    rand_x = random.randrange(2,4)
    rand_y = random.randrange(1,3)
    if direction == RIGHT:
        ball_vel = [rand_x,-rand_y]
    else:
        ball_vel = [-rand_x,-rand_y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, RIGHT, LEFT  # these are ints
    spawn_ball(LEFT)
    
        
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle((ball_pos[0], ball_pos[1]), BALL_RADIUS, 3, "White", "White")        
    # update paddle's vertical position, keep paddle on the screen
    dist_vertical_ball_top = ball_pos[1] - BALL_RADIUS
    dist_vertiacl_ball_bottom = ball_pos[1] + BALL_RADIUS - HEIGHT
    if dist_vertical_ball_top == 0 or dist_vertiacl_ball_bottom == 0:
        ball_vel[1] *= -1
    # draw paddles
    
    # determine whether paddle and ball collide    
    dist_horizontal_ball_left_paddle = ball_pos[0] - PAD_WIDTH - 0.01
    dist_horizontal_ball_right_paddle = ball_pos[0] + PAD_WIDTH -WIDTH + 0.01
    if dist_horizontal_ball_left_paddle < 0 or dist_horizontal_ball_right_paddle > 0:
        ball_vel[0] = ball_vel[1] = 0
        new_game()
    # draw scores
        
'''def keydown(key):
    global paddle1_vel, paddle2_vel 
   
def keyup(key):
    global paddle1_vel, paddle2_vel'''

 
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
'''frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)'''


# start frame
new_game()
frame.start()


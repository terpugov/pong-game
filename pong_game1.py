# Implementation of classic arcade game Pong

import simpleguitk as simplegui
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
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    rand_x = random.randrange(2,5)
    rand_y = random.randrange(1,4)
    if direction:
        ball_vel = [rand_x,-rand_y]
    else:
        ball_vel = [-rand_x,-rand_y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, RIGHT, LEFT  # these are ints
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(LEFT)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, RIGHT, LEFT
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
   
    # draw ball
    canvas.draw_circle((ball_pos[0], ball_pos[1]), BALL_RADIUS, 4, "White", "White")        
    # update paddle's vertical position, keep paddle on the screen

    paddles1_x1 = paddle1_pos[0] - HALF_PAD_WIDTH
    paddles1_x2 = paddle1_pos[0] + HALF_PAD_WIDTH 
    paddles1_y2 = paddle1_pos[1] + HALF_PAD_HEIGHT
    paddles1_y1 = paddle1_pos[1] - HALF_PAD_HEIGHT
    paddles2_x1 = paddle2_pos[0] + HALF_PAD_WIDTH
    paddles2_x2 = paddle2_pos[0] - HALF_PAD_WIDTH 
    paddles2_y1 = paddle2_pos[1] - HALF_PAD_HEIGHT
    paddles2_y2 = paddle2_pos[1] + HALF_PAD_HEIGHT
    
 
    if paddles1_y1 < 0 and paddle1_vel<0 or paddles1_y2 > HEIGHT and paddle1_vel >0:
        paddle1_vel = 0
    if paddles2_y1 < 0 and paddle2_vel<0 or paddles2_y2 > HEIGHT and paddle2_vel >0:
        paddle2_vel = 0
    
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    

    
         
    # draw paddles
    canvas.draw_polygon(([paddles1_x1, paddles1_y1], [paddles1_x2, paddles1_y1], [paddles1_x2, paddles1_y2], [paddles1_x1, paddles1_y2]), 1 , "White", "White")
    canvas.draw_polygon(([paddles2_x1, paddles2_y1], [paddles2_x2, paddles2_y1], [paddles2_x2, paddles2_y2], [paddles2_x1, paddles2_y2]), 1 , "White", "White")
    # determine whether paddle and ball collide  
   
#    dist_ball_rightpaddle = math.sqrt((ball_pos[0] - paddles2_x1)**2 + (ball_pos[1] - paddles2_x2)**2)
#    if dist_ball_rightpaddle <= 0:
#        ball_vel[0] *= -1
    
    # colide with paddle
    #left paddle
    if (ball_pos[0] + ball_vel[0]) <= (BALL_RADIUS + PAD_WIDTH ) and (ball_pos[1] + ball_vel[1] + BALL_RADIUS > paddles1_y1 and ball_pos[1] + ball_vel[1] - BALL_RADIUS < paddles1_y2):
        ball_vel[0] *= -1
        ball_vel[0] = ball_vel[0] + ball_vel[0]*0.1
    #right paddle
    elif (ball_pos[0] + ball_vel[0]) >= (WIDTH - BALL_RADIUS - PAD_WIDTH ) and (ball_pos[1] + ball_vel[1] + BALL_RADIUS > paddles2_y1 and ball_pos[1] - BALL_RADIUS < paddles2_y2):
        ball_vel[0] *= -1
        ball_vel[0] = ball_vel[0] + ball_vel[0]*0.1

    # collide with border
    if ball_pos[1] + ball_vel[1] < BALL_RADIUS or ball_pos[1] + ball_vel[1] > HEIGHT - BALL_RADIUS: 
        ball_vel[1] *= -1
    
    if ball_pos[0] + ball_vel[0] < BALL_RADIUS + PAD_WIDTH: 
        ball_vel[0] = ball_vel[1] = 0
        score1 += 1 
        LEFT = True
	RIGTH = False
        new_game()

    if ball_pos[0] + ball_vel[0] > WIDTH - BALL_RADIUS - PAD_WIDTH:
        ball_vel[0] = ball_vel[1] = 0
        score2 += 1
        LEFT = False
	RIGTH = True
        new_game()

    # print score on the canvas
    canvas.draw_text(str(score1), (3*WIDTH/4, 50 ), 40, 'Red')
    canvas.draw_text(str(score2), (WIDTH/4, 50), 40, 'Red')  

def keydown(key):
    global paddle1_vel, paddle2_vel

    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 4
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel += 4

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

def restart_handler():
    global score1, score2
    new_game()
    score1 = 0
    score2 = 0

 
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT, 300)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart_button = frame.add_button('Restart', restart_handler) 


# start frame
new_game()
frame.start()
# Implementation of classic arcade game Pong


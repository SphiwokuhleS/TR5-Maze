import random
import turtle
import time




obst = [
        (-85, 175), (-30, 175), (30, 175) , (80, 175),
        (-56, 150), (0, 150),(56, 150),
        (-85, 120), (-30, 120), (30, 120), (80, 120),
        (-56, 95), (0, 95), (56, 95),
        (-85, 70), (-30, 70), (30, 70), (80, 70),
        (-56, 45), (0, 45), (56, 45),
        (-85, 20), (-30, 20), (30, 20), (80, 20),
        (-56, 0), (-30,0),(30, 0),
        (-85, -25), (-30,-25), (30, -25),(80, -25),
        (-56, -60), (0, -60), (56,-60),
        (-85, -95), (-30, -95), (30, -95), (80, -95),
        (-56, -120), (0, -120), (-56, -120),
        (-85, -145), (-30, -145), (30, -145), (80, -145),
        (-56, -175), (0, -175), (56, -175),
        (-85, -185), (-30, -185), (30, -185), (80, -185)
    ]

n = 5

def generate_coords():
    """
    This function is for randomly generating random obstacles on the barrier
    """
    global obst
    ran = random.randint(10,10)
    for coord in range(ran):
        x_y = (random.randint(-85, 85), random.randint(-185, 185))
        obst.append(x_y)
    return obst

    
def show_obstacles(obst):
    """
    Prints out the obstacles coords in the required formart
    """

    if obst:
        print("There are some obstacles:")
        for obstacle in obst:
            print('- At position ' + str(obstacle[0]) +','+str(obstacle[1])+ ' (to '+ str(obstacle[0]+4)+ ','+ str(obstacle[1]+4) + ')')

def draw_obstacle_line_x_pos(x,y):
    """
    This function will draw a line from x,y to the right 
    :x is starting x_coordinate position.
    :y is starting x_coordinate position.
    """
    global obst
    for i in range(n):
        x_y = (x,y)
        x+=4
        obst.append(x_y)

def draw_obstacle_line_x_neg(x,y):
    """
    This function will draw a horizontal line from x,y to the left
    :x is starting x_coordinate position.
    :y is starting x_coordinate position.
    """
    global obst
    for i in range(n):
        x_y = (x,y)
        x-=4
        obst.append(x_y)

def draw_obstacle_line_y_pos(x,y):
    """
    This function will draw a vertical line from x,y to the top
    :x is starting x_coordinate position.
    :y is starting x_coordinate position.
    """
    global obst
    for i in range(5):
        x_y = (x,y)
        y+=4
        obst.append(x_y)

def draw_obstacle_line_y_neg(x,y):
    """
    This function will draw a vertical line from x,y to the bottom
    :x is starting x_coordinate position.
    :y is starting x_coordinate position.
    """
    global obst
    for i in range(5):
        x_y = (x,y)
        y-=4
        obst.append(x_y)

def is_position_blocked(x, y): #coord[0] =x coord[1]=y
    """
    This function checks if current x,y coordinate is in an obstacle coordinate
    """
    check_x = False
    check_y = False

    for obstacle in obst: #check x
        check_x = False
        check_y = False
        if x >= obstacle[0] and x <= obstacle[0]+4:
            check_x = True
        if y >= obstacle[1] and y <= obstacle[1]+4:
            check_y = True
    
        if check_x and check_y == True:
            return True 
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    This function checks if there is an obstacle in the way of current x,y and x,y destination
    Returns True if there is an obstacle in the way and returns False if there isn't 
    """
    check_x = False
    check_y = False
    step = 4
    steps_n = -4
    if is_neg(x2) or is_neg(y2): step = steps_n

    for x in range(x1, x2, step):
        if is_position_blocked(x, y2):
            check_x = True
            return True
    for y in range(y1, y2, step):
        if is_position_blocked(x2, y):
            check_y = True
            return True
    return False


def draw_maze_obstacle(x,y):
    """
    This function will be draw
    """
    draw_obstacle_line_x_pos(x,y)
    draw_obstacle_line_x_neg(x,y)
    draw_obstacle_line_y_neg(x,y)        
    draw_obstacle_line_y_pos(x,y)

def setup_maze_obstacles():
    global obst
    f = len(obst)
    for i in range(f):
        draw_maze_obstacle(obst[i][0], obst[i][1])
    obst = set(obst)

#setup maze obstacles
setup_maze_obstacles()

def return_obstacles():
    return obst

def reset_obstacle():
    global obst
    obst = []

def get_obstacles():
    return obst  

def is_neg(number):
    """
    checks if a given number is negative or positive
    :returns a boolean.
    """
    if number < 0:
        return True
    elif number > 0:
        return False
    return False

def delete_list():
    global obstacles
    obstacles = []

def check_obstacle():
    
    if is_path_blocked(old_x, old_y, new_x, new_y):
        return True
    return False
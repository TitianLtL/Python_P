import turtle
import random

# --- GAME CONFIGURATION ---
WIDTH, HEIGHT = 600, 600
TILE_SIZE = 20

# 1 = Wall, 0 = Pellet (Food)
MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,1,1,0,1,0,0,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,1,0,1,1,0,0,0,0,1],
    [1,1,1,0,1,1,0,0,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,0,0,0,1,1,0,1,1,1],
    [1,0,0,0,0,1,1,0,1,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,0,0,1,0,1,1,0,1],
    [1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# --- SCREEN SETUP ---
screen = turtle.Screen()
screen.title("Easy Python Pac-Man")
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)
screen.tracer(0) # Turns off automatic screen updates for smoother rendering

# --- GAME OBJECTS ---
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("yellow")
pacman.penup()
pacman.speed(0)

ghost = turtle.Turtle()
ghost.shape("square")
ghost.color("red")
ghost.penup()
ghost.speed(0)

# --- STATE VARIABLES ---
score = 0
pellets = []
walls = []

# Pacman / Ghost grid positions
pm_x, pm_y = 1, 1
gh_x, gh_y = 13, 13

# Direction vectors
pm_dx, pm_dy = 0, 0
gh_dx, gh_dy = -1, 0

# --- HELPER FUNCTIONS ---
def to_screen_coord(grid_x, grid_y):
    """Converts grid index matrix coordinates to screen pixel coordinates."""
    screen_x = -((len(MAZE[0]) * TILE_SIZE) / 2) + (grid_x * TILE_SIZE) + (TILE_SIZE / 2)
    screen_y = ((len(MAZE) * TILE_SIZE) / 2) - (grid_y * TILE_SIZE) - (TILE_SIZE / 2)
    return screen_x, screen_y

def draw_maze():
    """Draws the static maze components and tracks entity locations."""
    global pellets, walls
    for y in range(len(MAZE)):
        for x in range(len(MAZE[y])):
            sx, sy = to_screen_coord(x, y)
            if MAZE[y][x] == 1:
                pen.penup()
                pen.goto(sx - 10, sy + 10)
                pen.color("blue")
                pen.begin_fill()
                for _ in range(4):
                    pen.forward(TILE_SIZE)
                    pen.right(90)
                pen.end_fill()
                walls.append((x, y))
            elif MAZE[y][x] == 0:
                pen.penup()
                pen.goto(sx, sy - 2)
                pen.color("white")
                pen.dot(4)
                pellets.append((x, y))

# --- MOVEMENT INPUTS ---
def go_up():    global pm_dx, pm_dy; pm_dx, pm_dy = 0, -1
def go_down():  global pm_dx, pm_dy; pm_dx, pm_dy = 0, 1
def go_left():  global pm_dx, pm_dy; pm_dx, pm_dy = -1, 0
def go_right(): global pm_dx, pm_dy; pm_dx, pm_dy = 1, 0

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# --- INITIALIZATION ---
draw_maze()

# --- MAIN GAME LOOP ---
def game_loop():
    global pm_x, pm_y, gh_x, gh_y, gh_dx, gh_dy, score

    # 1. Update Pacman Position (Tile check)
    next_pm_x = pm_x + pm_dx
    next_pm_y = pm_y + pm_dy
    if (next_pm_x, next_pm_y) not in walls:
        pm_x, pm_y = next_pm_x, next_pm_y

    # 2. Check Pellet Collisions
    if (pm_x, pm_y) in pellets:
        pellets.remove((pm_x, pm_y))
        score += 10
        # Erase dot by drawing a black square over it
        sx, sy = to_screen_coord(pm_x, pm_y)
        pen.penup()
        pen.goto(sx - 8, sy + 8)
        pen.color("black")
        pen.begin_fill()
        for _ in range(4):
            pen.forward(16)
            pen.right(90)
        pen.end_fill()

    # 3. Update Ghost Position & Simple AI
    next_gh_x = gh_x + gh_dx
    next_gh_y = gh_y + gh_dy
    
    # If ghost hits a wall, find a random open alternative direction
    if (next_gh_x, next_gh_y) in walls or random.random() < 0.2:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        valid_directions = []
        for dx, dy in directions:
            if (gh_x + dx, gh_y + dy) not in walls:
                valid_directions.append((dx, dy))
        if valid_directions:
            gh_dx, gh_dy = random.choice(valid_directions)
    else:
        gh_x, gh_y = next_gh_x, next_gh_y

    # 4. Update Screen Visual Locations
    px, py = to_screen_coord(pm_x, pm_y)
    pacman.goto(px, py)

    gx, gy = to_screen_coord(gh_x, gh_y)
    ghost.goto(gx, gy)

    screen.update()

    # 5. Check Win/Loss Conditions
    if pm_x == gh_x and pm_y == gh_y:
        print(f"Game Over! Final Score: {score}")
        return
    
    if not pellets:
        print(f"You Win! Final Score: {score}")
        return

    # Repeat loop every 200ms
    screen.ontimer(game_loop, 200)

# Start execution
game_loop()
turtle.done()

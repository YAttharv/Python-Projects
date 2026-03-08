
import turtle
import random
import time

WIDTH, HEIGHT = 800, 400
FINISH_LINE = 9 * HEIGHT / 20
MAX_RACERS = 10  # 10
COLORS = [
    'red',
    'blue',
    'green',
    'orange',
    'yellow',
    'pink',
    'cyan',
    'brown',
    'purple',
    'black',
]


def get_num_of_racers():
    while True:
        racers = input(f"How many racers(2 - {MAX_RACERS}): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Enter a number")
            continue

        if 2 <= racers <= MAX_RACERS:
            return racers
        else:
            print(f"must be between 2 to {MAX_RACERS}")

def initiate_turtles():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")
    screen.cv._rootwindow.attributes("-topmost", True) # Puts the window on top
    return screen

def getColors(colors, numOfRacers):
    random.shuffle(colors)
    color_list = colors[:numOfRacers]
    return color_list

def create_turtles(colors, screen):
    screen.tracer(0)
    turtles = []
    numOfRacers = len(colors)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(((WIDTH/(numOfRacers+1))*(i+1)) - (WIDTH/2), -(9 * HEIGHT / 20))
        racer.pendown()
        turtles.append(racer)
    screen.update()
    screen.tracer(1)
    return turtles

def race_turtles(colors, screen):
    turtles = create_turtles(colors, screen)
    screen.tracer(0)
    while True:
        for racer in turtles:
            distance = random.randint(1, 5)
            racer.forward(distance)
        screen.update()
        time.sleep(0.05)
        for racer in turtles:
            x, y = racer.pos()
            if y >= FINISH_LINE:
                return colors[turtles.index(racer)]


numOfRacers = get_num_of_racers()
color_list = getColors(COLORS, numOfRacers)
screen = initiate_turtles()
winner = race_turtles(color_list, screen)
print(f"Winner: {winner}")
turtle.done()
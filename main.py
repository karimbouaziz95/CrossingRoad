import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
screen.onkeypress(fun=player.move_up, key="Up")
#screen.onkeypress(fun=player.move_down, key="Down")

game_is_on = True
cars = []
sleep_time = 0.1
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    random_int = random.randint(1, 6)
    if random_int == 6:
        cars.append(CarManager())


    for car in cars:
        car.move()
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if cars and cars[0].xcor() <= -340:
        cars.pop(0)
    
    if player.ycor() >= 280:
        player.reset_position()
        score.level_up()
        sleep_time *= 0.9

        
screen.update()
screen.exitonclick()

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 270)

        self.level = 1
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)


    def game_over(self):
        self.clear()
        self.goto(0, 270)
        self.write("Game over", move=False, align="center", font=FONT)
        self.goto(self.xcor(), self.ycor() - 20)
        self.write(f"Final score: {self.level}", move=False, align="center", font=FONT)



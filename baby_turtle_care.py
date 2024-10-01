import tkinter as tk
import turtle
import random

class RunawayGame:
    def __init__(self, canvas, baby_turtle1, baby_turtle2, caring_turtle, catch_radius=50):
        self.canvas = canvas
        self.baby_turtle1 = baby_turtle1
        self.baby_turtle2 = baby_turtle2
        self.caring_turtle = caring_turtle
        self.catch_radius2 = catch_radius ** 2

        self.baby_turtle1.shape('turtle')
        self.baby_turtle1.color('Sea Green')
        self.baby_turtle1.penup()
        self.baby_turtle1.initial_position = (-200, 0)

        self.baby_turtle2.shape('turtle')
        self.baby_turtle2.color('Sea Green')
        self.baby_turtle2.penup()
        self.baby_turtle2.initial_position = (200, 0)

        self.caring_turtle.shape('turtle')
        self.caring_turtle.color('green')
        self.caring_turtle.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.caring_turtle.penup()
        self.caring_turtle.initial_position = (0, 0)

        # Instantiate another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

        # Timer variables
        self.time_elapsed = 0
        self.time_limit = 60  # 60-second limit
        self.is_time_up = False

        # Score variable
        self.score = 0  # Initialize score

    def is_catched(self):
        p = self.baby_turtle1.pos()
        q = self.baby_turtle2.pos()
        r = self.caring_turtle.pos()
        dx1, dy1 = p[0] - r[0], p[1] - r[1]
        dx2, dy2 = q[0] - r[0], q[1] - r[1]

        caught = False
        if dx1 ** 2 + dy1 ** 2 < self.catch_radius2:
            self.baby_turtle1.setpos(self.baby_turtle1.initial_position)  # Return to initial position
            self.score += 1  # Increment score when caught
            caught = True
        elif dx2 ** 2 + dy2 ** 2 < self.catch_radius2:
            self.baby_turtle2.setpos(self.baby_turtle2.initial_position)  # Return to initial position
            self.score += 1  # Increment score when caught
            caught = True
        return caught

    def start(self, init_dist=400, ai_timer_msec=100):
        self.baby_turtle1.setpos(self.baby_turtle1.initial_position)
        self.baby_turtle1.setheading(0)
        self.baby_turtle2.setpos(self.baby_turtle2.initial_position)
        self.baby_turtle2.setheading(90)
        self.caring_turtle.setpos(0, 0)
        self.caring_turtle.setheading(180)

        # Timer interval
        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, 1000)  # Update every 1 second

    def step(self):
        # Update the timer if time is not up
        if not self.is_time_up:
            self.time_elapsed += 1  # Increment by 1 second

            # Check if time limit is reached
            if self.time_elapsed >= self.time_limit:
                self.is_time_up = True

        # If time is up, display the final message and stop the game
        if self.is_time_up:
            self.drawer.undo()
            self.drawer.penup()
            self.drawer.setpos(-260, 260)
            # Show the level when the game is over
            if self.score <= 0:
                self.drawer.write(f"Your caring level is {self.score}..  You need more practice :(", font=("Arial", 12, "bold"))
            else:
                self.drawer.write(f"Your caring level is {self.score} !  You did a great job :)", font=("Arial", 12, "bold"))
            return  # Stop the game by exiting the function

        self.baby_turtle1.run_ai(self.caring_turtle.pos(), self.caring_turtle.heading())
        self.baby_turtle2.run_ai(self.caring_turtle.pos(), self.caring_turtle.heading())
        self.caring_turtle.run_ai(self.baby_turtle1.pos(), self.baby_turtle1.heading())

        # Update score if caught
        self.is_catched()

        self.drawer.undo()
        self.drawer.penup()

        # Calculate remaining time
        remaining_time = max(0, self.time_limit - self.time_elapsed)

        # Display the remaining time and level status
        self.drawer.setpos(-260, 260)
        self.drawer.write(f'Remaining Work Time: {remaining_time:.0f} sec | Caring level: {self.score}', font=("Arial", 12, "bold"))

        # Ensure the turtles stay within the screen boundaries and handle scoring
        self.check_boundaries(self.baby_turtle1)
        self.check_boundaries(self.baby_turtle2)
        self.check_boundaries(self.caring_turtle)

        # Note) The following line should be the last of this function to keep the game playing
        self.canvas.ontimer(self.step, 1000)

    def check_boundaries(self, turtle_instance):
        if self.is_out_of_bounds(turtle_instance):
            turtle_instance.setpos(turtle_instance.initial_position)  # Return to initial position
            # When the caring turtle went off the screen
            if turtle_instance == self.caring_turtle:
                self.drawer.undo()
                self.drawer.penup()
                self.drawer.setpos(-260, 260)
                self.drawer.write("Working hours are not over yet !  Cheer up", font=("Arial", 12, "bold"))                

    def is_out_of_bounds(self, turtle_instance):
        x, y = turtle_instance.pos()
        return x < -290 or x > 290 or y < -290 or y > 290

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn
        self.name = 'caring_turtle'

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, game, step_move=10, step_turn=30):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn
        self.name = 'runner'
        self.initial_position = None  # Initialize initial_position
        self.game = game

    def run_ai(self, opp_pos, opp_heading):
        # Save initial position upon first movement
        if self.initial_position is None:
            self.initial_position = self.pos()

        mode = random.choices([0, 1, 2], weights=[7, 1.5, 1.5])[0]
        if mode == 0:
            self.forward(self.step_move)
        elif mode == 1:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)

        # Ensure the turtle stays within the screen boundaries
        x, y = self.pos()
        # When the baby turtle went off the screen
        if x < -290 or x > 290 or y < -290 or y > 290:
            self.game.score -= 1
            self.game.drawer.undo()
            self.game.drawer.penup()
            self.game.drawer.setpos(-260, 260)
            self.game.drawer.write("Ouch !  That hurt", font=("Arial", 12, "bold"))   
            self.setpos(self.initial_position)  # Return to initial position             


if __name__ == '__main__':
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk()
    root.title("Turtle Babysitting")
    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("Sky Blue")
    
    baby_turtle1 = RandomMover(screen, None, step_move=50) # Increase step_move for faster speed
    baby_turtle2 = RandomMover(screen, None, step_move=50) # Increase step_move for faster speed
    caring_turtle = ManualMover(screen)
    
    game = RunawayGame(screen, baby_turtle1, baby_turtle2, caring_turtle)
    
    # Assign the game object to turtles after game initialization
    baby_turtle1.game = game
    baby_turtle2.game = game
    
    
    game.start()
    screen.mainloop()

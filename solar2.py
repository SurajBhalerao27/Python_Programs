import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Simulation")
screen.setup(width=800, height=600)

# Create the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2)  # Increase the size of the Sun
sun.penup()

# Create the Earth
earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.shapesize(1)  # Set the size of the Earth
earth.penup()
earth.goto(150, 0)  # Position the Earth at a distance from the Sun

# Create the Moon
moon = turtle.Turtle()
moon.shape("circle")
moon.color("gray")
moon.shapesize(0.5)  # Set the size of the Moon
moon.penup()
moon.goto(200, 0)  # Position the Moon at a distance from the Earth

# Define the motion of the celestial bodies
def animate():
    earth.circle(150)  # Move the Earth in a circular path around the Sun
    moon.circle(50)  # Move the Moon in a circular path around the Earth

    screen.update()
    screen.ontimer(animate, 50)  # Repeat the animation after a delay

# Start the animation
animate()

# Exit the program when the screen is closed
turtle.done()

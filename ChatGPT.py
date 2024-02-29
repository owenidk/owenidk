"OMG IT ACTUALLY WORKS!"


import os
import time

def clear_screen():
    # Function to clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_bouncing_ball():
    clear_screen()

    # Initial position and direction of the ball
    ball_position = 0
    direction = 1

    while True:
        clear_screen()

        # Print empty lines before the ball
        for _ in range(ball_position):
            print()

        # Print the ball
        print("josh is dumb")

        # Print empty lines after the ball
        for _ in range(10 - ball_position):
            print()

        # Update ball position
        ball_position += direction

        # Change direction when hitting top or bottom
        if ball_position == 0 or ball_position == 9:
            direction *= -1

        time.sleep(0.1)  # Adjust speed of animation by changing sleep time

if __name__ == "__main__":
    animate_bouncing_ball()
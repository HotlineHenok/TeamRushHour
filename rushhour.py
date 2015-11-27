import pygame
import boardClass


# Define car colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE1 = (255, 213, 48)
BABYBLUE = (142, 244, 252)
ORANGE2 = (252, 191, 5)
BLUE = (38, 163, 186)
PURPLE = (213, 132, 209)
YELLOW = (249, 246, 86)


# WIDTH and HEIGHT of each grid location
WIDTH = 35
HEIGHT = 35
 
# The margin between each cell
MARGIN = 5

board = boardClass.Board(6, 6)

# Put cars in grid
board.grid[4][0] = 1
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [500, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Rush Hour")
 
# Loop until the user clicks the close button.
done = False
 
# Main loop
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(6):
        for column in range(6):
            color = WHITE
            if board.grid[row][column] == 1:
                color = ORANGE1 
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# To quit
pygame.quit()

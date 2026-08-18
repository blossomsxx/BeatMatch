import pygame
import sys


# ============================================================
# INITIATE GAME
# ============================================================

# initiate game
pygame.init()


# ============================================================
# CONSTANTS
# ============================================================

# constants
WIDTH, HEIGHT = 400, 350

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
slateBlue = (106, 90, 205)

# background colors
steel_blue = (70, 130, 180)
darkSlateBlue = (72, 61, 139)


# ============================================================
# SCREEN SETUP
# ============================================================

# sets instructions and screen properties size, title, and background
print("pay attention to the beats (purple circles) falling down.")
print('press the corresponding keys a, s, k, and l and match them with the corresponding targets.')
print('if you hit the corresponding target, your hit counter will go up. If you miss, your miss counter will go up.')
print('to win, get at least 50 hits. You will lose the game if you get more than 30 misses.')

# creates the game window
screen = pygame.display.set_mode((400, 400))

# sets the title of the game window
pygame.display.set_caption("BeatMatch")

# sets the initial background color
screen.fill((135, 206, 235))


# ============================================================
# FONT SETUP
# ============================================================

# set-up font
try:
    font = pygame.font.SysFont("Arial", 36)  # Use system font
except Exception as e:
    print(f"Font error: {e}")
    pygame.quit()
    sys.exit()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

# defines label creation
def create_label(text, font, text_color, bg_color=None):
    """
    Creates a label surface with optional background color.
    """
    if bg_color:
        return font.render(text, True, text_color, bg_color)
    else:
        return font.render(text, True, text_color)


# defines custom function win game
def winGame():
    green = (0, 128, 0)

    # changes the entire screen to green
    screen.fill(green)

    # creates the winning message
    label_ex = create_label("CONGRATS! YOU WON!", font, BLACK, WHITE)

    # places the winning message in the center of the screen
    label_rect = label_ex.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # draws the winning message onto the screen
    screen.blit(label_ex, label_rect)


# ============================================================
# CLASSES
# ============================================================

# defines class Beat which includes x position, y position, color, size, and speed of movement
class Beat(pygame.sprite.Sprite):
    def __init__(self, x):

        # initializes the Pygame Sprite
        pygame.sprite.Sprite.__init__(self)

        # creates the image/surface that represents the Beat
        self.image = pygame.Surface([30, 30])

        # stores the Beat's x position
        self.x = x

        # stores the Beat's starting y position
        self.y = 0

        # stores the Beat's color
        self.color = slateBlue

        # stores the Beat's size
        self.size = 15

        # stores the Beat's speed of movement
        self.speed = 5

        # creates the rectangular area used to position the Sprite
        self.rect = self.image.get_rect(center=(15, 15))

        # draws the Beat circle onto its image
        pygame.draw.circle(self.image, self.color, (15, 15), self.size)

        # places the Beat at its starting position on the game screen
        self.rect.center = (self.x, self.y)


# ============================================================
# GAME OBJECTS
# ============================================================

# creates a group to store all Beat Sprite objects
beats = pygame.sprite.Group()


# ============================================================
# BACKGROUND
# ============================================================

# background

# draws the large steel blue circles that make up the background
pygame.draw.circle(screen, steel_blue, (51, 400), 175)
pygame.draw.circle(screen, steel_blue, (400, 400), 200)
pygame.draw.circle(screen, steel_blue, (167, 374), 100)
pygame.draw.circle(screen, steel_blue, (215, 330), 100)


# ============================================================
# LINE INTERFACE
# ============================================================

# line interface and targets

# creates the vertical lines separating the four lanes
for i in range(3):

    # x-coordinate changes depending on the loop iteration
    white = (255, 255, 255)
    x = 100 + 100 * i

    # draws the lane line
    pygame.draw.line(screen, white, (x, 0), (x, 400))


# ============================================================
# TARGETS
# ============================================================

# declares target variables

# creates the four target circles
target1 = pygame.draw.circle(screen, darkSlateBlue, (50, 300), 20)
target2 = pygame.draw.circle(screen, darkSlateBlue, (150, 300), 20)
target3 = pygame.draw.circle(screen, darkSlateBlue, (250, 300), 20)
target4 = pygame.draw.circle(screen, darkSlateBlue, (350, 300), 20)


# ============================================================
# BEAT CREATION
# ============================================================

# defines custom createBeats function
def createBeats(x):

    # limits the number of Beats that can exist in the group
    if len(beats) < 20:

        # creates a new Beat at the specified x position
        beat = Beat(x)

        # adds the new Beat object to the beats group
        beats.add(beat)


# ============================================================
# GAME LOOP
# ============================================================

running = True

# game loop
while running:

    # --------------------------------------------------------
    # EVENT HANDLING
    # --------------------------------------------------------

    # gets all events that have occurred since the previous frame
    for event in pygame.event.get():

        # closes the game when the user presses the window's X button
        if event.type == pygame.QUIT:
            running = False

        # checks if keys a,s,k,l are pressed
        elif event.type == pygame.KEYDOWN:

            # checks whether the A key was pressed
            if event.key == pygame.K_a:
                print("a was pressed!")

            # checks whether the S key was pressed
            elif event.key == pygame.K_s:
                print("s was pressed!")

            # checks whether the K key was pressed
            elif event.key == pygame.K_k:
                print("k was pressed!")

            # checks whether the L key was pressed
            elif event.key == pygame.K_l:
                print("l was pressed!")

    # --------------------------------------------------------
    # UPDATE
    # --------------------------------------------------------

    # Need to figure out how to make existing Beats move downward over time.

    # --------------------------------------------------------
    # DRAW
    # --------------------------------------------------------

    # updates the display so everything drawn on the screen becomes visible
    pygame.display.flip()


# ============================================================
# CLEANUP
# ============================================================

# closes Pygame after the game loop ends
pygame.quit()

"""
NOTES TO SELF:
- Adding labels is much more complicated in Pygame than in CMU CS Academy.
  There is no direct "Label" widget, so text must be rendered using a font
  and then drawn onto the screen.

- Added a try-except block to handle potential font setup errors.

- Created a custom function to create labels so text creation can be reused.

- Had to import sys to use sys.exit() in the try-except block.

- pygame.draw.circle(...) draws a circle and returns a Rect describing the
  area that was drawn, but does not create a movable circle OBJECT.

- To make beats movable and give them properties such as position, color,
  size, and speed, I created a Beat OBJECT/class.

- Pygame does not have a direct onStep() function like CMU CS Academy;
  repeated updates are handled through the game loop.

- pygame.sprite.Group() can be used to store and manage multiple Sprite
  objects.

- A regular Python class is not automatically a Pygame Sprite. To use a
  class with pygame.sprite.Group(), the class should inherit from
  pygame.sprite.Sprite.

- When creating a Sprite subclass, pygame.sprite.Sprite needs to be
  initialized with super().__init__() or the parent class initializer.

- A Pygame Sprite uses an image to represent its appearance and a rect
  to represent its position/bounding area.

- self.image is the Surface containing the visual appearance of the Beat;
  it is separate from the main game screen.

- The coordinates used to draw a shape on self.image are relative to that
  image, not the main game screen.

- self.rect can be used to position the entire Sprite on the main screen.

- self.rect.center can be set using the Beat's x and y position.

- The Beat's x, y, color, size, and speed are stored as attributes of each
  individual Beat object.

- createBeats(x) creates a new Beat object and adds it to the beats group.

- len(beats) can be used to check how many Beat objects are currently in
  the Sprite group.

- Need to figure out how to make existing Beats move downward over time.
"""
import pygame
import sys
import random


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

        # Transparent background
        self.image = pygame.Surface([30,30],pygame.SRCALPHA)

        # stores the Beat's x position
        self.x = x

        # stores the Beat's starting y position
        self.y = 0

        # stores the Beat's color
        self.color = slateBlue

        # stores the Beat's size
        self.size = 15

        # stores the Beat's speed of movement
        self.speed = 2

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
clock = pygame.time.Clock()
beat_timer = 0

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

    # increases the timer by 1 every frame
    beat_timer += 1

    # creates a new beat pattern every 30 frames
    if beat_timer >=30:

        #randomly chooses one of the five possible patterns
        choice = random.choice([0, 1, 2, 3, 4])

        # choice 0 creates one Beat in the first lane
        if choice == 0:
            createBeats(50)
        
        # choice 1 creates one Beat in the second lane
        if choice == 1:
            createBeats(150)

        # choice 2 creates one Beat in the third lane
        if choice == 2:
            createBeats(250)

        # choice 3 creates one Beat in the fourth lane
        if choice == 3:
            createBeats(350)

        # choice 4 creates two Beats simultaneously in the first and fourth lane
        if choice == 4:
            createBeats(50)
            createBeats(350)

        # resets the timer to 0 so that the next Beat pattern will be created after another 30 frames
        beat_timer = 0

    # moves every existing beat downwards
    for beat in beats:

        # increases Beat's y-position by its speed while keep its x-position the same
        beat.rect.center = (beat.rect.centerx, beat.rect.centery + beat.speed)

        # removes the Beat once its bottom touches the bottom of the game screen
        if beat.rect.bottom >= 400:
            beats.remove(beat)
    

    # --------------------------------------------------------
    # DRAW
    # --------------------------------------------------------

    # redraw the background
    screen.fill((135, 206, 235))

    # redraw background circles
    pygame.draw.circle(screen, steel_blue, (51, 400), 175)
    pygame.draw.circle(screen, steel_blue, (400, 400), 200)
    pygame.draw.circle(screen, steel_blue, (167, 374), 100)
    pygame.draw.circle(screen, steel_blue, (215, 330), 100)

    # redraw lane lines
    for i in range(3):
        x = 100 + 100 * i
        pygame.draw.line(screen, WHITE, (x, 0), (x, 400))

    # redraw targets
    pygame.draw.circle(screen, darkSlateBlue, (50, 300), 20)
    pygame.draw.circle(screen, darkSlateBlue, (150, 300), 20)
    pygame.draw.circle(screen, darkSlateBlue, (250, 300), 20)
    pygame.draw.circle(screen, darkSlateBlue, (350, 300), 20)

    # draw beats at their new positions
    beats.draw(screen)

    # updates the display so everything drawn on the screen becomes visible
    pygame.display.flip()

    # keep game running at 60 frames per second
    clock.tick(60)


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

- pygame.draw.circle(...) draws a circle directly onto a surface. It returns a Rect describing the
  area affected by the drawing, but does not create a movable circle OBJECT.

- To make the circle movable, I need to create a Sprite OBJECT and use its
  self.image to display the circle and self.rect to control its position.

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

- Creating a Beat object does not automatically make it appear on the
  screen. The Sprite group must be drawn using beats.draw(screen).

- Moving a Beat's rect changes its position, but the old position can
  remain visible if the background is not redrawn.

- Pygame animation works by repeatedly updating object positions and
  redrawing the screen. The background should be redrawn each frame so
  the previous position of a moving object is covered.

- I do not need to manually delete the previous position of a Beat.
  Redrawing the background each frame effectively removes the old image.

- The game loop repeatedly handles events, updates objects, draws the
  current frame, and displays the frame.

- pygame.display.flip() updates the window so the newly drawn frame becomes
  visible.

- pygame.time.Clock() can be used to control the game's frame rate.

- clock.tick(60) limits the game loop to approximately 60 frames per second,
  making movement more consistent and smooth.

- A Beat's speed can be stored in self.speed and used when updating its
  position instead of hard-coding a movement value.

- To make Beats fall downward, increase their y-coordinate over time.

- A timer can control how frequently new Beats are created instead of
  creating a new Beat every frame.

- beat_timer can be increased once per frame and reset after creating a
  new Beat.

- random.choice(...) can be used to randomly choose which lane a new Beat
  appears in.

- The four lane x-coordinates are 50, 150, 250, and 350.

- If every Beat is created with the same x-coordinate, all Beats will
  appear in the same lane and can stack on top of each other.

- pygame.SRCALPHA allows a Surface to have transparency, which is useful
  when creating a circular Sprite because the corners of the Surface
  should remain transparent.

- The Beat's image and rect work together: self.image determines what the
  Beat looks like, while self.rect determines where the Beat is positioned
  on the screen.

- A Sprite's self.image is a Surface, so it can have a transparent background.
  pygame.SRCALPHA allows the Surface to store transparency.

- Making self.image transparent means only the shape drawn onto the Surface
  is visible, instead of seeing the rectangular Surface around the shape.

- The transparent part belongs to self.image, not self.rect. The rect
  itself is not something that gets visually drawn to the screen unless
  I specifically draw it.

- A Sprite can be removed from a pygame.sprite.Group() using
  beats.remove(beat).

- self.rect has properties for the different edges of a Sprite, such as
  top, bottom, left, and right.

- To remove a Beat when it reaches the bottom of the screen, I can check
  whether beat.rect.bottom has reached the screen height.

- Removing a Beat from the Sprite group means it will no longer be updated
  or drawn by beats.draw(screen).

- The original CMU CS Academy game has five possible Beat patterns:
  four patterns create one Beat in one of the four lanes, and the fifth
  pattern creates two Beats at the same time in the first and fourth lanes.

- random.choice(...) can be used to randomly select between different
  Beat patterns, not just individual lane positions.

- The original CMU game uses a random number from 0-4 to determine the
  Beat pattern.

- In the Pygame version, random.choice([0, 1, 2, 3, 4]) can be used to
  select one of the five Beat patterns.

- Choices 0-3 create one Beat in one of the four lanes.

- Choice 4 creates two Beats at the same time in the first and fourth lanes.

- The beat_timer controls how often a new Beat pattern is generated.

- At 60 FPS, a beat_timer of 30 means a new pattern is generated about
  every 0.5 seconds.

- The UPDATE section happens before the DRAW section, so the game first
  changes the Beat's position and then draws the Beat at its new position.

"""

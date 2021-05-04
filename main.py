import pygame.time as time
import pygame.display as display
import pygame.image as pyimage
import pygame.event as pyevent
import pygame
pygame.init()

FPS = 30

fpsClock = time.Clock()


screen = display.set_mode([500,500])
display.set_caption("animals")
WHITE = (255, 255, 255)
cat = pyimage.load("image/cat.png")
mouse = pyimage.load("image/mouse.png")
catx = 10
caty = 10
direction = 'right'
mousex = 200
mousey = 200


# Run until the user asks to quit
running = True
while running:
    screen.fill(WHITE)
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx==10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    # Did the user click the window close button?
    for event in pyevent.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    #screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    #pygame.display.flip()
    screen.blit(cat, (catx, caty))
    screen.blit(mouse,(mousex,mousey))
    display.update()
    fpsClock.tick(FPS)

# Done! Time to quit.
pygame.quit()

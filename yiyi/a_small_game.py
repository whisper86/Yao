import sys, pygame

pygame.init()

size = width, height = 600, 500
speed = [2, 2]
black = 0, 0, 0

ball = pygame.image.load("kit.png")
screen = pygame.display.set_mode(size)
pygame.display.set_icon(ball)
pygame.display.set_caption("ball", "Yao")

ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill("#535612")
    screen.blit(ball, ballrect)
    pygame.display.flip()

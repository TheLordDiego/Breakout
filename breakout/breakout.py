import pygame
import sprites

pygame.init()

"""Colors used in the game"""
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

"""Game Variables"""
WIDTH = 1280
HEIGHT = 720
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Breakout - PyGame Edition')

"""Sound effects"""
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/arcade_bleep_sound.wav')

"""Game loop"""
game_loop = True
game_clock = pygame.time.Clock()

"""Sprites"""
player = sprites.Player(WIDTH)
ball = sprites.Ball(WIDTH, HEIGHT)

bricks = []
x, y = 70, 20
for i in range(10):
    for j in range(20):
        bricks.append(sprites.Brick(x, y))
        x += 60

    x = 70
    y += 35

while game_loop:

    """Draw"""
    screen.fill(COLOR_BLACK)
    player.render(screen, COLOR_WHITE)
    ball.render(screen, COLOR_WHITE)

    for i in range(len(bricks)):
        bricks[i].render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        """Keystroke events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()

    """Ball's collision with player"""
    if ball.collision(player):
        ball.dx = 5
        ball.dy *= - 1
        bounce_sound_effect.play()

    """Bricks' collision and removal"""
    dead_bricks = []
    for brick in bricks:
        if ball.collision(brick):
            ball.dy *= - 1
            dead_bricks.append(brick)
            bounce_sound_effect.play()

    for brick in dead_bricks:
        bricks.remove(brick)

    if len(bricks) <= 0:
        screen.fill(COLOR_BLACK)
        font = pygame.font.Font('assets/press_start_font.ttf', 50)
        text = font.render('YOU WIN!', True, COLOR_WHITE, COLOR_BLACK)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(text, textRect)

    player.move(WIDTH)
    ball.move(WIDTH, HEIGHT)

    """Update screen"""
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()

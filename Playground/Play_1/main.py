import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Zombie Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player settings
player_pos = [WIDTH // 2, HEIGHT // 2]
player_angle = 0
player_speed = 3

# Zombie settings
zombies = []
zombie_speed = 1

# Weapon settings
bullet_speed = 10
bullets = []

# Game loop
clock = pygame.time.Clock()
running = True

def draw_3d_line(start, end, color):
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    for _ in range(int(steps)):
        z = 1 - (_ / steps)  # Simulating depth
        pygame.draw.circle(screen, color, (int(x), int(y)), max(1, int(2 * z)))
        x += x_inc
        y += y_inc

def spawn_zombie():
    angle = random.uniform(0, 2 * math.pi)
    distance = random.uniform(300, 500)
    x = player_pos[0] + math.cos(angle) * distance
    y = player_pos[1] + math.sin(angle) * distance
    zombies.append([x, y])

def move_zombies():
    for zombie in zombies:
        dx = player_pos[0] - zombie[0]
        dy = player_pos[1] - zombie[1]
        distance = math.sqrt(dx**2 + dy**2)
        if distance > 0:
            zombie[0] += (dx / distance) * zombie_speed
            zombie[1] += (dy / distance) * zombie_speed

def shoot():
    bullet_dx = math.cos(player_angle)
    bullet_dy = math.sin(player_angle)
    bullets.append([player_pos[0], player_pos[1], bullet_dx, bullet_dy])

def move_bullets():
    for bullet in bullets:
        bullet[0] += bullet[2] * bullet_speed
        bullet[1] += bullet[3] * bullet_speed

def check_collisions():
    global zombies
    for bullet in bullets[:]:
        for zombie in zombies[:]:
            if math.dist(bullet[:2], zombie) < 20:
                if bullet in bullets:
                    bullets.remove(bullet)
                if zombie in zombies:
                    zombies.remove(zombie)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                shoot()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_angle -= 0.1
    if keys[pygame.K_d]:
        player_angle += 0.1
    if keys[pygame.K_w]:
        player_pos[0] += math.cos(player_angle) * player_speed
        player_pos[1] += math.sin(player_angle) * player_speed
    if keys[pygame.K_s]:
        player_pos[0] -= math.cos(player_angle) * player_speed
        player_pos[1] -= math.sin(player_angle) * player_speed

    # Spawn zombies
    if random.random() < 0.02:
        spawn_zombie()

    move_zombies()
    move_bullets()
    check_collisions()

    # Drawing
    screen.fill(BLACK)

    # Draw zombies
    for zombie in zombies:
        draw_3d_line(player_pos, zombie, RED)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, (int(bullet[0]), int(bullet[1])), 2)

    # Draw player
    pygame.draw.circle(screen, WHITE, (int(player_pos[0]), int(player_pos[1])), 10)
    end_x = player_pos[0] + math.cos(player_angle) * 20
    end_y = player_pos[1] + math.sin(player_angle) * 20
    pygame.draw.line(screen, WHITE, player_pos, (end_x, end_y), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
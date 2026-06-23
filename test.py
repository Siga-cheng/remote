import pygame
import random

# 初始化
pygame.init()

# 屏幕设置
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("躲避方块小游戏")

# 颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 120, 255)

# 玩家
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 80
player_speed = 6

# 敌人
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = -enemy_size
enemy_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 键盘控制
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # 防止出界
    player_x = max(0, min(WIDTH - player_size, player_x))

    # 敌人下落
    enemy_y += enemy_speed

    # 重置敌人
    if enemy_y > HEIGHT:
        enemy_y = -enemy_size
        enemy_x = random.randint(0, WIDTH - enemy_size)

    # 碰撞检测
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        print("游戏结束！")
        running = False

    # 绘制玩家和敌人
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    pygame.display.update()

pygame.quit()
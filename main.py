import pygame
import random
import os
import time

# 初始化 Pygame
pygame.init()

# 设置游戏窗口
width, height = 1440, 900
screen = pygame.display.set_mode((width, height))

# 设置标题
pygame.display.set_caption("瞄准射击协同")


# 加载图片
background_image = pygame.image.load("picture/background.jpg").convert()
target_image = pygame.image.load("picture/target.png").convert_alpha()
crosshair_image = pygame.image.load("picture/crosshair.png").convert_alpha()
# 设置目标初始位置和是否可见
target_rect = target_image.get_rect(center=(random.randint(50, width-50), random.randint(50, height-50)))
target_visible = True


# 设置准星初始位置
crosshair_rect = crosshair_image.get_rect()

# 设置目标速度
target_speed = [random.choice([-2, 2]), random.choice([-2, 2])]

clock = pygame.time.Clock()
running = True
hit_time = 0  # 记录上次击中时间

def reset_target():
    """重置目标的位置和速度"""
    return target_image.get_rect(center=(random.randint(50, width-50), random.randint(50, height-50))), [random.choice([-2, 2]), random.choice([-2, 2])]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # 按下Esc键时退出游戏

    # 获取鼠标位置
    crosshair_rect.center = pygame.mouse.get_pos()

    # 检查是否击中目标
    if target_visible and crosshair_rect.collidepoint(target_rect.center) and pygame.key.get_pressed()[pygame.K_SPACE]:
        target_visible = False
        hit_time = time.time()

    # 目标消失后在随机时间内重生
    if not target_visible and time.time() - hit_time > random.randint(1, 5):
        target_rect, target_speed = reset_target()
        target_visible = True

    # 如果目标可见，则移动目标
    if target_visible:
        target_rect = target_rect.move(target_speed)
        # 边界检查，防止目标移出背景
        if target_rect.left < 0 or target_rect.right > width:
            target_speed[0] = -target_speed[0]
        if target_rect.top < 0 or target_rect.bottom > height:
            target_speed[1] = -target_speed[1]

    # 绘制背景、目标和准星
    screen.blit(background_image, (0, 0))
    if target_visible:
        screen.blit(target_image, target_rect)
    screen.blit(crosshair_image, crosshair_rect)

    pygame.display.flip()
    #计时60s
    clock.tick(60)

pygame.quit()
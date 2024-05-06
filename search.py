import time

import pygame
import random
import os

pygame.init()
pygame.display.set_caption("搜索躲避协同")
# 设置屏幕尺寸和分割
# 获取屏幕信息，以便以全屏模式启动
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h

# 创建全屏窗口; 分屏问题
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
left_area = pygame.Rect(0, 0, width // 2, height)
right_area = pygame.Rect(width // 2, 0, width // 2, height)

# 游戏基本设置
clock = pygame.time.Clock()
running = True
fps = 60

# 飞机和障碍物设置
plane_image = pygame.image.load("picture/target.png").convert_alpha()
plane_rect = plane_image.get_rect(center=(width // 4, height // 2))
obstacle_image = pygame.image.load("picture/logo32.png").convert_alpha()
obstacles = []
obstacle_spawn_time = 0
obstacle_interval = 3000  # milliseconds

# 血条设置
health = 100


# 右边区域的图片搜索
search_images = [pygame.image.load("picture/hud.png").convert_alpha(), pygame.image.load("picture/fac.png").convert_alpha()]
current_image = None
search_spawn_time = 0
search_interval = 5000  # milliseconds
score = 0

while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # 按下Esc键时退出游戏
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if right_area.collidepoint(event.pos):  # 点击在右边区域
                if current_image and current_image[1].collidepoint(event.pos):
                    score += 1
                    current_image = None

    # 更新飞机位置
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        plane_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        plane_rect.x += 5
    if keys[pygame.K_UP]:
        plane_rect.y -= 5
    if keys[pygame.K_DOWN]:
        plane_rect.y += 5
    plane_rect.clamp_ip(left_area)  # 限制飞机在左边区域内

    # 处理障碍物生成和移动
    current_time = pygame.time.get_ticks()
    if current_time - obstacle_spawn_time > obstacle_interval:
        obstacle_rect = obstacle_image.get_rect(midtop=(random.randint(0, width // 2), 0))
        obstacles.append(obstacle_rect)
        obstacle_spawn_time = current_time

    for obstacle in obstacles[:]:
        obstacle.y += 3
        if obstacle.top > height:
            obstacles.remove(obstacle)
        if obstacle.colliderect(plane_rect):
            health -= 10
            obstacles.remove(obstacle)

    # 处理右边区域的图片搜索
    if not current_image or (current_time - search_spawn_time > search_interval):
        selected_image = random.choice(search_images)
        rect = selected_image.get_rect(center=(random.randint(width // 2 + 50, width - 50), random.randint(50, height - 50)))
        current_image = (selected_image, rect)
        search_spawn_time = current_time

    # 清空屏幕
    screen.fill((0, 0, 0))

    # 绘制左边游戏
    pygame.draw.rect(screen, (255, 255, 255), left_area, 1)
    screen.blit(plane_image, plane_rect)
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)

    # 绘制血条
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, health * 2, 20))

    # 绘制右边游戏
    pygame.draw.rect(screen, (255, 255, 255), right_area, 1)
    if current_image:
        screen.blit(current_image[0], current_image[1])
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (width // 2 + 10, 10))

    # 更新屏幕
    pygame.display.flip()
    clock.tick(fps)

    # 检查游戏是否结束
    if health <= 0:
        running = False

pygame.quit()
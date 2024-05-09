# -*- coding: utf-8 -*-=
import pygame
import random
import os
import time

# 初始化 Pygame
pygame.init()

# 设置屏幕尺寸
screen_width, screen_height = 1200, 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# 定义游戏常量
grid_columns = 5
grid_rows = 4
cell_width = screen_width // grid_columns
cell_height = (screen_height - 250) // grid_rows
score = 0
time_limit = 120  # 秒
game_over = False

# 加载所有图片
image_folder = "picture/reset"  # 替换为你自己的文件夹路径
image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]

# 确保有足够多的图片
if len(image_files) < grid_columns * grid_rows:
    print("图片数量不足以填满游戏区域")
    exit()


# 函数用于加载图片
def load_image(filename):
    img = pygame.image.load(os.path.join(image_folder, filename)).convert_alpha()
    return pygame.transform.scale(img, (200, 200))


# 设置字体和颜色（pygame 不支持中文，可以将字体导入到Font文件夹）
font = pygame.font.Font("Font/simhei.ttf", 36)
small_font = pygame.font.Font("Font/simhei.ttf", 28)
text_color = (255, 255, 255)

# 随机选择目标图片
target_image_file = random.choice(image_files)
target_image = load_image(target_image_file)

# 图片和位置的映射列表
image_positions = []
all_images = []


# 函数用于生成图像网格
def generate_grid():
    global all_images, image_positions
    all_images = []
    image_positions = []

    # 随机选择目标图片
    target_files = random.sample(image_files, grid_columns * grid_rows - 2)
    target_files.append(target_image_file)
    target_files.append(target_image_file)
    random.shuffle(target_files)

    # 在下方网格内排列
    for row in range(grid_rows):
        for col in range(grid_columns):
            x = col * cell_width
            y = 200 + row * cell_height
            img = load_image(target_files.pop())
            all_images.append((img, pygame.Rect(x, y, 200, 200), img == target_image))


generate_grid()

# 游戏开始时间
start_time = time.time()

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = event.pos
            for i, (img, rect, is_target) in enumerate(all_images):
                if rect.collidepoint(pos):
                    if is_target:
                        all_images.pop(i)
                        break

            # 检查是否已点击所有目标图片
            if all(not target for img, rect, target in all_images):
                score += 1
                generate_grid()

    # 检查时间是否结束
    remaining_time = time_limit - int(time.time() - start_time)
    if remaining_time <= 0:
        game_over = True
        remaining_time = 0

    # 绘制背景
    screen.fill((0, 0, 0))

    # 绘制分隔线
    pygame.draw.line(screen, (255, 255, 255), (0, 250), (screen_width, 250), 3)

    # 绘制上方信息
    score_text = font.render(f"得分: {score}", True, text_color)
    screen.blit(score_text, (50, 50))
    target_text = font.render("目标图片：", True, text_color)
    screen.blit(target_text, (200, 150))
    screen.blit(target_image, (500, 50))
    time_text = font.render(f"时间: {remaining_time} 秒", True, text_color)
    screen.blit(time_text, (screen_width - 300, 50))


    # 绘制下方图片网格
    for img, rect, is_target in all_images:
        screen.blit(img, rect)

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)

# 退出 Pygame
pygame.quit()

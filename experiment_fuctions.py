import sys
import pygame
from time import sleep
from settings import Particle
import os
import numpy as np


def check1_events(base_settings, screen, interaction, particles):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            particles.clear()
            stats.exp1_active = False
            stats.exp2_active = False
            stats.interface_active = True
            initialization(base_settings, screen, interaction, particles)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_interaction_button(base_settings, screen, interaction, mouse_x, mouse_y, particles)


def check_interaction_button(base_settings, screen, interaction, mouse_x, mouse_y, particles):
    """设置鼠标交互"""
    # 设置变换速度交互
    if interaction.msg11_image_rect.collidepoint(mouse_x, mouse_y):
        interaction.rect16.center = interaction.msg11_image_rect.center
        particles.clear()
        base_settings.particle_speed = 2

    if interaction.msg12_image_rect.collidepoint(mouse_x, mouse_y):
        interaction.rect16.center = interaction.msg12_image_rect.center
        particles.clear()
        base_settings.particle_speed = 3

    if interaction.msg13_image_rect.collidepoint(mouse_x, mouse_y):
        interaction.rect16.center = interaction.msg13_image_rect.center
        particles.clear()
        base_settings.particle_speed = 4

    if interaction.msg14_image_rect.collidepoint(mouse_x, mouse_y):
        interaction.rect16.center = interaction.msg14_image_rect.center
        particles.clear()
        base_settings.particle_speed = 5

    if interaction.msg15_image_rect.collidepoint(mouse_x, mouse_y):
        interaction.rect16.center = interaction.msg15_image_rect.center
        particles.clear()
        base_settings.particle_speed = 7

    # 设置变换数量交互
    if interaction.msg21_image_rect.collidepoint(mouse_x, mouse_y):
        interaction.rect26.center = interaction.msg21_image_rect.center
        particles.clear()
        base_settings.amount_factor = 50
        base_settings.mode = 1

    if interaction.msg22_image_rect.collidepoint(mouse_x, mouse_y):
        interaction.rect26.center = interaction.msg22_image_rect.center
        particles.clear()
        base_settings.amount_factor = 15
        base_settings.mode = 1

    if interaction.msg23_image_rect.collidepoint(mouse_x, mouse_y):
        interaction.rect26.center = interaction.msg23_image_rect.center
        particles.clear()
        base_settings.amount_factor = 7
        base_settings.mode = 1

    if interaction.msg24_image_rect.collidepoint(mouse_x, mouse_y):
        interaction.rect26.center = interaction.msg24_image_rect.center
        particles.clear()
        base_settings.amount_factor = 2
        base_settings.mode = 1

    if interaction.msg25_image_rect.collidepoint(mouse_x, mouse_y):
        interaction.rect26.center = interaction.msg25_image_rect.center
        particles.clear()
        base_settings.amount_factor = 1
        base_settings.mode = 1

    if interaction.msg26_image_rect.collidepoint(mouse_x, mouse_y):
        particles.clear()
        base_settings.mode = 0
        base_settings.amount_factor = 1
        interaction.rect26.center = 1300, 0

    # 设置更改靶核交互
    if interaction.msg31_image_rect.collidepoint(mouse_x, mouse_y) or interaction.rect31.collidepoint(mouse_x, mouse_y):
        particles.clear()
        base_settings.material_subscript = 0
    if interaction.msg32_image_rect.collidepoint(mouse_x, mouse_y) or interaction.rect32.collidepoint(mouse_x, mouse_y):
        particles.clear()
        base_settings.material_subscript = 1
    if interaction.msg33_image_rect.collidepoint(mouse_x, mouse_y) or interaction.rect33.collidepoint(mouse_x, mouse_y):
        particles.clear()
        base_settings.material_subscript = 2
    if interaction.msg34_image_rect.collidepoint(mouse_x, mouse_y) or interaction.rect34.collidepoint(mouse_x, mouse_y):
        particles.clear()
        base_settings.material_subscript = 3


def creat_particle(base_settings, screen, particles):
    """创建一个氦原子"""
    new_particle = Particle(base_settings, screen)
    particles.append(new_particle)


def calculate_interaction_force(base_settings, material, particles):
    """计算两粒子的库仑力，得出x与y方向的分加速度"""
    for particle in particles:
        r = ((material[base_settings.material_subscript].rect.centerx - particle.rect.centerx) ** 2 + (
                material[base_settings.material_subscript].rect.centery - particle.rect.centery) ** 2) ** 0.5
        f = 75 * (material[base_settings.material_subscript].electric * 2) / (r ** 2)
        a = f
        cosx = (material[base_settings.material_subscript].rect.centerx - particle.rect.centerx) / r
        sinx = (material[base_settings.material_subscript].rect.centery - particle.rect.centery) / r

        aax = a * cosx
        aay = a * sinx
        # 一系列修正
        if 0.1 < abs(aay) < 0.5:
            aay = np.sign(aay)
        else:
            aay = int(aay)
        particle.ax += int(aax)
        if abs(particle.ay) >= 2:
            particle.ay = np.sign(particle.ay) * 2
        else:
            particle.ay -= aay


def updata_new_particle(base_settings, particles, screen, interaction):
    for particle in particles:
        if particle.rect.centerx > base_settings.screen_width - 150 or particle.rect.centery > base_settings.screen_height or particle.rect.centery < 0 or particle.rect.centerx < 0:
            particles.remove(particle)
    if base_settings.mode == 1:
        creat_particle(base_settings, screen, particles)
    elif base_settings.mode == 0 and len(particles) == 0:
        creat_particle(base_settings, screen, particles)


def initialization(base_settings, screen, interaction, particles):
    # 初始化
    base_settings.particle_speed = 4  # 初始化
    base_settings.amount_factor = 7
    base_settings.material_subscript = 0
    base_settings.mode = 1
    interaction.rect16.center = interaction.msg13_image_rect.center
    interaction.rect26.center = interaction.msg23_image_rect.center


def update_screen1(base_settings, screen, material, particles, interaction):
    """更新屏幕上的图像并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(base_settings.bg_color)

    # 画出靶核
    material[base_settings.material_subscript].blitme()

    # 画出氦原子
    for particle in particles:
        particle.update(base_settings)
        if particle.particle_y % base_settings.amount_factor == 0:
            particle.blitme()

    # 绘制交互
    interaction.draw_background()
    interaction.draw_interaction()
    interaction.draw_slider()
    interaction.draw_material()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

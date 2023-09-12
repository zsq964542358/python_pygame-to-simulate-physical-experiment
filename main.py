import pygame
from pygame.sprite import Group
import settings as st
import experiment_fuctions as ef


def run_game():
    # 初始化界面并创建一个屏幕对象
    pygame.init()

    """设置第一个模拟实验"""
    base_settings1 = st.BaseSettings()
    # 创建屏幕
    screen1 = pygame.display.set_mode((base_settings1.screen_width, base_settings1.screen_height))
    # 创建靶核
    material = [st.Al(base_settings1, screen1), st.Cu(base_settings1, screen1),
                st.Ag(base_settings1, screen1), st.Au(base_settings1, screen1)]
    # 创建α粒子
    particles = []
    ef.creat_particle(base_settings1, screen1, particles)
    # 创建交互
    interaction1 = st.Interaction(base_settings1, screen1)

    # 开始游戏主循环
    while True:
        ef.calculate_interaction_force(base_settings1, material, particles)
        ef.update_screen1(base_settings1, screen1, material, particles, interaction1)
        ef.check1_events(base_settings1, screen1, interaction1, particles)
        ef.updata_new_particle(base_settings1, particles, screen1, interaction1)


if __name__ == '__main__':
    run_game()

import pygame
import random
from time import sleep


# noinspection SpellCheckingInspection
class BaseSettings(object):
    """储存模拟中所有设置的类"""

    def __init__(self):
        """初始化游戏静态设置"""
        # 主屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (240, 240, 240)
        self.particle_speed = 4  # 原子入射速度
        self.amount_factor = 7  # 控制数量因子
        self.material_subscript = 0  # 控制靶核列表
        self.mode = 1  # 控制单粒子和多粒子模式


# 设置一系列可改变的靶核对象
# 设置父类
class Material(object):
    """初始化靶核"""

    def __init__(self, base_settings, screen):
        self.screen = screen
        self.base_settings = base_settings

        self.screen_rect = screen.get_rect()

    def blitme(self):
        """在指定位置绘制图像"""
        self.screen.blit(self.image, self.rect)


# 设置子类
class Al(Material):
    # 铝原子类
    def __init__(self, base_settings, screen):
        Material.__init__(self, base_settings, screen)
        # 设置及加载靶核图像
        self.image = pygame.image.load('Al.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # 放置其位置
        self.rect.centerx = base_settings.screen_width / 2
        self.rect.centery = base_settings.screen_height / 2

        # 确定电荷量
        self.electric = 13


class Cu(Material):
    # 铜原子类
    def __init__(self, base_settings, screen):
        Material.__init__(self, base_settings, screen)
        # 设置及加载靶核图像
        self.image = pygame.image.load('Cu.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # 放置其位置
        self.rect.centerx = base_settings.screen_width / 2
        self.rect.centery = base_settings.screen_height / 2

        # 确定电荷量
        self.electric = 29


class Ag(Material):
    # 银原子类
    def __init__(self, base_settings, screen):
        Material.__init__(self, base_settings, screen)
        # 设置及加载靶核图像
        self.image = pygame.image.load('Ag.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # 放置其位置
        self.rect.centerx = base_settings.screen_width / 2
        self.rect.centery = base_settings.screen_height / 2

        # 确定电荷量
        self.electric = 47


class Au(Material):
    # 金原子类
    def __init__(self, base_settings, screen):
        Material.__init__(self, base_settings, screen)
        # 设置及加载靶核图像
        self.image = pygame.image.load('Au.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # 放置其位置
        self.rect.centerx = base_settings.screen_width / 2
        self.rect.centery = base_settings.screen_height / 2

        # 确定电荷量
        self.electric = 79


# 创建α粒子类
class Particle(object):
    """创建α粒子"""

    def __init__(self, base_settings, screen):
        self.screen = screen

        # 随机设置粒子位置
        self.limit_up = base_settings.screen_height
        self.limit_down = 0

        self.particle_x = 0
        self.particle_y = random.randint(self.limit_down, self.limit_up)

        # 加载α粒子图像
        self.image = pygame.image.load('He.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = self.particle_x
        self.rect.y = self.particle_y
        self.screen_rect = screen.get_rect()

        self.ax = 0
        self.ay = 0

    def update(self, base_settings):
        self.rect.x += (base_settings.particle_speed - self.ax)
        self.rect.y += self.ay
        # sleep(0.005)

    def blitme(self):
        """在指定位置绘制图像"""
        self.screen.blit(self.image, self.rect)


# 设置所有交互界面
class Interaction(object):
    """绘制交互界面"""

    def __init__(self, base_settings, screen):
        # 总设置
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.Font(r'simhei.ttf', 20)
        self.font1 = pygame.font.Font(r'simhei.ttf', 15)
        self.msg_color = (120, 240, 150)

        # 设置整个交互界面背景的尺寸和其他属性
        self.background_width, self.background_height = 150, 600
        self.backgroundrect_color = (0, 0, 0)
        self.backgroundrect = pygame.Rect(base_settings.screen_width - self.background_width, 0, self.background_width,
                                          self.background_height)
        # 设置交互界面背景分隔板
        self.separate1_width, self.separate1_height = 150, 5
        self.separate1_color = (220, 20, 60)
        self.separate1_rect = pygame.Rect(1050, 95, self.separate1_width, self.separate1_height)

        self.separate2_width, self.separate2_height = 150, 5
        self.separate2_color = (220, 20, 60)
        self.separate2_rect = pygame.Rect(1050, 200, self.separate2_width, self.separate2_height)

        self.separate3_width, self.separate3_height = 150, 5
        self.separate3_color = (220, 20, 60)
        self.separate3_rect = pygame.Rect(1050, 380, self.separate3_width, self.separate3_height)

        # 设置第一个交互
        self.msg10 = '速度'
        self.msg11 = '1'
        self.msg12 = '2'
        self.msg13 = '3'
        self.msg14 = '4'
        self.msg15 = '5'

        self.width16, self.height16 = 10, 20  # 设置鼠标交互小滑块
        self.rect16_color = (20, 50, 180)
        self.rect16 = pygame.Rect(500, 300, self.width16, self.height16)

        # 创建msg1
        self.prep_msg1(self.msg10, self.msg11, self.msg12, self.msg13, self.msg14, self.msg15)
        self.rect16.center = self.msg13_image_rect.center

        # 设置第二个交互
        self.msg20 = '数量'
        self.msg21 = '1'
        self.msg22 = '2'
        self.msg23 = '3'
        self.msg24 = '4'
        self.msg25 = '5'
        self.msg26 = '单粒子模式'

        self.width26, self.height26 = 10, 20  # 设置鼠标交互小滑块
        self.rect26_color = (20, 50, 180)
        self.rect26 = pygame.Rect(500, 300, self.width26, self.height26)

        # 创建msg2
        self.prep_msg2(self.msg20, self.msg21, self.msg22, self.msg23, self.msg24, self.msg25, self.msg26)
        self.rect26.center = self.msg23_image_rect.center

        # 设置第三个交互
        self.msg30 = '靶核'
        self.msg31 = 'Al'
        self.msg32 = 'Cu'
        self.msg33 = 'Ag'
        self.msg34 = 'Au'

        self.image31 = pygame.image.load('Al.png')
        self.image31 = pygame.transform.scale(self.image31, (20, 20))
        self.rect31 = self.image31.get_rect()
        self.rect31.centerx = 1090
        self.rect31.centery = 300
        self.image32 = pygame.image.load('Cu.png')
        self.image32 = pygame.transform.scale(self.image32, (20, 20))
        self.rect32 = self.image32.get_rect()
        self.rect32.centerx = 1150
        self.rect32.centery = 300
        self.image33 = pygame.image.load('Ag.png')
        self.image33 = pygame.transform.scale(self.image33, (20, 20))
        self.rect33 = self.image33.get_rect()
        self.rect33.centerx = 1090
        self.rect33.centery = 360
        self.image34 = pygame.image.load('Au.png')
        self.image34 = pygame.transform.scale(self.image34, (20, 20))
        self.rect34 = self.image34.get_rect()
        self.rect34.centerx = 1150
        self.rect34.centery = 360

        # 创建msg3
        self.prep_msg3(self.msg30, self.msg31, self.msg32, self.msg33, self.msg34)

    def prep_msg1(self, msg10, msg11, msg12, msg13, msg14, msg15):
        """将msg1渲染为图像并设置位置"""
        # 设置第一个交互msg
        self.msg10_image = self.font.render(msg10, True, self.msg_color, self.backgroundrect_color)
        self.msg10_image_rect = self.msg10_image.get_rect()
        self.msg10_image_rect.center = (1120, 30)

        self.msg11_image = self.font.render(msg11, True, self.msg_color, self.backgroundrect_color)
        self.msg11_image_rect = self.msg11_image.get_rect()
        self.msg11_image_rect.center = (1060, 60)

        self.msg12_image = self.font.render(msg12, True, self.msg_color, self.backgroundrect_color)
        self.msg12_image_rect = self.msg12_image.get_rect()
        self.msg12_image_rect.center = (1090, 60)

        self.msg13_image = self.font.render(msg13, True, self.msg_color, self.backgroundrect_color)
        self.msg13_image_rect = self.msg13_image.get_rect()
        self.msg13_image_rect.center = (1120, 60)

        self.msg14_image = self.font.render(msg14, True, self.msg_color, self.backgroundrect_color)
        self.msg14_image_rect = self.msg14_image.get_rect()
        self.msg14_image_rect.center = (1150, 60)

        self.msg15_image = self.font.render(msg15, True, self.msg_color, self.backgroundrect_color)
        self.msg15_image_rect = self.msg15_image.get_rect()
        self.msg15_image_rect.center = (1180, 60)

    def prep_msg2(self, msg20, msg21, msg22, msg23, msg24, msg25, msg26):
        """将msg2渲染为图像并设置位置"""
        # 设置第二个交互msg
        self.msg20_image = self.font.render(msg20, True, self.msg_color, self.backgroundrect_color)
        self.msg20_image_rect = self.msg20_image.get_rect()
        self.msg20_image_rect.center = (1120, 130)

        self.msg21_image = self.font.render(msg21, True, self.msg_color, self.backgroundrect_color)
        self.msg21_image_rect = self.msg21_image.get_rect()
        self.msg21_image_rect.center = (1060, 160)

        self.msg22_image = self.font.render(msg22, True, self.msg_color, self.backgroundrect_color)
        self.msg22_image_rect = self.msg22_image.get_rect()
        self.msg22_image_rect.center = (1090, 160)

        self.msg23_image = self.font.render(msg23, True, self.msg_color, self.backgroundrect_color)
        self.msg23_image_rect = self.msg23_image.get_rect()
        self.msg23_image_rect.center = (1120, 160)

        self.msg24_image = self.font.render(msg24, True, self.msg_color, self.backgroundrect_color)
        self.msg24_image_rect = self.msg24_image.get_rect()
        self.msg24_image_rect.center = (1150, 160)

        self.msg25_image = self.font.render(msg25, True, self.msg_color, self.backgroundrect_color)
        self.msg25_image_rect = self.msg25_image.get_rect()
        self.msg25_image_rect.center = (1180, 160)

        self.msg26_image = self.font1.render(msg26, True, self.msg_color, self.backgroundrect_color)
        self.msg26_image_rect = self.msg26_image.get_rect()
        self.msg26_image_rect.center = (1125, 180)

    def prep_msg3(self, msg30, msg31, msg32, msg33, msg34):
        """将msg3渲染为图像并设置位置"""
        # 设置第三个交互msg
        self.msg30_image = self.font.render(msg30, True, self.msg_color, self.backgroundrect_color)
        self.msg30_image_rect = self.msg30_image.get_rect()
        self.msg30_image_rect.center = (1120, 230)

        self.msg31_image = self.font.render(msg31, True, self.msg_color, self.backgroundrect_color)
        self.msg31_image_rect = self.msg31_image.get_rect()
        self.msg31_image_rect.center = (1090, 270)

        self.msg32_image = self.font.render(msg32, True, self.msg_color, self.backgroundrect_color)
        self.msg32_image_rect = self.msg32_image.get_rect()
        self.msg32_image_rect.center = (1150, 270)

        self.msg33_image = self.font.render(msg33, True, self.msg_color, self.backgroundrect_color)
        self.msg33_image_rect = self.msg33_image.get_rect()
        self.msg33_image_rect.center = (1090, 330)

        self.msg34_image = self.font.render(msg34, True, self.msg_color, self.backgroundrect_color)
        self.msg34_image_rect = self.msg34_image.get_rect()
        self.msg34_image_rect.center = (1150, 330)

    def draw_slider(self):
        # 绘制交互小滑块
        self.screen.fill(self.rect16_color, self.rect16)
        self.screen.fill(self.rect26_color, self.rect26)

    def draw_interaction(self):
        # 绘制msg1图像
        self.screen.blit(self.msg10_image, self.msg10_image_rect)
        self.screen.blit(self.msg11_image, self.msg11_image_rect)
        self.screen.blit(self.msg12_image, self.msg12_image_rect)
        self.screen.blit(self.msg13_image, self.msg13_image_rect)
        self.screen.blit(self.msg14_image, self.msg14_image_rect)
        self.screen.blit(self.msg15_image, self.msg15_image_rect)
        # 绘制msg2图像
        self.screen.blit(self.msg20_image, self.msg20_image_rect)
        self.screen.blit(self.msg21_image, self.msg21_image_rect)
        self.screen.blit(self.msg22_image, self.msg22_image_rect)
        self.screen.blit(self.msg23_image, self.msg23_image_rect)
        self.screen.blit(self.msg24_image, self.msg24_image_rect)
        self.screen.blit(self.msg25_image, self.msg25_image_rect)
        self.screen.blit(self.msg26_image, self.msg26_image_rect)
        # 绘制msg3图像
        self.screen.blit(self.msg30_image, self.msg30_image_rect)
        self.screen.blit(self.msg31_image, self.msg31_image_rect)
        self.screen.blit(self.msg32_image, self.msg32_image_rect)
        self.screen.blit(self.msg33_image, self.msg33_image_rect)
        self.screen.blit(self.msg34_image, self.msg34_image_rect)

    def draw_material(self):
        """在指定位置绘制图像"""
        self.screen.blit(self.image31, self.rect31)
        self.screen.blit(self.image32, self.rect32)
        self.screen.blit(self.image33, self.rect33)
        self.screen.blit(self.image34, self.rect34)

    def draw_background(self):
        """绘制颜色"""
        # 绘制交互界面背景
        self.screen.fill(self.backgroundrect_color, self.backgroundrect)
        self.screen.fill(self.separate1_color, self.separate1_rect)
        self.screen.fill(self.separate2_color, self.separate2_rect)
        self.screen.fill(self.separate3_color, self.separate3_rect)



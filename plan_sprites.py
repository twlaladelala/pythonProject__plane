import random

import pygame

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 刷新率
FRAME_PER_SCOEND = 60

# 敌人出现频率
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹
HERO_FIRE_EVENT = pygame.USEREVENT + 1

HERO_FIRE2_EVENT = pygame.USEREVENT + 2


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1, speedx=0):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speedx = speedx

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speedx


class Background(GameSprite):

    def __init__(self, is_alt=False):
        image_name = './images/background.png'
        super().__init__(image_name)
        if is_alt:
            self.rect.y = -self.rect.height

    # 游戏背景
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        super().__init__('./images/enemy1.png')
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # print('飞机飞出屏幕，需从精灵组中删除....')
            self.__dict__
            # print('敌机飞出屏幕挂了 %s' % self.rect)


class Hero(GameSprite):
    def __init__(self):
        super().__init__('images/me1.png', 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - self.rect.y
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        # if self.rect.x <0:        #plan_main.py 中 Line 55 效果相同
        #     self.rect.x = 0
        # elif self.rect.right > SCREEN_RECT.right:
        #     self.rect.right = SCREEN_RECT.right

    def fire(self):
        print('发射子弹')
        # 创建子弹精灵 ---设置精灵位置 ——————将精灵添加到精灵组
        for i in (0, 1, 2,):
            bullet = Bullte()
            bullet.rect.bottom = self.rect.y - 20 * i
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)

    def fire2(self):
        print('我发射了牛逼的子弹')
        for i in (0, 1, 2,):
            bullet = Bullte()
            bullet.rect.centerx = self.rect.x - 20 * i
            bullet.rect.bottom = self.rect.y - 20 * i


class Bullte(GameSprite):
    def __init__(self):
        # 设置子弹图片
        super().__init__('./images/bullet1.png', -2)

    def update(self):
        # 调用父类方法。让子弹沿垂直方向飞行
        super().update()
        if self.rect.bottom < 0:
            self.kill()

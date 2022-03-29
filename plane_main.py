import random

import pygame
from plan_sprites import *


class PlanGame(object):
    def __init__(self):
        print('游戏初始化')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

        # 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, random.randint(100, 200))
        pygame.time.set_timer(HERO_FIRE_EVENT,500)
        pygame.time.set_timer(HERO_FIRE2_EVENT,200)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print('游戏开始')

        while True:
            self.clock.tick(FRAME_PER_SCOEND)
            self.__event_handler()
            # self.__create_sprites()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

            pass

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlanGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print('敌人出现...')
                # 创建敌飞精灵
                enemy = Enemy()
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print('我向右移动...')
            elif  event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == HERO_FIRE2_EVENT:
            #     self.hero.fire2()
        #使用键盘方法获取按下的按键
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT] is True:
            self.hero.speed = 2
            print('向右移动')
            if self.hero.rect.right > SCREEN_RECT.right:
                self.hero.rect.right = SCREEN_RECT.right
                print('不能在向右了')

        elif keys_pressed[pygame.K_LEFT] is True:
            self.hero.speed = -2
            print('向左移动')
            if self.hero.rect.x < 0:
                self.hero.rect.x = 0

        else :
            self.hero.speed = 0



    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies =  pygame.sprite.spritecollide (self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlanGame.__game_over()


    def __update_sprites(self):
        for group in [self.back_group, self.enemy_group, self.hero_group ,self.hero.bullets]:
            group.update()
            group.draw(self.screen)


    @staticmethod
    def __game_over():
        print('游戏结束')
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = PlanGame()
    game.start_game()

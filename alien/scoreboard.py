#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-09 15:30:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
计分系统
"""

import pygame.font

from pygame.sprite import Group
from ship import Ship
from kill_effect import KillEffect


class Scoreboard:
    """统计分数"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 外星人死亡的坐标、分数
        self.aline_dead_x = 0
        self.aline_dead_y = 0
        self.aline_dead_score = 0

        # 显示得分信息时使用的字体设置

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 24, )

        # 准备初始得分图像、最高分图像、等级图像、剩余飞船图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships_left()
        self.prep_ships()

        # 准备击杀外星人得分图像
        #self.prep_aline_point()


    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        self.rounded_score = round(self.stats.score, -1)
        score_str = u"得分: " + "{:,}".format(self.rounded_score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高得分渲染成一副图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "最高分: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,
                True, self.text_color, self.ai_settings.bg_color)
        # 将最商得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render("等级: " + str(self.stats.level),
                 True, self.text_color,)
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships_left(self):
        """将等级转换为渲染的图像"""
        self.ships_number_image = self.font.render(
                "飞船: " + str(self.stats.ships_left),
                 True, self.text_color,)
        # 将等级放在得分下方
        self.ships_number_rect = self.ships_number_image.get_rect()
        self.ships_number_rect.left = self.screen_rect.left + 20
        self.ships_number_rect.top = 20

    def prep_aline_point(self):
        """将击杀外星人的当前分数转换为渲染的图像"""
        self.aline_point_image = self.font.render(
                '+' + str(self.aline_dead_score),
                 True, self.text_color,)
        # 将等级放在得分下方
        self.aline_point_rect = self.aline_point_image.get_rect()
        self.aline_point_rect.x = self.aline_dead_x
        self.aline_point_rect.y = self.aline_dead_y


    def prep_ships(self):
        """显示还余下多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            Ship.filename = 'images/hp.png'
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * (ship.rect.width + 10)
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_kill_scores (self):
        """击杀外星人得分"""
        self.kill_scores = Group()
        self.kill_scores_numbers = 1
        for kill_scores_number in range(self.kill_scores_numbers):
            kill_score = KillEffect(self.ai_settings)
            kill_score.rect.x = self.aline_dead_x
            kill_score.rect.y = self.aline_dead_y
            self.kill_scores.add(kill_score)

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #self.screen.blit(self.ships_number_image, self.ships_number_rect)

        #self.screen.blit(self.aline_point_image, self.aline_point_rect)


        # 绘制飞船、击杀得分
        self.ships.draw(self.screen)
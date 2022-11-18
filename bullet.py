import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        """Создает объект снаряда в текущей позиции корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Создание снаряда в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиция снаряда хранится в вещественнном формате
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение снаряда вверх по экрану"""
        # Обновление позиции снаряда в вещественном формате
        self.y -= self.settings.bullet_speed
        # Обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """Выводит снаряд на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)

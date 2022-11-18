import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Класс представляющий звёзды"""

    def __init__(self, ai_game):
        """Инициализирует звёзды и задает начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения звезды и получение атрибута rect
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Каждая новая звезда появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позициии пришельца
        self.x = float(self.rect.x)

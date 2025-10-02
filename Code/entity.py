# entity.py
from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    """
    Classe base abstrata para todas as entidades do jogo.
    """
    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        self.name = name
        self.surf = surf
        self.rect = rect

    @abstractmethod
    def move(self) -> None:
        """
        Método abstrato para o movimento da entidade.
        Deve ser implementado por todas as subclasses.
        """
        pass
# entity_factory.py
import pygame
from entity import Entity
from player import Player
from enemy import Enemy
from background import Background

class EntityFactory:
    """
    Fábrica para criar diferentes tipos de entidades do jogo.
    """
    @staticmethod
    def get_entity(entity_type: str, name: str, position=(0, 0)) -> Entity:
        """
        Retorna uma nova instância de uma entidade com base no tipo especificado.
        """
        # Valores de exemplo para Surface e Rect.
        # Na implementação real, você carregaria imagens e definiria posições.
        surf = pygame.Surface((50, 50)) # Tamanho de exemplo
        surf.fill((255, 255, 255)) # Cor branca de exemplo
        rect = surf.get_rect(topleft=position)

        if entity_type == "player":
            return Player(name, surf, rect)
        elif entity_type == "enemy":
            return Enemy(name, surf, rect)
        elif entity_type == "background":
            # O fundo normalmente teria um tamanho diferente
            surf = pygame.Surface((800, 600))
            surf.fill((50, 50, 100)) # Cor de fundo de exemplo
            rect = surf.get_rect(topleft=position)
            return Background(name, surf, rect)

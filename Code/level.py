# level.py
import pygame
from entity import Entity
from entity_factory import EntityFactory
from entity_mediator import EntityMediator

class Level:
    """
    Representa um nível do jogo, com suas próprias entidades e lógica.
    """
    def __init__(self, window: pygame.Surface, name: str):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_factory = EntityFactory()
        self.entity_mediator = EntityMediator()

    def run(self):
        """
        Executa o loop principal do nível.
        """
        print(f"Iniciando nível: {self.name}")
        # Exemplo de como popular o nível com entidades
        self.entity_list.append(self.entity_factory.get_entity("background", "FundoMontanhas"))
        self.entity_list.append(self.entity_factory.get_entity("player", "JogadorPrincipal", position=(375, 500)))
        self.entity_list.append(self.entity_factory.get_entity("enemy", "Inimigo1", position=(100, 100)))

        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False # Encerra apenas o nível
                    pygame.quit() # Encerra o pygame para fechar a janela
                    exit()

            # Limpa a tela
            self.window.fill((0, 0, 0))

            # Atualiza e desenha todas as entidades
            for entity in self.entity_list:
                entity.move()
                self.entity_mediator.control(entity, self.entity_list)
                self.window.blit(entity.surf, entity.rect)

            pygame.display.flip()
            clock.tick(60) # Limita o FPS
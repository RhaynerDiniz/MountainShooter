# game.py
import pygame
from menu import Menu
from level import Level

class Game:
    """
    Classe principal que gerencia o fluxo do jogo,
    alternando entre menu e níveis.
    """
    def __init__(self):
        pygame.init()
        self.window: pygame.Surface = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mountain Shooter")

    def run(self):
        """
        Inicia e gerencia o loop principal do jogo.
        """
        while True:
            menu = Menu(self.window)
            option = menu.run()

            if option == 1: # Se a opção 1 for escolhida no menu
                level = Level(self.window, "Fase 1")
                level.run() # Executa o nível
            elif option == -1: # Se o usuário fechar a janela no menu
                break

        pygame.quit()
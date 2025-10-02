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
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        #Inicia e gerencia o loop principal do jogo.

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # check for all events
            # for event in pygame.event.get():
            #  if event.type == pygame.QUIT:
            #        pygame.quit()  # fechar a janela
            #        quit()  # fechar pygame



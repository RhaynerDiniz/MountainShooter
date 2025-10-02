# menu.py
import pygame

class Menu:
    """
    Gerencia a tela de menu do jogo.
    """
    def __init__(self, window: pygame.Surface):
        self.window = window

    def run(self) -> int:
        """
        Executa o loop do menu e retorna a opção selecionada.
        """
        print("Menu está em execução. Pressione ENTER para iniciar ou feche a janela.")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1 # Sinaliza para fechar o jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print("Opção 'Iniciar Jogo' selecionada.")
                        return 1 # Retorna 1 para iniciar o primeiro nível

            self.window.fill((100, 100, 100)) # Fundo cinza para o menu
            pygame.display.flip()
        return -1
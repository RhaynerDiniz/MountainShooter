import pygame

print('Setup START')
pygame.init()
window = pygame.display.set_mode(size = (600,480))
print('Setup END')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # fechar a janela
            quit() # fechar pygame
# background.py
from entity import Entity

class Background(Entity):
    """
    Representa o cenário de fundo do jogo.
    """
    def move(self) -> None:
        """
        Implementa o movimento do fundo para criar efeitos como parallax.
        """
        # print(f"Background {self.name} está se movendo.")
        pass
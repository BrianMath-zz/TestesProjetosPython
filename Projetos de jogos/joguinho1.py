import pygame
from time import sleep

# Cores
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

# Inicializar tudo
pygame.init()

# Tamanho da tela e título
screen = pygame.display.set_mode((640, 480))  # (x, y)
pygame.display.set_caption("Desenhando na tela")

# Cor do fundo
screen.fill(Black)

# Desenhando na tela
pygame.draw.polygon(screen, Green, [[180, 50], [40, 400], [620, 220]])  # superfície, cor, [[x0, y0], [x1, y1], ... [xn, yn]]
pygame.draw.line(screen, White, [0, 10], [640, 10], 3)  # superfície, cor, [x0, y0], [x, y], espessura
pygame.draw.rect(screen, Blue, [200, 210, 40, 40])  # superfície, cor, [x0, y0, largura, altura]
pygame.draw.ellipse(screen, Red, [200, 210, 40, 40])  # superfície, cor, [x0, y0, largura, altura]
pygame.draw.circle(screen, White, [400, 230], 20)  # superfície, cor, [xCentral, yCentral], raio

# Atualizando a tela
pygame.display.flip()

# Aguarda com a tela até continuar o código
sleep(5)

# Cor do fundo
screen.fill(White)

# Formatando o texto
font = pygame.font.SysFont("Bahnschrift", 60)  # fonte (None: escolhe a fonte padrão), tamanho da fonte

# Definindo o texto
text = font.render("Brian Bonitão", True, Blue)  # string, antialias (suaviza o contorno do texto), cor

# Copiando o texto para a superfície
screen.blit(text, [150, 200])  # texto formatado e definido, [x, y]

# Atualizando a tela
pygame.display.flip()

# Aguarda com a tela até finalizar o programa
sleep(5)

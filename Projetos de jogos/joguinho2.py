import pygame
from math import floor
from random import random

# Cores
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

# Inicializar tudo
pygame.init()

# Tamanho da tela e título
screen = pygame.display.set_mode((600, 500))  # (x, y)
pygame.display.set_caption("Laço while")

# variáveis da bola
position_x = 310
position_y = 260
velocity_x = 0.5
velocity_y = 0.5

# Laço de repetição da tela
while True:
	# PROCESSAMENTO DE ENTRADA

	# capturar eventos
	event = pygame.event.poll()

	# se clicar no no botão x, sai
	if event.type == pygame.QUIT:
		break

	# ATUALIZAÇÃO DO JOGO

	# mover a bola
	position_x += velocity_x
	position_y += velocity_y

	# mudando a direção no eixo x nas bordas
	if position_x > 550:
		velocity_x = -random()
	elif position_x < 0:
		velocity_x = random()

	# mudando a direção no eixo y nas bordas
	if position_y > 450:
		velocity_y = -random()
	elif position_y < 0:
		velocity_y = random()

	# DESENHO

	# preenchendo o fundo com preto
	screen.fill(Black)

	# desenhando a bola
	pygame.draw.ellipse(screen, Blue, [floor(position_x), floor(position_y), 60, 60])

	# atualizando a tela
	pygame.display.flip()

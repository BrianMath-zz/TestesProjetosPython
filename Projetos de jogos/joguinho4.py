import pygame
from pygame.locals import *  # QUIT, K_DOWN, K_UP, etc.
from random import randint

# Cores
Black = (0, 0, 0)
Red = (255, 0, 0)
White = (255, 255, 255)

# Inicializar, colocar tela e título
pygame.init()
tamanhoTela = (600, 600)
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("Jogo da cobrinha")


# Função para alinhar a maçã às posições da cobra (múltiplos de 10)
def align_apple_random():
	x = randint(0, tamanhoTela[1]-10)  # Tela de "tamanhoTela"px e maçã de 10px, então tira 10px
	y = randint(0, tamanhoTela[1]-10)
	return (x//10 * 10, y//10 * 10)


# Função para verificar colisão
def collision(c1, c2):
	return (c1[0] == c2[0]) and (c1[1] == c2[1])


# Direções
Left = 0
Up = 1
Right = 2
Down = 3

# Tamanho, cor e direção da cobrinha
cobra = [(200, 200), (210, 200), (220, 200)]
cobraCor = pygame.Surface((10, 10))  # Criar superfície 10x10 da cobra
cobraCor.fill(White)  # Cobra branca
direction = Left

# Tamanho e cor da maçã
apple = pygame.Surface((10, 10))  # Criar superfície 10x10 da maçã
apple.fill(Red)  # Cor vermelha
posApple = align_apple_random()

fps = pygame.time.Clock()

while True:
	# Ajustar os 30 fps
	fps.tick(30)

	# Pegar os eventos
	for event in pygame.event.get():
		# Fechar a tela
		if event.type == QUIT:
			pygame.quit()

		# Detectar a tecla pressionada
		if event.type == pygame.KEYDOWN:
			if event.key == K_UP:
				direction = Up
			if event.key == K_DOWN:
				direction = Down
			if event.key == K_LEFT:
				direction = Left
			if event.key == K_RIGHT:
				direction = Right

	# Verificar colisão. Se o "x" e "y" das posiçôes 0 forem iguais, houve colisão
	if collision(cobra[0], posApple):
		posApple = align_apple_random()
		cobra.append((0, 0))  # Não importa a posição, pois ela ocupa a posição anterior

	# Verificar colisão com o próprio corpo
	for j in range(1, len(cobra)):
		corpoCobra = cobra[j]
		if collision(cobra[0], corpoCobra):
			pygame.quit()

	# Ocupar posição anterior
	for i in range(len(cobra) - 1, 0, -1):  # Passa por todas as posições de trás para frente
		cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])
	'''
	Explicação com cobra de 3 posições: range(2, 0, -1)
	1º- cobra[2] = (cobra[1][0], cobra[1][1]) -> posição 2 recebe os dois valores da posição 1
	2º- cobra[1] = (cobra[0][0], cobra[0][1]) -> posição 1 recebe os dois valores da posição 0
	'''

	# Movimento da cobrinha
	if direction == Up:
		cobra[0] = (cobra[0][0], cobra[0][1] - 10)  # Mexe a cabeça 10px para cima
	if direction == Down:
		cobra[0] = (cobra[0][0], cobra[0][1] + 10)  # Mexe a cabeça 10px para baixo
	if direction == Left:
		cobra[0] = (cobra[0][0] - 10, cobra[0][1])  # Mexe a cabeça 10px para esquerda
	if direction == Right:
		cobra[0] = (cobra[0][0] + 10, cobra[0][1])  # Mexe a cabeça 10px para direita

	# Fundo preto
	tela.fill(Black)

	# Desenhar maçã e cobrinha na tela
	tela.blit(apple, posApple)
	for posCobra in cobra:
		tela.blit(cobraCor, posCobra)  # superfície, posição

	# Atualizar a tela. pygame.display.update() == pygame.display.flip()
	pygame.display.update()

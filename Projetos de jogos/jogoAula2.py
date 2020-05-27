import pygame
from math import floor

# Cores
azul = (0, 0, 255)
preto = (0, 0, 0)
branco = (255, 255, 255)
amarelo = (255, 211, 0)

# Tamanho da tela e título
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Aula 2 - Pular")

x1, y1 = 30, 450
x2, y2 = 450, 450
larg = altu = 20
vel = 5

# Variáveis do pulo
taPulando1 = taPulando2 = False
contPulo1 = contPulo2 = 10

fps = pygame.time.Clock()
while True:
	fps.tick(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	tecla = pygame.key.get_pressed()  # Vê se as teclas estão pressionadas ou não

	# A segunda condição é para não sair da borda
	# Jogador 1
	if tecla[pygame.K_LEFT] and (x1 > 0):
		x1 -= vel
	if tecla[pygame.K_RIGHT] and (x1 < 480):
		x1 += vel
	if not(taPulando1):           # Normalmente será not(False) == True, portanto, funcionará de boa
		if tecla[pygame.K_UP] and (y1 > 0):
			y1 -= vel
		if tecla[pygame.K_DOWN] and (y1 < 480):
			y1 += vel
		if tecla[pygame.K_KP0]:   # Quando apertar no espaço a condição ficará not(True) == False,
			taPulando1 = True     # portanto, o jogador não pode subir nem descer, só ir para os lados
	# Código do pulo
	else:
		if contPulo1 >= -10:
			neg = 1
			if contPulo1 < 0:     # Se estiver positivo multiplicará por 1 (sem diferença)
				neg = -1          # Se estiver negativo multiplicará por -1 (- com - = +)
			y1 -= (contPulo1 ** 2) * 0.5 * neg
			contPulo1 -= 1
		else:                     # Quando o pulo acabar as variáveis reiniciam
			contPulo1 = 10
			taPulando1 = False

	# Jogador 2
	if tecla[pygame.K_a] and (x2 > 0):
		x2 -= vel
	if tecla[pygame.K_d] and (x2 < 480):
		x2 += vel
	if not(taPulando2):
		if tecla[pygame.K_w] and (y2 > 0):
			y2 -= vel
		if tecla[pygame.K_s] and (y2 < 480):
			y2 += vel
		if tecla[pygame.K_g]:
			taPulando2 = True
	else:
		if contPulo2 >= -10:
			neg = 1
			if contPulo2 < 0:
				neg = -1
			y2 -= (contPulo2 ** 2) * 0.5 * neg
			contPulo2 -= 1
		else:
			contPulo2 = 10
			taPulando2 = False

	pygame.draw.rect(tela, azul, (x1, floor(y1), larg, altu))  # superfície, cor, (x, y, largura, altura)
	pygame.draw.rect(tela, amarelo, (x2, floor(y2), larg, altu))  # Usei floor() para ficar inteiro

	pygame.display.update()  # Atualiza a tela
	tela.fill(preto)  # Preenche o funco com preto

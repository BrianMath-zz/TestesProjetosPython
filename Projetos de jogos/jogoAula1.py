import pygame

# Cores
azul = (0, 0, 255)
preto = (0, 0, 0)
branco = (255, 255, 255)

# Tamanho da tela e título
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Aula 1")

x1, y1 = 30, 450
x2, y2 = 450, 450
larg, altu = 20, 20
vel = 3

while True:
	pygame.time.delay(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	tecla = pygame.key.get_pressed()  # Vê se as teclas estão pressionadas ou não

	# A segunda condição é para não sair da borda
	# Jogador 1
	if tecla[pygame.K_UP] and (y1 > 0):
		y1 -= vel
	if tecla[pygame.K_DOWN] and (y1 < 480):
		y1 += vel
	if tecla[pygame.K_LEFT] and (x1 > 0):
		x1 -= vel
	if tecla[pygame.K_RIGHT] and (x1 < 480):
		x1 += vel

	# Jogador 2
	if tecla[pygame.K_w] and (y2 > 0):
		y2 -= vel
	if tecla[pygame.K_s] and (y2 < 480):
		y2 += vel
	if tecla[pygame.K_a] and (x2 > 0):
		x2 -= vel
	if tecla[pygame.K_d] and (x2 < 480):
		x2 += vel

	pygame.draw.rect(tela, azul, (x1, y1, larg, altu))  # superfície, cor, (x, y, largura, altura)
	pygame.draw.rect(tela, branco, (x2, y2, larg, altu))

	pygame.display.update()  # Atualiza a tela
	tela.fill(preto)  # Preenche o funco com preto

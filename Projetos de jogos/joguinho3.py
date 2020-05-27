import pygame

# Cores
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)

# Inicializar tudo
pygame.init()

# Tela e título
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Título")

# Criar Rect para o quadrado que mexe
square = pygame.Rect(280, 220, 18, 18)  # x0, y0, largura, altura

# Criar Rect para os pads
left_pad = pygame.Rect(20, 190, 20, 80)
right_pad = pygame.Rect(560, 190, 20, 80)

pads = [left_pad, right_pad]

# Relogio do pygame funciona em ms, então 200px/s deve ser 0.2px/s
velocity_x = 0.2

# Instância do relógio
clock = pygame.time.Clock()

while True:
	# Capturar evento de fechar o jogo
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break

	# Ticks são os fps, portanto, 30fps
	dt = clock.tick(30)

	# Usar função move in place (move no lugar) == delta S = V*dt (delta t)
	square.move_ip(int(velocity_x * dt), 0)  # x, y --> y = 0, não altera o y

	# Checar colisão com pads. collidelist(list) recebe uma lista e retorna -1 se não houver colisão
	if square.collidelist(pads) >= 0:
		velocity_x = -velocity_x

	# Preencher o fundo com cor preta
	screen.fill(Black)

	# Desenhar quadrado de acordo com a posição do Rect do quadrado
	pygame.draw.rect(screen, White, square)

	# Desenhar os pads
	for pad in pads:
		pygame.draw.rect(screen, Blue, pad)

	# Atualizar tela
	pygame.display.flip()

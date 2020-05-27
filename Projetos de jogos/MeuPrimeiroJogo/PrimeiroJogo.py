import pygame
from pygame import image as img

# Cores
preto = (0, 0, 0)
cinza = (80, 80, 80)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
amarelo = (255, 211, 0)

# Tamanho da tela e título
largTela, altuTela = 925, 520
tela = pygame.display.set_mode((largTela, altuTela))
pygame.display.set_caption("Meu primeiro jogo")

# Relógio para configurar fps
fps = pygame.time.Clock()

# Carregar fundo
fundo = pygame.image.load("background.png")


# Classe do jogador 1
class Jogador1(object):
	andarDireita = [img.load(f"J1-D{j}.png") for j in range(8)]
	andarEsquerda = [img.load(f"J1-E{i}.png") for i in range(8)]
	paradoLados = [img.load("J1-D.png"), img.load("J1-E.png")]
	jogador1 = pygame.image.load("J1.png")

	def __init__(self, largJ1, altuJ1, x, y):  # Estes argumentos serão definidos pelo usuário. Os outros, não
		self.x = x
		self.y = y
		self.largJ1 = largJ1
		self.altuJ1 = altuJ1
		self.vel = 7
		self.taPulando = False
		self.contPulo = 10
		self.direita = False
		self.esquerda = False
		self.contAndar = 0
		self.taParado = True

	def desenhar(self, tela):  # Desenha os sprites
		if self.contAndar + 1 >= 32:  # 8 sprites * 4 vezes
			self.contAndar = 0        # Contagem reinicia

		if not self.taParado:  # Se não está parado, portanto, está movendo
			if self.direita:
				tela.blit(self.andarDireita[self.contAndar // 4], (self.x, self.y))  # 4 frames/imagem
				self.contAndar += 1                                                  # Passa por todos os sprites
			elif self.esquerda:
				tela.blit(self.andarEsquerda[self.contAndar // 4], (self.x, self.y))
				self.contAndar += 1
		else:  # Parado ou pulando
			if self.direita:  # Parou olhando para a direita
				tela.blit(self.paradoLados[0], (self.x, self.y))  # Fica com o primeiro sprite para a direita
			else:             # Parou olhando para a esquerda
				tela.blit(self.paradoLados[1], (self.x, self.y))  # Fica com o primeiro sprite para a direita


# Classe da bala
class Projetil(object):
	def __init__(self, x, y, raio, cor, direcao):
		self.x = x
		self.y = y
		self.raio = raio
		self.cor = cor
		self.direcao = direcao
		self.vel = 8 * direcao

	def desenhar(self, tela):
		pygame.draw.circle(tela, self.cor, (self.x, self.y), self.raio)


# Classe do inimigo
class Inimigo(object):
	andarDireita = [img.load(f"E1-D{i}.png") for i in range(11)]
	andarEsquerda = [img.load(f"E1-E{j}.png") for j in range(11)]

	def __init__(self, largura, altura, x, y, fim):
		self.largura = largura
		self.altura = altura
		self.x = x
		self.y = y
		self.fim = fim
		self.caminho = [self.x, self.fim]
		self.vel = 7
		self.contAndar = 0

	def desenhar(self, tela):
		self.mover()

		if self.contAndar + 1 >= 44:
			self.contAndar = 0

		if self.vel > 0:  # Se estiver indo para a direita
			tela.blit(self.andarDireita[self.contAndar // 4], (self.x, self.y))
			self.contAndar += 1
		else:             # Se estiver indo para a esquerda
			tela.blit(self.andarEsquerda[self.contAndar // 4], (self.x, self.y))
			self.contAndar += 1

	def mover(self):
		if self.vel > 0:  # Se a velocidade for positiva
			if self.x + self.vel < self.caminho[1]:  # Se o inimigo puder andar dentro dos limites
				self.x += self.vel  # Inimigo anda
			else:                                    # Se o inimigo não puder andar dentro dos limites
				self.vel *= -1     # Velocidade inverte, portanto, inimigo anda para trás
				self.contAndar = 0
		else:             # Se a velocidade for negativa
			if self.x - self.vel > self.caminho[0]:
				self.x += self.vel
			else:
				self.vel *= -1
				self.contAndar = 0


# Função dos desenhos
def desenharNaTela():
	tela.blit(fundo, (0, 0))  # Põe a imagem do fundo para cobrir tudo -> imagem, (x, y)
	Sam.desenhar(tela)
	Larry.desenhar(tela)
	for bala in balas:
		bala.desenhar(tela)
	pygame.display.update()  # Atualiza a tela


"""    Loop do jogo     """


# Sam é a referência à classe 'Jogador1'
Sam = Jogador1(90, 120, 417, 390)  # largJ1, altuJ1, x0, y0
Larry = Inimigo(90, 120, 0, 390, 835)  # largura, altura, x0, y0, xFinal
balas = []
while True:
	fps.tick(32)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	for bala in balas:
		if 0 < bala.x < 925:  # Dentro da tela
			bala.x += bala.vel
		else:                 # Fora da tela
			balas.pop(balas.index(bala))  # Deleta a bala

	teclas = pygame.key.get_pressed()  # Vê se as teclas estão pressionadas ou não

	if teclas[pygame.K_SPACE]:
		if Sam.direita:
			direcao = 1
		else:
			direcao = -1

		if len(balas) < 8:  # No máximo 8 balas na tela por vez
			balas.append(Projetil(Sam.x + (Sam.largJ1//2), Sam.y + (Sam.altuJ1//2), 6, amarelo, direcao))
			# Projetil(x, y, raio, cor, direcao)

	# A segunda condição é para não sair da borda
	# Jogador 1
	if teclas[pygame.K_LEFT] and (Sam.x > 0):
		Sam.x -= Sam.vel
		Sam.direita = False
		Sam.esquerda = True
		Sam.taParado = False
	elif teclas[pygame.K_RIGHT] and (Sam.x < largTela - Sam.largJ1):
		Sam.x += Sam.vel
		Sam.direita = True
		Sam.esquerda = False
		Sam.taParado = False
	else:  # Se não estiver indo para a direita nem para a esquerda tá parado
		Sam.taParado = True
		Sam.contAndar = 0

	if not Sam.taPulando:  # Normalmente será not(False) == True, portanto, funcionará de boa
		if teclas[pygame.K_UP]:
			Sam.taPulando = True
			Sam.direita = False
			Sam.esquerda = False
			Sam.contAndar = False
	# Código do pulo
	else:
		if Sam.contPulo >= -10:
			neg = 1
			if Sam.contPulo < 0:  # Se estiver positivo multiplicará por 1 (sem diferença)
				neg = -1       # Se estiver negativo multiplicará por -1 (- com - = +)
			Sam.y -= (Sam.contPulo ** 2) // 2 * neg
			Sam.contPulo -= 1
		else:  # Quando o pulo acabar as variáveis reiniciam
			Sam.contPulo = 10
			Sam.taPulando = False

	desenharNaTela()

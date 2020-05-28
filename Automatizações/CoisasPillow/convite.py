from PIL import Image, ImageDraw, ImageFont

Convidados = [
	"Alberto",
	"Bernardo",
	"Clarita",
	"Danila"
]

fonte = ImageFont.truetype("./Futura Md BT Medium.ttf", size=90)

for convidado in Convidados:
	imagem = Image.open("./convite.jpg").convert("RGBA")

	lapis = ImageDraw.Draw(imagem)

	lapis.text(
		(158, 490),
		text=f"Olá, {convidado}",
		fill="#000000",
		font=fonte
	)

	lapis.line(
		(158, 588, 1650, 588),
		fill="#808080",
		width=10
	)

	lapis.text(
		(130, 800),
		text="Venha à minha festinha!",
		fill="#000000",
		font=fonte
	)

	lapis.text(
		(130, 900),
		text="E não se esqueça do meu presente, hein!",
		fill="#000000",
		font=fonte
	)

	lapis.text(
		(130, 1200),
		text="Dia 28/05/2020",
		fill="#000000",
		font=fonte
	)

	imagem.save(f"./convite_{convidado}.png")

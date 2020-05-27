import turtle

colors = ["red", "purple", "blue", "green", "orange", "yellow", "pink", "white", "cyan", "gray"]  # Cores da caneta
tPen = turtle.Pen()  # Caneta que desenha na tela
turtle.bgcolor("black")  # Cor do fundo

for i in range(8):
    tPen.pencolor(colors[i])  # Troca as cores a cada loop
    tPen.forward(40)  # Vai para a frente
    tPen.left(135)  # Vira para a esquerda

turtle.done()  # Finaliza

import pyautogui as pg

pg.confirm("Clique em OK?")  # Pop-up com botão OK e Cancelar
simNao = pg.confirm(title="Confirmação (ou não)",
                    text="Você deve confirmar (ou não)",
                    buttons=["Confirmar", "Ou não", "Ué, 3 botões?"])
print(simNao, type(simNao))  # Imprime o texto do botão


texto = pg.prompt("Digita aí:")  # Janela para escrever
resp = pg.prompt(title="Pregunta muy difícil",
                 text="Quanto é (-5*(5)/(-(-5)))*0?",
                 default="O que eu faço?")

if resp == "0":
    pg.alert("Congratulations, you got it!")
else:
    pg.alert("Sua professora de matemática teria vergonha de você!")


pg.password(title="Qual a senha do wi-fi?",
            text="Eu juro, eu não aguento mais",
            default="1234567890", mask="+")
senha = pg.password("Digita sua senha do banco aí rapidinho:")  # Janela para escrever senha
pg.alert(f'Seria "{senha}" a sua senha?')


pg.alert(f'Você digitou "{texto}"')  # Pop-up com um botão OK
alerta = pg.alert(text="Isso é um texto", title="Isso é um título", button="Isso é um botão")
print(alerta, type(alerta))  # Imprime o texto do botão

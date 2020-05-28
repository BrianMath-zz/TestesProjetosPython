from time import sleep
import pyautogui as pg

sleep(3)
simNao = pg.confirm(title="Já tentou alguma vez?", text="Escolha uma resposta:", buttons=["Sim", "Não"])

if simNao == "Sim":
	pg.moveTo(78, 557, duration=2)
	pg.click()
	sleep(4)
	pg.moveTo(91, 635, duration=1)
	pg.click()

if simNao == "Não":
	pg.moveTo(75, 550, duration=2)
	pg.click()
	sleep(4)
	pg.moveTo(79, 632, duration=1)
	pg.click()

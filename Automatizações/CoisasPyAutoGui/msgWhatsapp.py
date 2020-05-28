import pyautogui as pg
from time import sleep

sleep(5)
pg.moveTo(162, 13, duration=3)
pg.click()
pg.moveTo(737, 975, duration=3)
pg.click()
for i in range(30):
	pg.typewrite("Oi, escrito em Python", interval=0.001)
	pg.press("Enter")

# x=162, y=13: aba do Whatsapp
# x=737, y=975: espaço para escrever

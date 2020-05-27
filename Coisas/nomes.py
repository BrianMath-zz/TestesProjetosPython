import names
import random

nomesFem = []
for i in range(3):
	nomesFem.append(names.get_first_name("male"))
print(nomesFem)
print(random.choice(nomesFem))

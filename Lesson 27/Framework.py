# модуль
# встроенным модулем и модули проекта
import module # модуль проекта
# модули пайтона (встроенные)
import math as m
from random import randint, choice
# библиотека
# невстроенные библиотека (устанавливается через команду в терминале pip install название библиотеки/модуля
import requests
# фреймворк
print(requests.get("https://youtube.com"))
random_integer = randint(1, 100)
print(random_integer)
print(m.floor(3.5))
print(m.ceil(4.5))
module.hello()

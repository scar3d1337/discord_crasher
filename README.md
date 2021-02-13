# Discord Crasher Bot/DCB
![Лого](https://i.ibb.co/VjfhxXQ/photo-2021-02-13-22-31-00.jpg)
# Установка
```
sudo apt install python3 python3-pip
pip3 install discord
pip3 install colorama
pip3 install requests
git clone https://github.com/GlUTEN-BASH/discord_crasher/
cd discord_crasher
```
# Запуск 
Для начала отредактируйте файл modded.py, и в самом конце найдите строку
```
client.run('токен сюда')
```
Где написанно 'токен сюда' вставьте токен своего бота, не удаляя кавычки.

Во вкладке bot в discord developers нужно пролистать вниз и включить server members intent
![Воть](https://i.ibb.co/c8cZ68g/unknown.png)

Далее сохраните изменения и пропишите 
```
python3 modded.py
```

Готово! Бот должен быть онлайн, а в окне программы появиться:
![вот](https://i.ibb.co/CBjMWqf/photo-2021-02-13-22-41-43.jpg)

Боту на сервере нужно выдать администратора, или встроить администраторку заранее в OAuth2


# FAQ:
# Не работает на windows:
Качаем python 3.7 - https://www.python.org/downloads/
В установщике ставим галочку add to path
Далее устанавливаем
и открываем cmd 
Пишем:
```
python -m pip install discord
python -m pip install colorama
python -m pip install requests
```
Готово! Можно открывать.

# Не крашит, только меняет имя:

Вы не дали боту права администратора на сервере, это нужно было сделать заранее, во вкладе OAuth2 в создании приглашения.

![Вот так](https://i.ibb.co/nnsgk4w/chrome-kdp4-Swtw22.png)

# Сразу закрывается:

Вы не ввели токен в программу.

Для этого нужно отредактировать программу, и в самом конце в строке
```
client.run('токен сюда')
```
вместо слов "токен сюда" вводите ваш токен, !!!не убирая кавычки!!!

# Дисклеймер и контакты
Внимание: Автор не берет на себя ответственность за совершенные вами действия, поэтому не надо писать что-то по типу "ой, я нажил себе проблем"

Телеграмм автора для связи: @GLUTESHUNECHKA

Дискорд:sPicY_mAmmA_Mia_T00lbar#6593

Дискорд сервер:https://discord.gg/Un7umZQp8z

Всем цмок ;)

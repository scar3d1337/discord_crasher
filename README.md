# Discord Crasher Bot/DCB
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

Далее сохраните изменения и пропишите 
```
python3 modded.py
```
Готово! Бот должен быть онлайн
Боту на сервере нужно выдать администратора, или встроить администраторку заранее в OAuth2

FAQ:
Не работает на windows:
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

Не крашит, только меняет имя:

Вы не дали боту права администратора на сервере, это нужно было сделать заранее, во вкладе OAuth2 в создании приглашения.

Сразу закрывается:

Вы не ввели токен в программу.


Внимание: Автор не берет на себя ответственность за совершенные вами действия, поэтому не надо в тг писать что-то по типу "ой, я нажил себе проблем"
Телеграмм автора для связи: @GLUTESHUNECHKA
Всем цмок ;)

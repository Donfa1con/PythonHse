# Homework-_-4
### 1) Для работы консольного скрипта необходитмо:
##### Получить "client_secret" для VK <https://vk.com/dev/client_cred_flow>. Скопировать его в файл (Homework-_-4/Console script/check_vk_online.py) в поле client_secret = '???' вместо вопросов.

### 2) Для работы сайта необходимо:
##### Полученный в 1) пункте "client_secret" скопировать в файл Homework-_-4/app/check_vk_online.py. Установить модули из requirements.txt. 

___
## Console script/check_vk_online.py
Консольный скрипт, который принимает на вход айди или ник человека Вконтакте и выдаёт список его друзей онлайн.
Запускать его надо так: python check_vk_online.py 1 (1 – айди пользователя)
    
    Пример:
    check_vk_online.py 1
    Александра Владимирова https://vk.com/id2
    Юлий Джумасултанов https://vk.com/id12
    Татьяна Плуталова https://vk.com/id34
    Сергей Виноградов https://vk.com/id45
    Сергей Владимиров https://vk.com/id57
    Ольга Усманова https://vk.com/id169
    Вальтер Киршнер https://vk.com/id198
    
    python check_vk_online.py 3
    User was deleted or banned
    
    python check_vk_online.py rexpekt3v
    User has no friends
    
    python check_vk_online.py 124123124124214
    Invalid ID or nickname for the user
 
## run.py
Скрипт, запускающий сайт, сделанный на Фласке, который делает то же, что и консольный скрипт, но в браузере.
В папке app исходники сайта.
 
Ссылка на сайт: <http://flask-friends-online.herokuapp.com>
 

from os import system
import time
import socket

print("Устанавливаю модули...")
try:
    socket.create_connection(("www.google.com", 80))
    system("pip install colorama")
    print("Модули установлены. Запускаю основной код...")
    time.sleep(1)
    system("python maincode.py")
except OSError:
    print("Модули не установлены. Проверьте подключение к интернету.")
    exit()
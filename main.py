import time
import webbrowser
from colorama import Fore, Style
from os import system
import socket

baza = ['алгебра', 'русский', 'геометрия', 'физика', 'англ', 'английский воркбук', 'англ ворк', 'физика']

logo = '''
╔══════════════════════════════════════════════════════════════╗
║ ████████   █████    ██████        ███████  ███████  ████████ ║
║ ██         ██ ██          ██      ██       ██   ██     ██    ║
║ ██         ██ ██    ██████        ███████  ██   ██     ██    ║
║ ██         █████          ██      ██   ██  ██   ██     ██    ║
║ ██       █████████        ██      ██   ██  ██   ██     ██    ║
║ ██       ██     ██  ██████        ███████  ███████     ██    ║
║                                                              ║
║             Версия 1.0 by Ronbin & RelativeModder            ║
╚══════════════════════════════════════════════════════════════╝
'''


def logotip():
    print(Fore.GREEN + logo)
    print(Style.RESET_ALL)


def clear():
    system("clear")


def nemozhet():
    print(Fore.RED + "Не может быть меньше 1!")
    print(Style.RESET_ALL)
    exit()


def opened():
    print(Fore.GREEN + "Ссылка открыта")
    print(Style.RESET_ALL)


def nopage():
    print(Fore.RED + "Такой страницы нет!")
    print(Style.RESET_ALL)


def checkinternet():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        print(Fore.RED + "Проверьте подключение к интернету")
    exit()
    

def tostart():
	opt = input("Нажмите Enter чтобы вернуться в начало.")
	if opt == "":
		mainp()

def mainp():
    clear()
    logotip()
    print("Выберите опцию:")
    print("1. Найти гдз")
    print("2. Посмотреть список предметов")
    op = int(input("Опция: "))

    if op == 1:
        clear()
        logotip()
        predm = input("Какой предмет? ")
        if predm in baza:
            if predm == "алгебра":
                nomer = int(input("Какой номер? "))
                if nomer >= 1:
                    webbrowser.open(f'https://gdz.ru/class-7/algebra/kolyagin-tkacheva/{nomer}-nom/', new=2)
                    print(Fore.GREEN + 'Ссылка открыта!')
                    print(Style.RESET_ALL)
                    tostart()
                elif nomer < 1:
                    nemozhet()
                    tostart()
            elif predm == "русский":
                nomer = int(input("Какой номер? "))
                if nomer >= 1:
                    webbrowser.open(f'https://gdz.ru/class-7/russkii_yazik/baranova/{nomer}-nom/', new=2)
                    print(Fore.GREEN + 'Ссылка открыта!')
                    print(Style.RESET_ALL)
                    tostart()
                elif nomer < 1:
                    nemozhet()
                    tostart()
            elif predm == "геометрия":
                glava = int(input("Какая глава? "))
                if glava >= 1:
                    nomer = int(input("Какой номер? "))
                    if nomer >= 1:
                        webbrowser.open(f"https://gdz.ru/class-7/geometria/atanasyan-7-9/{glava}-chapter-{nomer}/")
                        print('Ссылка открыта!')
                        print(Fore.GREEN)
                        tostart()
                    elif nomer < 1:
                        print(Fore.RED + "Не может быть меньше 1!")
                        print(Style.RESET_ALL)
                        tostart()
                elif glava > 14:
                    print(Fore.RED + "Такой главы нет!")
                    print(Style.RESET_ALL)
                    tostart()
                elif glava < 1:
                    print(Fore.RED + "Такой главы нет!")
                    print(Style.RESET_ALL)
                    tostart()
            elif predm == "англ":
                page = int(input("Какая страница? "))
                if page >= 1 and page <= 166:
                    webbrowser.open(f"https://gdz.ru/class-7/english/starlight-baranova/{page}-s/")
                    opened()
                    tostart()
                elif page < 1:
                    print(Fore.RED + "Не может быть меньше 1!")
                    print(Style.RESET_ALL)
                    tostart()
                elif page > 166:
                    print(Fore.RED + "Такой страницы нет!")
                    print(Style.RESET_ALL)
                    tostart()
            elif predm == "англ ворк":
                page = int(input("Какая страница? "))
                if page >= 1 and page <= 95:
                    webbrowser.open(f"https://gdz.ru/class-7/english/starlight-tetrad-baranova/{page}-s/")
                    opened()
                    tostart()
                elif page < 1 or page > 95:
                    nopage()
                    tostart()
            elif predm == "физика":
                print("Выберите тип задания.")
                print("1. Упражнения.")
                print("2. Вопросы в конце параграфа.")
                print("3. Задания. Параграфы.")
                tip = int(input("Тип: "))
                if tip == 1:
                    nomerupr = int(input("Введите номер упражнения. Он изображается так: (ссылка) "))
                    if nomerupr >= 1:
                        nomer = int(input("Введите номер задания: "))
                        if nomer >= 1:
                            webbrowser.open(f"https://gdz.ru/class-7/fizika/peryshkin-7/{nomerupr}-nom-{nomer}/")
                            tostart()
                    elif nomerupr < 1:
                        nemozhet()
                elif tip == 2:
                	paragraf = int(input("Введите номер параграфа: "))
                	if paragraf >= 1:
                		opened()
                		webbrowser.open(f"https://gdz.ru/class-7/fizika/peryshkin-7/{paragraf}-quest/")
                		tostart()
                	elif paragraf < 1:
                		nemozhet()
                		tostart()
                elif tip == 3:
                	paragraf = int(input("Введите номер параграфа: "))
                	if paragraf >= 1:
                		opened()
                		webbrowser.open(f"https://gdz.ru/class-7/fizika/peryshkin-7/{paragraf}-inom/")
                		tostart()
                	elif paragraf < 1:
                		nemozhet()
                elif tip > 3 or  tip < 1:
                	print(Fore.RED + "Вы ввели число больше 3 или меньше 1.")
                	print(Style.RESET_ALL)
                	tostart()
        elif predm != baza:
            print(Fore.RED + "Вы ввели предмет который не находится в нашей базе.")
            print(Style.RESET_ALL)
            tostart()
    elif op == 2:
        clear()
        logotip()
        print(baza)
        tomain = int(input("Чтобы вернуться нажмите 0: "))
        if tomain == 0:
            mainp()
        elif tomain != 0:
            exit()


checkinternet()
mainp()

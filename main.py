try:
	import time
	import webbrowser
	from os import system
	import socket
	from colorama import Fore, Style
	
	baza = ['--- 6 класс ---', 'английский 6 класс Старлайт', 'география 6 класс Ложбанидзе','история россии 6 класс Пчелов', 'литература 6 класс Коровина', 'математика 6 класс Мерзляк', 'русский 6 класс Ладыженская', '', '--- 7 класс ---', 'алгебра 7 класс Колягин', 'английский 7 класс Старлайт', 'английский 7 класс Старлайт Воркбук',
	'биология 7 класс Латюшин', 'геометрия 7 класс Атанасян', 'география 7 класс Алексеев', 'информатика 7 класс Босова', 'литература 7 класс Коровина', 'русский язык 7 класс Ладыженская', 'физика 7 класс Перышкин']
	
	logo = '''
	╔══════════════════════════════════════════════════════════════╗
	║ ████████   █████    ██████        ███████  ███████  ████████ ║
	║ ██         ██ ██          ██      ██       ██   ██     ██    ║
	║ ██         ██ ██    ██████        ███████  ██   ██     ██    ║
	║ ██         █████          ██      ██   ██  ██   ██     ██    ║
	║ ██       █████████        ██      ██   ██  ██   ██     ██    ║
	║ ██       ██     ██  ██████        ███████  ███████     ██    ║
	║                                                              ║
	║             Версия 1.1 by Ronbin & RelativeModder            ║
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
	    clear()
	    try:
	        print("Проверка подключения интернета...")
	        socket.create_connection(("www.google.com", 80))
	        print(Fore.GREEN + "Интернет доступен")
	        print(Style.RESET_ALL)
	        time.sleep(0.5)
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
	    print("0. Выйти")
	    try:
	    	op = int(input("Опция: "))
	    	pass
	    except ValueError:
	    	print(Fore.RED + "Введено неверное значение.")
	    	print(Style.RESET_ALL)
	    	exit()
	
	    if op == 1:
	        clear()
	        logotip()
	        predm = input("Какой предмет? ")
	        if predm in baza:
	            # 6 КЛАСС
	            if predm == "английский 6 класс Старлайт":
	            	page = int(input("Какая страница? "))
	            	if page >= 1:
	            		opened()
	            		webbrowser.open(f"https://gdz.ru/class-6/english/reshebnik-baranova-k-m-starlight-6-zvezdnyy-angliyskiy/{page}-s/")
	            		tostart()
	            	elif page < 1:
	            		nemozhet()
	            		tostart()
	            elif predm == "география 6 класс Ложбанидзе":
	            	paragraf = int(input("Какой параграф? "))
	            	if paragraf >= 1:
	            		opened()
	            		webbrowser.open(f"https://gdz.ru/class-5/geografiya/lobzhanidze/{paragraf}-item/")
	            		tostart()
	            	elif paragraf < 1:
	            		nemozhet()
	            		tostart()
	            elif predm == "история россии 6 класс Пчелов":
	            	paragraf = int(input("Какой параграф? "))
	            	if paragraf >= 1 and paragraf != 6:
	            		opened()
	            		webbrowser.open(f"https://gdz.ru/class-6/istoriya/pchelov/{paragraf}-item/")
	            		tostart()
	            	elif paragraf == 6:
	            		opened()
	            		webbrowser.open("https://gdz.ru/class-6/istoriya/pchelov/5-item/")
	            		tostart()
	            	elif paragraf < 1:
	            		nemozhet()
	            		tostart()
	            elif predm == "литература 6 класс Коровина":
	            	part = int(input("Какая часть учебника? "))
	            	if part < 1 or part > 2:
	            		print(Fore.RED + "Такой части нет!")
	            		print(Style.RESET_ALL)
	            		tostart()
	            	elif part == 1:
	            		page = int(input("Какая страница? "))
	            		if page >= 1:
	            			opened()
	            			webbrowser.open(f"https://gdz.ru/class-6/literatura/poluhina-korovina/1-prt-{page}/")
	            			tostart()
	            		elif page < 1:
	            			nemozhet()
	            			tostart()
	            	elif part == 2:
	            		page = int(input("Какая страница? "))
	            		if page >= 1:
	            			opened()
	            			webbrowser.open(f"https://gdz.ru/class-6/literatura/poluhina-korovina/2-prt-{page}/")
	            			tostart()
	            		elif page < 1:
	            			nemozhet()
	            			tostart()
	            elif predm == "математика 6 класс Мерзляк":
	            	nomer = int(input("Какой номер? "))
	            	if nomer >= 1:
	            		opened()
	            		webbrowser.open(f"https://gdz.ru/class-6/matematika/a-g-merzlyak/{nomer}-nom/")
	            		tostart()
	            	elif nomer < 1:
	            		nemozhet()
	            		tostart()
	            elif predm == "русский 6 класс Ладыженская":
	            	nomer = int(input("Какой номер? "))
	            	if nomer >= 1:
	            		opened()
	            		webbrowser.open(f"https://gdz.ru/class-6/russkii_yazik/baranov-2008/{nomer}-nom/")
	            		tostart()
	            	elif nomer < 1:
	            		nemozhet()
	            		tostart()
	            # 7 КЛАСС
	            if predm == "алгебра 7 класс Колягин":
	                nomer = int(input("Какой номер? "))
	                if nomer >= 1:
	                    webbrowser.open(f'https://gdz.ru/class-7/algebra/kolyagin-tkacheva/{nomer}-nom/', new=2)
	                    opened()
	                    tostart()
	                elif nomer < 1:
	                    nemozhet()
	                    tostart()
	            elif predm == "русский язык 7 класс Ладыженская":
	                nomer = int(input("Какой номер? "))
	                if nomer >= 1:
	                    webbrowser.open(f'https://gdz.ru/class-7/russkii_yazik/baranova/{nomer}-nom/', new=2)
	                    opened()
	                    tostart()
	                elif nomer < 1:
	                    nemozhet()
	                    tostart()
	            elif predm == "геометрия 7 класс Атанасян":
	                glava = int(input("Какая глава? "))
	                if glava >= 1:
	                    nomer = int(input("Какой номер? "))
	                    if nomer >= 1:
	                        webbrowser.open(f"https://gdz.ru/class-7/geometria/atanasyan-7-9/{glava}-chapter-{nomer}/")
	                        opened()
	                        tostart()
	                    elif nomer < 1:
	                        nemozhet()
	                        tostart()
	                elif glava > 14:
	                    print(Fore.RED + "Такой главы нет!")
	                    print(Style.RESET_ALL)
	                    tostart()
	                elif glava < 1:
	                    print(Fore.RED + "Такой главы нет!")
	                    print(Style.RESET_ALL)
	                    tostart()
	            elif predm == "английский 7 класс Старлайт":
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
	            elif predm == "английский 7 класс Старлайт Воркбук":
	                page = int(input("Какая страница? "))
	                if page >= 1 and page <= 95:
	                    webbrowser.open(f"https://gdz.ru/class-7/english/starlight-tetrad-baranova/{page}-s/")
	                    opened()
	                    tostart()
	                elif page < 1 or page > 95:
	                    nopage()
	                    tostart()
	            elif predm == "физика 7 класс Перышкин":
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
	                            opened()
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
	                elif tip > 3 or tip < 1:
	                    print(Fore.RED + "Вы ввели число больше 3 или меньше 1.")
	                    print(Style.RESET_ALL)
	                    tostart()
	            elif predm == "география 7 класс Алексеев":
	                paragraf = int(input("Введите номер параграфа: "))
	                if paragraf >= 1:
	                    nomerupr = int(input("Введите номер упражнения: "))
	                    if nomerupr >= 1:
	                        opened()
	                        webbrowser.open(f"https://gdz.ru/class-7/geografiya/alekseev/{paragraf}-item-{nomerupr}/")
	                        tostart()
	                    elif nomerupr < 1:
	                        nemozhet()
	                elif paragraf < 1:
	                    nemozhet()
	            elif predm == "информатика 7 класс Босова":
	                paragraf = input("Введите номер параграфа (например 3-2): ")
	                nomerupr = int(input("Введите номер упражнения: "))
	                if nomerupr >= 1:
	                    opened()
	                    webbrowser.open(f"https://gdz.ru/class-7/informatika/reshebnik-bosova-l-l-7/{paragraf}-item-{nomerupr}/")
	                    tostart()
	                elif nomerupr < 1:
	                    nemozhet()
	            elif predm == "биология 7 класс Латюшин":
	            	paragraf = int(input("Введите номер параграфа: "))
	            	if paragraf >= 1:
	            		opened()
	            		webbrowser.open(f"https://gdz.ru/class-7/biologiya/latiushin/{paragraf}-item/")
	            		tostart()
	            	elif paragraf < 1:
	            		nemozhet()
	            elif predm == "литература 7 класс Коровина":
	            	part = int(input("Часть учебника: "))
	            	if part == 1:
	            		page = int(input("Введите страницу: "))
	            		if page >= 1:
	            			opened()
	            			webbrowser.open(f"https://gdz.ru/class-7/literatura/korovina/1-prt-{page}/")
	            			tostart()
	            		elif page < 1:
	            			nemozhet()
	            	elif part == 2:
	            		page = int(input("Введите страницу: "))
	            		if page >= 1:
	            			opened()
	            			webbrowser.open(f"https://gdz.ru/class-7/literatura/korovina/2-prt-{page}/")
	            			tostart()
	            		elif page < 1:
	            			nemozhet()
	            	elif part > 2:
	            		print(Fore.RED + "Такой части нет!")
	            		print(Style.RESET_ALL)
	            		tostart()
	        elif predm != baza:
	            print(Fore.RED + "Вы ввели предмет который не находится в нашей базе.")
	            print(Style.RESET_ALL)
	            tostart()
	    elif op == 2:
	        clear()
	        logotip()
	        for i in range(len(baza)):
	            print(baza[i])
	            time.sleep(0.01)
	        print("")
	        tomain = input("Чтобы вернуться нажмите Enter: ")
	        if tomain == "":
	            mainp()
	        else:
	        	mainp()
	    elif op >= 3:
	    	mainp()
	    if op == 0:
	    	exit()
	
	
	checkinternet()
	mainp()

except ModuleNotFoundError:
	system("clear")
	print("Не найдены необходимые для работы модули. Начинается установка...")
	system("pip install colorama")
	system("python main.py")

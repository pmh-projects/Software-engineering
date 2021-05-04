import speech_recognition  # automatic speech recognition (ASR),
# computer speech recognition, or speech-to-text, is a capability which
# enables a program to process human speech into a written format.
import speech_recognition as s_r  #
import wikipedia  # Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
import random  # his module implements pseudo-random number generators for various distributions.
import webbrowser  # The webbrowser module provides a high-level interface
# to allow displaying Web-based documents to users.
import os  # The OS module in Python provides functions for interacting with the operating system.
import pyttsx3  # yttsx3 is a text-to-speech conversion library in Python.
# Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
import pyaudio  # PyAudio provides Python bindings for PortAudio,
# the cross-platform audio I/O library. With PyAudio, you can easily
# use Python to play and record audio on a variety of platforms.
import sys  # This module provides access to some variables used or
# maintained by the interpreter and to
# functions that interact strongly with the interpreter.
import operator  # The operator module exports a set of efficient
# functions corresponding to the intrinsic operators of Python.
# For example, operator. add(x, y) is equivalent to the expression x+y
# import pickle #The pickle module can transform a complex object
# into a byte stream and it can transform
# the byte stream into an object with the same internal structure.
from time import sleep  # This module provides various time-related functions.
# For related functionality, see also the datetime and calendar modules..
# The sleep() function suspends (waits) execution
# of the current thread for a given number of seconds.
import pyautogui  # https://github.com/asweigart/pyautogui BSD-3-Clause License
from googlesearch import search  # https://github.com/Nv7-GitHub/googlesearch on MIT License

# Voice mechanism
voice_mechanism = pyttsx3.init('sapi5')

wikipedia.set_lang("pl")


def say(audio):
    voice_mechanism.say(audio)
    voice_mechanism.runAndWait()


def introduction():
    say("Witaj w asystencie głosowym")
    print("Witaj w asystencie głosowym")


def command_recognition():
    # Create voice recognition
    r = s_r.Recognizer()
    record = ''

    with s_r.Microphone() as source:
        sleep(2)
        say("Abym mogła Tobie pomóc podaj nazwę funkcji.")

        print(
            "Podstawowe funkcje:"
            "\nwikipedia - uruchamia funkcję wyszukiwania haseł na wikipedii z możlwiością zapisu do pliku."
            "\nzapisz plik - funkcja zapisujaca plik o podanym głosowo tytule i zawartośći podanej."
            "\notwórz plik - otwieranie zapisanego pliku."
            "\ngoogle - wyszukuję 5 pierwszych wyników i uruchamia wyszukiwarkę z podanych hasłem"
            "\nscreenshot - pobiera i zapisuje zawartość ekranu do pliku png z podanym przez użytkownika tytułem"
            "\n"
            "\nFunkcje NET:"
            "\nwyszukiwarka - otwiera wyszukiwarkę bez deklaracji hasła."
            "\notwórz youtube - chcesz posłuchać muzyki?"
            "\npomocy - masz problem z kodem? Otworzę stackoverflow."
            "\nStrona uniwersytetu - uruchamia stronę główną UG."
            "\nstrona wydziału - uruchamia stronę wydziału."
            "\nportal edukacyjny - uruchamia stronę portalu edukacyjnego"
            "\nportal studenta - uruchamia stronę portalu studenta"
            "\n"
            "\nFunkcje dodatkowe:"
            "\nlotto - symulator lotto. Zastanawiałeś się jakie masz szczęście w grach losowych? Sprawdź się."
            "\ngra - rozerwij się i ogadnij wylosowaną liczbę"
            "\nzamknij - wyjście z programu.")

        say("Słucham Cię.")
        print("Słucham Cię.")
        # period of silence allowed
        r.pause_threshold = 1
        # listening to calibrate the energy threshold for ambient noise levels
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Sprawdzam co powiedziano.")
        record = r.recognize_google(audio, language='pl-PL')
        print(f"Powiedziano: {record}\n")

    except Exception as e:
        print(e)
        say("Spróbuj jeszcze raz.")

    return record


def save_to_file_title():
    p = s_r.Recognizer()
    record2 = ''
    with s_r.Microphone() as source:
        say("Podaj tytuł pliku.")
        print("Slucham...")
        p.pause_threshold = 1
        p.adjust_for_ambient_noise(source)
        audio2 = p.listen(source)

    try:
        print("Sprawdzam co powiedziano")
        record2 = p.recognize_google(audio2, language='pl-PL')
        print(f"Powiedziano: {record2}\n")

    except Exception as e:
        print(e)
        say("Polecenie było dla mnie niezrozumiałe...")

    # else:
    #     print("Nieoblisugwany blad", sys.exc_info()[0])

    return record2


def save_to_file_content():
    w = s_r.Recognizer()
    record3 = ''
    with s_r.Microphone() as source:
        say("Podaj tekst zapisu")
        print("Slucham...")
        w.pause_threshold = 3
        w.adjust_for_ambient_noise(source)
        audio3 = w.listen(source)

    try:
        print("Sprawdzam co powiedziano")
        record3 = w.recognize_google(audio3, language='pl-PL')
        print(f"Powiedziano: {record3}\n")
        f = open(record2 + '.txt', 'w+')
        f.write(record3)
        say("Plik został zapisany.")
        print("Plik został zapisany.")

    except Exception as e:
        print(e)
        say("Nie zrozumiałe jest to co do mnie mówisz, może następnym razem...")

    # else:
    #     print("Nieobsługiwany błąd", sys.exc_info()[0])

    return record3


def wikipedia_search():
    wiki = s_r.Recognizer()
    with s_r.Microphone() as source:
        say("Co mam znaleźć na wikipedii?")

        wiki.pause_threshold = 2
        wiki.adjust_for_ambient_noise(source)
        wikisearch = wiki.listen(source)
        varwiki = wiki.recognize_google(wikisearch, language='pl-PL')

        say("Przeszukuję wikipedię w poszukiwaniu hasła")

        wikifound = wikipedia.summary(varwiki, sentences=2)

        say("Jak mówi wikipedia: ")
        print("Jak mówi wikipedia: ")
        print(wikifound)
        say(wikifound)

        r = s_r.Recognizer()

        with s_r.Microphone() as source2:
            say("Czy zapisać treść do pliku?")
            print("Czy zapisać treść do pliku?")
            r.pause_threshold = 1
            # listening to calibrate the energy threshold for ambient noise levels
            r.adjust_for_ambient_noise(source2)
            audio = r.listen(source2)

            try:
                print("Słucham...")
                record_wiki = r.recognize_google(audio, language='pl-PL')
                print(f"Odpowiedziano: {record_wiki}\n")

                if "tak" in record_wiki:
                    try:

                        p = s_r.Recognizer()

                        with s_r.Microphone() as source:
                            say("Podaj tytuł pliku.")
                            print("Slucham...")
                            p.pause_threshold = 1
                            p.adjust_for_ambient_noise(source)
                            audio2 = p.listen(source)

                        try:
                            print("Przetwarzam...")
                            record_title_wiki = p.recognize_google(audio2, language='pl-PL')
                            print(f"Podano tytuł: {record_title_wiki}\n")
                            f = open(record_title_wiki + '.txt', 'w+')
                            f.write(wikifound)
                            say("Plik o nazwie " + record_title_wiki + " został zapisany.")
                            print("Plik o nazwie " + record_title_wiki + " został zapisany.")

                        except Exception as e:
                            print(e)
                            say("Nie zrozumiałam, więc plik nie został zapisany")

                    except Exception as e:
                        print(e)
                        say("Coś poszło nie tak.")

            except Exception as y:
                print(y)
                say("Spróbuj jeszcze raz.")

            # return record_wiki
            #
            # record_wiki = command_recognition().lower()


def google_search():

    google = s_r.Recognizer()
    with s_r.Microphone() as source:
        say("Co mam znaleźć w GOOGLE?")

        google.pause_threshold = 2
        google.adjust_for_ambient_noise(source)
        googlesearch = google.listen(source)
        vargoogle = google.recognize_google(googlesearch, language='pl-PL')

        say("Przeszukuję GOOGLE w poszukiwaniu hasła")
        for url in search(vargoogle, lang='pl'):
            print(url)

        webbrowser.open("https://www.google.pl/search?q=" + vargoogle)
        # response = search(vargoogle, num_results=1)
        # url = str(response[0])
        # webbrowser(url)
        # print(url)


def open_from_file():
    q = s_r.Recognizer()
    record4 = ''

    with s_r.Microphone() as source:
        say("Jaki plik mam otworzyć?")
        print("Słucham...")
        q.pause_threshold = 2
        q.adjust_for_ambient_noise(source)
        audio4 = q.listen(source)

    try:
        print("Otwieram plik...")
        record4 = q.recognize_google(audio4, language='pl-PL')
        print(f"Powiedziano: {record4}\n")

        file = open(record4 + ".txt", "r")
        print(file.read())
        webbrowser.open(record4 + ".txt")

    except Exception as e:
        print(e)
        say("Nie zrozumiałam, może następnym razem...")

    # else:
    #     print("Nieoblisugwany blad", sys.exc_info()[0])

    return record4


def lotto_draw():
    try:
        say("Wybierz liczby:")
        print("Wybierz liczby:")

        with s_r.Microphone() as source:

            try:

                say("Podaj pierwszą liczbę")
                print("Podaj pierwszą liczbę")
                audio_in0 = s_r.Recognizer()
                audio_in0.pause_threshold = 2
                audio_listuj0 = audio_in0.listen(source)
                print(audio_listuj0)
                record10 = audio_in0.recognize_google(audio_listuj0, language='pl-PL')

                if record10 == 'pięć':
                    a = 5
                elif record10 == 'osiem':
                    a = 8
                elif record10 == 'siedem':
                    a = 7
                elif record10 == 'jeden':
                    a = 1
                else:
                    a = int(record10)

                print(a)

                if a < 1 or a > 49:
                    say("Nie odnotowano liczby z zakresu od 1 do 49. Proszę wprowadź liczbę ręcznie.")
                    a = int(input("Podaj liczbę: "))

                b = a
                while a == b:

                    say("Podaj drugą liczbę")
                    print("Podaj drugą liczbę")
                    audio_in1 = s_r.Recognizer()
                    audio_in1.pause_threshold = 2
                    audio_listuj1 = audio_in1.listen(source)
                    print(audio_listuj1)
                    record20 = audio_in1.recognize_google(audio_listuj1, language='pl-PL')

                    b = ''
                    if record20 == 'pięć':
                        b = 5
                    elif record20 == 'osiem':
                        b = 8
                    elif record20 == 'siedem':
                        b = 7
                    elif record20 == 'jeden':
                        b = 1
                    else:
                        b = int(record20)

                    print(b)

                    if b <= 0 or b > 49:
                        say("Nie odnotowano liczby z zakresu od 1 do 49. Proszę wprowadź liczbę ręcznie.")
                        b = int(input("Podaj liczbę: "))

                c = a
                while a == c or b == c:

                    say("Podaj trzecią liczbę")
                    print("Podaj trzecią liczbę")
                    audio_in2 = s_r.Recognizer()
                    audio_in2.pause_threshold = 2
                    audio_listuj2 = audio_in2.listen(source)
                    print(audio_listuj2)
                    record30 = audio_in2.recognize_google(audio_listuj2, language='pl-PL')

                    c = ''
                    if record30 == 'pięć':
                        c = 5
                    elif record30 == 'osiem':
                        c = 8
                    elif record30 == 'siedem':
                        c = 7
                    elif record30 == 'jeden':
                        c = 1
                    else:
                        c = int(record30)

                    print(c)
                    if c < 1 or c > 49:
                        say("Nie odnotowano liczby z zakresu od 1 do 49. Proszę wprowadź liczbę ręcznie.")
                        c = int(input("Podaj liczbę: "))

                d = a
                while a == d or b == d or c == d:
                    say("Podaj czwartą liczbę")
                    print("Podaj czwartą liczbę")
                    audio_in3 = s_r.Recognizer()
                    audio_in3.pause_threshold = 2
                    audio_listuj3 = audio_in3.listen(source)
                    print(audio_listuj3)
                    record40 = audio_in3.recognize_google(audio_listuj3, language='pl-PL')

                    d = ''
                    if record40 == 'pięć':
                        d = 5
                    elif record40 == 'osiem':
                        d = 8
                    elif record40 == 'siedem':
                        d = 7
                    elif record40 == 'jeden':
                        d = 1
                    else:
                        d = int(record40)

                    print(d)
                    if d < 1 or d > 49:
                        say("Nie odnotowano liczby z zakresu od 1 do 49. Proszę wprowadź liczbę ręcznie.")
                        d = int(input("Podaj liczbę: "))

                f = a
                while a == f or b == f or c == f or d == f:
                    say("Podaj piątą liczbę")
                    print("Podaj piątą liczbę")
                    audio_in4 = s_r.Recognizer()
                    audio_in4.pause_threshold = 2
                    audio_listuj4 = audio_in4.listen(source)
                    print(audio_listuj4)
                    record50 = audio_in4.recognize_google(audio_listuj4, language='pl-PL')
                    f = ''
                    if record50 == 'pięć':
                        f = 5
                    elif record50 == 'osiem':
                        f = 8
                    elif record50 == 'siedem':
                        f = 7
                    elif record50 == 'jeden':
                        f = 1
                    else:
                        f = int(record50)

                    print(f)
                    if f < 1 or f > 49:
                        say("Nie odnotowano liczby z zakresu od 1 do 49. Proszę wprowadź liczbę ręcznie.")
                        f = int(input("Podaj liczbę: "))

                g = a
                while a == g or b == g or c == g or d == g or f == g:
                    say("Podaj szóstą liczbę")
                    print("Podaj szóstą liczbę")
                    audio_in4 = s_r.Recognizer()
                    audio_in4.pause_threshold = 2
                    audio_listuj4 = audio_in4.listen(source)
                    print(audio_listuj4)
                    record60 = audio_in4.recognize_google(audio_listuj4, language='pl-PL')

                    g = ''
                    if record60 == 'pięć':
                        g = 5
                    elif record60 == 'osiem':
                        g = 8
                    elif record60 == 'siedem':
                        g = 7
                    elif record60 == 'jeden':
                        g = 1
                    else:
                        g = int(record60)

                    print(g)
                    if g < 1 or g > 49:
                        say("Nie odnotowano liczby z zakresu od 1 do 49. Proszę wprowadź liczbę ręcznie.")
                        g = int(input("Podaj liczbę: "))

            except Exception as e:
                print(e)
                say("Błędnie wprowadzone liczby.")

        podane_liczby = [a, b, c, d, f, g]

        losowanie_lotto = []
        i = 0

        while i < 6:
            r = random.randint(1, 49)
            if losowanie_lotto.count(r) == 0:
                losowanie_lotto.append(r)
                i += 1
        trafiony = []
        for x in losowanie_lotto:
            y = len(podane_liczby)
            t = 0
            while t < y:
                z = podane_liczby[t]
                if x == z:
                    trafiony.append(z)
                t = t + 1

        print("Wybrane Liczby: ")
        print(podane_liczby)
        losowanie_lotto.sort()
        print("Wylosowane Liczby: ")
        print(losowanie_lotto)
        print("Trafione liczby: ")
        say("Trafione liczby: ")
        trafiony.sort()
        say(trafiony)
        print(trafiony)

    except Exception as e:
        print(e)
        say("Coś poszło nie tak")


def guess_the_number():

    number = random.randint(1, 100)
    running = True
    audio_in0 = s_r.Recognizer()
    print(number)

    while running:

        with s_r.Microphone() as source:

            try:

                say("Odgadnij liczbę od 1 do 100 lub powiedz stop aby zakończyć.")
                audio_in0.pause_threshold = 2

                audio_listuj0 = audio_in0.listen(source, timeout=2)
                print(audio_listuj0)

                record10 = audio_in0.recognize_google(audio_listuj0, language='pl-PL')

                a = ''
                if record10 == 'pięć':
                    a = 5
                elif record10 == 'osiem':
                    a = 8
                elif record10 == 'siedem':
                    a = 7
                elif record10 == 'jeden':
                    a = 1
                elif record10 == 'stop':
                    say("Następnym razem się uda")
                    break
                else:
                    a = int(record10)

                print(a)
                # //say("Wybrałeś liczbę " + str(a))

                if a < 1 or a > 100:
                    say("Wybrałeś liczbę z poza zakresu. Proszę jeszcze raz.")
                    print("Wybrałeś liczbę z poza zakresu. Proszę jeszcze raz.")

                elif number == a:
                    print("Brawo")
                    say("Zgadłeś. brawo")
                    running = False

                elif a < number:
                    print('Szukana liczba jest wyższa niż ta którą podałeś. Spróbuj jeszcze raz')
                    say('Szukana liczba jest wyższa niż ta którą podałeś. Spróbuj jeszcze raz')
                    print(number)

                elif a > number:

                    print('Szukana liczba jest niższa niż ta którą podałeś. Spróbuj jeszcze raz')
                    say('Szukana liczba jest niższa niż ta którą podałeś. Spróbuj jeszcze raz')
                    print(number)

                else:
                    print('Hmm')
                    say('Hmm')

            except Exception as e:
                print(e)
                say("Poproszę powiedz jeszcze raz")

    else:
        print('Gra skończona.')

#FUNKCJA WYCOFANA Z UWAGI NA PROBLEMY Z ROZPOZNAWANIEM LICZB
# def calculator():
#     while True:
#
#         try:
#
#             say("Podaj dwie liczby do działania")
#
#             with s_r.Microphone() as source:
#
#                 try:
#
#                     say("Podaj pierwszą liczbę")
#                     print("Podaj pierwszą liczbę")
#                     audio_0 = s_r.Recognizer()
#                     audio_0.pause_threshold = 2
#                     audio_listuj0 = audio_0.listen(source)
#                     print(audio_listuj0)
#                     record10 = audio_0.recognize_google(audio_listuj0, language='pl-PL')
#
#                     check = isinstance(record10, float)
#                     if not check:
#                         say("Nie odnotowano liczby z zakresu od 1 do 49. Proszę wprowadź liczbę ręcznie.")
#                         x = float(input("Pierwsza: "))
#                     else:
#                         x = float(record10)
#
#                     say("Podaj drugą liczbę")
#                     print("Podaj drugą liczbę")
#                     audio_1 = s_r.Recognizer()
#                     audio_1.pause_threshold = 2
#                     audio_listuj0 = audio_1.listen(source)
#                     print(audio_listuj0)
#                     record11 = audio_1.recognize_google(audio_listuj0, language='pl-PL')
#
#                     check2 = isinstance(record11, float)
#                     if check2 != True:
#                         say("Nie odnotowano liczby z zakresu od 1 do 49. Proszę wprowadź liczbę ręcznie.")
#                         y = float(input("Druga: "))
#                     else:
#                         y = float(record11)
#
#                     dzialanie = int(input(
#                         "Jakie działanie wykonać? "
#                         "\n1. Dodawanie 2. Odejmowanie 3. Mnożenie 4. Dzielenie "
#                         "\nAby wyjść kliknij 00\n "))
#
#                     if (dzialanie == 1):
#                         z = round((x + y), 2)
#                         print(z)
#                         say("Wynik dodowania wynosi")
#                         say(z)
#                     elif (dzialanie == 2):
#                         z = round((x - y), 2)
#                         print(z)
#                         say("Wynik odejmowania wynosi:")
#                         say(z)
#                     elif (dzialanie == 3):
#                         z = round((x * y), 2)
#                         print(z)
#                         say("Wynik mnożenia wynosi:")
#                         say(z)
#                     elif (dzialanie == 4):
#
#                         if y == 0:
#
#                             say("Pamiętaj cholero nie dziel przez zero")
#
#                         else:
#                             z = round((x / y), 2)
#                             print(z)
#                             say("Wynik dzielenia wynosi:")
#                             say(z)
#                     elif (dzialanie == 0):
#
#                         say("Wychodzę z kalkulatora. ")
#                         break
#
#                     else:
#
#                         say("Błąd.")
#                         print("Błąd.")
#
#                 except Exception as e:
#                     print("Nieobsługiwany błąd", sys.exc_info()[0])
#
#         except Exception as e:
#             print(e)
#             say("Spróbuj jeszcze raz")


def screenshot():
    try:
        s = s_r.Recognizer()
        with s_r.Microphone() as source:
            say("Podaj nazwę pod jaką mam zapisać plik")

            s.adjust_for_ambient_noise(source)
            s_audio = s.listen(source)
            s_screen = s.recognize_google(s_audio, language='pl-PL').lower()

            print(s_screen)
            try:
                image = pyautogui.screenshot()
                image.save(s_screen + '.png')
                print("Zapisano")

            except Exception as e:
                print(e)
                say("Błąd.")

    except Exception as e:
        print(e)
        say("Nie zrozumiałam, spróbuj jeszcze raz")

def klawiatura():
    say("Proszę podaj co mam wybrać z klawiatury. Jeśli chcesz zakończyć działanie funkcji powiedz STOP")

    klawisze = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'f1', 'f10', 'f11', 'f12',
                'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'stop'}

    spacebar = 'spacja'
    capslock = 'caps lock'
    backspace = 'back space'
    select = 'zaznacz wszystko'
    copy = 'kopiuj'
    past = 'wklej'
    back = 'cofnij'
    delete = 'usuń'
    unselect = 'odznacz'
    right = 'prawo'
    left = 'lewo'
    volumedown = 'ścisz'
    volumeup = 'podgłośnij'
    volumemute = 'wycisz'
    dot = 'kropka'
    comma = 'przecinek'
    em = 'wykrzynik'
    one = 'jeden'
    five = 'pięć'
    seven = 'siedem'
    eight = 'osiem'

    rec_klawisz = ''
    while rec_klawisz != 'stop':

        try:
            rec = s_r.Recognizer()
            with s_r.Microphone() as source:

                say("Wybierz klawisz?")

                rec.adjust_for_ambient_noise(source)
                rec_audio = rec.listen(source)
                rec_klawisz = rec.recognize_google(rec_audio, language='pl-PL').lower()

                print(rec_klawisz)

                try:
                    for x in klawisze:
                        if x == rec_klawisz:
                            pyautogui.press(x)

                    if rec_klawisz == spacebar:
                        pyautogui.press("space")
                    if rec_klawisz == capslock:
                        pyautogui.press("capslock")
                    if rec_klawisz == backspace:
                        pyautogui.press("backspace")
                    if rec_klawisz == select:
                        pyautogui.hotkey('ctrl', 'a')
                    if rec_klawisz == copy:
                        pyautogui.hotkey('ctrl', 'c')
                    if rec_klawisz == past:
                        pyautogui.hotkey('ctrl', 'v')
                    if rec_klawisz == back:
                        pyautogui.hotkey('ctrl', 'z')
                    if rec_klawisz == delete:
                        pyautogui.hotkey('del')
                    if rec_klawisz == unselect:
                        pyautogui.hotkey('ctrl', 'right')
                    if rec_klawisz == right:
                        pyautogui.hotkey('right')
                    if rec_klawisz == left:
                        pyautogui.hotkey('left')
                    if rec_klawisz == volumedown:
                        pyautogui.hotkey('volumedown')
                    if rec_klawisz == volumeup:
                        pyautogui.hotkey('volumeup')
                    if rec_klawisz == volumemute:
                        pyautogui.hotkey('volumemute')
                    if rec_klawisz == dot:
                        pyautogui.press('.')
                    if rec_klawisz == comma:
                        pyautogui.press(',')
                    if rec_klawisz == em:
                        pyautogui.press('!')
                    if rec_klawisz == one:
                        pyautogui.press('1')
                    if rec_klawisz == five:
                        pyautogui.press('5')
                    if rec_klawisz == seven:
                        pyautogui.press('7')
                    if rec_klawisz == eight:
                        pyautogui.press('8')

                except Exception as e:
                    print(e)
                    say("Nie zrozumiałam, spróbuj jeszcze raz")

        except Exception as e:
            print(e)
            say("Spróbuj jeszcze raz")


if __name__ == "__main__":  # funkcja glowna

    introduction()

    while True:

        record = command_recognition().lower()

        if 'wikipedia' in record:

            try:

                wikipedia_search()

            except Exception as e:

                print(e)
                say("Spróbuj jeszcze raz...")

        if 'google' in record:

            try:

                google_search()

            except Exception as e:

                print(e)
                say("Spróbuj jeszcze raz...")

        if 'klawiatura' in record:
            try:
                klawiatura()

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        if 'screenshot' in record:

            try:
                screenshot()

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        if 'otwórz youtube' in record:

            try:
                say("Już otwieram.")
                webbrowser.open("https://www.youtube.com")

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        if 'portal studenta' in record:

            try:
                say("Już otwieram.")
                webbrowser.open("https://ps.ug.edu.pl/")

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        if 'portal edukacyjny' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https://pe.ug.edu.pl/")

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        if 'strona wydziału' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https://wzr.ug.edu.pl/")

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        if 'strona uniwersytetu' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https://ug.edu.pl/")

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        if 'zapisz plik' in record:

            try:

                record2 = save_to_file_title().lower()
                record3 = save_to_file_content()

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        #FUNKCJA WYCOFANA Z POWODU NIEROZPOZNAWANIA NIEKTÓRYCH LICZB PRZEZ SR W WERSJI POLSKIEJ
        # if 'kalkulator' in record:
        #
        #     try:
        #
        #         calculator()
        #
        #     except Exception as e:
        #         print(e)
        #         say("Coś poszło nie tak.")

        if "otwórz plik" in record:

            try:

                record4 = open_from_file().lower()

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        if "gra" in record:

            try:

                guess_the_number()

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        if "lotto" in record:

            try:

                say("Witaj w symulatorze lotto:")
                lotto_draw()

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        if "wyszukiwarka" in record:

            try:
                say("Już otwieram.")
                webbrowser.open("https:\\www.google.com")

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        if 'pomocy' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("stackoverflow.com")

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

        # if "muzyka" in record:
        #
        #     try:
        #
        #         webbrowser.open("https://www.youtube.com/watch?v=vpXlYbstRDs&list=PLIut9bR_W7KX9OK1BwJvLoidfirixgPPN")
        #
        #     except Exception as e:
        #         print(e)
        #         say("Coś poszło nie tak.")

        if 'zamknij' in record:

            try:
                say("Zamykam program. Do usłyszenia")
                sys.exit()

            except Exception as e:
                print(e)
                say("Coś poszło nie tak.")

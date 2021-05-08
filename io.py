import pyowm
import speech_recognition  # automatic speech recognition (ASR),
# computer speech recognition, or speech-to-text, is a capability which
# enables a program to process human speech into a written format.
import speech_recognition as s_r  #
import wikipedia  # Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
import random  # his module implements pseudo-random number generators for various distributions.
import webbrowser  # The webbrowser module provides a high-level interface
# to allow displaying Web-based documents to users.
import os  # The OS module in Python provides functions for interacting with the operating system.
import pyttsx3  # pyttsx3 is a text-to-speech conversion library in Python.
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
import test
from googlesearch import search  # https://github.com/Nv7-GitHub/googlesearch on MIT License
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

# Voice mechanism
voice_mechanism = pyttsx3.init('sapi5')


def say(audio):
    voice_mechanism.say(audio)
    # a mechanism for hearing the voice
    voice_mechanism.runAndWait()
    voice_mechanism.stop()


def introduction():
    say("Witaj w asystencie głosowym")
    print("Witaj w asystencie głosowym")


def command_recognition():
    # Create voice recognition
    r = s_r.Recognizer()
    record = ''

    with s_r.Microphone() as source:

        say("Abym mogła Tobie pomóc podaj nazwę funkcji.")
        test.menu()

        print("Słucham Cię.")
        say("Słucham Cię.")
        # period of silence allowed
        # r.pause_threshold = 1
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


def wikipedia_search():
    # wikipedia language declaration
    wikipedia.set_lang("pl")

    wiki = s_r.Recognizer()
    sentences = s_r.Recognizer()
    with s_r.Microphone() as source:

        say("Co mam znaleźć na wikipedii?")

        # wiki.pause_threshold = 1
        wiki.adjust_for_ambient_noise(source)
        wikisearch = wiki.listen(source)
        varwiki = wiki.recognize_google(wikisearch, language='pl-PL')
        print(f"Powiedziano: {varwiki}\n")

        with s_r.Microphone() as source2:

            # intnum = ''
            # check = isinstance(intnum, int)
            # while check == False:

            say("Ile zdań mam przeczytać? Podaj liczbę.")

            sentences.pause_threshold = 1
            sentences.adjust_for_ambient_noise(source2)
            sentencesnumber = wiki.listen(source2)
            number = wiki.recognize_google(sentencesnumber, language='pl-PL')
            print(f"Powiedziano: {number}\n")

            if number == 'pięć':
                intnum = 5
            elif number == 'osiem':
                intnum = 8
            elif number == 'siedem':
                intnum = 7
            elif number == 'jeden' or number == 'jedno':
                intnum = 1
            else:
                intnum = int(number)

            say("Przeszukuję wikipedię w poszukiwaniu hasła")

            wikifound = wikipedia.summary(varwiki, sentences=intnum)

            print("Jak mówi wikipedia: ")
            say("Jak mówi wikipedia: ")
            print(wikifound)
            say(wikifound)

            r = s_r.Recognizer()

            with s_r.Microphone() as source3:

                print("Czy zapisać treść do pliku? TAK/ NIE")
                say("Powiedz TAK, jeśli mam zapisać treść do pliku.")
                # r.pause_threshold = 1
                # listening to calibrate the energy threshold for ambient noise levels
                r.adjust_for_ambient_noise(source3)
                audio = r.listen(source3)

                try:

                    print("Słucham...")
                    record_wiki = r.recognize_google(audio, language='pl-PL')
                    print(f"Odpowiedziano: {record_wiki}\n")

                    if "tak" in record_wiki:

                        try:

                            p = s_r.Recognizer()

                            with s_r.Microphone() as source4:

                                say("Podaj tytuł pliku.")
                                print("Slucham...")
                                p.pause_threshold = 1
                                p.adjust_for_ambient_noise(source4)
                                title = p.listen(source4)

                            try:

                                print("Przetwarzam...")
                                record_title_wiki = p.recognize_google(title, language='pl-PL')
                                print(f"Podano tytuł: {record_title_wiki}\n")
                                f = open(record_title_wiki + '.txt', 'w+')
                                f.write(wikifound)

                                print("Plik o nazwie " + record_title_wiki + " został zapisany.")
                                say("Plik o nazwie " + record_title_wiki + " został zapisany.")

                            except Exception as e:

                                print(e)
                                say("Nie zrozumiałam, więc plik nie został zapisany")

                        except Exception as e:

                            print(e)
                            say("Coś poszło nie tak.")

                except Exception as y:

                    print(y)
                    say("Coś poszło nie tak. Spróbuj jeszcze raz.")

        # return record_wiki
        #
        # record_wiki = command_recognition().lower()


def save_to_file_title():
    p = s_r.Recognizer()
    record2 = ''

    with s_r.Microphone() as source:

        print("Slucham...")
        say("Podaj tytuł pliku.")
        p.pause_threshold = 1
        p.adjust_for_ambient_noise(source)
        audio2 = p.listen(source)

    try:

        print("Sprawdzam co powiedziano")
        record2 = p.recognize_google(audio2, language='pl-PL')
        print(f"Powiedziano: {record2}\n")

    except Exception as e:

        print(e)
        say("Nie zrozumiałam co mówisz. Plik zostanie zapisany bez tytułu.")

    # else:
    #     print("Nieoblisugwany blad", sys.exc_info()[0])

    return record2


def save_to_file_content():
    w = s_r.Recognizer()
    record3 = ''

    with s_r.Microphone() as source:

        print("Slucham...")
        say("Podaj tekst zapisu")
        w.pause_threshold = 3
        w.adjust_for_ambient_noise(source)
        audio3 = w.listen(source)

    try:

        print("Sprawdzam co powiedziano")
        record3 = w.recognize_google(audio3, language='pl-PL')
        print(f"Powiedziano: {record3}\n")
        f = open(record2 + '.txt', 'w+')
        f.write(record3)
        voice_mechanism.save_to_file(record3, record2 + '.mp3')

        print("Plik został zapisany.")
        say("Plik został zapisany.")

    except Exception as e:
        print(e)
        say("Nie zrozumiałe jest to co do mnie mówisz, może następnym razem. Plik nie został zapisany")

    # else:
    #     print("Nieobsługiwany błąd", sys.exc_info()[0])

    return record3


def open_from_file():
    q = s_r.Recognizer()
    record4 = ''

    with s_r.Microphone() as source:

        print("Słucham...")
        say("Jaki plik mam otworzyć?")
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
        say("Nie udało się otworzyć pliku. Notatka o podanym tytule nie istnieje.")

    # else:
    #     print("Nieoblisugwany blad", sys.exc_info()[0])

    return record4


def klawiatura():
    say("Proszę podaj co mam wybrać z klawiatury. Jeśli chcesz zakończyć działanie funkcji powiedz STOP")

    klawisze = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'f1', 'f10', 'f11', 'f12',
                'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'shift', 'stop'}

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
    altf4 = 'zamknij okno'
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
    windows = 'windows'

    rec_klawisz = ''
    while rec_klawisz != 'stop':

        try:
            rec = s_r.Recognizer()
            with s_r.Microphone() as source:

                say("Wybierz klawisz")

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
                    if rec_klawisz == altf4:
                        pyautogui.hotkey('alt', 'f4')
                    if rec_klawisz == windows:
                        pyautogui.hotkey('win')
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


def google_search():
    google = s_r.Recognizer()
    with s_r.Microphone() as source:
        say("Co mam znaleźć w GOOGLE?")

        google.pause_threshold = 2
        google.adjust_for_ambient_noise(source)
        googlesearch = google.listen(source)
        vargoogle = google.recognize_google(googlesearch, language='pl-PL')

        say("Przeszukuję GOOGLE w poszukiwaniu hasła")

        for url in search(vargoogle, lang='pl', num_results=5):
            print(url)

        webbrowser.open("https://www.google.pl/search?q=" + vargoogle)

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


# FUNKCJA WYCOFANA Z UWAGI NA PROBLEMY Z ROZPOZNAWANIEM LICZB
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


def lotto_draw():
    try:

        print("Wybierz liczby:")
        say("Wybierz liczby:")

        with s_r.Microphone() as source:

            try:

                print("Podaj pierwszą liczbę")
                say("Podaj pierwszą liczbę")
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
                    while a < 1 or a > 49:
                        a = int(input("Podaj liczbę: "))

                b = a
                while a == b:

                    print("Podaj drugą liczbę")
                    say("Podaj drugą liczbę")
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
                        while b < 1 or b > 49:
                            b = int(input("Podaj liczbę: "))

                c = a
                while a == c or b == c:

                    print("Podaj trzecią liczbę")
                    say("Podaj trzecią liczbę")
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
                        while c < 1 or c > 49:
                            c = int(input("Podaj liczbę: "))

                d = a
                while a == d or b == d or c == d:

                    print("Podaj czwartą liczbę")
                    say("Podaj czwartą liczbę")
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
                        while d < 1 or d > 49:
                            d = int(input("Podaj liczbę: "))

                f = a
                while a == f or b == f or c == f or d == f:

                    print("Podaj piątą liczbę")
                    say("Podaj piątą liczbę")
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
                        while f < 1 or f > 49:
                            f = int(input("Podaj liczbę: "))

                g = a
                while a == g or b == g or c == g or d == g or f == g:

                    print("Podaj szóstą liczbę")
                    say("Podaj szóstą liczbę")
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
                        while g < 1 or g > 49:
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
        podane_liczby.sort()
        print(podane_liczby)
        losowanie_lotto.sort()
        print("Wylosowane Liczby: ")
        print(losowanie_lotto)
        print("Trafione liczby: ")
        say("Trafione liczby: ")
        trafiony.sort()
        print(trafiony)
        say(trafiony)

    except Exception as e:

        print(e)
        say("Coś poszło nie tak")


def guess_the_number():
    number = random.randint(1, 100)
    running = True
    audio_in0 = s_r.Recognizer()
    # print(number)

    while running:

        with s_r.Microphone() as source:

            try:

                say("Odgadnij liczbę od 1 do 100 lub powiedz stop aby zakończyć.")
                audio_in0.pause_threshold = 1

                audio_listuj0 = audio_in0.listen(source)
                print(audio_listuj0)

                record10 = audio_in0.recognize_google(audio_listuj0, language='pl-PL')

                a = ''
                stop = 'stop'
                if record10 == 'pięć':
                    a = 5
                elif record10 == 'osiem':
                    a = 8
                elif record10 == 'siedem':
                    a = 7
                elif record10 == 'jeden':
                    a = 1
                elif record10 == stop:
                    say("Następnym razem się uda.")
                    break
                else:
                    a = int(record10)

                # print(a)
                # //say("Wybrałeś liczbę " + str(a))

                if a < 1 or a > 100:

                    print("Wybrałeś liczbę z poza zakresu. Proszę jeszcze raz.")
                    say("Wybrałeś liczbę z poza zakresu. Proszę jeszcze raz.")

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


def weather(record):

    try:
        check_city = record.replace("Pogoda", "")

        if check_city == "":
            say("Nie podano miasta. Spróbuj jeszcze raz.")

        else:
            city = check_city
            #city = check_city.recognize_google(check_city, language='pl-PL')
            print(city)

            config_dict = get_default_config()
            config_dict['language'] = 'pl'

            owm = pyowm.OWM('74940aca9b5a0b8e0ca18806718b52b3', config_dict)
            mng = owm.weather_manager()
            obs = mng.weather_at_place(city + ', PL')
            w = obs.weather
            temp = w.temperature('celsius')

            print(w)
            act_temp = int(temp['temp'])
            print(act_temp)
            say("Aktualna temperatura w mieście " + city + " wynosi")
            say(act_temp)
            say("stopnie celcjusza")
            say("Minimalna temparatura:")
            say(temp['temp_min'])
            say("Maksymalna temperatura:")
            say(temp["temp_max"])
            actstat = w.detailed_status
            print(actstat)
            say("Aktualnie jest na dworze:")
            say(actstat)

            if 'deszcz' in actstat or 'burza' in actstat or 'mżawka' in actstat or 'śnieg' in actstat:

                say('Lepiej dobrze się ubierz.')

    except Exception as e:

        print(e)
        say("Prawdopodnie podano nieprawidłowe parametry. Spróbuj jeszcze raz.")


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

        elif 'notatka' in record:

            try:

                record2 = save_to_file_title().lower()
                record3 = save_to_file_content()

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif 'klawiatura' in record:

            try:

                klawiatura()

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif "otwórz plik" in record or 'otwórz notatkę' in record:

            try:

                record4 = open_from_file().lower()

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif 'google' in record or 'gugle' in record or 'gogle' in record:

            try:

                google_search()

            except Exception as e:

                print(e)
                say("Spróbuj jeszcze raz...")

        elif 'screenshot' in record:

            try:

                screenshot()

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif 'strona uniwersytetu' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https://ug.edu.pl/")

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif 'strona wydziału' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https://wzr.ug.edu.pl/")

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif 'portal edukacyjny' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https://pe.ug.edu.pl/")

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif 'portal studenta' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https://ps.ug.edu.pl/")

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif "wyszukiwarka" in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https:\\www.google.com")

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif 'pomoc' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("stackoverflow.com")

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif 'otwórz youtube' in record or 'youtube' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https://www.youtube.com")

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif "lotto" in record:

            try:

                say("Witaj w symulatorze lotto:")
                lotto_draw()

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif "pogoda" in record:

            try:

                record = record.title()
                weather(record)

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif "gra" in record:

            try:

                guess_the_number()

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif 'zamknij' in record:

            try:

                say("Zamykam program. Do usłyszenia")
                sys.exit()

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

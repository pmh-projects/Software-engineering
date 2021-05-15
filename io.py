import pyowm
# computer speech recognition, or speech-to-text, is a capability which
# enables a program to process human speech into a written format.
import speech_recognition as s_r  #
import wikipedia  # Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
import random  # his module implements pseudo-random number generators for various distributions.
import webbrowser  # The webbrowser module provides a high-level interface
# to allow displaying Web-based documents to users.
import pyttsx3  # pyttsx3 is a text-to-speech conversion library in Python.
# Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
# the cross-platform audio I/O library. With PyAudio, you can easily
# use Python to play and record audio on a variety of platforms.
import sys  # This module provides access to some variables used or
# maintained by the interpreter and to
# functions that interact strongly with the interpreter.
# functions corresponding to the intrinsic operators of Python.
# For example, operator. add(x, y) is equivalent to the expression x+y
# import pickle #The pickle module can transform a complex object
# into a byte stream and it can transform
# the byte stream into an object with the same internal structure.
# For related functionality, see also the datetime and calendar modules..
# The sleep() function suspends (waits) execution
# of the current thread for a given number of seconds.
import pyautogui  # https://github.com/asweigart/pyautogui BSD-3-Clause License
import menu
from googlesearch import search  # https://github.com/Nv7-GitHub/googlesearch on MIT License
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from PIL import ImageTk, Image
import tkinter.font as tkFont
import time

# Voice mechanism
voice_mechanism = pyttsx3.init()

root = tk.Tk()
root.title('ASGLOS Asystent głosowy studenta')
root.iconbitmap('textspeech.ico')
img = tk.PhotoImage(file="logo.png")
label = tk.Label(root, image=img)
label.pack()


def say(audio):
    voice_mechanism.say(audio)
    voice_mechanism.runAndWait()
    voice_mechanism.stop()


def view_tk():

    var = StringVar()
    font = tkFont.Font(family="Helvetica", size=12)
    label = tk.Message(root, textvariable=var, relief=RAISED, border=20, bg='lightblue', justify=CENTER, font=font,
                       pady=30)
    var.set("Witaj w asystencie głosowym\n\n"
            "Aby wywołać funkcję wystarczy wymówić wyraźnie jej nazwę.\n\n"
            "\nFunkcje podstawowe:\n"
            '\n"Wikipedia" - uruchamia funkcję wyszukiwania haseł na wikipedii z możliwością zapisu do pliku'
            '\n"Notatka" - funkcja zapisująca plik o podanym głosowo tytule i zawartością'
            '\n"Otwórz plik" lub "otwórz notatkę" - otwieranie zapisanego pliku'
            '\n"Wyszukiwarka" - wyświetla 5 pierwszych wyników i uruchamia wyszukiwarkę z podanych hasłem'
            '\n"Screenshot" - pobiera i zapisuje zawartość ekranu do pliku png z podanym przez użytkownika tytułem'
            "\n"
            "\nFunkcje NET:\n"
            '\n"Strona Uniwersytetu" - uruchamia stronę główną UG.'
            '\n"Strona wydziału" - uruchamia stronę wydziału WZR'
            '\n"Portal edukacyjny" - uruchamia stronę portalu edukacyjnego'
            '\n"Portal studenta" - otwiera stronę portalu studenta'
            '\n"Rozkład zajęć" - wyświetla podstronę z planem zajęć WZR'
            '\n"Aktualności" - uruchamia witrynę z aktualnościami studenckimi'
            '\n"Wsparcie" - masz problem z kodem? Otworzę Stack Overflow.'
            '\n"Otwórz youtube" - chcesz posłuchać muzyki lub obejrzeć video?'
            '\n'
            '\nFunkcje dodatkowe:\n'
            '\n"Pogoda + {miasto}"- zapytaj o aktualną pogodę wypowiadając funkcję wraz z nazwą krajowej miejscowości, która chcesz sprawdzić'
            '\n"Klawiatura" - funkcja umożliwiająca wybór pojedynczego klawisza lub skrótu klawiszowego'
            '\n"Lotto" - symulator lotto. Zastanawiałeś się jakie masz szczęście w grach losowych? Sprawdź się.'
            '\n"Gierka" - rozerwij się i ogadnij wylosowaną liczbę'
            '\n"Zamknij" - wyjście z programu.')

    label.pack(anchor=CENTER)
    root.update()


def introduction():
    say("Witaj w asystencie głosowym")
    print("Witaj w asystencie głosowym")


def command_recognition():
    time.sleep(2)
    # Create voice recognition
    r = s_r.Recognizer()
    record = ''

    with s_r.Microphone() as source:

        say("Podaj nazwę funkcji.")
        # menu.menu()
        r.pause_threshold = 3
        print("Słucham Cię.")
        say("Słucham Cię.")

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
        print(f"Powiedziano: {varwiki}")

        with s_r.Microphone() as source2:

            say("Ile zdań mam przeczytać? Podaj liczbę.")

            sentences.pause_threshold = 1
            sentences.adjust_for_ambient_noise(source2)
            sentencesnumber = wiki.listen(source2)
            number = wiki.recognize_google(sentencesnumber, language='pl-PL')
            print(f"Powiedziano: {number}")

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
                # listening to calibrate the energy threshold for ambient noise levels
                r.adjust_for_ambient_noise(source3)
                audio = r.listen(source3)

                try:

                    print("Słucham...")
                    record_wiki = r.recognize_google(audio, language='pl-PL')
                    print(f"Odpowiedziano: {record_wiki}")

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
                                print(f"Podano tytuł: {record_title_wiki}")
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
        print(f"Powiedziano: {record2}")

    except Exception as e:

        print(e)
        say("Nie zrozumiałam co mówisz. Plik zostanie zapisany bez tytułu.")

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
        print(f"Powiedziano: {record3}")
        f = open(record2 + '.txt', 'w+')
        f.write(record3)
        voice_mechanism.save_to_file(record3, record2 + '.mp3')

        print("Plik został zapisany.")
        say("Plik został zapisany.")

    except Exception as e:
        print(e)
        say("Nie zrozumiałe jest to co do mnie mówisz, może następnym razem. Plik nie został zapisany")

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
        print(f"Powiedziano: {record4}")

        file = open(record4 + ".txt", "r")
        print(file.read())
        webbrowser.open(record4 + ".txt")

    except Exception as e:

        print(e)
        say("Nie udało się otworzyć pliku. Notatka o podanym tytule nie istnieje.")

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
        say("Co mam znaleźć w wyszukiwarce?")

        google.pause_threshold = 2
        google.adjust_for_ambient_noise(source)
        googlesearch = google.listen(source)
        vargoogle = google.recognize_google(googlesearch, language='pl-PL')

        print("Przeszukuję sieć...")
        say("Przeszukuję sieć...")

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
                say("Zapisano")

            except Exception as e:

                print(e)
                say("Błąd.")

    except Exception as e:

        print(e)
        say("Nie zrozumiałam, spróbuj jeszcze raz")


def lotto_draw():
    try:

        print("Wybierz liczby:")
        say("Wybierz liczby:")

        with s_r.Microphone() as source:

            try:
                a = b = c = d = f = g = 0
                check_var0 = isinstance('a', int)
                check_var1 = isinstance('a', int)
                check_var2 = isinstance('a', int)
                check_var3 = isinstance('a', int)
                check_var4 = isinstance('a', int)
                check_var5 = isinstance('a', int)
                while check_var0 == False or a < 1 or a > 49:

                    print("Podaj pierwszą liczbę")
                    say("Podaj pierwszą liczbę")
                    audio_in0 = s_r.Recognizer()
                    audio_in0.pause_threshold = 2
                    audio_listuj0 = audio_in0.listen(source)
                    print(audio_listuj0)
                    record10 = audio_in0.recognize_google(audio_listuj0, language='pl-PL')
                    if record10 == 'pięć':
                        a = check_var0 = 5
                    elif record10 == 'osiem':
                        a = check_var0 = 8
                    elif record10 == 'siedem':
                        a = check_var0 = 7
                    elif record10 == 'jeden':
                        a = check_var0 = 1
                    else:
                        try:
                            a = check_var0 = int(record10)

                        except Exception as e:

                            say("Nie podałeś prawidłowej wartości.")

                    print(a)

                while check_var1 == False or b < 1 or b > 49 or b == a:

                    print("Podaj drugą liczbę")
                    say("Podaj drugą liczbę")
                    audio_in1 = s_r.Recognizer()
                    audio_in1.pause_threshold = 2
                    audio_listuj1 = audio_in1.listen(source)
                    print(audio_listuj1)
                    record20 = audio_in1.recognize_google(audio_listuj1, language='pl-PL')

                    if record20 == 'pięć':
                        b = check_var1 = 5
                    elif record20 == 'osiem':
                        b = check_var1 = 8
                    elif record20 == 'siedem':
                        b = check_var1 = 7
                    elif record20 == 'jeden':
                        b = check_var1 = 1
                    else:
                        try:
                            b = check_var1 = int(record20)

                        except Exception as e:

                            say("Nie podałeś prawidłowej wartości.")

                    print(b)

                while check_var2 == False or c < 1 or c > 49 or c == a or c == b:

                    print("Podaj trzecią liczbę")
                    say("Podaj trzecią liczbę")
                    audio_in2 = s_r.Recognizer()
                    audio_in2.pause_threshold = 2
                    audio_listuj2 = audio_in2.listen(source)
                    print(audio_listuj2)
                    record30 = audio_in2.recognize_google(audio_listuj2, language='pl-PL')

                    if record30 == 'pięć':
                        c = check_var2 = 5
                    elif record30 == 'osiem':
                        c = check_var2 = 8
                    elif record30 == 'siedem':
                        c = check_var2 = 7
                    elif record30 == 'jeden':
                        c = check_var2 = 1
                    else:
                        try:
                            c = check_var2 = int(record30)

                        except Exception as e:

                            say("Nie podałeś prawidłowej wartości.")

                    print(c)

                while check_var3 == False or d < 1 or d > 49 or d == a or d == b or d == c:

                    print("Podaj czwartą liczbę")
                    say("Podaj czwartą liczbę")
                    audio_in3 = s_r.Recognizer()
                    audio_in3.pause_threshold = 2
                    audio_listuj3 = audio_in3.listen(source)
                    print(audio_listuj3)
                    record40 = audio_in3.recognize_google(audio_listuj3, language='pl-PL')

                    if record40 == 'pięć':
                        d = check_var3 = 5
                    elif record40 == 'osiem':
                        d = check_var3 = 8
                    elif record40 == 'siedem':
                        d = check_var3 = 7
                    elif record40 == 'jeden':
                        d = check_var3 = 1
                    else:
                        try:
                            d = check_var3 = int(record40)

                        except Exception as e:

                            say("Nie podałeś prawidłowej wartości.")

                    print(d)

                while check_var4 == False or f < 1 or f > 49 or f == a or f == b or f == c or f == d:

                    print("Podaj piątą liczbę")
                    say("Podaj piątą liczbę")
                    audio_in4 = s_r.Recognizer()
                    audio_in4.pause_threshold = 2
                    audio_listuj4 = audio_in4.listen(source)
                    print(audio_listuj4)
                    record50 = audio_in4.recognize_google(audio_listuj4, language='pl-PL')

                    if record50 == 'pięć':
                        f = check_var4 = 5
                    elif record50 == 'osiem':
                        f = check_var4 = 8
                    elif record50 == 'siedem':
                        f = check_var4 =7
                    elif record50 == 'jeden':
                        f = check_var4 = 1
                    else:
                        try:
                            f = check_var4 = int(record50)

                        except Exception as e:

                            say("Nie podałeś prawidłowej wartości.")

                    print(f)

                while check_var5 == False or g < 1 or g > 49 or a == g or b == g or c == g or d == g or f == g:

                    print("Podaj szóstą liczbę")
                    say("Podaj szóstą liczbę")
                    audio_in4 = s_r.Recognizer()
                    audio_in4.pause_threshold = 2
                    audio_listuj4 = audio_in4.listen(source)
                    print(audio_listuj4)
                    record60 = audio_in4.recognize_google(audio_listuj4, language='pl-PL')

                    if record60 == 'pięć':
                        g = check_var5 = 5
                    elif record60 == 'osiem':
                        g = check_var5 = 8
                    elif record60 == 'siedem':
                        g = check_var5 = 7
                    elif record60 == 'jeden':
                        g = check_var5 = 1
                    else:
                        try:
                            g = check_var5 = int(record60)

                        except Exception as e:

                            say("Nie podałeś prawidłowej wartości.")

                    print(g)

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

    while running:

        with s_r.Microphone() as source:

            try:

                say("Odgadnij liczbę od 1 do 100 lub powiedz stop aby zakończyć.")
                audio_in0.pause_threshold = 1

                audio_listuj0 = audio_in0.listen(source)
                print(audio_listuj0)

                record10 = audio_in0.recognize_google(audio_listuj0, language='pl-PL')

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
            print(check_city)

            # https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html
            # from pyowm.owm import OWM
            # from pyowm.utils.config import get_default_config
            # config_dict = get_default_config()
            # config_dict['language'] = 'pt'  # your language here, eg. Portuguese
            # owm = OWM('your-api-key', config_dict)

            config_dict = get_default_config()
            config_dict['language'] = 'pl'
            owm = pyowm.OWM('74940aca9b5a0b8e0ca18806718b52b3', config_dict)
            mng = owm.weather_manager()
            obs = mng.weather_at_place(check_city + ', PL')
            w = obs.weather
            temp = w.temperature('celsius')

            print(w)
            act_temp = int(temp['temp'])
            print(act_temp)
            say("Aktualna temperatura w stopniach celcjusza w mieście " + check_city + " wynosi:")
            say(act_temp)
            say("Odczuwalna:")
            say(temp['feels_like'])
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


if __name__ == "__main__":

    introduction()
    view_tk()

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

        elif 'wyszukiwarka' in record:

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

        elif 'aktualności' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https://www.dlastudenta.pl/")

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        elif 'rozkład zajęć' in record:

            try:

                say("Już otwieram.")
                webbrowser.open("https://wzr.ug.edu.pl/studia/index.php?str=462")

            except Exception as e:

                print(e)
                say("Coś poszło nie tak.")

        # elif "wyszukiwarka" in record:
        #
        #     try:
        #
        #         say("Już otwieram.")
        #         webbrowser.open("https:\\www.google.com")
        #
        #     except Exception as e:
        #
        #         print(e)
        #         say("Coś poszło nie tak.")

        elif 'wsparcie' in record:

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

        elif "gierka" in record:

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
                say("Coś poszło nie tak")

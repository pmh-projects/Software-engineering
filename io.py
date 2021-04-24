import speech_recognition # automatic speech recognition (ASR), computer speech recognition, or speech-to-text, is a capability which enables a program to process human speech into a written format.
import speech_recognition as s_r #
import wikipedia #Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
import random #his module implements pseudo-random number generators for various distributions.
import webbrowser #The webbrowser module provides a high-level interface to allow displaying Web-based documents to users.
import os #The OS module in Python provides functions for interacting with the operating system.
import pyttsx3 # yttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3. 
import csv 
import pyaudio #PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio on a variety of platforms. 
import sys #This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import operator #The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator. add(x, y) is equivalent to the expression x+y 
#import pickle #The pickle module can transform a complex object into a byte stream and it can transform the byte stream into an object with the same internal structure.
from time import sleep #This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.. The sleep() function suspends (waits) execution of the current thread for a given number of seconds.

#Voice mechanism
voice_mech = pyttsx3.init('sapi5')

wikipedia.set_lang("pl")

def say(audio):
    voice_mech.say(audio)
    voice_mech.runAndWait()

def introduction():
        say("Witaj w asystencie głosowym")
        print("Witaj w asystencie głosowym")

def command_recognition():

    #Create voice recognition
    r = s_r.Recognizer()
    record=''
  
    with s_r.Microphone() as source:
        sleep(2)
        say("Abym mogła Tobie pomóc podaj nazwę funkcji.")
        print("Lista dostępnych funkcji:\nwikipedia - uruchamia funkcję wyszukiwania haseł na wikipedii.\nOtwórz stronę uniwersytetu - uruchamia przegladarke.\nzapisz plik - funkcja zapisujaca plik o podanym głosowo tytule i zawartośći podanej.\notwórz plik - otwieranie zapisanego pliku.\nkalkulator - dodawanie, odejmowanie, mnożenie i dzielenie\nlotto - symulator lotto. Zastanawiałeś się jakie masz szczęście w grach losowych? Sprawdź się.\notwórz google - otwiera stronę google.\npomocy - masz problem z kodem? Otworzę stackoverflow.\notwórz youtube - chcesz posłuchać muzyki?\notwórz playlistę - funkcja otwierajaca zadeklarowana playlistę.\nutwór drugi - otwiera drugi utwór na playliście.\nutwór trzeci - otwiera trzeci utwór na playliście.\ngra - rozerwij się i ogadnij wylosowana liczbę\nzamknij - wyjście z programu.")
        say("Słucham Cię.")
        print("Słucham Cię.")
        #period of silence allowed
        r.pause_threshold = 1     
        #listening to calibrate the energy threshold for ambient noise levels 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
       
    try:
        print("Sprawdzam co powiedziano.") 
        record = r.recognize_google(audio, language='pl-PL')
        print(f"Powiedziano: {record}\n")

    except Exception as e:
        print(e)   
        sleep(2) 
        say("Nie rozumiem co do mnie mówisz.")
           

    return record

def save_to_file_title():
    p = s_r.Recognizer()

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
        return(":)")
    except:
        print("Nieoblisugwany blad", sys.exc_info()[0])    

    return record2    

def save_to_file_content():
    w = s_r.Recognizer()
    with s_r.Microphone() as source:
        say("Podaj tekst zapisu")
        print("Slucham...")
        w.pause_threshold = 2     
        w.adjust_for_ambient_noise(source)
        audio3 = w.listen(source)   

    try:
        print("Sprawdzam co powiedziano")   
        record3 = w.recognize_google(audio3, language='pl-PL') 
        print(f"Powiedziano: {record3}\n")
        f=open(record2 + '.txt','w+')
        f.write(record3)    
        say("Plik został zapisany.")
        say("Plik został zapisany.")

    except Exception as e:
        print(e)   
        say("Nie zrozumiałe jest to co do mnie mówisz, może następnym razem...")
        return(":)")
    except:
        print("Nieoblisugwany blad", sys.exc_info()[0])    

    return record3     

def wikipedia_search():

    wiki = s_r.Recognizer()
    with s_r.Microphone() as source:
        say("Co mam znaleźć na wikipedii?")

        wiki.pause_threshold = 2 
        wiki.adjust_for_ambient_noise(source)
        wikisearch = wiki.listen(source) 
        varwiki = wiki.recognize_google(wikisearch, language='pl-PL') 

        say("Przeszukuję wikipedię.")
    
        wikifound = wikipedia.summary(varwiki, sentences = 2)
          
        say("Jak mówi wikipedia: ")
        print(wikifound)
        say(wikifound)


def open_from_file():
    q = s_r.Recognizer()
    with s_r.Microphone() as source:
        say("Jaki plik mam otworzyć?")
        print("Slucham...")
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
        return(":)")
    except:
        print("Nieoblisugwany blad", sys.exc_info()[0])    

    return record4 


def lotto_draw():

    try:

        say("Podaj liczby:")
        print("Podaj liczby:")
        a = int(input("Pierwsza:"))
        b = int(input("Druga:"))
        c = int(input("Trzecia:"))
        d = int(input("Czwarta"))
        e = int(input("Piąta"))

        podane_liczby = [a,b,c,d,e]


        losowanie_lotto = []
        i = 0

        while i < 5:
            r = random.randint(1, 49)
            if losowanie_lotto.count(r) == 0:
                losowanie_lotto.append(r)
                i+=1
        trafiony = [] 
        for x in losowanie_lotto:
            y = len(podane_liczby)
            t=0
            while t < y:
                z = podane_liczby[t]
                if x==z:
                    trafiony.append(z)
                t=t+1 
        
        print("Wybrane Liczby: ") 
        print(podane_liczby)
        print("Wylosowane Liczby: ") 
        print(losowanie_lotto) 
        print("Trafione liczby: ") 
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

                say("Odgadnij liczbę.")
                audio_in0.pause_threshold = 2
               
                audio_listuj0 = audio_in0.listen(source, timeout=2)
                print(audio_listuj0)

                record10 = audio_in0.recognize_google(audio_listuj0, language='pl-PL')
                a=int(record10)  
                print(a)
                say("Wybrałeś liczbę " + str(a))

                if number == a:
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




def calculator():

    while True:
       
        try:

            say("Podaj dwie liczby do działania")
            x=float(input("Pierwsza: "))
            y=float(input("Druga: "))
            dzialanie=int(input("Jakie działanie wykonać? \n1. Dodawanie 2. Odejmowanie 3. Mnożenie 4. Dzielenie \nAby wyjść kliknij 00\n "))
            
            if(dzialanie == 1):
                z=round((x+y),2)
                print(z)
                say("Wynik dodowania wynosi")
                say(z)
            elif(dzialanie == 2):
                z=round((x-y),2)    
                print(z)
                say("Wynik odejmowania wynosi:")
                say(z)
            elif(dzialanie == 3):
                z=round((x*y),2)
                print(z)
                say("Wynik mnożenia wynosi:")
                say(z)
            elif(dzialanie == 4): 

                if y == 0:

                    say("Pamiętaj cholero nie dziel przez zero")

                else:    
                    z=round((x/y),2)   
                    print(z)
                    say("Wynik dzielenia wynosi:")
                    say(z)
            elif(dzialanie == 0):
                
                say("Wychodzę z kalkulatora. ")
                break

            else:

                say("Błąd.")
                print("Błąd.")   

        except ValueError:
            print("Bład wartości")
        except:
            print("Nieobsługiwany błąd", sys.exc_info()[0])  
        



if __name__ == "__main__":   #funkcja glowna

    introduction()

    while True:
       
        record = command_recognition().lower()

         
        if 'wikipedia' in record:                  #jeśli coś powiemy to zacznie szukac na wikipedi
   
            try:

                wikipedia_search()

            except Exception as e:

                print(e)   
                say("Brak wyników w wikipedi...")

       
    
        if 'otwórz youtube' in record:
            
            try: 
                webbrowser.open("https:\\www.youtube.com")  

            except Exception as e:   
                print(e)      
                say("Coś poszło nie tak.")    


        # if 'dodaj wpis do listy' in record:
        #     try: 

        #         add_entry()

        #     except Exception as e:   
        #         print(e)      
        #         say("Coś poszło nie tak.")   

        if 'otwórz stronę uniwersytetu' in record:

            try: 
                webbrowser.open("https://wzr.ug.edu.pl/")

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
 
        # if 'dodaj użytkownika' in record:
        #     try:
        #         lista_prac()

        #     except Exception as e:   
        #         print(e)      
        #         say("Coś poszło nie tak.")        

        if 'kalkulator' in record:

            try:

                calculator()

            except Exception as e:   
                print(e)      
                say("Coś poszło nie tak.")
           
        if "otwórz plik" in record:

            try:

                record4 = open_from_file().lower()

            except Exception as e:   
                print(e)      
                say("Coś poszło nie tak.")
                
        
        if "gra" in record:

            try:

                guess_the_number()
                say("Mam nadzieję, że się podobało.")

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

        if "otwórz google" in record:

            try:
                webbrowser.open("https:\\www.google.com") 

            except Exception as e:   
                print(e)      
                say("Coś poszło nie tak.")      

        if 'pomocy' in record:

            try:
                webbrowser.open("stackoverflow.com")

            except Exception as e:   
                print(e)      
                say("Coś poszło nie tak.")        

        if "otwórz playlistę" in record:

            try:
                webbrowser.open("https://www.youtube.com/watch?v=vpXlYbstRDs&list=PLIut9bR_W7KX9OK1BwJvLoidfirixgPPN") 

            except Exception as e:   
                print(e)      
                say("Coś poszło nie tak.")        

        if "utwór drugi" in record:

            try:

                webbrowser.open("https://www.youtube.com/watch?v=P61Qy1vEsTU&list=PLIut9bR_W7KX9OK1BwJvLoidfirixgPPN&index=2")

            except Exception as e:   
                print(e)      
                say("Coś poszło nie tak.")      

        if "utwór trzeci" in record:

            try:

                webbrowser.open("https://www.youtube.com/watch?v=Ak1-qLbHHCM&list=PLIut9bR_W7KX9OK1BwJvLoidfirixgPPN&index=3") 

            except Exception as e:   
                print(e)      
                say("Coś poszło nie tak.")      


            
        if 'zamknij' in record:

            try:
                say("Zamykam program. Do usłyszenia")
                sys.exit()           

            except Exception as e:   
                print(e)      
                say("Coś poszło nie tak.")      
                
#License: Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

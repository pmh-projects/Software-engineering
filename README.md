#  (AG) AsGlos - asystent głosowy  --- DOKUMENTACJA IN PROGRESS

* [Charakterystyka  oprogramowania](#Charakterystyka-oprogramowania)
* [Prawa autorskie](#Prawa-autorskie)
  * [Autorzy](#Autorzy-projektu)
  * [Licencja](#Licencja)
* [Specyfikacja wymagań](#Specyfikacja-wymagań)
  * [Wymagania funkcjonalne](#Wymagania-funkcjonalne)
  * [Wymagania niefunkcjonalne](#Wymagania-niefunkcjonalne)
* [Projekt (diagramy UML)](#Projekt-UML)
  * [Diagram przypadków użycia](#Diagram-przypadków-użycia)
  * [Diagram czynnosci dla każdego przypadku użycia](#Diagram-czynnosci-dla-każdego-przypadku-użycia)
  * [Diagram komponentów](#Diagram-komponentów)
  * [Diagram wdrożeń](#Diagram-wdrożeń)
* [Architektura systemu/oprogramowania](#Architektura-oprogramowania)
  * [Architektura rozwoju](#Architektura-rozwoju)
  * [Architektura uruchomieniowa](#Architektura-uruchomieniowa)
* [Testy](#Testy)
* [Kontakt](#Kontakt)


## Charakterystyka oprogramowania

Nazwa skrócona: (S)AG<br>
Nazwa pełna: (S)AsGlos studencki asystent głosowy
<br><br>
Krótki opis ze wskazaniem celów:<br>
Asystent głosowy bla bla bla stworzony z myślą o studentach i dla studentów bla bla bla, który bla bla bla.
Celem jego jest bla bla, ułatwienie poruszania się po świecie studenckim, bla bla bla.
	
## Prawa autorskie

### Autorzy projektu
Paweł Mach, Marcin Edel, Damian Jaszewski

### Licencja
Licencja GPLv3
+ info o licencjach poszczególnych modułów

## Specyfikacja wymagań

Pogrupowana lista składająca się z następujących kolumn: (1) identyfikator, (2) nazwa, (3) opis, (4) priorytet: 1- wymagane, 2-przydatne, 3-opcjonalne 

### Wymagania funkcjonalne. 

### Wymagania niefunkcjonalne.

## Projekt UML

### Diagram przypadków użycia:

<img src="https://raw.githubusercontent.com/pmh-projects/io/master/diagramy/UML_diagram_przypadkow_uzycia.png" width=100%/>

### Diagram czynnosci dla każdego przypadku użycia

<img src="https://raw.githubusercontent.com/pmh-projects/io/master/diagramy/UML_dpu1.png" width=100%/>
<img src="https://raw.githubusercontent.com/pmh-projects/io/master/diagramy/UML_dpu22.png" width=100%/>
<img src="https://raw.githubusercontent.com/pmh-projects/io/master/diagramy/UML_dpu3.png" width=100%/>

### Diagram komponentów

<img src="https://raw.githubusercontent.com/pmh-projects/io/master/diagramy/UML_diagram_komponentow.png" width=100%/>

### Diagram wdrożeń

<img src="https://raw.githubusercontent.com/pmh-projects/io/master/diagramy/UML_diagram_wdrozen.png" width=100%/>

## Architektura oprogramowania

### Architektura rozwoju:

+ Python 3.9 -  wydanie Python'a
+ PyCharm - zintegrowane środowisko programistyczne używane w programowaniu komputerowym, specjalnie dla języka Python
+ pip - system zarządzania pakietami napisany w Pythonie, używany do instalowania pakietów oprogramowania i zarządzania nimi.
+ Pipenv - narzędzie, które ma na celu wprowadzenie do świata Pythona tego, co najlepsze ze wszystkich światów pakowania (bundler, composer, npm, cargo, yarn, itp.).
+ Python Virtual Environments (virtualenv)
+ Niezbędne moduły/biblioteki: speech_recognition, pyowm, wikipedia, random, webbrowser,
pyttsx3, pyautogui, googlesearch, tkinter, time, freeze etc.(wszystkie moduły in requirements.txt)
+ Połączenie sieciowe w celu połączenia się z modułami
+ System operacyjny umożliwiający wykorzystanie Pyttsx3 i Speech Recognition przy konwersji z tesktu do głosu i głosu do tekstu w języku polskim 
+ Mikrofon (bardzo dobrze wychwytujący dźwięki)
+ Głośniki

### Architektura uruchomieniowa:

+ Python 3.9
+ Niezbędne moduły/biblioteki: speech_recognition, pyowm, wikipedia, random, webbrowser, pyttsx3, pyautogui, googlesearch, tkinter, time
(w celu instalacji wszystkich modułów za jednym razem proszę użyć "pip freeze > requirements.txt")
+ Skonfigurowane środowisko (PATH i zmienne środowiskowe)
+ Połączenie sieciowe w celu połączenia się z modułami
+ System umożliwiający wykorzystanie Pyttsx3 i Speech Recognition przy konwersji z tesktu do głosu i głosu do tekstu w języku polskim 
+ Mikrofon (bardzo dobrze wychwytujący dźwięki)
+ Głośniki

## Testy

Processing........................

## Kontakt

pawelmach@pm.me<br>
damian.jaszewski.@<br>
marcin.edel@

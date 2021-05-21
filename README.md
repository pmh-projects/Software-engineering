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

Nazwa skrócona: AG<br>
Nazwa pełna: AsGlos studencki asystent głosowy
<br><br>
Krótki opis ze wskazaniem celów:<br>
Asystent głosowy stworzony z myślą o studentach mających niepełnosprawność ruchową. 
Prawo do nauki jest jednym z  fundamentalnych praw człowieka, którego 
realizacja umożliwia rozwój osobisty oraz pozwala na osiągnięcie samodzielności 
i niezależności, a także pełny udział we wszystkich sferach życia.
Motywem stowrzenia aplikacji była, chęć pomocy studentom z niepełnosprawnością ruchową w poruszaniu się po świecie akademickim.
	
## Prawa autorskie

### Autorzy projektu
Paweł Mach, Marcin Edel, Damian Jaszewski

### Licencja
Licencja aplikacji: GPLv3
| nazwa modułu | licencja |
| --- | --- |
| aiohttp | Apache Software License (Apache 2) |
altgraph	|	MIT License (MIT)
async-timeout	|	Apache Software License (Apache 2)
attrs		|	MIT License (MIT)
beautifulsoup4	|	MIT License (MIT)
bottle-websocket |	MIT License (MIT)
bs4		|	brak licencji
cachetools	|	MIT License (MIT)
certifi		|	Mozilla Public License 2.0 (MPL 2.0) (MPL-2.0)
cffi		|	MIT License (MIT)
chardet		|	GNU Library or Lesser General Public License (LGPL) (LGPL)
comtypes	|	MIT License (MIT License)
cx-Freeze	|	Python Software Foundation License (Python Software Foundation License)
cx-Logging	|	Python Software Foundation License (Python Software Foundation License)
distutils-pytest|	Apache Software License (Apache-2.0)
docopt		|	MIT License (MIT)
Eel		|	MIT License (MIT)
future		|	OSI Approved, MIT License (MIT)
geojson		|	BSD License (BSD)
gevent		|	MIT License (MIT)
gevent-websocket|	Apache Software License (Apache-2.0)
google		|	BSD License
google-search	|	MIT License (MIT license)
google-search-results	|MIT License (MIT)
googlesearch-python	|MIT License
greenlet	|	MIT License (MIT License)
idna		|	BSD License (BSD-3-Clause)
importlib-metadata |	Apache Software License
Js2Py		|	MIT License (MIT)
lxml		|	BSD License (BSD)
MouseInfo	|	GNU General Public License v3 or later (GPLv3+) (GPLv3+)
multidict	|	Apache Software License (Apache 2)
numpy		|	BSD License (BSD)
packaging	|	Apache Software License, BSD License (BSD-2-Clause or Apache-2.0)
pandas		|	Apache License, Version 2.0
pefile==2019.4.18|	brak licencji
Pillow		|	Historical Permission Notice and Disclaimer (HPND) (HPND)
pipwin		|	BSD License (BSD)
py2exe		|	MIT License, Mozilla Public License 2.0 (MPL 2.0) (MIT/X11)
PyAudio		|	brak licencji
PyAutoGUI	|	BSD License (BSD)
pycparser	|	BSD License (BSD)
PyGetWindow	|	BSD License (BSD)
pyinstaller	|	GNU General Public License v2 (GPLv2) 
pyinstaller-hooks-contrib	|brak licencji
pyjsparser	|	MIT License
PyMsgBox	|	GNU General Public License v3 or later (GPLv3+)
pyowm		|	MIT License (MIT)
pyparsing	|	MIT License (MIT License)
pyperclip	|	Apache Software License (Apache)
pypiwin32==223	|	brak licencji
PyPrind		|	BSD License (BSD 3-Clause)
PyQt5		|	GPL v3
PyQt5-Qt5	|	LGPL v3
PyQt5-sip	|	SIP
PyQt5-stubs	|	GNU General Public License v3 (GPLv3)
PyRect		|	BSD License (BSD)
PyScreeze	|	MIT License (MIT)
PySimpleGUI	|	GNU Lesser General Public License v3 or later (LGPLv3+)
pySmartDL	|	Public Domain (Public Domain)
PySocks		|	BSD License
python-dateutil	|	Apache Software License, BSD License (Dual License)
python-weather	|	MIT License (MIT)
pyttsx3		|	GNU General Public License v3 (GPLv3)
PyTweening	|	BSD License (BSD)
pytz		|	MIT License (MIT)
PyUserInput	|	GNU General Public License v3 (GPLv3)
pywin32		|	BSD License (BSD 3-clause)
pywin32-ctypes	|	BSD License (BSD 3-clause)
PyYAML		|	MIT License (MIT)
requests	|	Apache Software License (Apache 2.0)
six		|	MIT License (MIT)
soupsieve	|	MIT License (MIT)
SpeechRecognition|	BSD License (BSD)
typing-extensions|	Python Software Foundation License (PSF)
tzlocal		|	MIT License (MIT)
urllib3		|	MIT License (MIT)
whichcraft	|	BSD License (BSD)
wikipedia	|	MIT License (MIT)
wxPython	|	OSI Approved (wxWindows Library License)
xmltodict	|	MIT License (MIT)
yarl		|	Apache Software License (Apache 2)
zipp		|	MIT License
zope.event	|	Zope Public License (ZPL 2.1)
zope.interface	|	Zope Public License (ZPL 2.1)


## Specyfikacja wymagań

Pogrupowana lista składająca się z następujących kolumn: (1) identyfikator, (2) nazwa, (3) opis, (4) priorytet: 1- wymagane, 2-przydatne, 3-opcjonalne 

### Wymagania funkcjonalne. 

| 	ID 	| 	Nazwa 		| 	Opis 											| 	Priorytet 	|
| 	--- 	|	 --- 		| 	--- 											| 	--- 		|
|	1	| 	Wikipedia 	| 	uruchamia funkcję wyszukiwania haseł na wikipedii z możliwością zapisu do pliku 	|	1		|
|	2	|	Notatka		|	funkcja zapisująca plik o podanym głosowo tytule i zawartością				|	1		|
|	3	|	Otwórz plik	|	otwieranie zapisanego pliku								|	1		|
|	4	|	Wyszukiwarka	|	wyświetla 5 pierwszych wyników i uruchamia wyszukiwarkę z podanych hasłem		|	1		|
|	5	|	Screenshot	|	pobiera i zapisuje zawartość ekranu do pliku png z podanym przez użytkownika tytułem	|	1		|
|	6	|	Strona WWW	|	uruchamia zdefiniowane strony www (stronę UG, stackoverflow, yputube, inne		|	2		|
|	7	|	Pogoda		|	podaje pogodę w wybranym mieście							|	2		|
|	8	|	Klawiatura	|	sterowanie głosowe klawiaturą								|	1		|
|	9	|	Skróty klawiszowe	|	Obsługa podstawowych skrótów klawiszowych					|	2		|
|	10	|	Gra		|	prosta gra typu lotto, lub zgadywanie liczb						|	3		|

### Wymagania niefunkcjonalne.

| 	ID 	| 	Nazwa 		| 	Opis 											| 	Priorytet 	|
| 	---	| 	--- 		| 	--- 											| 	--- 		|
|	1	|	Niezawodność	|	program powinien działać bez zarzutów; nie powinno być sytuacji, w które aplikacja nie działa stabilnie lub generuje błędy|	1	|
|	2	|	Użyteczność	|	aplikacja nie powinna sprawiać problemów w obsłudze					|	1		|
|	3	|	Szybkość działania|	aplikacja powinna działać nie powodując dyskomfortu spowodowanego zbyt długim oczekiwaniem na reakcję|	1	|
|	4	|	Estetyka	|	aplikacja powinna mieć wysoki poziom estetyki						|	2		|
|	5	|	Bezpłatna	|	aplikacja powinna być bezpłatna, korzystająca z darmowych modułów			|	1		|
|	6	|	Krótki czas wdrożenia	|	aplikacja powinna zostać wdrożona wciągu 30 dni					|	3		|
|	7	|	Otwartość	|	aplikacja powinna mieć możliwość rozbudowy o kolejne funkcje				|	2		|
|	8	|	Lekka		|	aplikacja powinna wykorzystywać minimalny poziom zasobów komputera			|	2		|




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

+ Python 3.9.4 - minimalna wersja wydania Python'a
+ PyCharm - zintegrowane środowisko programistyczne używane w programowaniu komputerowym, specjalnie dla języka Python
+ pip - system zarządzania pakietami napisany w Pythonie, używany do instalowania pakietów oprogramowania i zarządzania nimi.
+ Pipenv - narzędzie, które ma na celu wprowadzenie do świata Pythona tego, co najlepsze ze wszystkich światów pakowania (bundler, composer, npm, cargo, yarn, itp.).
+ Python Virtual Environments (virtualenv)
+ Niezbędne moduły/biblioteki: speech_recognition, pyowm, wikipedia, random, webbrowser,
pyttsx3, pyautogui, googlesearch, tkinter, time, freeze etc.(wszystkie moduły w requirements.txt)
+ System operacyjny umożliwiający wykorzystanie Pyttsx3 i Speech Recognition przy konwersji z tesktu do głosu i głosu do tekstu w języku polskim
+ Git i GitHub

### Architektura uruchomieniowa:

+ Python 3.9.4 - minimalna wersja wydania Python'a
+ Niezbędne moduły/biblioteki: speech_recognition, pyowm, wikipedia, random, webbrowser, pyttsx3, pyautogui, googlesearch, tkinter, time
W celu instalacji wszystkich modułów za jednym razem proszę użyć:
```
$  pip install -r /path/to/requirements.txt
```
+ Skonfigurowane środowisko (PATH i zmienne środowiskowe)
+ System umożliwiający wykorzystanie Pyttsx3 i Speech Recognition przy konwersji z tesktu do głosu i głosu do tekstu w języku polskim 

Pozostałe niezbędne elementy(zarówno przy tworzeniu jak i korzystaniu z aplikacji):
+ Mikrofon (bardzo dobrze wychwytujący dźwięki) i głośniki
+ Połączenie sieciowe w celu nawiązania komunikacji z modułami odpowiadającymi za niektóre funkcje

## Testy

### Scenariusze testów.
<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>1</th>
            <th colspan=2>Wyświetlenie menu asystenta głosowego</th>
            <th colspan=2>Test sprawdza czy po uruchomieniu aplikacji użytkownikowi wyświetli się menu z dostępnymi opcjami oraz czy aplikacja głosowo zachęci użytkownika do wybrania jednej z dostępnych opcji.</th>
        </tr>
        <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
        <tr>
            <td>1.1</td>
            <td>Pozytywny</td>
            <td>Uruchom aplikację</td>
            <td>Menu zostaję wyświetlone. Asystent głosowy się wita i zachęca głosowo do wprowadzenia funkcji.</td>
            <td>Menu wyświetliło się. Asystent się przywitał i zachęcił do wyboru funkcji.</td>
        </tr>
        <tr>
            <td>1.2</td>
            <td>Pozytywny</td>
            <td>Sprawdź wyświetlane opcje, oczekiwane funkcje menu.
             
Podstawowe funkcje:
- Wikipedia
- Notatka
- Otwórz plik
- Klawiatura
- Google
- Screenshot

Funkcje webowe:
- Strona Uniwersytetu
- Strona wydziału
- Portal edukacyjny
- Portal studenta
- Aktualności
- Wyszukiwarka
- Wsparcie
- Otwórz youtube

Funkcje dodatkowe:
- Pogoda
- Lotto
- Gierka
- Zamknij</td>
            <td>Wymienione opcje się wyświetlają.
 
Podstawowe funkcje:
- Wikipedia
- Notatka
- Otwórz plik
- Klawiatura
- Google
- Screenshot

Funkcje webowe:
- Strona Uniwersytetu
- Strona wydziału
- Portal edukacyjny
- Portal studenta
- Aktualności
- Wyszukiwarka
- Wsparcie
- Otwórz youtube

Funkcje dodatkowe:
- Pogoda
- Lotto
- Gierka
- Zamknij</td>
            <td>Wymienione pola zostały wyświetlone.
 
Podstawowe funkcje:
- Wikipedia
- Notatka
- Otwórz plik
- Klawiatura
- Google
- Screenshot

Funkcje webowe:
- Strona Uniwersytetu
- Strona wydziału
- Portal edukacyjny
- Portal studenta
- Aktualności
- Wyszukiwarka
- Wsparcie
- Otwórz youtube

Funkcje dodatkowe:
- Pogoda
- Lotto
- Gierka
- Zamknij</td>
        </tr>
        <tr>
            <td>1.3</td>
            <td>Pozytywny</td>
            <td>W przypadku braku reakcji ze strony użytkownika</td>
            <td>Asystent poinformuje o oczekiwaniu na wybranie funkcji</td>
            <td>Asystent prosi o wybranie funkcji "Podaj nazwę funkcji. Słucham Cię"</td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>2</th>
            <th colspan=2>Funkcje podstawowe - korzystanie z funkcji "Wikipedia"</th>
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji wikipedia program prawidłowo przetworzy i pobierze hasło od użytkownika, następnie pobierze liczbę zdań od użytkownika. Podyktuje treść. Daną treść będzie można następnie zapisać do nowego pliku. </th>
        </tr>
        <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
        <tr>
            <td>2.1</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Wikipedia"</td>
            <td>Po wybraniu funkcji aplikacja pobiera od użytkownika hasło oraz ilość zdań które ma dyktować.
            Następnie program dyktuje treść.</td>
            <td>Po wybraniu funkcji aplikacja prosi o podanie hasła oraz podanie liczby zdań.
            Pogram pobiera dane z wikipedii i dyktuje fragment.</td>
        </tr>
          <tr>
            <td>2.2</td>
            <td>Pozytywny</td>
            <td>Zapisywanie do pliku</td>
            <td>Po odsłuchaniu fragmentu z wikipedii mamy możliwość zapisać treść do pliku, program pyta czy chcemy zapisać plik "tak/nie", następnie prosi o podanie tytułu.</td>
            <td>Po wybraniu opcji program poprosił o podanie tytułu pliku i zapisał nowy plik o tym tytule.</td>
        </tr>
          <tr>
            <th colspan=2>Uwagi</th>
            <th colspan=3>W przypadku problemu z pobraniem hasła od użytkownika asystent przekazuje komunikat "Spróbuj jeszcze raz" i wraca do podstawowych funkcji nie dając nam możliwości kontynuowania.</th>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>3</th>
            <th colspan=2>Funkcje podstawowe - korzystanie z funkcji "Notatka"</th>
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji notatka program pobierze od użytkownika tytuł notatki oraz treść notatki. Następnie program ma za zadanie zapisać notatkę do nowego pliku.</th>
        </tr>
      <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
      <tr>
            <td>3.1</td>
            <td>Pozytywny</td>
            <td>Wprowadź tytuł notatki.</td>
            <td>Program po wybraniu funkcji zapyta nas o tytuł notatki.</td>
            <td>Program po wybraniu funkcji zapytał o tytuł notatki, w przypadku nie zrozumienia tytułu, program utworzył notatkę bez tytułu.</td>
        </tr>
        <tr>
            <td>3.2</td>
            <td>Pozytywny</td>
            <td>Wprowadź treść notatki.</td>
            <td>Program pobierze od użytkownika treść notatki.</td>
            <td>Program prawidłowo pobiera treść notatki.</td>
        </tr>
          <tr>
            <th colspan=2>Uwagi</th>
            <th colspan=3>W przypadku nie zrozumienia tytułu, program utworzył notatkę bez tytułu.</th>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>4</th>
            <th colspan=2>Funkcje podstawowe - korzystanie z funkcji "Otwórz plik" lub "Otwórz notatkę"</th>
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji otwórz plik, otwórz notatkę program pobierze nazwę wybranego przez użytkownika pliku, notatki oraz otworzy go.</th>
        </tr>
      <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
      <tr>
            <td>4.1</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcję pod hasłem "Otwórz notatkę"</td>
            <td>Asystent po wybraniu funkcji zapyta o nazwę pliku i wyświetli użytkownikowi notatkę.</td>
            <td>Po wybraniu funkcji asystent zapytał o tytuł notatki, następnie ją wyswietlił.</td>
        </tr>
        <tr>
            <td>4.2</td>
            <td>Negatywny</td>
            <td>Wybierz głosowo funkcję pod hasłem "Otwórz plik"</td>
            <td>Asystent po wybraniu funkcji zapyta o nazwę pliku i wyświetli ją użytkownikowi.</td>
            <td>Asystent po wybraniu funkcji pobrał i wyświetlił tylko pliki z roszrzeszniem txt.</td>
        </tr>
            <tr>
            <th colspan=2>Uwagi</th>
            <th colspan=3>W przypadku wybrania funkcji otwórz plik nie ma możliwości wyboru rozszerzenia pliku w praktyce można otworzyć jedynie notatkę.</th>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>5</th>
            <th colspan=2>Funkcje podstawowe - korzystanie z funkcji "Wyszukiwarka"</th>
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji wyszukiwarka program prawidłowo przetworzy i pobierze hasło wyszukiwania, które następnie wyszuka w domyślnej przeglądarce użytkownika.</th>
        </tr>
      <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
      <tr>
            <td></td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Wyszukiwarka"</td>
            <td>Program pobiera od użytkownika hasło wyszukiwania, które następnie wyszukuje w oknie domyślnej preglądarki.</td>
            <td>Program pobrał hasło i prawidłowo wyświetlił okno przeglądarki z wskazanym hasłem.</td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>6</th>
            <th colspan=2>Funkcje podstawowe - korzystanie z funkcji "Screenshot"</th>
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji screenshot asystent wykona screenshot ekranu i poprosi użytkownika o podanie nazwy pliku, jaki ma zostać utworzony, po czym zapiszę plik.</th>
        </tr>
      <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
      <tr>
            <td></td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Screenshot"</td>
            <td>Asystent wykona screenshot okna, poprosi o podanie nazwy i zapiszę go do pliku.</td>
            <td>Asystent wykonał screenshot okna, poprosił o podanie nazwy i zapisał go do pliku.</td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>7</th>
            <th colspan=2>Korzystanie z funkcji  NET - wyświetlanie wybranych stron inernetowych</th>
            <th colspan=2>Test sprawdza czy po wybraniu funkcji z kategorii Net program otworzy przeglądarkę z właściwą stroną. </th>
        </tr>
      <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
      <tr>
            <td>7.1</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Strona Uniwersytetu"</td>
            <td>Po wywołaniu funkcju, program powinien otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji hasłem "Strona Uniwersytetu" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://ug.edu.pl/".</td>
        </tr>
         <tr>
            <td>7.2</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Strona wydziału"</td>
            <td>Po wywołaniu funkcju, program powinien otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji hasłem "Strona wydziału" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://wzr.ug.edu.pl/".</td>
        </tr>
         <tr>
            <td>7.3</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Portal edukacyjny"</td>
            <td>Po wywołaniu funkcju, program powinien otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji hasłem "Portal edukacyjny" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://pe.ug.edu.pl/".</td>
        </tr>
         <tr>
            <td>7.4</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Portal studenta"</td>
            <td>Po wywołaniu funkcju, program powinien otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji hasłem "Portal studenta" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://ps.ug.edu.pl/".</td>
        </tr>
         <tr>
            <td>7.5</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Rozkład zajęć"</td>
            <td>Po wywołaniu funkcju, program powinien otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji hasłem "Rozkład zajęć" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://wzr.ug.edu.pl/studia/index.php?str=462".</td>
        </tr>
         <tr>
            <td>7.6</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Aktualności"</td>
            <td>Po wywołaniu funkcju, program powinien otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji hasłem "Aktualności" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://www.dlastudenta.pl/".</td>
        </tr>
         <tr>
            <td>7.7</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Wsparcie"</td>
            <td>Po wywołaniu funkcju, program powinien otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji hasłem "Wsparcie" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://www.stackoverflow.com".</td>
        </tr>
         <tr>
            <td>7.8</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Otwórz YouTube"</td>
            <td>Po wywołaniu funkcju, program powinien otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji hasłem "Otwórz Youtube" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://www.youtube.com".</td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>8</th>
            <th colspan=2>Funkcje dodatkowe - Korzystanie z funkcji "Pogoda"</th>
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji Pogoda i podaniu wybranego przez użytkownika miasta program prawidłowo przetworzy i pobierze miasto oraz przekarze dane pogodowe dla danej miejscowosci.</th>
        </tr>
      <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
      <tr>
            <td></td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Pogoda" + wybrane miasto</td>
            <td>Program po wywołaniu funkcji i po podaniu miasta przekazuje dane odnośnie pogody.</td>
            <td>Program po wywołaniu funkcji pogoda i podaniu miasta pobrał i przekazał głosowo aktualną informację o pogodzie.</td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>9</th>
            <th colspan=2>Funkcje dodatkowe - Korzystanie z funkcji "Klawiatura"</th>
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji Klawiatura program prawidłowo przetworzy i pobierze symbol klawisza przekazywany ustnie przez użytkownika.</th>
        </tr>
      <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
      <tr>
            <td></td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Klawiatura"</td>
            <td>Funkcja umożliwia wybór pojedynczego klawisza lub skrótu klawiszowego</td>
            <td>Funkcja pobiera zarówno litery jak i znaki specjalne, dizęki pobraniu znaków można wyszukać hasło w internecie.</td>
        </tr>
           <tr>
            <th colspan=2>Uwagi</th>
            <th colspan=3>Pomimo wpisania hasła brak obsługi skrótów klawiszowych, albo jest to niejasne, program pobiera np. hasło "enter", "backspace", ale nie wiążę się to z właściwą akcją. </th>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>10</th>
            <th colspan=2>Funkcje dodatkowe - Korzystanie z funkcji "Lotto"</th>
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji Lotto program zleci użytkownikowi wybranie po kolei 6 kolejnych różnych cyfr z zakresu od 1-49, po czym wylosuje liczby i zestawi je z liczbami użytkownika. </th>
        </tr>
      <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
      <tr>
            <td></td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Lotto"</td>
            <td>Asystent pobiera od użytkownika po kolei 6 liczb z zakresu 1 - 49, aplikacja przyjmuje tylko liczby. Aplikacja pokazuje wylosowane liczby i informuje o wyniku.</td>
            <td>Asystent pobrał 6 liczb, zaznaczając każdą z nich. Następnie wylosował liczby i pokazał wynik.</td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>11</th>
            <th colspan=2>Funkcje dodatkowe - Korzystanie z funkcji "Gierka"</th>
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji program zleci użytkownikowi odgadnięcie liczby z zakresu 1-100, program poinformuje jeśli zgadywana liczba jest większa lub mniejsza od poszukiwanej. Program poinformuje użytkownia w momencie odgadnięcia liczby.</th>
        </tr>
      <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
      <tr>
            <td></td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Gierka"</td>
            <td>Funkcja losuje liczbę następnie prosi użytkownika o jej odgadnięcie, asysent informuje czy liczba jest zbyt mała lub zbyt duża.</td>
            <td>Funkcja wylosowała liczbę i poprosiła o jej podanie, asystent poinformował gdy liczba była zbyt mała lub zbyt duża, asystent poinformował i odgadnięciu liczby hasłem "brawo".</td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th colspan=2>Nazwa</th>
            <th colspan=2>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>12</th>
            <th colspan=2>Funkcje dodatkowe - Korzystanie z funkcji "Zamykanie programu"</th>
            <th colspan=2>Test sprawdza czy po wywołaniu funkcji "Zamknij" program się wyłączy. </th>
        </tr>
      <tr>
            <td></td>
            <td>Typ testu</td>
            <td>Opis Kroku</td>
            <td>Oczekiwany wynik</td>
            <td>Rzeczywisty wynik</td>
        </tr>
      <tr>
            <td></td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Zamykanie programu"</td>
            <td>Funkcja ma za zadanie zamknąć program.</td>
            <td>Po wybraniu funkcji program się zamyka.</td>
        </tr>
    </tbody>
</table>

### Sprawozdanie z wykonania scenariuszy testów.

<table>
    <thead>
        <tr>
            <th>Nazwa funkcjonalności</th>
            <th>Rezultat</th>
            <th>Uwagi</th>
        </tr>
    </thead>
    <tbody>
       <tr>
            <td>Wyświetlenie menu asystenta głosowego</td>
            <td>Pozytywnie przetestowany przypadek testowy.</td>
            <td></td>
       </tr>
       <tr>
            <th colspan=3>Funkcje podstawowe</th>
        </tr>
	<tr>
            <td>Korzystanie z funkcji "Wikipedia"</td>
            <td>2/2 Pozytywnie przetestowane przypadki testowe.</td>
            <td>W przypadku problemu z pobraniem hasła od użytkownika asystent przekazuje komunikat "Spróbuj jeszcze raz" i wraca do podstawowych funkcji nie dając nam możliwości kontynuowania.</td>
        </tr>
	<tr>
            <td>Korzystanie z funkcji "Notatka"</td>
            <td>2/2 Pozytywnie przetestowane przypadki testowe.</td>
            <td>W przypadku nie zrozumienia tytułu, program utworzył notatkę bez tytułu.</td>
        </tr>
	<tr>
            <td>Korzystanie z funkcji "Otwórz plik" lub "Otwórz notatkę"</td>
            <td>1/2 Pozytywne przypadki testowe, funkcja otwórz plik działa identycznie jak otwórz notatkę i nie spełnia swoich założeń.</td>
            <td>W przypadku wybrania funkcji otwórz plik nie ma możliwości wyboru rozszerzenia pliku w praktyce można otworzyć jedynie notatkę.</td>
        </tr>
	<tr>
            <td>Korzystanie z funkcji "Wyszukiwarka"</td>
            <td>Pozytywnie przetestowany przypadek testowy.</td>
            <td></td>
        </tr>
	<tr>
            <td>Korzystanie z funkcji "Screenshot"</td>
            <td>Pozytywnie przetestowany przypadek testowy.</td>
            <td></td>
        </tr>
	<tr>
            <th colspan=3>Funkcje NET</th>
        </tr>
	<tr>
            <td>Korzystanie z funkcji wyświetlania wybranych stron inernetowych</td>
            <td>8/8 Pozytywnie przetestowane przypadki testowe, wszystkie strony otwierają się równie sprawnie.</td>
            <td></td>
        </tr>
	<tr>
  	    <th colspan=3>Funkcje dodatkowe</th>
        </tr>
	    <tr>
  	    <td>Korzystanie z funkcji "Pogoda"</td>
     	    <td>Pozytywnie przetestowany przypadek testowy.</td>
            <td></td>
        </tr>
	    <tr>
  	    <td>Korzystanie z funkcji "Klawiatura"</td>
     	    <td>Pozytywnie przetestowany przypadek testowy.</td>
            <td>Pomimo wpisania hasła brak obsługi skrótów klawiszowych, albo jest to niejasne, program pobiera np. hasło "enter", "backspace", ale nie wiążę się to z właściwą akcją.</td>
        </tr>
	    <tr>
  	    <td>Korzystanie z funkcji "Lotto"</td>
     	    <td>Pozytywnie przetestowany przypadek testowy.</td>
            <td></td>
        </tr>
	    <tr>
  	    <td>Korzystanie z funkcji "Gierka"</td>
     	    <td>Pozytywnie przetestowany przypadek testowy.</td>
            <td></td>
        </tr>
	    <tr>
  	    <td>Korzystanie z funkcji "Zamykanie programu"</td>
     	    <td>Pozytywnie przetestowany przypadek testowy.</td>
            <td></td>
    </tbody>
</table>

## Kontakt

pawelmach@pm.me<br>
damianjaszewski@gmail.com<br>
marcin.edel@

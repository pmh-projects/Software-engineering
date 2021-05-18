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
(w celu instalacji wszystkich modułów za jednym razem proszę użyć "pip freeze > requirements.txt")
+ Skonfigurowane środowisko (PATH i zmienne środowiskowe)
+ System umożliwiający wykorzystanie Pyttsx3 i Speech Recognition przy konwersji z tesktu do głosu i głosu do tekstu w języku polskim 

Pozostałe niezbędne elementy(zarówno przy tworzeniu jak i korzystaniu z aplikacji):
+ Mikrofon (bardzo dobrze wychwytujący dźwięki) i głośniki
+ Połączenie sieciowe w celu nawiązania komunikacji z modułami odpowiadającymi za niektóre funkcje

## Testy

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
            <td>Po wybraniu funkcju aplikacja pobiera od użytkownika hasło oraz ilość zdań które ma dyktować.
            Następnie program dyktuje treść.</td>
            <td>Po wybraniu funkcji aplikacja prosi o podanie hasła, podanie ilosći zdań.
            Pogram pobiera dane z wikipedii i dyktuje fragment.</td>
        </tr>
          <tr>
            <td>2.2</td>
            <td>Pozytywny</td>
            <td>Zapisywanie do pliku</td>
            <td>Po odsłuchaniu fragmentu z wikipedii mamy możliwość zapisać treść do pliku, program pyta czy chcemy zapisać plik tak/nie, następnie prosi o podanie tytułu</td>
            <td>Po wybraniu opcji program poprosił o podanie tytułu pliku i zapisał nowy plik o tym tytule.</td>
        </tr>
          <tr>
            <th colspan=2>Uwagi</th>
            <th colspan=3>W przypadku problemu z pobraniem hasła od użytkownika asystent przekauzuje komunikat "Spróbuj jeszcze raz" i wraca do podstawowych funkcji nie dając nam możliwości kontynuowania</th>
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
            <td></td>
            <td>Pozytywny</td>
            <td>Wprowadź tytuł notatki.</td>
            <td>Program po wybraniu funkcji zapyta nas o tytuł notatki.</td>
            <td>Program po wybraniu funkcji zapytał o tytuł notatki, w przypadku nie zrozumienia tytułu, program utworzył notatkę bez tytułu.</td>
        </tr>
        <tr>
            <td></td>
            <td>Pozytywny</td>
            <td>Wprowadź treść notatki.</td>
            <td>Program pobierze od użytkownika treść notatki.</td>
            <td>Program prawidłowo pobiera treść notakti.</td>
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
            <td></td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Otwórz notatkę"</td>
            <td>Asystent po wybraniu funkcji zapyta o nazwę pliku i wyświetli użytkownikowi notatkę.</td>
            <td>Po wybraniu funkcji assytent zapytał i tytuł notatki następnie ją wyswietlił</td>
        </tr>
        <tr>
            <td></td>
            <td>Negatywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Otwórz plik"</td>
            <td>Asystent po wybraniu funkcji zapyta o nazwę pliku i wyświetli ją użytkownikowi</td>
            <td>Asystent po wybraniu funkcji pobrał i wyświetlił tylko pliki z roszrzeszniem txt</td>
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
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji wyszukiwarka program prawidłowo przetworzy i pobierze haslo wyszkiwania, które następnie wyszuka w domyślnej przeglądarce użytkownika.</th>
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
            <td>Program pobiera od użytkownika haslo wyszukiwania, które następnie wyszukuje w oknie domyślnej preglądarki</td>
            <td>Program pobrał haslo i prawidłowo wyświetlił okno przeglądarki z wskazanym hasłem</td>
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
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji screenshot asystent wykona screenshot ekrany i poprosi użytkownika o podanie nazwy pliku, jaki ma zostać utworzony, po czym zapiszę plik.</th>
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
            <td>Asystent wykona screenshot okna, poprosi o podanie nazwy i zapiszę go do pliku</td>
            <td>Asystent wykonał screenshot okna, poprosił o podanie nazwy i zapisał go do pliku</td>
        </tr>
         c
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
            <td>Po wywołaniu funkcju, program powininen otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji haslem "Strona Uniwersytetu" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://ug.edu.pl/"</td>
        </tr>
         <tr>
            <td>7.2</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Strona wydziału"</td>
            <td>Po wywołaniu funkcju, program powininen otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji haslem "Strona wydziału" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://wzr.ug.edu.pl/"</td>
        </tr>
         <tr>
            <td>7.3</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Portal edukacyjny"</td>
            <td>Po wywołaniu funkcju, program powininen otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji haslem "Portal edukacyjny" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://pe.ug.edu.pl/"</td>
        </tr>
         <tr>
            <td>7.4</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Portal studenta"</td>
            <td>Po wywołaniu funkcju, program powininen otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji haslem "Portal studenta" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://ps.ug.edu.pl/"</td>
        </tr>
         <tr>
            <td>7.5</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Rozkład zajęć"</td>
            <td>Po wywołaniu funkcju, program powininen otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji haslem "Rozkład zajęć" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://wzr.ug.edu.pl/studia/index.php?str=462"</td>
        </tr>
         <tr>
            <td>7.6</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Aktualności"</td>
            <td>Po wywołaniu funkcju, program powininen otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji haslem "Aktualności" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://www.dlastudenta.pl/"</td>
        </tr>
         <tr>
            <td>7.7</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Wsparcie"</td>
            <td>Po wywołaniu funkcju, program powininen otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji haslem "Wsparcie" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://www.stackoverflow.com"</td>
        </tr>
         <tr>
            <td>7.8</td>
            <td>Pozytywny</td>
            <td>Wybierz głosowo funkcje pod hasłem "Otwórz YouTube"</td>
            <td>Po wywołaniu funkcju, program powininen otworzyć odpowiedni adres w domyślnej przeglądarce.</td>
            <td>Po wywołaniu funkcji haslem "Otwórz Youtube" program otwiera domyślną przeglądarkę i przenosi nas pod adres: "https://www.youtube.com"</td>
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
            <td>Program po wywołaniu funkcji pogoda i podaniu miasta pobrał i przekazał głosowo aktualną informację o pogodzie</td>
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
            <td>Funkcja pobiera zarówno litery jak i znaki specjalne, dizęki pobraniu znaków można wyszukać hasło w interncie.</td>
        </tr>
           <tr>
            <th colspan=2>Uwagi</th>
            <th colspan=3>Pomimo wpisania hasła brak obsługi skrótów klawiszowych, albo jest to niejasne, program pobiera np. hasło enter, backspace, ale nie wiążę się to z właściwą akcją. </th>
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
            <td>Asystent pobiera od użytkownika po kolei 6 liczb z zakresu 1 - 49, aplikacja przujmuje tylko liczby. Pokazuje </td>
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
            <th colspan=2>Test sprawdza czy po uruchomieniu funkcji gra program zleci użytkownikowi odgadnięcie liczby z zakresy 1-100, program poinformuje jeśli zgadywana liczba większa lub mniejsza od poszukiwanej. Program poinformuje użytkownia w momencie odgadnięcia liczby.</th>
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
            <td>Funkcja losuje liczbę następnie prosi użytkownika o jej odgadnięcie, asysent informuje czy liczba jest zbyt mała lub zbyt duża</td>
            <td>Funkcja wylosowała liczbę i poprosiła o jej podanie, asystent poinformował gdy licznba była zbyt mała lub zbyt duża, asystent poinformował i odgadnięciu liczby hasłem "brawo".</td>
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
            <th colspan=2>Funkcje dodatkowe - Korzystanie z funkcji "Zamykanie programy"</th>
            <th colspan=2>Test sprawdza czy po wywołaniu funkcji "Zamknij" program skończy działanie. </th>
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
            <td>Wybierz głosowo funkcje pod hasłem "Zamykanie programy"</td>
            <td>Funkcja ma za zadanie zamknąć program.</td>
            <td>Po wybraniu funkcji program się zamyka.</td>
        </tr>
    </tbody>
</table>

## Kontakt

pawelmach@pm.me<br>
damian.jaszewski.@<br>
marcin.edel@

# Python-project

1. Zawartość
Katalog projekt zawiera się z następujących plików:
• Filmy.py – główny program
• Lista.txt – plik zawierający dane do wczytania w naszą bazę danych

2. Wprowadzenie
Baza danych została stworzona do zbierania oraz organizowania informacji dotyczących
filmów. Po uruchomieniu programu, w terminalu zostanie nam przedstawione menu z
różnymi opcjami wyboru.

3. Wczytanie z pliku oraz wypisanie w postaci tabelki
Na początku menu jest opcja wczytania już gotowych filmów z danymi dzięki funkcji
wczytaj_dane_z_pliku(). Program wyświetli nam ilość rekordów znajdujących się w danym
pliku. Funkcja ta pozwala nam wraz z funkcją wypisz_dane_w_postaci_tabelki() wyświetlić
wszystkie filmy zgodnie z kolejnością w pliku lista.txt. 

4. Sortowanie
Po wybraniu tej opcji program przedstawi nam sposoby sortowania według kryteriów. Jest to
bardzo przydatne jeśli chcemy mieć dane przedstawione w sposób chronologiczny. Dla
każdego kryterium jest zrobiona funkcja porównania.

5. Wyszukiwanie
W celu nie potrzebnego szukania w dużej bazie danych opcja wyszukiwania ułatwi nam
znalezienie konkretnego filmu. Jest to opcja numer 4 w opcji menu. Po wybraniu tej opcji
program poprosi o metodę wyszukiwania tj.: tytuł, kategoria, rok premiery, długość Filmu.
Należy wpisać słowo kluczowe po wybraniu opcji wyszukiwania. Jeśli w naszej bazie danych
nie ma filmu spełniające dane kryterium program wyświetli nam informację o ich braku, w
innym przypadku ukaże nam w postaci tabelki.

6. Dodanie filmu do bazy danych
Za dodanie filmu do bazy danych odpowiedzialna jest funkcja dodaj_rekord(). Program
poprosi o wpisanie takich danych jak: Nazwa filmu, kategoria, rok produkcji oraz długość
filmu. Niestety przy wprowadzaniu danych trzeba uważać, aby nie wpisywać polskich znaków
(prowadzi to do poszerzenia tabeli w danym wierszu) oraz w przypadku wieloczłonowej
nazwy filmu należy wprowadzić nazwę filmu razem lub zamiast spacji użyć „_”. Może to
doprowadzić do tego że nazwa filmu może zostać podzielona na kilka kolumn.

7. Usunięcie filmu z bazy danych
Za usunięcie filmu z bazy odpowiedzialna jest funkcja usun_rekord(). Całkowicie usuwa
wszystkie dane z danego rekordu. Jeśli wpiszemy zły rekord (nie istniejący lub już usunięty)
wyświetli nam się komunikat „Brak rekordu do usunięcia”. W przypadku poprawnie
dokonanego wyboru zobaczymy „Poprawnie usunięto rekord”. Żeby można było zobaczyć
efekt należy przed usunięciem wyświetlić tabelę, a zarazem po dokonaniu operacji.

8. Zapis oraz wyjście z programu
Po wybraniu opcji numer 7 mamy możliwość zapisać nasze zmiany do pliku dzięki funkcji
zapisz_dane_do_pliku(). Plik jaki chcemy stworzyć z naszymi danymi można dowolnie
nazwać. Jeśli wszystko będzie poprawne, wyskoczy komunikat „Poprawnie zapisano do
pliku”. W tym momencie możemy być pewni że nasze dane zostały poprawnie zapisane i
wyjść bezpiecznie z terminala.

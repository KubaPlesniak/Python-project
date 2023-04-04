class Film:
    def __init__(self, tytul_: str, kategoria_: str, rok_premiera_: int, dlugosc_Filmu_: int):
        self.tytul = tytul_
        self.kategoria = kategoria_
        self.rok_premiera = rok_premiera_
        self.dlugosc_Filmu = dlugosc_Filmu_

    def print(self) -> None:
        print(f"{self.tytul:<15}{self.kategoria:<19}{self.rok_premiera:>12}{self.dlugosc_Filmu:>13}")

    def read(self, ist: str) -> bool:
        parts = ist.strip().split(" ")
        if len(parts) != 4:
            return False
        self.tytul = parts[0]
        self.kategoria = parts[1]
        self.rok_premiera = int(parts[2])
        self.dlugosc_Filmu = int(parts[3])
        return True


f = Film('tytul_', 'kategoria_', 'rok_premiera_', 'dlugosc_Filmu_')
v = []


def wczytaj_dane_z_pliku():
    lista = input("Aby wczytac dane, wpisz nazwe pliku:")

    try:
        with open(lista, "r") as ist:
            while True:
                f = Film('tytul_', 'kategoria_', 'rok_premiera_', 'dlugosc_Filmu_')
                if not f.read(ist.readline()):
                    break
                v.append(f)
    except:
        print("Blad otwarcia pliku")
        exit(-1)

    print(f"Wczytano {len(v)} rekordow")


def wypisz_dane_w_postaci_tabelki():
    if not v:
        print("Nie ma wczytanych danych z pliku")
    else:
        print("+-----+----------------+--------------------+--------------+---------------+")
        print("| lp  | tytul          | kategoria          | rok premiery | dlugosc filmu |")
        print("+-----+----------------+--------------------+--------------+---------------+")
    for i, film in enumerate(v, start=1):
        print(f"|{i:4} | {film.tytul:14} | {film.kategoria:18} | {film.rok_premiera:12} | {film.dlugosc_Filmu:10.0f} min|")
    print("+-----+----------------+--------------------+--------------+---------------+")


def porownaj_a(f1, f2):
    if f1.kategoria < f2.kategoria:
        return True
    elif f1.kategoria == f2.kategoria:
        if f1.tytul < f2.tytul:
            return True
        elif f1.tytul == f2.tytul:
            if f1.rok_premiera < f2.rok_premiera:
                return True
            elif f1.rok_premiera == f2.rok_premiera:
                if f1.dlugosc_filmu < f2.dlugosc_filmu:
                    return True
    return False


def porownaj_b(f1, f2):
    if f1.tytul < f2.tytul:
        return True
    elif f1.tytul == f2.tytul:
        if f1.kategoria < f2.kategoria:
            return True
        elif f1.kategoria == f2.kategoria:
            if f1.rok_premiera < f2.rok_premiera:
                return True
            elif f1.rok_premiera == f2.rok_premiera:
                if f1.dlugosc_Filmu < f2.dlugosc_Filmu:
                    return True
    return False


def porownaj_c(f1, f2):
    if f1.rok_premiera < f2.rok_premiera:
        return True
    elif f1.rok_premiera == f2.rok_premiera:
        if f1.kategoria < f2.kategoria:
            return True
        elif f1.kategoria == f2.kategoria:
            if f1.tytul < f2.tytul:
                return True
            elif f1.tytul == f2.tytul:
                if f1.dlugosc_Filmu < f2.dlugosc_Filmu:
                    return True
    return False


def porownaj_d(f1, f2):
    if f1.dlugosc_Filmu < f2.dlugosc_Filmu:
        return True
    elif f1.dlugosc_Filmu == f2.dlugosc_Filmu:
        if f1.kategoria < f2.kategoria:
            return True
        elif f1.kategoria == f2.kategoria:
            if f1.tytul < f2.tytul:
                return True
            elif f1.tytul == f2.tytul:
                if f1.rok_premiera < f2.rok_premiera:
                    return True
    return False


def sortuj_dane():
    if len(v) == 0:
        print("Brak wczytanych danych z pliku")
    else:
        print("Metody sortowania:")
        print("a) kategoria, tytul, rok premiera, dlugosc Filmu")
        print("b) tytul, kategoria, rok premiera, dlugosc Filmu")
        print("c) rok premiera, kategoria, tytul, dlugosc Filmu")
        print("d) dlugosc Filmu, kategoria, tytul, rok premiera")
        sortowanie = input("Wybierz opcje sortowania:")
        if sortowanie == 'a':
            v.sort(key=lambda x: x.kategoria)
        elif sortowanie == 'b':
            v.sort(key=lambda x: x.tytul)
        elif sortowanie == 'c':
            v.sort(key=lambda x: x.rok_premiera)
        elif sortowanie == 'd':
            v.sort(key=lambda x: x.dlugosc_Filmu)
        else:
            print("Niepoprawny wybór")


def wyniki_wyszukiwania(w):
    print("\nWyniki wyszukiwania\n")
    print("+-----+----------------+--------------------+--------------+---------------+")
    print("| lp  | tytul          | kategoria          | rok premiery | dlugosc Filmu |")
    print("+-----+----------------+--------------------+--------------+---------------+")
    for i, j in enumerate(w, start=1):
        print("| {:<3} | {:<14} | {:<18} | {:>12} | {:>10.0f} min|".format(i, v[j].tytul, v[j].kategoria, v[j].rok_premiera, v[j].dlugosc_Filmu))
    print("+-----+----------------+--------------------+--------------+---------------+")
    print("\n")


def szukaj():
    szukaj_opcja = input(
        "Metody wyszukiwania:\na) tytul\nb) kategoria\nc) rok premiera\nd) dlugosc Filmu\nWybierz opcje wyszukiwania:")
    szukaj_slowo = input("Wpisz slowo kluczowe:")

    w = []

    for i, film in enumerate(v):
        if szukaj_opcja == 'a':
            if film.tytul == szukaj_slowo:
                w.append(i)
        elif szukaj_opcja == 'b':
            if film.kategoria == szukaj_slowo:
                w.append(i)
        elif szukaj_opcja == 'c':
            if film.rok_premiera == int(szukaj_slowo):
                w.append(i)
        elif szukaj_opcja == 'd':
            if film.dlugosc_filmu == int(szukaj_slowo):
                w.append(i)
        else:
            break

    if len(w) == 0:
        print("Nie odznaleziono zadnych rekordow")
    else:
        wyniki_wyszukiwania(w)


def dodaj_rekord(sortowanie):
    x = len(v)
    v.append(f)
    tytul = input("Aby dodać nowy rekord, podaj tytul: ")
    v[x].tytul = tytul
    kategoria = input("kategoria: ")
    v[x].kategoria = kategoria
    rok_premiera = input("rok_premiera: ")
    v[x].rok_premiera = int(rok_premiera)
    dlugosc_filmu = input("dlugosc_Filmu: ")
    v[x].dlugosc_Filmu = int(dlugosc_filmu)

    if sortowanie == 'a':
        v.sort(key=lambda z: z.kategoria)
    elif sortowanie == 'b':
        v.sort(key=lambda z: z.tytul)
    elif sortowanie == 'c':
        v.sort(key=lambda z: z.rok_premiera)
    elif sortowanie == 'd':
        v.sort(key=lambda z: z.dlugosc_Filmu)
    print("Poprawnie dodano rekord")


def usun_rekord():
    if not v:
        print("Brak rekordow do usuniecia")
    else:
        usun = int(input("Podaj rekord do usuniecia"))
        if usun < 1 or usun > len(v):
            print("Brak rekordu do usuniecia")
        else:
            v.pop(usun - 1)
            print("Poprawnie usunieto rekord")


def zapisz_dane_do_pliku():
    wyjscie = input("Podaj nazwe pliku do ktorego chcesz zapisac dane:")

    with open(wyjscie, 'w') as ost:
        for film in v:
            ost.write(f"{film.tytul} {film.kategoria} {film.rok_premiera} {film.dlugosc_Filmu}\n")
    print("Poprawnie zapisano do pliku")


def menu():
    print()
    print("         Menu")
    print("1. Wczytaj dane z pliku")
    print("2. Wypisz dane w postaci tabelki")
    print("3. Sortuj dane")
    print("4. Wyszukaj")
    print("5. Dodaj rekord")
    print("6. Usun rekord")
    print("7. Zapisz dane do pliku")
    print("8. Koniec programu")

    n = int(input("Wybierz: "))
    print()

    return n


def main(sortowanie=None):
    while True:
        option = menu()
        if option == 1:
            wczytaj_dane_z_pliku()
        elif option == 2:
            wypisz_dane_w_postaci_tabelki()
        elif option == 3:
            sortuj_dane()
        elif option == 4:
            szukaj()
        elif option == 5:
            dodaj_rekord(sortowanie)
        elif option == 6:
            usun_rekord()
        elif option == 7:
            zapisz_dane_do_pliku()
        elif option == 8:
            exit()
        elif option:
            print("Nie wybrano polecenia")


if __name__ == '__main__':
    main()

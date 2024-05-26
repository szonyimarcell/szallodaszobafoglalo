from datetime import datetime, date, timedelta
from models import Szalloda, EgyagyasSzoba, KetagyasSzoba, Foglalas, datum_ervenyes


def read_adatok_file():
    with open('adatok.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def initial_setup(szalloda):
    szalloda.add_szoba(EgyagyasSzoba(101))
    szalloda.add_szoba(KetagyasSzoba(102))
    szalloda.add_szoba(EgyagyasSzoba(103))

    today = date.today()
    foglalasok = [
        Foglalas(szalloda.get_szoba(101), today + timedelta(days=1)),
        Foglalas(szalloda.get_szoba(102), today + timedelta(days=2)),
        Foglalas(szalloda.get_szoba(103), today + timedelta(days=3)),
        Foglalas(szalloda.get_szoba(101), today + timedelta(days=4)),
        Foglalas(szalloda.get_szoba(102), today + timedelta(days=5)),
    ]

    for foglalas in foglalasok:
        szalloda.add_foglalas(foglalas)


def main():
    read_adatok_file()

    szalloda_nev = "PyTel"
    szalloda = Szalloda(szalloda_nev)

    initial_setup(szalloda)

    print(f"Üdvözlünk a {szalloda_nev}-ban! Kérjük válasszon az alábbi menüpontokból.")

    while True:
        print("\nSzállodai Szobafoglaló Rendszer")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasz = input("Válasszon egy opciót: ")

        if valasz == '1':
            datum_str = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN): ")
            datum = datetime.strptime(datum_str, '%Y-%m-%d').date()

            if datum_ervenyes(datum):
                szabad_szobak = szalloda.get_szabad_szobak(datum)
                if szabad_szobak:
                    print("Szabad szobák:")
                    for szoba in szabad_szobak:
                        print(szoba)
                    szobaszam = int(input("Válasszon egy szobaszámot a foglaláshoz: "))
                    szoba = szalloda.get_szoba(szobaszam)
                    if szoba and szoba in szabad_szobak:
                        foglalas = Foglalas(szoba, datum)
                        ar = szalloda.add_foglalas(foglalas)
                        print(f"Sikeres foglalás: {foglalas}")
                    else:
                        print("A választott szoba nem elérhető!")
                else:
                    print("Nincs szabad szoba a megadott dátumra!")
            else:
                print("Érvénytelen dátum!")

        elif valasz == '2':
            szobaszam = int(input("Adja meg a szobaszámot: "))
            datum_str = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN): ")
            datum = datetime.strptime(datum_str, '%Y-%m-%d').date()

            if szalloda.remove_foglalas(szobaszam, datum):
                print("Foglalás lemondva!")
            else:
                print("Nincs ilyen foglalás!")

        elif valasz == '3':
            foglalasok = szalloda.list_foglalasok()
            if foglalasok:
                print("Foglalások:")
                for foglalas in foglalasok:
                    print(foglalas)
            else:
                print("Nincsenek foglalások.")

        elif valasz == '4':
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás! Próbálja újra.")


if __name__ == '__main__':
    main()
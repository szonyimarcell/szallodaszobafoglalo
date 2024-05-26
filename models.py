from abc import ABC, abstractmethod
from datetime import date

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def __str__(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

    def __str__(self):
        return f'Egyágyas szoba #{self.szobaszam}, Ár: {self.ar} HUF'

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

    def __str__(self):
        return f'Kétágyas szoba #{self.szobaszam}, Ár: {self.ar} HUF'

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def add_foglalas(self, foglalas):
        self.foglalasok.append(foglalas)
        return foglalas.szoba.ar

    def remove_foglalas(self, szobaszam, datum):
        foglalas_to_cancel = None
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                foglalas_to_cancel = foglalas
                break
        if foglalas_to_cancel:
            self.foglalasok.remove(foglalas_to_cancel)
            return True
        return False

    def get_szoba(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba
        return None

    def get_szabad_szobak(self, datum):
        foglalt_szobak = [f.szoba.szobaszam for f in self.foglalasok if f.datum == datum]
        return [szoba for szoba in self.szobak if szoba.szobaszam not in foglalt_szobak]

    def list_foglalasok(self):
        sorted_foglalasok = sorted(self.foglalasok, key=lambda x: (x.datum, x.szoba.szobaszam))
        return sorted_foglalasok

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f'{self.datum}: {self.szoba}'
def datum_ervenyes(datum):
    return datum > date.today()
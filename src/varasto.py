class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = max(0.0, tilavuus)

        self.saldo = 0.0
        if 0 < alku_saldo <= tilavuus:
            # mahtuu
            self.saldo += alku_saldo
        elif alku_saldo > self.tilavuus:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = self.tilavuus

    # huom: ominaisuus voidaan myös laskea eikä sille tarvita erillistä kenttää
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"

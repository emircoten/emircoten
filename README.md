# Proje Hesaplama Kodu

class EvYatirim:
    def __init__(self, birikim_miktari, kredi_faizi, kredi_suresi, pesinat_orani, ev_fiyati, kira):
        self.birikim_miktari = birikim_miktari
        self.kredi_faizi = kredi_faizi
        self.kredi_suresi = kredi_suresi
        self.pesinat_orani = pesinat_orani
        self.ev_fiyati = ev_fiyati
        self.kira = kira
        self.ev_sayisi = 0
        self.kira_getirisi = 0

    def ev_al(self):
        pesinat = self.ev_fiyati * self.pesinat_orani
        kredi_tutarı = self.ev_fiyati - pesinat
        aylik_odeme = kredi_tutarı / (self.kredi_suresi * 12)
        self.birikim_miktari -= pesinat

        for _ in range(self.kredi_suresi * 12):
            self.birikim_miktari += self.kira - aylik_odeme
            self.kira_getirisi += self.kira
            if self.birikim_miktari >= (self.ev_fiyati * 0.2):
                self.ev_sayisi += 1
                self.birikim_miktari -= (self.ev_fiyati * 0.2)

def senaryo_hesapla(birikim_miktari, kredi_faizi, kredi_suresi, pesinat_orani, ev_fiyati, kira):
    ev_yatirim = EvYatirim(birikim_miktari, kredi_faizi, kredi_suresi, pesinat_orani, ev_fiyati, kira)
    ev_yatirim.ev_al()
    return ev_yatirim.ev_sayisi, ev_yatirim.kira_getirisi

# Örnek senaryo
birikim_miktari = 3000
kredi_faizi = 0
kredi_suresi = 15
pesinat_orani = 0.2
ev_fiyati = 1250000
kira = 8000

ev_sayisi, kira_getirisi = senaryo_hesapla(birikim_miktari, kredi_faizi, kredi_suresi, pesinat_orani, ev_fiyati, kira)
print(f"Hakan'ın 65 yaşına geldiğinde {ev_sayisi} adet evi olacak ve toplam kira getirisi {kira_getirisi} ₺ olacaktır.")

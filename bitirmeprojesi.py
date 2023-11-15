
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

# Streamlit Arayüz Kodu

import streamlit as st

st.title("Ev Yatırımı Senaryo Hesaplama")

birikim_miktari = st.slider("Aylık Birikim Miktarı (₺)", min_value=1000, max_value=5000, step=500, value=3000)
kredi_faizi = st.slider("Kredi Faizi (%)", min_value=0, max_value=10, step=1, value=0)
kredi_suresi = st.slider("Kredi Süresi (Yıl)", min_value=5, max_value=30, step=1, value=15)
pesinat_orani = st.slider("Peşinat Oranı", min_value=0.1, max_value=0.5, step=0.05, value=0.2)
ev_fiyati = st.slider("Ev Fiyatı (₺)", min_value=500000, max_value=2000000, step=100000, value=1250000)
kira = st.slider("Kira (₺)", min_value=5000, max_value=15000, step=1000, value=8000)

if st.button("Hesapla"):
    ev_sayisi, kira_getirisi = senaryo_hesapla(birikim_miktari, kredi_faizi, kredi_suresi, pesinat_orani, ev_fiyati, kira)
    st.success(f"Hakan'ın 65 yaşına geldiğinde {ev_sayisi} adet evi olacak ve toplam kira getirisi {kira_getirisi} ₺ olacaktır.")


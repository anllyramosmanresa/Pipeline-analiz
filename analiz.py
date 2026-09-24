import pandas as pd

# CSV dosyasını okuma
veri = pd.read_csv("varyantlar.csv", header=None, names=["Kromozom", "Pozisyon", "Referans", "Alternatif", "Kalite"])

# İlk 5 satırı görme
print(veri.head(5))

# Temel istatistikleri görme
print(veri.describe())

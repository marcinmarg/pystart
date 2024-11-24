import pandas as pd

# Ścieżka do pliku Excel
plik_excel = r'C:\temp\warszawa_praca.xlsx'
data = pd.read_excel(plik_excel, sheet_name='Arkusz1')

# Wczytanie danych z Excela
dane = pd.read_excel(plik_excel)

# Zapisanie do pliku TXT z oddzieleniem przecinkami
plik_txt = r'C:\temp\plik.txt'
dane.to_csv(plik_txt, sep=',', index=False)

print(f"Dane zapisano do pliku {plik_txt}")

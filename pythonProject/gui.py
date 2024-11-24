import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd


def wybierz_plik():
    # Otwórz okno dialogowe do wyboru pliku
    sciezka_pliku = filedialog.askopenfilename(
        title="Wybierz plik Excel",
        filetypes=(("Pliki Excel", "*.xlsx *.xls"), ("Wszystkie pliki", "*.*"))
    )
    if sciezka_pliku:
        etykieta_sciezka.config(text=f"Wybrany plik: {sciezka_pliku}")
        try:
            # Wczytaj plik Excel za pomocą pandas
            dane = pd.read_excel(sciezka_pliku)
            wyswietl_dane(dane)
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się wczytać pliku.\n{e}")


def wyswietl_dane(dane):
    # Wyświetl dane w nowym oknie
    okno_danych = tk.Toplevel(root)
    okno_danych.title("Dane z pliku Excel")

    # Tworzymy widżet tekstowy, aby pokazać dane
    tekst = tk.Text(okno_danych, wrap="none")
    tekst.insert("1.0", dane.to_string(index=False))  # Konwertujemy dane na tekst
    tekst.pack(fill="both", expand=True)

    # Dodaj pasek przewijania
    scrollbar = tk.Scrollbar(okno_danych, command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")


# Tworzenie głównego okna
root = tk.Tk()
root.title("Wczytaj plik Excel")

# Etykieta i przycisk wyboru pliku
etykieta_sciezka = tk.Label(root, text="Nie wybrano pliku.")
etykieta_sciezka.pack(pady=10)

przycisk_wybierz = tk.Button(root, text="Wybierz plik Excel", command=wybierz_plik)
przycisk_wybierz.pack(pady=10)

# Uruchomienie pętli głównej
root.mainloop()

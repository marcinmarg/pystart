import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

# Wczytanie danych
df = pd.read_csv('nazwa_pliku.csv')

# Wyświetlenie pierwszych kilku wierszy danych
print(df.head())

# Podstawowe statystyki opisowe
print(df.describe())

# Wykres rozkładu zmiennych
sns.pairplot(df)
plt.show()

# Podział danych na zbiór treningowy i testowy
X = df.drop('target_column', axis=1)
y = df['target_column']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

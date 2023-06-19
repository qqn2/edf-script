import pandas as pd

# Lire le fichier CSV en spécifiant seulement les colonnes 1 et 2 et l'encodage
df = pd.read_csv("C:\\Users\\3600X-2700\\Desktop\\test.csv", usecols=[0, 1], delimiter=';', encoding='latin-1', dtype=str)

dates = []
puissances = []

# Renommer les colonnes
df.columns = ['Date', 'Puissance']

# Obtenir le nombre total de lignes du DataFrame
#N = df.shape[0]
N = 15564
# Parcourir les lignes du dataframe jusqu'à la ligne N
for index, row in df.iterrows():
    if index >= N:
        break
    # Ignorer les lignes où la deuxième colonne est vide
    if pd.isnull(row['Puissance']):
        continue
    else:
        # Ajouter la date à la liste des dates
        dates.append(row['Date'])
        # Ajouter la puissance à la liste des puissances
        puissances.append(row['Puissance'])

# Créer un nouveau dataframe avec les dates et les puissances
df_final = pd.DataFrame({'Date': dates, 'Puissance': puissances})

# Convertir la colonne 'Date' en type datetime
df_final['Date'] = pd.to_datetime(df_final['Date'], format='%H:%M:%S', errors='coerce')

# Convertir la colonne 'Puissance' en type numérique (int ou float)
df_final['Puissance'] = pd.to_numeric(df_final['Puissance'], errors='coerce')

# Afficher le DataFrame
print(df_final)

# Agréger les données par heure et calculer la somme de la puissance pour chaque heure
df_hourly = df_final.groupby(pd.Grouper(key='Date', freq='30min'))['Puissance'].sum()

# Convertir les heures en objets datetime pour pouvoir les trier
df_hourly.index = pd.to_datetime(df_hourly.index, format='%H').time

# Trier les résultats par date
df_hourly = df_hourly.sort_index()

# Afficher les résultats
print(df_hourly)
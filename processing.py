import pandas as pd



file_name = 'C:\\Users\\PBL_Basia\\Documents\\My scripts\\EV_chargers\\data\\sample_excel_reports_2\\report_20230912_152810.xlsx'

dataframe = pd.read_excel(file_name)
df_reversed = dataframe[::-1]

df_reversed['Zewnętrzny numer ID karty '].unique()


#DataFrame without few columns ('Data faktury', 'Event', 'Informacje uzupełniające', 'Moc (kW)',
#        'Energia (kWh)', 'Czas trwania transakcji')

df_without_clients_ID = df_reversed.drop(['Zewnętrzny numer ID karty ', 'Wewnętrzny numer ID karty ','Numer ID klienta', 'Nazwa'], axis=1)



# Nazwy kolumn: ['Data faktury', 'Event', 'Informacje uzupełniające', 'Moc (kW)',
#        'Energia (kWh)', 'Czas trwania transakcji',
#        'Zewnętrzny numer ID karty ', 'Wewnętrzny numer ID karty ',
#        'Numer ID klienta', 'Nazwa']

# Informacje uzupełniające: np.: 
#     'Channel:1, Transaction ID: 111441108, Meter values count:1: , Timestamp:2023-08-25T09:37:29Z, Values:Energy.Active.Import.Register (Outlet|Sample.Periodic|Raw): 7972915.0 Wh, ',
#     'Channel:1, Transaction ID: 111441108, Meter values count:1: , Timestamp:2023-08-25T09:40:29Z, Values:Energy.Active.Import.Register (Outlet|Sample.Periodic|Raw): 7975398.0 Wh, ',


# Odwrócic kolejnosc danych
# Wykres mocy na podstawie kolumny Moc (kw)
# przykladowa tabela zawiera tylko dane dla jednej ładowarki (typ Delta); sa jeszcze ladowarki dwoch typow (maja inaczej skonstruowane raporty, to ladowarki ABB Terra i ABB EVlunic) wszystkich ładowarek jest w sumie 50; musialabym zrobic trzy wersje 
# dodac do analizy licznik calego zakladu
# ? czytanie wartosci mocy co 15 minut? Dopytać


# =============================================================================
# 
# Rodzaje statusów:
    
# 'WebSocket rozłączony', 
# 'WebSocket połączony', 
# 'Gotowe',
# 'Powiadomienie o statusie OCPP', 
# 'Heartbeat OCPP',
# 'Autoryzacja OCPP', 
# 'Przygotowanie transakcji', 
# 'Ładowanie ',
# 'Rozpoczęcie transakcji OCPP', 
# 'Odczyt licznika (OCPP)',
# 'Bateria pełna', 
# 'Kończenie transakcji', 
# 'Rozpocznij transakcję',
# 'Blokada', 
# 'Wystąpił błąd', 
# 'Pobranie diagnostyki OCPP',
# 'Uruchamianie diagnostyki', 
# 'Powiadomienie o diagnostyce OCPP',
# 'Reset OCPP', 
# 'Reset zaakceptowany', 
# 'Powiadomienie OCPP',
# 'Błąd komunikacji z pojazdem', 
# 'Ładowanie (brak dostępnej mocy)',
# 'Inny błąd', 
# 'Brak akceptacji karty', 
# 'Brak komunikacji',
# 'Zdalne rozpoczęcie transakcji OCPP',
# 'Zdalne rozpoczęcie transakcji zaakceptowane.'

# =============================================================================



df_reversed["Event"].unique()

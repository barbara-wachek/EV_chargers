import pandas as pd



file_name = 'C:\\Users\\PBL_Basia\\Documents\\My scripts\\EV_chargers\\data\\sample_excel_reports_2\\report_20230912_152810.xlsx'

dataframe = pd.read_excel(file_name)
df_reversed = dataframe[::-1]


# Odwrócic kolejnosc danych
# Wykres mocy na podstawie kolumny Moc (kw)
# przykladowa tabela zawiera tylko dane dla jednej ładowarki (typ Delta); sa jeszcze ladowarki dwoch typow (maja inaczej skonstruowane raporty, to ladowarki ABB Terra i ABB EVlunic) wszystkich ładowarek jest w sumie 50; musialabym zrobic trzy wersje 
# dodac do analizy licznik calego zakladu


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

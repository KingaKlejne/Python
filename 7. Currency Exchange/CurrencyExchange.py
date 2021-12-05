import requests
import pandas as pd

def GetData():
    response = requests.get('http://api.nbp.pl/api/exchangerates/tables/a?format=json')
    data = response.json()[0]
    df = pd.DataFrame(data)
    df['currency'] = df['rates'].map(lambda x: x['currency'])
    df['code'] = df['rates'].map(lambda x: x['code'])
    df['mid'] = df['rates'].map(lambda x: x['mid'])
    df = df.drop(["rates"], axis = 1)
    return df


def CurrencyExchange(df):
    try:
        kod = input("Jaką walutę potrzebujesz?\nPodaj skrót, np. dla euro - 'EUR'\n").upper()
        kwota = int(input("Jaką kwotę potrzebujesz?\n"))
        kod = str(kod)
        wybrana_waluta = df[df['code'] == kod]
        waluta = wybrana_waluta['currency'].values[0]
        wybrana_waluta = float(wybrana_waluta['mid'].to_numpy())
        print(f"Za {kwota} {waluta} '{kod}' musisz zapłacić {round(wybrana_waluta * kwota,2)} zł.")
    except TypeError:
        print("Podano złe dane")

CurrencyExchange(GetData())
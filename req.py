import requests

def getData(language, chapter, verses):
    response = requests.get(f"https://gita-api.vercel.app/{language}/verse/{chapter}/{verses}")
    response.raise_for_status()
    return response.json()

poke = getData("tel",2,18)
print(poke)
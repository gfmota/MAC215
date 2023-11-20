import requests
from PIL import Image
import os

POKEMON_COUNT = 1017
POKE_API_ROUTE = "https://pokeapi.co/api/v2/pokemon/"

for i in range(1, POKEMON_COUNT):
    json_res = requests.get(POKE_API_ROUTE + str(i))
    pokemon = json_res.json()
    pokemon_sprite_path = pokemon["sprites"]["front_default"]
    pokemon_type = pokemon["types"][0]["type"]["name"]
    img_res = requests.get(pokemon_sprite_path, stream=True)
    img = Image.open(img_res.raw)
    if not os.path.isdir(pokemon_type):
        os.mkdir(pokemon_type)
    filename = pokemon_type + "/" + str(i) + ".png"
    img.save(filename)
    print(str(i) + "/" + str(POKEMON_COUNT))
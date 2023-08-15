#!/usr/bin/python3

import requests
import pandas as pd

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=2000")
    pokemon = pokemon.json()
    df = pd.DataFrame(pokemon)
    # Loop through data, and print pokemon names


    print(f"Total number of Pokemon returned: {len(df)}")
    print(df)
if __name__ == "__main__":
    main()

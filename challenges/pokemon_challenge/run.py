#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    #print(pokeapi)

    #1
    pokIMG=pokeapi['sprites']['front_default']
    print((pokIMG))

    #2
    move_dicts=pokeapi['moves']

    for d in move_dicts:
        print(d['move']['name'])

    #3
    game_dicts=pokeapi['game_indices']
    print('Solve-1 total count:',len(game_dicts))
    c=0
    for i in game_dicts:
        c+=1
    print('Solve-2 total count:',c)

    #4
    pokeImage = requests.get(pokIMG)
    
    with open('/home/student/static/' +pokeapi['name'] + '.png', 'wb') as f:
        f.write(pokeImage.content) 

main()
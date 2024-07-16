import random
import time
import os
from engine.pkm import Pokemon

#Nome do player
jogador = input("Olá, qual é mesmo seu nome?")
#Escolhe um pokemon selvagem aleatório
def create_random_pokemon():
    pokemons = [
        {"name": "Bulbasaur", "nickname": "", "lvl": 5, "hpt": 45, "hp": 45},
        {"name": "Charmander", "nickname": "", "lvl": 5, "hpt": 39, "hp": 39},
        {"name": "Squirtle", "nickname": "", "lvl": 5, "hpt": 44, "hp": 44},
        {"name": "Pikachu", "nickname": "", "lvl": 5, "hpt": 35, "hp": 35}
    ]
    chosen = random.choice(pokemons)
    return Pokemon(name=chosen["name"], nickname=chosen["nickname"], lvl=chosen["lvl"], hpt=chosen["hpt"], hp=chosen["hp"])

#Easter egg do Missingno
missingno = Pokemon('MissingNo', '', 99, 111, 111)
def error():
    messages = [
        f"Os olhos de {player_pokemon} brilham com uma luz vermelha por um momento...",
        "Você ouve um sussurro: 'Saia daqui...'",
        "Uma sombra passa rapidamente pelo canto do seu olho...",
        "O ar ao seu redor fica gelado...",
        "Você vê um reflexo estranho nos olhos do seu Pokémon...",
        "Um riso sombrio ecoa à distância...",
        "Seu Pokémon parece estar olhando algo atrás de você..."
    ]
    print(random.choice(messages))
    time.sleep(2) 
    print("OLHE PARA TRÁS, EU DISSE OLHE PARA TRÁS")
def battle_menu(player, opponent):
    #"loop" do jogo
    while player.hp > 0 and opponent.hp > 0:
        print("\nO que você quer fazer?")
        print("1. Atacar")
        print("2. Curar")
        print("3. Fugir")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            damage = random.randint(5, 10)
            opponent.damage(damage)
            print(f"Você causou {damage} de dano em {opponent.nickname}!")
        elif choice == "2":
            heal = random.randint(5, 10)
            player.heal(heal)
            print(f"Você curou {heal} de HP!")
        elif choice == "3":
            print("Você fugiu da batalha!")
            return
        else:
            print("Escolha inválida!")
            continue

        if opponent.hp > 0:
            damage = random.randint(5, 10)
            player.damage(damage)
            print(f"{opponent.nickname} causou {damage} de dano em você!")

        print(f"\n{player.nickname} - HP: {player.hp}/{player.hpt}")
        print(f"{opponent.nickname} - HP: {opponent.hp}/{opponent.hpt}")

    if player.hp <= 0:
        print(f"Pokemon de {jogador} foi derrotado!")
    elif opponent.hp <= 0:
        print(f"{jogador} derrotou {opponent.nickname}!")

if __name__ == "__main__":
    player_pokemon = Pokemon(name="Pikachu", nickname="Bono Vox", lvl=5, hpt=35, hp=35)
    if jogador != 'Luis Alarcon':
        opponent_pokemon = create_random_pokemon()
    else:
        opponent_pokemon = missingno
    print(f"{jogador} foi desafiado por um {opponent_pokemon.name} selvagem!")
    print(opponent_pokemon)

    battle_menu(player_pokemon, opponent_pokemon)
    if jogador == 'Luis Alarcon':
        time.sleep(3)
        os.system('CLS')
        error()
    else:
        pass
import random

winner = False
players = {}
players_number = None
special_fields_possitive = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    78: 98,
    87: 94,
}

special_fields_negative = {
    16: 6,
    92: 87,
    95: 75,
    99: 80,
    74: 53,
    46: 25,
    49: 11,
    64: 60,
    62: 19,
}

# Number of players
while players_number == None or players_number <= 1:
    try:
        players_number = int(input("Zadejte počet hráčů:\n"))
    except ValueError:
        print("Nezadali jste celé číslo.")

# Create player names
for i in range(1, players_number + 1):
    player_name = input(f"Zadjte jméno hráče č. {i}:\n")
    players[player_name] = 0

print(players)


# Function roll the dice
def roll_dice(player_name: str) -> int:
    """
    Function returning dice number
    """
    number = random.randint(1, 6)
    while number % 6 == 0:
        number += random.randint(1, 6)
        print(f"Výborně! {player_name} hodil jsi 6, házíš ještě jednou!")
    return number


# Check special field procedure
def check_field(player_name: str, move_points: int) -> None:
    global winner
    # If player score more than 100 points
    if players[player_name] > 100:
        players[player_name] -= move_points
        print(
            f"Hráč {player_name} hodil {move_points} ale musí hodit {100-players[player_name]}, nebo méně."
        )
    # If winner player score 100 points
    elif players[player_name] == 100:
        print(f"Gratulujeme! Hráč {player_name} hodil {move_points} a vyhrál!!!")
        winner = True

    else:
        # If player move to positive field
        if players[player_name] in special_fields_possitive:
            players[player_name] = special_fields_possitive[players[player_name]]
            print(
                f"Výborně hráči {player_name}! Hodil jsi {move_points} a posunul jsi se na políčko se žebříkem, tím pádem postupuješ na políčko {players[player_name]}"
            )

        # If player move to negative field
        elif players[player_name] in special_fields_negative:
            players[player_name] = special_fields_negative[players[player_name]]
            print(
                f"Smůla! Hráč {player_name} hodil {move_points} ale stoupnul na políčko s hadí hlavou a vrací se na políčko {players[player_name]}"
            )

        else:
            check_occupied_field(player_name, move_points)


# Check occupied field procedure
def check_occupied_field(player_name: str, move_points: int) -> None:
    occupier = None
    for name, points in players.items():
        if points == players[player_name] and name != player_name:
            occupier = name
            break

    if occupier:
        print(
            f"Políčko {players[player_name]} je již obsazeno hráčem {occupier}. Hráč {occupier} se vrací o jedno pole zpět."
        )
        players[occupier] -= 1
        check_field(player_name, move_points)
    else:
        print(
            f"Hráči {player_name}, hodil jsi {move_points} a postupuješ na políčko {players[player_name]}"
        )


def main() -> None:
    # Main loop
    global winner
    while not winner:
        for player_name, player_possition in players.items():
            print(
                f"Na řadě je hráč {player_name}, který stojí na poli číslo {player_possition}.\n"
            )
            option = input("Zadejte Enter pro hod kostkou, 0 pro ukončení hry.\n")

            if option == 0:
                print("Hra byla ukončena.")
                winner = True
                break
            else:
                move_points = roll_dice(player_name)
                players[player_name] += move_points
                check_field(player_name, move_points)
                if winner:
                    break


if __name__ == "__main__":
    main()

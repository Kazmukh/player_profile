def show_player(player):
    print("Игрок:", player["name"])
    print("Здоровье:", player["health"])
    print("Очки:", player["score"])


def add_score(player, points):
    if points <= 0:
        print("Очки должны быть положительными")
        return
    player["score"] += points


def take_damage(player, damage):
    if damage <= 0:
        print("Урон должен быть положительным")
        return

    player["health"] -= damage

    if player["health"] < 0:
        player["health"] = 0


def read_int(prompt):
    text = input(prompt).strip()
    try:
        return int(text)
    except ValueError:
        print("Нужно целое число")
        return None


def choose_player(players):
    number = read_int("Номер игрока (1-" + str(len(players)) + "): ")
    if number is None:
        return None
    if number < 1 or number > len(players):
        print("Нет игрока с таким номером")
        return None
    return players[number - 1]


def find_leaders(players):
    if len(players) == 0:
        return []

    best = players[0]["score"]
    for player in players:
        if player["score"] > best:
            best = player["score"]

    leaders = []
    for player in players:
        if player["score"] == best:
            leaders.append(player)
    return leaders


def show_leaders(players):
    leaders = find_leaders(players)
    if len(leaders) == 1:
        print("Лидер по очкам:")
    else:
        print("Лидеры по очкам (равенство):")
    for player in leaders:
        print(" ", player["name"], "—", player["score"])


def main():
    players = [
        {"name": "Айдар", "health": 100, "score": 0},
        {"name": "Алина", "health": 80, "score": 15},
        {"name": "Данияр", "health": 90, "score": 10},
    ]
    current = players[0]  # выбранный игрок

    while True:
        print()
        print("Текущий игрок:", current["name"])
        print("1 — профиль, 2 — очки, 3 — урон,")
        print("4 — выбрать игрока, 5 — все игроки, 6 — лидеры, 0 — выход")
        choice = input("Команда: ").strip()

        if choice == "1":
            show_player(current)
        elif choice == "2":
            amount = read_int("Сколько очков добавить? ")
            if amount is not None:
                add_score(current, amount)
        elif choice == "3":
            damage = read_int("Сколько урона нанести? ")
            if damage is not None:
                take_damage(current, damage)
        elif choice == "4":
            selected = choose_player(players)
            if selected is not None:
                current = selected
        elif choice == "5":
            for player in players:
                show_player(player)
                print()
        elif choice == "6":
            show_leaders(players)
        elif choice == "0":
            break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()

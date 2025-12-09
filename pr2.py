import random

inventory = [] 
keys_collected = set()  
rooms = {
    "hall": {"description": "Вы находитесь в зале. Здесь темно и жутко.", "key_required": False},
    "kitchen": {"description": "Вы находитесь на кухне. В воздухе витает запах еды.", "key_required": True},
    "library": {"description": "Вы в библиотеке. Здесь множество книг и тишина.", "key_required": False},
    "dungeon": {"description": "Вы находитесь в подземелье. Повсюду страшные звуки.", "key_required": True},
}
monsters = ["огр", "вампир", "зомби", "дракон", "гоблин"]  
weapons = ["меч", "лук", "арбалет", "копье"]  
puzzles_solved = 0  

def show_inventory():
    if inventory:
        print("Ваш инвентарь:", ", ".join(inventory))
    else:
        print("Ваш инвентарь пуст.")

def add_item(item):
    if item not in inventory:
        inventory.append(item)
        print(f"{item} добавлен в ваш инвентарь.")
    else:
        print(f"{item} уже находится в вашем инвентаре.")

def level_one():
    print("\nУровень 1: Найдите ключи, чтобы открыть дверь.")
    print(rooms["hall"]["description"])
    while True:
        action = input("Что вы хотите сделать? (взять ключи, выход): ").lower()
        if action == "взять ключи":
            add_item("ключи")
            keys_collected.add("ключи")
        elif action == "выход":
            if "ключи" in inventory:
                print("Вы открыли дверь и переходите на следующий уровень.")
                break
            else:
                print("Вы не можете выйти, так как у вас нет ключей.")
        else:
            print("Неизвестная команда.")

def level_two():
    print("\nУровень 2: Вы встречаете монстра!")
    monster = random.choice(monsters)
    print(f"Это {monster}!")

    while True:
        action = input("Что вы хотите сделать? (попытаться сбежать, использовать оружие, осмотреться): ").lower()
        if action == "попытаться сбежать":
            print("Вы успешно сбежали от монстра!")
            break
        elif action == "использовать оружие":
            if "меч" in inventory:
                print("Вы используете меч и побеждаете монстра!")
                break
            if "лук" in inventory:
                print("Вы используете лук и побеждаете монстра!")
                break
            if "арбалет" in inventory:
                print("Вы используете арбалет и побеждаете монстра!")
                break
            if "копье" in inventory:
                print("Вы используете копье и побеждаете монстра!")
                break
            else:
                print("У вас нет оружия для защиты.")
        elif action == "осмотреться":
            print("Вы видите, что в комнате есть разные предметы.")
            item_found = random.choice(weapons)
            add_item(item_found)
        else:
            print("Неизвестная команда.")

def level_three():
    print("\nУровень 3: Вам нужно разгадать загадку, чтобы выбраться.")
    print("Загадка: Я всегда впереди, но никогда не могу быть пойман. Что я?")

    while True:
        answer = input("Ваш ответ: ").lower()
        if answer == "будущее":
            print("Вы разгадали загадку и выбрались из замка! Поздравляем!")
            global puzzles_solved
            puzzles_solved += 1
            break
        else:
            print("Неверный ответ. Попробуйте еще раз.")

def level_four():
    print("\nУровень 4: Вы находитесь в библиотеке. Ищите древнюю книгу.")
    print(rooms["library"]["description"])

    while True:
        action = input("Что вы хотите сделать? (поиск книги, выход): ").lower()
        if action == "поиск книги":
            if "ключи" in inventory:
                add_item("древняя книга")
                print("Вы нашли древнюю книгу!")
                break
            else:
                print("Вам нужно было взять ключи из зала, чтобы найти книгу.")
        elif action == "выход":
            print("Вы можете выйти только после нахождения книги.")
        else:
            print("Неизвестная команда.")

def game_status():
    print("\nСтатус игры")
    show_inventory()
    print(f"Собранные ключи: {', '.join(keys_collected)}")
    print(f"Разгадано головоломок: {puzzles_solved}")
    print("----------------------")

def main():
    print("Добро пожаловать в 'Подземелья и Драконы'!\n")
    
    level_one()
    game_status() 
    level_two()
    game_status() 
    level_three()
    game_status() 
    level_four()
    game_status() 
    
    print("Спасибо за игру!")

if __name__ == "__main__":
    main()
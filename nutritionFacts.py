fruits = [
    {"apple": "130"},
    {"avocado": "50"},
    {"banana": "110"},
    {"cantaloupe": "50"},
    {"grapefruit": "60"},
    {"grapes": "90"},
    {"melon": "50"},
    {"kiwifruit": "90"},
    {"lemon": "15"},
    {"lime": "20"},
    {"nectarine": "60"},
    {"orange": "80"},
    {"peach": "60"},
    {"pear": "100"},
    {"pineapple": "50"},
    {"plums": "70"},
    {"strawberries": "50"},
    {"cherries": "100"},
    {"tangerine": "50"},
    {"watermelon": "80"},
]

query = input("Item: ").lower()

for fruit in fruits:
    if query in fruit:
        print("Calories:", fruit[query])
"""
HAM I 100
Ham I 100
Ham O 100
Butter I 50
Butter O 10
Butter O 10
"""
inventory = {}

while True:
    try:
        inputs = input().split(" ")
        item, action, quantity = inputs[0].lower(), inputs[1], int(inputs[2])
        if item not in inventory:
            inventory[item] = 0
        if action == "I":
            inventory[item] += quantity
        elif action == "O":
            inventory[item] -= quantity
    except:
        break

for item, quantity in inventory.items():
    print(f"{item} {quantity}")

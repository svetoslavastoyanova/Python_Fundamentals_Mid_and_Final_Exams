number_of_heroes = int(input())
heroes_hp = {}
heroes_mp = {}
max_hp = 100
max_mp = 200
line = input()
for i in range(number_of_heroes):
    tokens = line.split(" ")
    hero = tokens[0]
    hit_points = int(tokens[1])
    mana_points = int(tokens[2])

    if hero not in heroes_hp and hero not in heroes_mp:
        heroes_hp[hero] = hit_points
        heroes_mp[hero] = mana_points

    line = input()

while line != "End":
    tokens = line.split(" - ")
    command = tokens[0]
    if command == "CastSpell":
        hero_name = tokens[1]
        mp_needed = int(tokens[2])
        spell_name = tokens[3]
        if heroes_mp[hero_name] >= mp_needed:
            heroes_mp[hero_name] -= mp_needed
            print(f"{hero_name} has successfully cast ViewEarth and now has ")
            print(f"{heroes_mp[hero_name]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        hero_name = tokens[1]
        damage = int(tokens[2])
        attacker = tokens[3]
        if heroes_hp[hero_name] <= 0:
            print(f"{hero_name} has been killed by {attacker}!")
        elif heroes_hp[hero_name] >= damage:
            heroes_hp[hero_name] -= damage
            print(f"{hero_name} was hit for 66 HP by Orc and now has {heroes_hp[hero_name]} HP")
            print(f"left!")

    elif command == "Recharge":
        hero_name = tokens[1]
        amount = int(tokens[2])
        if (amount + heroes_mp[hero_name]) >= max_mp:
            diff = max_mp - heroes_mp[hero_name]
            heroes_mp[hero_name] += diff
        else:
            heroes_mp[hero_name] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif command == "Heal":
        hero_name = tokens[1]
        amount = int(tokens[2])
        if (amount + heroes_hp[hero_name]) >= max_mp:
            diff = max_hp - heroes_mp[hero_name]
            heroes_hp[hero_name] += diff
        else:
            heroes_hp[hero_name] += amount
        print(f"{hero_name} recharged for {amount} MP!")
    line = input()

for key, value in heroes_hp.items():
    print(key)
    print(f"HP:  {value}")
for value in heroes_mp.values():
    print(f"MP:  {value}")







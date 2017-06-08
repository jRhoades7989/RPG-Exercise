


magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

magic_color = [bcolors.FAIL, bcolors.OKYELLOW, bcolors.OKBLUE]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)


running = True

def prompt_restart():
    global running

    while running:
        choice = input("Would you like to play again?: ")
        if (str.lower(choice) == "yes"):
            reset_game()
            break
        elif str.lower(choice) == "no":
            print("Thank you for playing!")
            running = False
        else:
            print('Please select "yes" or "no"')
            continue
    return running

def reset_game():
    enemy.hp = enemy.maxhp
    enemy.mp = enemy.maxmp
    player.hp = player.maxhp
    player.mp = player.maxmp
    print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!"
          + bcolors.ENDC)
    
def choose_spell():
        print("======================================")
        player.choose_magic()
        spell = None
        while spell == None:
            choice_spell = input("Choose a spell: ")
            if (choice_spell == "1") or (str.lower(choice_spell) == "fire"):
                spell = 0
            elif (choice_spell == "2") or (str.lower(choice_spell) == "thunder"):
                spell = 1
            elif (choice_spell == "3") or (str.lower(choice_spell) == "blizzard"):
                spell = 2
            else:
                print("That is not a valid spell. Try again")
                continue
        return spell


print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)


while running:
    print("======================================")
    player.choose_action()
    

    
    choice = input("Choose an action: ")

    if (choice == "1") or (str.lower(choice) == "attack"):
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        if enemy.hp > 0:
            print("You dealt", dmg, "points of damage! the enemy has",
                  enemy.hp, "hit points left")
        else:
            enemy.hp = 0
            print("You dealt" + bcolors.BOLD + bcolors.FAIL, dmg, bcolors.ENDC +
                  "points of damage! the enemy has been defeated")
            prompt_restart()
            continue
    elif (choice == "2") or (str.lower(choice) == "magic"):
        spell = choose_spell()
        spell_name = player.get_spell_name(spell)
        magic_damage = player.generate_spell_damage(spell)
        mp_left = player.mp
        player.use_mp(player.get_mp_cost(spell))

        if player.mp == 0:
            player.mp = mp_left
            print("You are low on mp! You cannot cast that spell.")
            continue
        else:
            enemy.take_damage(magic_damage)
            if enemy.hp > 0:
                print("You attack it with " + magic_color[spell] + bcolors.BOLD
                      + spell_name + bcolors.ENDC + " and deal", magic_damage, 
                      "points of damage!")
            else:
                enemy.hp = 0
                print("You attack it with " + magic_color[spell] + bcolors.BOLD
                      + spell_name + bcolors.ENDC + " and deal", magic_damage, 
                      "points of damage!")
                prompt_restart()

        
    elif (str.lower(choice) == "quit") or (str.lower(choice) == "exit"):
        print("Thank you for playing!")
        running = False
        continue
    elif (str.lower(choice) == "check hp"):
        print(player.hp)
        continue
    elif (str.lower(choice) == "check mp"):
        print(player.mp)
        continue
    elif (str.lower(choice) == "check maxmp"):
        print(player.maxmp)
        continue
    else:
        print("That is not a valid option. Try again.")
        continue

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    if player.hp > 0:
        print("Enemy attacks for" + bcolors.BOLD + bcolors.FAIL, enemy_dmg,
              bcolors.ENDC + "points of damage! You have", player.hp,
              "hit points left.")
    else:
        player.hp = 0
        print("Enemy attacks for", enemy_dmg, "points of damage! You are "
              "defeated.")
        prompt_restart()



from classes.game import Person, bcolors


magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

magic_color = [bcolors.FAIL, bcolors.OKYELLOW, bcolors.OKBLUE]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)


running = True


print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)


while running:
    print("======================================")
    player.choose_action()
    

    
    index = None

    while(index == None):
        
        choice = input("Choose an action: ")

        if (choice == "1") or (str.lower(choice) == "attack"): 
            index = 0
        elif (choice == "2") or (str.lower(choice) == "magic"):
            index = 1
            print("======================================")
            player.choose_magic()
            
            i = None
            while(i == None):
                choice_spell = input("Choose a spell: ")
                if (choice_spell == "1") or (str.lower(choice_spell) == "fire"):
                    i = 0
                elif (choice_spell == "2") or (str.lower(choice_spell) == "thunder"):
                    i = 1
                elif (choice_spell == "3") or (str.lower(choice_spell) == "blizzard"):
                    i = 2
                else:
                    print("That is not a valid spell. Try again")
                    continue

            choice_spell = player.get_spell_name(i)
            
            print("You attack it with " + magic_color[i] + bcolors.BOLD +
                  choice_spell + bcolors.ENDC)
        else:
            print("That is not a valid option. Try again.")
            continue


    print("You chose", index)
    running = False


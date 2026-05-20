import random 

USER_HEALTH = 50
ENEMY_HEALTH = 50 
NUMBER_POTION = 3
SKIP_TURN = False

while True : 
    if SKIP_TURN : 
        print("Vous passez votre tour...")
        SKIP_TURN = False  
    else : 
        user_choice = " "
        while user_choice not in ["1", "2"] : 
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if user_choice == "1" : 
            your_attack = random.randint(5, 10)
            ENEMY_HEALTH -= your_attack
            print(f"Vous avez infligé {your_attack} points de dégats à l'ennemi ")
        
        elif user_choice == "2" and NUMBER_POTION > 0 :
            potion_health = random.randint(15, 50)
            USER_HEALTH += potion_health
            NUMBER_POTION -= 1
            SKIP_TURN = True
            print(f"Vous récupérez {potion_health} points de vie ({NUMBER_POTION} restantes) ")

        else : 
            print("Vous n'avez plus de potions... ")
            continue

        if ENEMY_HEALTH <= 0 : 
            print("Tu as gagné !! ")
            break
        enemy_attack = random.randint(5, 15)
        USER_HEALTH -= enemy_attack
        print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ")

        if USER_HEALTH <= 0 : 
            print("Tu as perdu... ")
            break 

        print(f"Il vous reste {USER_HEALTH} points de vie. ")
        print(f"Il reste {ENEMY_HEALTH} points de vie à l'ennemi. ")
        print("-" * 60)

print("Fin du jeu")

        




        


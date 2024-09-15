print('Welcome to my Choose Your Own Adventure game!')
health = 10
name = input('What is your name? ')
age = int(input('What is your age? '))

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input('Do you want to play? ').lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("Let's play!")
    
        left_or_right = input("First choice... Would you like to go left or right? [left/right] ")
        if left_or_right == "left":
            ans = input("Nice! You follow the path and reach a lake... Do you swim across or go around? [across/around] ")
                
            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but you were bitten by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river in the distance. Which do you go to? [river/house] ")
            if ans == "house" :
                print("You go to the house and are greeted by the owner... He yells at you, and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health, and you lost the game.")
                else: 
                    print("You have survived! You WIN!!!")

            else: 
                print("You fell in the river and lost...")
    
        else:
            print("You fell down a cliff and lost...")
    else:
        print("Later, gator!")
else:
    print("You aren't old enough to play. Later, gator!")
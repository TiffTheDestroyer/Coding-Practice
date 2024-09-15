print('Welcome to my Choose Your Own Adventure game!')
health = 20
name = input('What is your name? ')
age = int(input('What is your age? '))

if age >= 18:
    print("You're old enough to go on this adventure!")

    wants_to_play = input('Do you want to play? ').lower()
    if wants_to_play == "yes":
        print("Excellent! You are starting this adventure with", health, "health")
        print("Let's go exploring!")
    
        left_or_right = input("First choice... Would you like to go left or right? [Type Left/Right] ").lower()
        if left_or_right == "left":
            
            ans = input("Nice! You see a path, and you follow it. It leads you to a lake... Do you swim across or go around? [Across/Around] ").lower()
                
            if ans == "around":
                print("You went around and safely reached the other side of the lake.")

            elif ans == "across":
                print("You managed to get across, but you were bitten by a fish and lost 5 health.")
                health -= 5
                print("Your health is now", health)
     
            left_or_right = input("Now, you come upon a crossroad. Do you take the path on the left, or the one on the right? [Left/Right] ").lower()
            if left_or_right == "right":
                ans = input("Oh, no! It's a dead end! You have to turn back [Press 'Enter' to turn back]")

                yes_or_no = input("Once again, you're facing the crossroad. Would you like to explore the path that you did not choose? ['Yes' to explore/'No' to return to your original path] ").lower()
            
                if yes_or_no == "yes":
                    print("Looks like there were supplies, but they've already been taken. You head back to your original path.")

            if left_or_right == "left":
                print("You found supplies! That will add 5 health points to your health and return you to your original path!" )
                health +=5
                print("Your health is now", health)

            ans = input("Now you notice a house and a river in the distance. Which do you approach? [River/House] ").lower()

            if ans == "house" :
                print("You go to the house, and you're confronted by the owner... He throws a rock at you! You're hit, and you lose 5 health")
                health -= 5
                print("Your health is now", health) 
            
                yes_or_no = input("You notice that he has an inflatable raft in his yard. Do you take it?? [Yes/No] ").lower()
                
                if yes_or_no == "no":
                    print("Now you've turned around, and you're back at the river.")

                if yes_or_no == "yes": 
                    print("You grab the raft and bolt towards the river!")
        
                yes_or_no = input("You have to cross the river in order to move foward. Do you have anything that can help you cross it? [Yes/No] ").lower()

                if yes_or_no == "no":
                        print("Oh, no! You'll have to try to cross it without any help!")
                        print("You try crossing, but fell in the river and lost 10 health points")
                        health -=10
                        print("Your health is now", health)

                if yes_or_no == "yes":
                    print("Great! You can use the raft!")

                    raft_no_raft = input("Type 'Raft' to use the raft to cross the river ").lower()
                    if raft_no_raft == "raft":
                        print("You successfully crossed the river!")

                ans = input("Now that you're on the other side of the river, you see an abandoned car on your left, and you see another path to your right. Which do you choose? [Left/Right] ").lower()
                if ans == "left":
                    yes_or_no = input("The car looks old, but it could have some supplies. Do you want to search the car? [Yes/No] ")
                    if yes_or_no == "yes":
                        print("You check the car and you find supplies!")

            elif ans == "river":
                print("You fell in the river and lost 10 health points.")
                health -=10
                print("Your health is now", health)   

                        
        else:
            print("You fell down a cliff and lost...")
    else:
        print("Aww, that's too bad. Later, gator!")
else:
    print("You aren't old enough to play. Later, gator!")
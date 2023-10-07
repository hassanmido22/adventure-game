import time
import random

def print_pause(*args):
    # Combine the messages into one string
    all_msg = " ".join(args)
    print(all_msg)
    time.sleep(2)

def game_start(monster):
    # Introduction to the game
    print_pause("You find yourself standing in an open field, filled with grass",
                "and yellow wildflowers.")
    print_pause("Rumor has it that a wicked "+monster+" is somewhere around here,",
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)",
                "rusty old magic wand.")

def knock_house_door(items, monster, weapon):
    # Encounter at the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a wicked "+monster+".")
    print_pause("Eep! This is the wicked "+monster+"'s house!")
    print_pause("The wicked "+monster+" finds you!")

    if weapon not in items:
        # Player has no weapon
        print_pause("You feel a bit under-prepared for this, what with only having a tiny, rusty old magic wand.")
        while True:
            action = input("Would you like to (1) cast a spell or (2) run away?")
            if action == "1":
                print_pause("You do your best...")
                print_pause("but your rusty old magic wand is no match for the "+monster+".")
                print_pause("You have been turned into a frog!")
            elif action == "2":
                print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
                go_to_the_field(items, monster, weapon)
                break
            play_again()
            break
    else:
        # Player has a weapon
        while True:
            action = input("Would you like to (1) cast a spell or (2) run away?")
            if action == "1":
                print_pause("As the "+monster+" moves to cast a spell, you raise your new "+weapon+".")
                print_pause("The Wand of Ogoroth shines brightly in your hand as you brace yourself for the spell.")
                print_pause("But the "+monster+" takes one look at your shiny new wand and runs away!")
                print_pause("You have rid the town of the "+monster+". You are victorious!")
            elif action == "2":
                print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
                go_to_the_field(items, monster, weapon)
                break
            play_again()
            break

def play_again():
    # Ask if the player wants to play again
    action = input("Would you like to play again? (y/n)")
    if action == "y":
        print_pause("Excellent! Restarting the game ...")
        play()
    elif action == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()

def peer_into_cave(items, monster, weapon):
    if weapon not in items:
        # Player finds a weapon in the cave
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical "+weapon+"!")
        print_pause("You discard your rusty old magic wand and take the "+weapon+" with you.")
        print_pause("You walk back out to the field.")
        items.append(weapon)
    else:
        # Player has already explored the cave
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    go_to_the_field(items, monster, weapon)

def go_to_the_field(items, monster, weapon):
    # Main field where the player chooses their actions
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?\n")

    while True:
        action = input("(Please enter 1 or 2.)")
        if action == "1":
            knock_house_door(items, monster, weapon)
            break
        elif action == "2":
            peer_into_cave(items, monster, weapon)
            break

def play():
    items = []
    weapons = [
        "Blade of Valor",
        "Staff of Eldrath",
        "Shield of Durandal",
        "Bow of Seraphina",
        "Hammer of Thundertop",
        "Dagger of Shadowsong"
    ]
    weapon = random.choice(weapons)
    monster = random.choice(["wicked fairie", "pirate", "troll", "dragon", "gorgon"])
    game_start(monster)
    go_to_the_field(items, monster, weapon)

# Start the game
play()
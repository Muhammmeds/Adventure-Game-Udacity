import time
import random


def print_sleep(prompt, sleep_time=0):
    """Prints a prompt and pauses for a specified duration."""
    print(prompt)
    time.sleep(sleep_time)


def valid_input(prompt, options):
    """Prompts the user for input until a valid option is provided."""
    while True:
        response = input(prompt).lower()
        if response in options:
            return response


def play_again():
    """Asks the player if they would like to play again."""
    choice = valid_input("Would you like to play again? (y/n) ", ["y", "n"])
    if choice == "y":
        print_sleep("Excellent! Restarting the game ...", 2)
        adventure_game()  # Restart the game
    else:
        print_sleep("Thanks for playing! See you next time.", 2)
        exit(0)


def run_away():
    """Handles the player's choice to run away from danger."""
    print_sleep("You run back into the field. Luckily, "
                "you don't seem to have been followed.\n", 2)


def fight(fight_texts):
    """Executes the fight sequence with a given list of fight texts."""
    for text in fight_texts:
        print_sleep(text, 1)
    print_sleep("\n", 1)


def fight_choice(fight_texts):
    """Presents the player with a choice to fight or run away."""
    choice = valid_input("Would you like to (1) fight or (2) run away?\n",
                         ['1', '2'])
    if choice == '1':
        fight(fight_texts)
        return True
    else:
        run_away()
        return False


def knock_on_door(monster, weapon):
    """Handles the scenario when the player knocks on the door."""
    print_sleep("You approach the door of the house.", 1)
    print_sleep(f"You are about to knock when the door opens and out steps "
                f"a {monster}.", 1)
    print_sleep(f"Eep! This is the {monster}'s house!", 1)
    print_sleep(f"The {monster} attacks you!", 1)
    if weapon == "dagger":
        print_sleep("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.", 1)
        return fight_choice([
            "You do your best...",
            f"but your dagger is no match for the {monster}.",
            "You have been defeated!"
        ])
    else:
        return fight_choice([
            f"As the {monster} moves to attack, you unsheath your new sword.",
            "The Sword of Ogoroth shines brightly in your hand as you "
            "brace yourself for the attack.",
            "But the pirate takes one look at your shiny new toy and "
            "runs away!",
            f"You have rid the town of the {monster}. You are victorious!"
        ])


def peer_in_cave(weapon):
    """Handles the scenario when the player peers into the cave."""
    if weapon == 'dagger':
        print_sleep("You peer cautiously into the cave.", 1)
        print_sleep("It turns out to be only a very small cave.", 1)
        print_sleep("Your eye catches a glint of metal behind a rock.", 1)
        print_sleep("You have found the magical Sword of Ogoroth!", 1)
        print_sleep("You discard your silly old dagger and take the sword "
                    "with you.", 1)
        weapon = "sword"
    else:
        print_sleep("You peer cautiously into the cave.", 1)
        print_sleep("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.", 1)
    print_sleep("You walk back out to the field.\n", 2)
    return weapon


def intro(monster):
    """Displays the introductory text for the game."""
    print_sleep("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.", 2)
    print_sleep(f"Rumor has it that a {monster} is somewhere around here, "
                "and has been terrifying the nearby village.", 2)
    print_sleep("In front of you is a house.", 2)
    print_sleep("To your right is a dark cave.", 2)
    print_sleep("In your hand you hold your trusty "
                "(but not very effective) dagger.\n", 2)


def play_game(monster, weapon):
    """Main game loop where the player makes choices."""
    while True:
        print_sleep("Enter 1 to knock on the door of the house.", 2)
        print_sleep("Enter 2 to peer into the cave.", 2)
        print_sleep("What would you like to do?", 2)
        choice = valid_input("(Please enter 1 or 2).\n", ['1', '2'])
        if choice == '1':
            if knock_on_door(monster, weapon):
                break
        else:
            weapon = peer_in_cave(weapon)


def adventure_game():
    """Starts the adventure game."""
    village_monsters = ['dragon', 'wicked fairie', 'pirate', 'troll']
    weapon = 'dagger'
    while True:
        monster = random.choice(village_monsters)
        intro(monster)
        play_game(monster, weapon)
        play_again()


if __name__ == '__main__':
    adventure_game()

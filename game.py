"""a basic text dungeon for learn python the hardway exercise"""
import random
import time
import os

class StandardRoom(object):
    """ This generates a dungeon room."""
    def __init__(self):
        self.room_id = random.randint(0, 9999)
        self.description = random.choice(open("dungeons.txt").readlines())

    def room_description(self):
        """prints room description"""
        print self.description

    def has_mob(self):
        """Need a better solution to populate mobs"""
        if self.room_id % random.randint(1, 10) == 0:
            return True

class Villian(object):
    """A basic monster"""
    def __init__(self):
        self.health = random.randint(8, 16)
        self.gold_value = random.randint(6, 20)
        self.experience = random.randint(85, 225)
        self.attack_count = 0

    def gold_amount(self):
        """gold value for killing mob"""
        PLAYER_STATS[1] = PLAYER_STATS[1] + self.gold_value
        return self.gold_value

    def exp_value(self):
        """experience value for killing mob"""
        PLAYER_STATS[2] = PLAYER_STATS[2] + self.experience
        return self.experience

    def attack_increment(self):
        """Counter incremented everytime the player attacks"""
        self.attack_count = self.attack_count + 1

def start_game():
    """for now this is how I start the game."""
    print "You leave the ground level and "
    print "begin your descent into the dark dungeon."
    print "The large door begins to open slowly"

    if raw_input("Continue? (y/n)") == 'y':
        enter_room()
    else:
        print "GoodBye"

def battle_victory(mob):
    """player wins a battle"""
    print "***************************************"
    print "You defeated the monster!"
    print "You gained %i gold" % mob.gold_value
    print "You have %i health remaining." % PLAYER_STATS[0]
    print "You have %i gold."   % PLAYER_STATS[1]
    print "***************************************"
    time.sleep(1)
    if raw_input("Continue deeper into the dungeon?(y/n)") == 'y':
        enter_room()
    else:
        exit(0)
    return True

def battle_defeat(mob):
    """player loses a battle"""
    print "***************************************"
    print "You were defeated!"
    print "The monsters health is %i" % mob.health
    print "***************************************"
    return False

def attack():
    """This handles the battle system for now"""
    mob = Villian()
    while PLAYER_STATS[0] > 0 and mob.health > 0:
        #Use a random int for monster attack value#
        mob_attack = random.randint(0, 4)
        #arandom int for player attack#
        player_attack = random.randint(2, 8)
        PLAYER_STATS[0] = PLAYER_STATS[0] - mob_attack
        mob.health = mob.health - player_attack
        mob.attack_increment()
        print "Hero rolls %i attack" % player_attack
        time.sleep(.5)
        print "Monster rolls %i attack" % mob_attack
        time.sleep(.5)
        print "Current health: %i " % PLAYER_STATS[0]
        print "Monsters health: %i" % mob.health
        print "You have attacked %i times" % mob.attack_count
        if PLAYER_STATS[0] > 0 and mob.health > 0:
            time.sleep(.5)
            attack_choice(mob.attack_count)

        elif PLAYER_STATS[0] > 0 and mob.health <= 0:
            mob.gold_amount()
            battle_victory(mob)
        else:
            battle_defeat(mob)

def attack_choice(attack_count):
    """User input before attacking"""
    if attack_count == 0:
        answer = raw_input("Attack (y/n):")
        if answer == 'y':
            attack()
        if answer == 'n':
            print "Pansy"
            exit(0)
        else:
            print "Invalid Input"

    if attack_count >= 1:

        answer = raw_input("Attack again?:(y/n)")
        if  answer == 'y':
            return
        elif answer == 'n':
            print "Pansy"
            exit(0)
        else:
            print "Invalid Input"

def room_move():
    """user input to continue game"""
    while True:
        answer = raw_input("Enter the next room?(y/n)")
        if answer == 'y':
            enter_room()
        if answer == 'n':
            print "GoodBye"
            exit(0)
        else:
            print "Invalid Input"

def enter_room():
    """generates a room and check for mobs"""
    current_room = StandardRoom()
    os.system('clear')
    current_room.room_description()
    attack_count = 0
    if current_room.has_mob():
        print "There is a large creature in this room!"
        attack_choice(attack_count)
    else:
        print "This room is empty! "
        room_move()

PLAYER_STATS = [100, 0, 0]
start_game()


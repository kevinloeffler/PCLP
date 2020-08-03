# Welcome to Python command line pokemon.
# This is a small "game" I created as an excercise to learn more about classes in Python.
# Built for Python 3.7.7

import random
from time import sleep

# Game variables
damage = 20  # Pokemon base damage. Higher damage results in faster rounds. Default: 20
startingGold = 100  # Make it easier for yourself by starting with more gold. Default: 100

# Pokemon Class:
# Initiate with Name, Type, Maximum Health, Current Health and its status
# every method prints what happens for a better overview and returns the changed value

class Pokemon:
    # Initiate a pokemon with a name, type, the maximum and the current health
    def __init__(self, name, type, maxHealth, Health):
        self.name = name
        self.level = 1
        self.type = type
        self.maxHealth = maxHealth
        self.health = Health
        self.isAlive = True

    def __repr__(self):
        return "{name} has {health} health.".format(name = self.name, health = self.health)

    # Increase the level of a pokemon by 1 - no user input!
    def levelUp(self):
        self.level += 1
        self.maxHealth += int(self.level * self.maxHealth * 0.25)
        print("{name} has leveled up to level {level}!".format(name = self.name, level = self.level))
        return self.level

    # heal a pokemon by a certain amount
    def heal(self, amount):
        self.health += amount
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        print("{name} has healed {amount} and has now {health} health.".format(name = self.name, amount = amount, health = self.health))
        return self.health

    # damage a pokemon by a certain amount
    def loseHealth(self, amount):
        self.health -= amount
        if self.health < 0:
            self.knockOut()
        print("{name} has lost {amount} health and has now {health} health.".format(name = self.name, amount = amount, health = self.health))
        return self.health

    # knock out a pokemon, sets the health to 0 - no user input!
    def knockOut(self):
        self.health = 0
        self.isAlive = False
        print("{name} is knocked out!".format(name = self.name))
        return self.isAlive

    # restores a pokemons health - no user input!
    def revive(self):
        self.health = self.maxHealth
        self.isAlive = True
        print("{name} has been revived!".format(name = self.name))
        return self.isAlive

    # Attacks another pokemon
    def attack(self, target):
        # Check if Pokemon is alive
        if self.isAlive is False:
            print("{name} can't attack because it is knocked out.".format(name = self.name))
            return 0
        # Attack if it is alive
        dmg = damage
        # Check for advantages
        dmg = int(dmg * compareTypes(self.type, target.type))
        print("{name} attacked {target} and dealt {damage} damage.".format(name = self.name, target = target.name, damage = dmg))
        target.loseHealth(dmg)
        return target.health

def compareTypes(type1, type2):
    # Return: 1.5 = advantage, 0.75 = disadvantage
    # Check for Electro
    if type1 == "Electro":
        return 1.5
    elif type2 == "Electro":
        return 0.75
    # Compare Earth
    elif type1 == "Earth":
        if type2 == "Air":
            return 1.5
        elif type2 == "Fire":
            return 0.75
        else:
            return 1
    # Compare Air
    elif type1 == "Air":
        if type2 == "Water":
            return 1.5
        elif type2 == "Earth":
            return 0.75
        else:
            return 1
    # Compare Water
    elif type1 == "Water":
        if type2 == "Fire":
            return 1.5
        elif type2 == "Air":
            return 0.75
        else:
            return 1
    elif type1 == "Fire":
        if type2 == "Earth":
            return 1.5
        elif type2 == "Water":
            return 0.75
        else:
            return 1

def checkStatus(pk1, pk2):
    if pk1.isAlive is False or pk2.isAlive is False:
        return False
    return True

class Potion:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return "This is a {name} potion. You have {amount}.".format(name = self.name, amount = self.amount)

    def use(self, pokemon):
        # Use a healing potion
        if self.name == "healing":
            if self.amount > 0:
                pokemon.heal(50)
                self.amount -= 1
                if self.amount == 1:
                    print("You have 1 healing potion left.")
                else:
                    print("You have {amount} healing potions left.".format(amount = self.amount))
            else:
                print("You have no more healing potions.")
        # Use a revive potion
        elif self.name == "revive":
            if self.amount > 0:
                pokemon.revive()
                self.amount -= 1
                if self.amount == 1:
                    print("You have 1 revive potion left.")
                else:
                    print("You have {amount} revive potions left.".format(amount = self.amount))
            else:
                print("You have no more revive potions.")
        # Use a level potion
        elif self.name == "level":
            if self.amount > 0:
                pokemon.levelUp()
                self.amount -= 1
                if self.amount == 1:
                    print("You have 1 level potion left.")
                else:
                    print("You have {amount} level potions left.".format(amount = self.amount))
            else:
                print("You have no more level potions.")
        # Error message
        else:
            print("There is no potion with that name.")

    def add(self, addAmount = 1):
        self.amount += addAmount
        if self.amount == 1:
            print("You now have {amount} {name} potion".format(amount = self.amount, name = self.name))
        else:
            print("You now have {amount} {name} potions".format(amount = self.amount, name = self.name))

class Player:
    def __init__(self, name, pokemon = [], potions = []):
        self.name = name
        self.gold = startingGold
        self.pokemon = pokemon
        self.potions = potions

    def __repr__(self):
        return "{name} has {gold} gold, {pokemon} pokemon and {potions} potions.".format(name = self.name, gold = self.gold, pokemon = str(len(self.pokemon)), potions = str(len(self.potions)))

# Pokemon types: Earth > Air > Water > Fire > Earth. The special type "Electro" beats all!
bisasam = Pokemon("Bisasam", "Earth", 100, 100)
glumanda = Pokemon("Glumanda", "Fire", 100, 100)
schiggy = Pokemon("Schiggy", "Water", 100, 100)
taubsi = Pokemon("Taubsi", "Air", 100, 100)
pikachu = Pokemon("Pikachu", "Electro", 200, 200)

# All Pockemons:
nidoran = Pokemon("Nidoran", "Earth", 120, 120)
zubar = Pokemon("Zubat", "Air", 90, 90)
omot = Pokemon("Omot", "Air", 80, 80)
paras = Pokemon("Paras", "Water", 110, 110)
fukano = Pokemon("Fukano", "Fire", 130, 130)
abra = Pokemon("Abra", "Fire", 120, 120)
oppPokemons = [nidoran, zubar, omot, paras, fukano, abra]

startingPokemon = [bisasam, glumanda, schiggy, taubsi]
allPokemon = [bisasam, glumanda, schiggy, taubsi, nidoran, zubar, omot, paras, fukano, abra]
playerPokemon = "False"

# Potions: Healing, Revive, Level
healingPotion = Potion("healing", 1)
revivePotion = Potion("revive", 1)
levelPotion = Potion("level", 1)

# Command Line Interface
yes = ["y", "Y", "yes", "Yes"]
no = ["n", "N", "no", "No", ""]
commands = ["fight", "shop"]

# Messages

startingMessage = """
Welcome to a new Pokemon experience... This is "Phyton Command Line Pokemon!"
You start with {gold} gold, one pokemon and one healing potion. You have to fight other pokemon trainers to earn more gold, buy cool stuff and level your pokemon up. Like the name suggest you can only control this game via command line. To learn more about what you can do, type "help" and to exit, type "quit".
""".format(gold = startingGold)

helpMessage = """
fight       start a fight
  attack    order your pokemon to attack the opponents pokemon
  potion    use a potion: healing | revive | level
  stats     shows the stats for your active pokemon (costs no move)
  flee      run away

shop
  healing   buys one healing potion
  revive    buys one revive potion
  level     buys one level potion
  [type]    shows all available Pokemon of this type
    [name]  enter the name of the Pokemon you want to buy
    no      cancel the buy process
  exit      leave the shop

stats       print your gold and all your Pokemon
credits     show the credits
quit        Close PCLP
"""

# Story

opponents = ["Barry", "Cheren", "Bianca", "Hugh", "Shauna", "Trevor", "Tierno", "Hau", "Gladion", "Trace", "Hop"]

def helpMe():
    print(helpMessage)

def fight():
    print("You face off against {opponent}".format(opponent = random.choice(opponents)))

    # Opponent
    oppPokemon = random.choice(oppPokemons)
    print("Your opponent picked {pk} ({type})\n".format(pk = oppPokemon.name, type = oppPokemon.type))

    # Choose Pokemon
    print("Pick a Pokemon:")
    activePokemon = player.pokemon[0]
    for i in range(len(player.pokemon)):
        print(str(i + 1) + " " + player.pokemon[i].name + " - " + str(player.pokemon[i].health) + " hp")
    cache = input("Pick a number - Default [1] ")
    for i in range(len(player.pokemon)):
        if cache == str(i + 1):
            activePokemon = player.pokemon[i]
    print("You picked {pk} with {hp} health.\n".format(pk = activePokemon.name, hp = str(activePokemon.health)))

    # Start fight
    oppPokemon.attack(activePokemon)
    status = True
    while status is True:
        fightUserInput = input("\nattack | potion | flee | stats: ")
        # User Input Attack
        if fightUserInput == "attack":
            activePokemon.attack(oppPokemon)
            status = checkStatus(activePokemon, oppPokemon)
            sleep(0.4)
            # Opponent move
            probality = random.randint(0, 6)
            print("")
            if probality == 1:
                oppPokemon.heal(50)
            else:
                oppPokemon.attack(activePokemon)
        # User Input Potion
        elif fightUserInput == "potion":
            potionUserInput = input("What potion do you want to use [healing | revive | level]: ")
            if potionUserInput == "healing":
                healingPotion.use(activePokemon)
                print("")
                sleep(0.4)
                # Opponent move
                oppPokemon.attack(activePokemon)
            elif potionUserInput == "revive":
                revivePotion.use(activePokemon)
                print("")
                sleep(0.4)
                # Opponent move
                oppPokemon.attack(activePokemon)
            elif potionUserInput == "level":
                levelPotion.use(activePokemon)
                print("")
                sleep(0.4)
                # Opponent move
                oppPokemon.attack(activePokemon)
        # User Input Flee
        elif fightUserInput == "flee":
            break
        elif fightUserInput == "stats":
            print("{pk} has {hp} of {max} hp left.".format(pk = activePokemon.name, hp = activePokemon.health, max = activePokemon.maxHealth))
            print("{pk} has {hp} of {max} hp left.".format(pk = oppPokemon.name, hp = oppPokemon.health, max = oppPokemon.maxHealth))
    # Result:
    if activePokemon.isAlive is False:
        print("Oh no, you lost! You can buy revive potions in the store.")
    elif oppPokemon.isAlive is False:
        print("Congratulations, you won! You got 80 Gold.")
        player.gold += 80
    else:
        print("You ran away.")
    status = True

shopErrorMessage = "You don't have enough gold."

def shop():
    print("Welcome to the shop. What are you looking for? When your done, type exit.")
    print("Potions: [healing | revive | level]")
    print("Pokemon: [Earth | Water | Air | Fire | Electro]")
    shopInput = input("shop > ")
    # Buy a healing potion
    if shopInput == "healing":
        print("Do you want to buy a healing potion for 25 Gold? You have {gold} gold.".format(gold = player.gold))
        shopInput = input("[y/N] ")
        if shopInput in yes:
            healingPotion.amount += 1
            if player.gold >= 25:
                player.gold -= 25
                print("You now have {nr} healing Potions and {gold} gold left.".format(nr = healingPotion.amount, gold = player.gold))
            else:
                print(shopErrorMessage)
        else:
            print("Canceled")
    # Buy a revive potion
    elif shopInput == "revive":
        print("DEBUG: " + str(revivePotion.amount))
        print("Do you want to buy a revive potion for 60 Gold? You have {gold} gold.".format(gold = player.gold))
        shopInput = input("[y/N] ")
        if shopInput in yes:
            revivePotion.amount += 1
            if player.gold >= 60:
                player.gold -= 60
                print("You now have {nr} revive potions and {gold} gold left.".format(nr = revivePotion.amount, gold = player.gold))
            else:
                print(shopErrorMessage)
        else:
            print("Canceled")
    # Buy a level potion
    elif shopInput == "level":
        print("Do you want to buy a level potion for 100 Gold? You have {gold} gold.".format(gold = player.gold))
        shopInput = input("[y/N] ")
        if shopInput in yes:
            levelPotion.amount += 1
            if player.gold >= 100:
                player.gold -= 100
                print("You now have {nr} level potions and {gold} gold left.".format(nr = levelPotion.amount, gold = player.gold))
            else:
                print(shopErrorMessage)
        else:
            print("Canceled")
    # Buy a pokemon
    elif shopInput == "Earth" or shopInput == "Water" or shopInput == "Air" or shopInput == "Fire" or shopInput == "Electro":
        pkTypeArray = []
        for pk in allPokemon:
            if shopInput == pk.type:
                print(pk)
                pkTypeArray.append(pk)
        print("\nLike anything you see?")
        shopInput = input("Type the name of a Pokemon or [no] to exit: ")
        for pk in pkTypeArray:
            if shopInput == pk.name:
                print("Do you want to buy {name} for 100 Gold?".format(name = pk.name))
                shopInput = input("[y/N] ")
                if shopInput in yes:
                    if pk in player.pokemon:
                        print("You already own this Pokemon...")
                        break
                    else:
                        player.pokemon.append(pk)
                        if player.gold >= 60:
                            player.gold -= 60
                            print("Congratulations, you can now use {pk}. You have {gold} left.".format(pk = pk.name, gold = player.gold))
                else:
                    print("Have a good day.")
                    break

def stats():
    print("You have {gold} gold and you Pokemon are:".format(gold = player.gold))
    for pk in player.pokemon:
        print(pk)

############################################# Let's Play #############################################

playerName = input("Enter your name: ")
sleep(0.4)
print("Hi " + playerName)
sleep(0.6)
print("Pick your starting Pokemon:")
sleep(0.6)

while playerPokemon not in startingPokemon:
    for strPokemon in startingPokemon:
        cache = input(strPokemon.name + " [y/N] ")
        if cache in yes:
            playerPokemon = strPokemon
            print("You choose " + playerPokemon.name)
            break

player = Player(playerName, [playerPokemon])
sleep(0.6)

print(startingMessage)

while True:
    pass
    userQuit = False
    userInput = input("> ")
    # Check user command against all commands:
    for command in commands:
        if userInput == "help":
            helpMe()
            break
        elif userInput == "fight":
            fight()
            break
        elif userInput == "quit" or userInput == "q":
            userQuit = True
            print("Goodby and thanks for playing")
            break
        elif userInput == "shop":
            shop()
            break
        elif userInput == "stats":
            stats()
            break
        elif userInput == "credits":
            print("Developed as a student project by Kevin Loeffler")
            break
        elif userInput == "hello world":
            print("Hi there!")
            break
        else:
            print("Invalid Command")
            break
    if userQuit is True:
        break

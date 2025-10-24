import random
import time
import sys
import os
import math
from ast import literal_eval

global tab
tab = "\t\t\t"
global newScreen
newScreen = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

os.system('mode con: cols=100 lines=1000')

global name
name = []
global group
group = []
global strength
strength = []
global magic
magic = []
global defense
defense = []
global resistance
resistance = []
global speed
speed = []
global intellect
intellect = []
global skill
skill = []
global HP
HP = []
global currentHP
currentHP = []
global MP
MP = []
global currentMP
currentMP = []
global level
level = []
global XP
XP = []
global players
global spells
spells = {}
global supportSpells
supportSpells = {}
global totalLevel
totalLevel = 0
global numOfEnemies
global menuChoice
global spellCost
spellCost = {"1MP" : ["Fire", "Ice", "Wind", "Heal", "DefUP"]} 
global spellStats
#first is hit rate, second is damage
spellStats = {"Fire" : [-10, 2], "Ice" : [0, 0], "Wind" : [20, -1]}
global supportSpellStats
#first is the stat that is modified, second is by how much, third is the duration. If the duration is 0 it lasts the whole match
supportSpellStats = {"Heal" : ["currentHP", 10], "DefUP" : ["defense", 2, 4], "AtkUP" : ["attack", 2, 4], "SpdUP" : ["speed", 2, 4]}
global items
#The first is the amount, the second is the description, third is what it changes, fourth is by how much, fifth is the duration?.
items = {"consumableItems": {"Potion" : [1, "Heals the player who uses it by 10", "currentHP", 10, 0], "Soda" : [1, "refreshes the player's current MP by 10", "currentMP", 10, 0]}, "equipableItems" : {}}
global equipped
equipped = {}
global alive
alive = []
HPFull = "\u2B1B"
HPHalf= "\u25FE"
HPEmpty = "\u2B1C"
MPFull = "\u26AB"
MPHalf = "\u2B24"
MPEmpty = "\u26AA"

def levelUP():
    global name
    global group
    global strength
    global magic
    global defense
    global resistance
    global speed
    global intellect
    global skill
    global HP
    global currentHP
    global MP
    global currentMP
    global level
    global XP
    global spells
    global supportSpells
    global players
    
    growthLine = open("Ally Growth Rates.txt", "r")
    growthGroup = growthLine.readline()
    growthGroup = growthGroup.split(", ")
    
    growthStrength = growthLine.readline()
    growthStrength = growthStrength.split(", ")
    for x in range (len(growthStrength)-1):
        growthStrength[x] = int(growthStrength[x])
    
    growthMagic = growthLine.readline()
    growthMagic = growthMagic.split(", ")
    for x in range (len(growthMagic)-1):
        growthMagic[x] = int(growthMagic[x])
    
    growthDefense = growthLine.readline()
    growthDefense = growthDefense.split(", ")
    for x in range (len(growthDefense)-1):
        growthDefense[x] = int(growthDefense[x])
    
    growthResistance = growthLine.readline()
    growthResistance = growthResistance.split(", ")
    for x in range (len(growthResistance)-1):
        growthResistance[x] = int(growthResistance[x])
    
    growthSpeed = growthLine.readline()
    growthSpeed = growthSpeed.split(", ")
    for x in range (len(growthSpeed)-1):
        growthSpeed[x] = int(growthSpeed[x])
    
    growthIntellect = growthLine.readline()
    growthIntellect = growthIntellect.split(", ")
    for x in range (len(growthIntellect)-1):
        growthIntellect[x] = int(growthIntellect[x])
    
    growthSkill = growthLine.readline()
    growthSkill = growthSkill.split(", ")
    for x in range (len(growthSkill)-1):
        growthSkill[x] = int(growthSkill[x])
    
    growthHP = growthLine.readline()
    growthHP = growthHP.split(", ")
    for x in range (len(growthHP)-1):
        growthHP[x] = int(growthHP[x])
    
    growthMP = growthLine.readline()
    growthMP = growthMP.split(", ")
    for x in range (len(growthMP)-1):
        growthMP[x] = int(growthMP[x])
    
    
    for check in range (players):
        if (XP[check] >= 100):
            while (XP[check] >= 100):
                print("==========Level UP!!==========")
                classGrowth = growthGroup.index(group[check])
                XP[check]-=100
                level[check]+= 1
                statRoll = random.randint(1, 100)
                if (statRoll <= growthStrength[classGrowth]):
                    strUP = True
                else:
                    strUP = False
                    
                statRoll = random.randint(1, 100)
                if (statRoll <= growthMagic[classGrowth]):
                    magUP = True
                else:
                    magUP = False

                statRoll = random.randint(1, 100)
                if (statRoll <= growthDefense[classGrowth]):
                    defUP = True
                else:
                    defUP = False
                
                statRoll = random.randint(1, 100)
                if (statRoll <= growthResistance[classGrowth]):
                    resUP = True
                else:
                    resUP = False
                
                statRoll = random.randint(1, 100)
                if (statRoll <= growthSpeed[classGrowth]):
                    spdUP = True
                else:
                    spdUP = False
                
                statRoll = random.randint(1, 100)
                if (statRoll <= growthIntellect[classGrowth]):
                    intUP = True
                else:
                    intUP = False
                
                statRoll = random.randint(1, 100)
                if (statRoll <= growthSkill[classGrowth]):
                    skillUP = True
                else:
                    skillUP = False
                
                statRoll = random.randint(1, 100)
                if (statRoll <= growthHP[classGrowth]):
                    HPUP = True
                else:
                    HPUP = False
                
                statRoll = random.randint(1, 100)
                if (statRoll <= growthMP[classGrowth]):
                    MPUP = True
                else:
                    MPUP = False
                    
                print("        " + name[check])
                print("Strength: ", end = "\t")
                print(strength[check], end = "\t")
                if (strUP == True):
                    print("+1", end = "")
                    strength[check] += 1
                print()
                
                print("Magic: ", end = "\t\t")
                print(magic[check], end = "\t")
                if (magUP == True):
                    print("+1", end = "")
                    magic[check] += 1
                print()
                
                print("Defense: ", end = "\t")
                print(defense[check], end = "\t")
                if (defUP == True):
                    print("+1", end = "")
                    defense[check] += 1
                print()
                
                print("Resistance: ", end = "\t")
                print(resistance[check], end = "\t")
                if (resUP == True):
                    print("+1", end = "")
                    resistance[check] += 1
                print()
                
                print("Speed: ", end = "\t\t")
                print(speed[check], end = "\t")
                if (spdUP == True):
                    print("+1", end = "")
                    speed[check] += 1
                print()
                
                print("Intellect: ", end = "\t")
                print(intellect[check], end = "\t")
                if (intUP == True):
                    print("+1", end = "")
                    intellect[check] += 1
                print()
                
                print("Skill: ", end = "\t\t")
                print(skill[check], end = "\t")
                if (skillUP == True):
                    print("+1", end = "")
                    skill[check] += 1
                print()
                
                print("HP: ", end = "\t\t")
                print(HP[check], end = "\t")
                if (HPUP == True):
                    print("+1", end = "")
                    HP[check] += 1
                print()
                
                print("MP: ", end = "\t\t")
                print(MP[check], end = "\t")
                if (MPUP == True):
                    print("+1", end = "")
                    MP[check] += 1
                print()
                input("Press enter when you are finished.")
                
                
                
                
            
def addSpell():
    sladfj = 1

def battle():
    global name
    global group
    global strength
    global magic
    global defense
    global resistance
    global speed
    global intellect
    global skill
    global HP
    global currentHP
    global MP
    global currentMP
    global level
    global XP
    global spells
    global supportSpells
    global numOfEnemies
    global enemyName
    global enemyStrength
    global enemyMagic
    global enemyDefense
    global enemyResistance
    global enemySpeed
    global enemyIntellect
    global enemySkill
    global enemyHP
    global enemyCurrentHP
    global enemyMP
    global enemyCurrentMP
    global enemyLevel
    global players
    global totalLevel
    global spellCost
    global supportSpellStats
    global alive
    #The variable is the name of the person, the first is the stat that changed, the second is by how much, the third is the duration,
    #and the fourth is the same as the first if there is multiple stat changes, and so on and so forth.
    statChange = {}
    for x in range (players):
        statChange.update({name[x] : []})
    for x in range (numOfEnemies):
        statChange.update({enemyName[x] : []})
    print("Stat change: " + str(statChange))
    addXP = 0
    defend = []
    print(str(numOfEnemies) + " enemies have appeared!")
    print("Their Stats:\n")
    print("Class: ", end = "\t\t\t") 
    for x in range (numOfEnemies):
        if (len(enemyName[x]) >= 16):
            tab = "\t"
        elif (len(enemyName[x]) >= 8):
            tab = "\t\t"
        else:
            tab = "\t\t\t"
        print(enemyName[x], end = tab)
    print("")
    tab = "\t\t\t"
    print("Strength:", end = "\t\t")
    for x in range (numOfEnemies):
        print(enemyStrength[x], end = tab)
    print("")
    print("Magic:", end = tab)
    for x in range (numOfEnemies):
        print(enemyMagic[x], end = tab)
    print("")
    print("Defense:", end = "\t\t")
    for x in range (numOfEnemies):
        print(enemyDefense[x], end = tab)
    print("")
    print("Resistance:", end = "\t\t")
    for x in range (numOfEnemies):
        print(enemyStrength[x], end = tab)
    print("")
    print("Speed:", end = tab)
    for x in range (numOfEnemies):
        print(enemySpeed[x], end = tab)
    print("")
    print("Intellect:", end = "\t\t")
    for x in range (numOfEnemies):
        print(enemyIntellect[x], end = tab)
    print("")
    print("Skill:", end = tab)
    for x in range (numOfEnemies):
        print(enemySkill[x], end = tab)
    print("")
    print("HP:", end = tab)
    for x in range (numOfEnemies):
        print(enemyHP[x] , end = tab)
    print("")
    print("MP:", end = tab)
    for x in range (numOfEnemies):
        print(enemyMP[x] , end = tab)
    print("")
    print("Level:", end = tab)
    for x in range (numOfEnemies):
        print(enemyLevel[x] , end = tab)
    print("")
    input("Press Enter when you have finished viewing.")
    speedGroup = {}
    for x in range (players):
        speedGroup.update({name[x] : speed[x]})
    for x in range (numOfEnemies):
        speedGroup.update({enemyName[x] : enemySpeed[x]})

    turn = sorted(speedGroup.items(), key=lambda x : x[1], reverse = True)
    turnDict = {}
    for x in range (len(turn)):
        turnDict.update({turn[x]})

    turnOrder = []
    print(newScreen)
    print("Turn order:")
    for x in turnDict:
        print("----", end = "")
        print(x)
        turnOrder.append(x)
    time.sleep(3)
    battle = True
    while (battle == True):
        for y in range (len(turnOrder)):
            if (turnOrder[y] in name and battle == True):
                if (turnOrder[y] in alive):
                    turn = turnOrder[y]
                    if (turn in statChange):
                        print(statChange[turn])
                        #print(len(statChange[turn])/3)
                        removedstats = 0
                        for statcheck in range (1, int(len(statChange[turn])/3) + 1):
                            print(statcheck)
                            print("multiplyer: " + str(removedstats))
                            statChange[turn][(3*(statcheck - removedstats))-1] -= 1
                            if (statChange[turn][(3*(statcheck - removedstats))-1] <= 0):
                                if (statChange[turn][(3*(statcheck - removedstats))-3] == "attack"):
                                    attack[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
                                if (statChange[turn][(3*(statcheck - removedstats))-3] == "magic"):
                                    magic[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
                                if (statChange[turn][(3*(statcheck - removedstats))-3] == "defense"):
                                    defense[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
                                if (statChange[turn][(3*(statcheck - removedstats))-3] == "resistance"):
                                    resistance[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
                                if (statChange[turn][(3*(statcheck - removedstats))-3] == "speed"):
                                    speed[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
                                if (statChange[turn][(3*(statcheck - removedstats))-3] == "intellect"):
                                    intellect[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
                                if (statChange[turn][(3*(statcheck - removedstats))-3] == "skill"):
                                    skill[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
                                    
                                for x in range (3):
                                    statChange[turn].pop((3*(statcheck-removedstats))-3)
                                removedstats += 1
                    print(statChange)
                    #print("Turn: " + turn)
                    #print("Turn order: " + turnOrder[y])
                    while (turn == turnOrder[y] and battle == True):
                        print(newScreen)
                        line(20)
                        print(turn + ", it's your turn!")
                        if (turn in defend):
                            defend.remove(turn)
                        printHP(name.index(turn))
                        for x in range(6):
                            print("----", end = "")
                            if (x == 0):
                                print("Fight")
                            elif (x == 1):
                                print("Magic")
                            elif (x == 2):
                                print("Defend")
                            elif (x == 3):
                                print("Item")
                            elif (x == 4):
                                print("Check Stats")
                            elif (x == 5):
                                print("Run")
                        choice = input()
                        choice = choice.lower()
                        
                        if (choice == "fight"):
                            print ("Who?")
                            for enemyNum in range(len(enemyName)):
                                print("----", end = "")
                                print(str(enemyNum+1)+ ") " + enemyName[enemyNum])
                                print("--------HP: " + str(enemyCurrentHP[enemyNum]) + "/" + str(enemyHP[enemyNum]))
                                print("--------Hitrate: " + str(2.5*((skill[name.index(turn)]-enemySkill[enemyNum])-8)+100) + "%")
                                print()
                            choice = input()
                            if (checkNum(choice) == True):
                                choice = int(choice) - 1
                                if (choice >= 0 and choice <= len(enemyName)):
                                    if (strength[name.index(turn)] > enemyDefense[choice]):
                                        if (random.randint(0, 100) <= (2.5*((skill[name.index(turn)]-enemySkill[choice])-8)+100)):
                                            if (enemyName[choice] in defend):
                                                defendNumber = 2
                                            else:
                                                defendNumber = 1
                                            print(turn + " did " + str(int((abs(strength[name.index(turn)] - enemyDefense[choice]))/defendNumber)) + " damage to " + str(enemyName[choice]) + "!")
                                            enemyCurrentHP[choice] -= int((strength[name.index(turn)] - enemyDefense[choice])/defendNumber)
                                            turn = ""
                                        else:
                                            print("Missed!")
                                            turn = ""
                                    else:
                                        print ("No damage!")
                                        turn = ""
                                    print(enemyName[choice] + " has " + str(enemyCurrentHP[choice]) + " HP left!")
                                    time.sleep(1)
                        elif (choice == "magic"):
                            print("What Kind of Magic?")
                            for x in range (2):
                                print("----", end ="")
                                if (x == 0):
                                    print("Attack ")
                                elif(x == 1):
                                    print("Support ")
                            choice = input()
                            choice = choice.lower()
                            if (choice == "attack"):
                                for magAttack in range (len(spells[turn + "Spells"])):
                                    if (spells[turn + "Spells"][magAttack] in spellCost["1MP"]):
                                        spellMP = 1
                                        
                                    print(str(magAttack + 1) + ") " + spells[turn + "Spells"][magAttack] + " - " + str(spellMP) + "MP")
                                choice = input()
                                if (checkNum(choice) == True):
                                    choice = int(choice) - 1
                                    if (choice >= 0 and choice <= len(spells[turn + "Spells"])):
                                        spellChoice = spells[turn + "Spells"][choice]
                                        print("Who?")
                                        for enemyNum in range(len(enemyName)):
                                            print("----" + str(enemyNum + 1) + ") " + enemyName[enemyNum])
                                            print("--------HP: " + str(enemyCurrentHP[enemyNum]) + "/" + str(enemyHP[enemyNum]))
                                            print("--------Hitrate: " + str((2.5*((skill[name.index(turn)]-enemySkill[enemyNum])-8)+100) + (spellStats[spellChoice][0])) + "%")
                                            print()
                                        choice = input()
                                        if (checkNum(choice) == True):
                                            choice = int(choice) - 1
                                            #print ("choice: " + str(choice))
                                            if (choice >= 0 and choice <= len(enemyName)):
                                                """
                                                print("Magic: " + str(magic[name.index(turn)]))
                                                print("Length of resistance: " + str(re
                                                print("Resistance: " + str(resistance[choice]))
                                                """
                                                if (spells[turn + "Spells"][magAttack] in spellCost["1MP"]):
                                                    spellMP = 1
                                                currentMP[name.index(turn)] -= spellMP
                                                if ((magic[name.index(turn)] + spellStats[spellChoice][1]) > enemyResistance[choice]):
                                                    if (random.randint(0, 100) <= (2.5*((skill[name.index(turn)]-enemySkill[choice])-8)+100) + (spellStats[spellChoice][0])):
                                                        print(str(turn) + " did " + str((magic[name.index(turn)] + spellStats[spellChoice][1]) - enemyResistance[choice]) + " damage to " + str(enemyName[choice]) + "!")
                                                        enemyCurrentHP[choice] -= ((magic[name.index(turn)] + spellStats[spellChoice][1]) - enemyResistance[choice])
                                                        turn = ""
                                                    else:
                                                        print("Missed!")
                                                        turn = ""
                                                else:
                                                    print("No damage!")
                                                    turn = ""
                                                print(enemyName[choice] + " has " + str(enemyCurrentHP[choice]) + " HP left!")
                                                time.sleep(1)
                            elif (choice == "support"):
                                if (len(supportSpells[turn + "Support"]) > 0):
                                    for magSupport in range (len(supportSpells[turn + "Support"])):
                                        if (supportSpells[turn + "Support"][magSupport] in spellCost["1MP"]):
                                            spellMP = 1
                                        print(str(magSupport + 1) + ") " + supportSpells[turn + "Support"][magSupport] + " - " + str(spellMP) + "MP")
                                    choice = input()
                                    if (checkNum(choice) == True):
                                        choice = int(choice) - 1
                                        if (choice >= 0 and choice <= len(supportSpells[turn + "Support"])):
                                            spellChoice = supportSpells[turn + "Support"][choice]
                                            print("On Who?")
                                            for usedon in range (players):
                                                print("----" + str(usedon + 1) + ") " + name[usedon])
                                                print("--------HP: " + str(currentHP[usedon]) + "/" + str(HP[usedon]))
                                                print()
                                            choice = input()
                                            if (checkNum(choice) == True):
                                                choice = int(choice) - 1
                                                if ("currentHP" in supportSpellStats[spellChoice]):
                                                    #print(supportSpells)
                                                    #print(supportSpells[turn + "Support"][spellChoice])
                                                    #print(spellCost["1MP"])
                                                    if (supportSpells[turn + "Support"][supportSpells[turn + "Support"].index(spellChoice)] in spellCost["1MP"]):
                                                        MP[name.index(turn)] -= 1
                                                    newHP=currentHP[choice]+supportSpellStats[spellChoice][1]+int(magic[name.index(turn)]/2)
                                                    if (newHP > HP[choice]):
                                                        newHP = HP[choice]
                                                    print(name[choice] + " recovered " + str(newHP-currentHP[choice]) + " HP, making their total HP " + str(newHP) + "!")
                                                    
                                                    currentHP[choice] = newHP
                                                    time.sleep(1.5)
                                                    turn = ""
                                                else:
                                                    if ("attack" in supportSpellStats[spellChoice]):
                                                        if (not("attack" in statChange[name[choice]])):
                                                            attack[choice] += supportSpellStats[spellChoice][1]
                                                            statChange[name[choice]].extend(supportSpellStats[spellChoice])
                                                            print(name[choice] + "'s attack increased by " + str(supportSpellStats[spellChoice][1]) + " for " + str(supportSpellStats[spellChoice][2]) + " turns!")
                                                        else:
                                                            statChange[statChange[name[choice]].index("attack") + 2] += supportSpellStats[spellChoice][2]
                                                            print(name[choice] + "'s attack buff has increased by " + str(supportSpellStats[spellChoice][2]) + " turns!")
                                                            
                                                    if ("magic" in supportSpellStats[spellChoice]):
                                                        magic[choice] += supportSpellStats[spellChoice][1]
                                                        statChange[name[choice]].extend(supportSpellStats[spellChoice])
                                                        print(name[choice] + "'s magic increased by " + str(supportSpellStats[spellChoice][1]) + " for " + str(supportSpellStats[spellChoice][2]) + " turns!")
                                                    if ("defense" in supportSpellStats[spellChoice]):
                                                        defense[choice] += supportSpellStats[spellChoice][1]
                                                        statChange[name[choice]].extend(supportSpellStats[spellChoice])
                                                        print(name[choice] + "'s defense increased by " + str(supportSpellStats[spellChoice][1]) + " for " + str(supportSpellStats[spellChoice][2]) + " turns!")
                                                    if ("resistance" in supportSpellStats[spellChoice]):
                                                        resistance[choice] += supportSpellStats[spellChoice][1]
                                                        statChange[name[choice]].extend(supportSpellStats[spellChoice])
                                                        print(name[choice] + "'s resistance increased by " + str(supportSpellStats[spellChoice][1]) + " for " + str(supportSpellStats[spellChoice][2]) + " turns!")
                                                    if ("speed" in supportSpellStats[spellChoice]):
                                                        speed[choice] += supportSpellStats[spellChoice][1]
                                                        statChange[name[choice]].extend(supportSpellStats[spellChoice])
                                                        print(name[choice] + "'s speed increased by " + str(supportSpellStats[spellChoice][1]) + " for " + str(supportSpellStats[spellChoice][2]) + " turns!")
                                                    if ("intellect" in supportSpellStats[spellChoice]):
                                                        intellect[choice] += supportSpellStats[spellChoice][1]
                                                        statChange[name[choice]].extend(supportSpellStats[spellChoice])
                                                        print(name[choice] + "'s intellect increased by " + str(supportSpellStats[spellChoice][1]) + " for " + str(supportSpellStats[spellChoice][2]) + " turns!")
                                                    if ("skill" in supportSpellStats[spellChoice]):
                                                        skill[choice] += supportSpellStats[spellChoice][1]
                                                        statChange[turn].extend(supportSpellStats[spellChoice])
                                                        print(name[choice] + "'s skill increased by " + str(supportSpellStats[spellChoice][1]) + " for " + str(supportSpellStats[spellChoice][2]) + " turns!")
                                                    time.sleep(1.5)
                                                    turn = ""
                                else:
                                    print("No support spells!")
                                    time.sleep(1)
                                
                        elif (choice == "defend"):
                            print(turn + " has defended!")
                            defend.append(turn)
                            turn = ""
                            time.sleep(1)
                        elif (choice == "item"):
                            print("no items yet")
                        elif (choice == "checkstats" or choice == "check stats" or choice == "check" or choice == "stats"):
                            print("Who?")
                            for enemyNum in range (numOfEnemies + 1):
                                if (enemyNum in range (numOfEnemies)):
                                    print("----" + str(enemyNum + 1) + ") " + enemyName[enemyNum])
                                else:
                                    print("----" + str(enemyNum + 1) + ") Turn Order")
                            choice = input()
                            if (checkNum(choice) == True):
                                choice = int(choice) - 1
                                if (choice in range (numOfEnemies + 1)):
                                    if (choice in range (numOfEnemies - 1)):
                                        print(enemyName[choice])
                                        print("----HP: " + str(enemyCurrentHP[choice]) + "/" + str(enemyHP[choice]))
                                        print("----MP: " + str(enemyCurrentMP[choice]) + "/" + str(enemyMP[choice]))
                                        print("----Strength: " + str(enemyStrength[choice]))
                                        print("----Defense: " + str (enemyDefense[choice]))
                                        print("----Magic: " + str(enemyMagic[choice]))
                                        print("----Resistance: " + str(enemyResistance[choice]))
                                        print("----Skill: " + str(enemySkill[choice]))
                                        print("----Speed: " + str(enemySpeed[choice]))
                                        print("----Intellect: " + str(enemyIntellect[choice]))
                                        print("----Level: " + str(enemyLevel[choice]))
                                        input ("press Enter when you are finished.")
                                    elif (choice == numOfEnemies):
                                        for turnorder in turnDict:
                                            print("----", end = "")
                                            print(turnorder)
                                        input("press Enter when you are finished.")
                                    else:
                                        print("none")
                                        input("press Enter when you are finished.")
                                        
                        elif (choice == "run"):
                            print("Attempting to run", end = "")
                            for dot in range(3):
                                print(".", end = "")
                                time.sleep(.2)
                            print()
                            chance = random.randint(-50,50)
                            print("Before" + str(chance))
                            totalspeed = 0
                            for groupspeed in range (players):
                                totalspeed += speed[groupspeed]
                                totalspeed += intellect[groupspeed]
                            chance += totalspeed
                            print("After: " + str(chance))
                            if (chance > 0):
                                print("Sucessfully escaped!")
                                turn = ""
                                battle = False
                                time.sleep(1.5)
                            else:
                                print("Failed to escape!")
                                turn = ""
                                time.sleep(1.5)
                enemiesRemoved = 0
                for check in range (len(enemyName)):
                    if (enemyCurrentHP[check-enemiesRemoved] <= 0):
                        print(enemyName[check-enemiesRemoved] + " has fallen!")
                        time.sleep(.5)
                        addXP +=int((.8*(enemyLevel[check-enemiesRemoved]/(sum(level)/len(level)))**3)+20)
                        #print("XP Added: " + str(int(.8*(enemyLevel[check-enemiesRemoved]/(sum(level)/len(level)))**3)+20))
                        #turnOrder.remove(enemyName[check-enemiesRemoved])
                        enemyName.pop(check-enemiesRemoved)
                        enemyStrength.pop(check-enemiesRemoved)
                        enemyMagic.pop(check-enemiesRemoved)
                        enemyDefense.pop(check-enemiesRemoved)
                        enemyResistance.pop(check-enemiesRemoved)
                        enemySpeed.pop(check-enemiesRemoved)
                        enemyIntellect.pop(check-enemiesRemoved)
                        enemySkill.pop(check-enemiesRemoved)
                        enemyHP.pop(check-enemiesRemoved)
                        enemyCurrentHP.pop(check-enemiesRemoved)
                        enemyMP.pop(check-enemiesRemoved)
                        enemyCurrentMP.pop(check-enemiesRemoved)
                        enemyLevel.pop(check-enemiesRemoved)
                        enemiesRemoved += 1
                        numOfEnemies -= 1
                        if (len(enemyName) == 0):
                            battle = False
                for check in range (players):
                    if (currentHP[check] <= 0 and name[check] in alive):
                        currentHP[check] = 0
                        print(name[check] + " has fallen!")
                        time.sleep(1.5)
                        alive.remove(name[check])
                if (alive == "[]"):
                    print("There are none left to fight!")
                    time.sleep(1)
                    print("Game Over")
                    sys.exit()
                    
                if (enemyName == ""):
                    battle = False
            if (len(enemyName) > 0):
                if (turnOrder[y] in enemyName and battle == True):
                    turn = turnOrder[y]
                    line()
                    if (turn in defend):
                        defend.remove(turn)
                    enfluence = -35*(((enemyCurrentHP[enemyName.index(turn)] / enemyHP[enemyName.index(turn)])-1)**2)+100
                    #print("Percent: " + str(enfluence) + "%")
                    enemyChoice = random.randint(1, 100)
                    #print("Number: " + str(enemyChoice) + "%")
                    
                    if (enemyChoice <= enfluence):
                        enemyChoice = random.randint(1,5)
                        enemyChoice = 2
                        if (enemyMagic[enemyName.index(turn)] > enemyStrength[enemyName.index(turn)]):
                            if (enemyChoice == 1):
                                print(turn + " chose fight!")
                                enemyChoice = "fight"
                            else:
                                print(turn + " chose magic!")
                                enemyChoice = "magic"
                        else:
                            if (enemyChoice == 1):
                                print(turn + " chose magic!")
                                enemyChoice = "magic"
                            else:
                                print(turn + " chose fight!")
                                enemyChoice = "fight"
                                
                        if (enemyChoice == "fight"):
                            enemyChoice = random.randint(0, players-1)
                            while ((name[enemyChoice] in alive) == False):
                                enemyChoice = random.randint(0, players-1)
                            if (name[enemyChoice] in alive):
                                if (enemyStrength[enemyName.index(turn)] > defense[enemyChoice]):
                                    if (random.randint(0, 100) <= (2.5*((enemySkill[enemyName.index(turn)]-skill[enemyChoice])-8)+100)):
                                        if (name[enemyChoice] in defend):
                                            defendNumber = 2
                                        else:
                                            defendNumber = 1
                                        print(turn + " did " + str(int((enemyStrength[enemyName.index(turn)]-defense[enemyChoice])/defendNumber)) + " damage to " + name[enemyChoice] + "!")
                                        currentHP[enemyChoice] -=int((enemyStrength[enemyName.index(turn)]-defense[enemyChoice])/defendNumber)
                                        turn = ""
                                    else:
                                        print(turn + " missed!")
                                        turn = ""
                                else:
                                    print(turn + " did 0 damage to " + name[enemyChoice])
                                    turn = ""
                            else:
                                print("???")
                        elif (enemyChoice == "magic"):
                            print("Magic is not implemented yet!")
                            enemyChoice = random.randint(1, 100)
                            if (len(enemySupportSpells[enemyName[enemyName.index(turn)]])):
                                pernumber = 100
                            else:
                                pernumber = 80
                            if (enemyChoice <= pernumber):
                                enemyChoice = random.randint(1,len(enemySpells[turn]))
                                enemyChoice -= 1
                                enemySpellChoice = enemySpells[turn][enemyChoice]
                                enemyChoice = random.randint(0, players-1)
                                while ((name[enemyChoice] in alive) == False):
                                    enemyChoice = random.randint(0, players-1)
                                if (name[enemyChoice] in alive):
                                    if ((enemyMagic[enemyName.index(turn)] + spellStats[enemySpellChoice][1]) > resistance[enemyChoice]):
                                        if (random.randint(0, 100) <= (2.5*((enemySkill[enemyName.index(turn)]-skill[enemyChoice])-8)+100) + (spellStats[enemySpellChoice][0])):
                                            print(str(turn) + " did " + str((enemyMagic[enemyName.index(turn)] + spellStats[enemySpellChoice][1]) - resistance[enemyChoice]) + " damage to " + str(name[enemyChoice]) + "!")
                                            CurrentHP[enemyChoice] -= ((enemyMagic[enemyName.index(turn)] + spellStats[enemySpellChoice][1]) - resistance[enemyChoice])
                                    else:
                                        print(enemyName[enemyName.index(turn)] + " did 0 damage to " + name[enemyChoice])
                                        
                                turn = ""    
                            else:
                                enemyChoice = random.randint(1,len(enemySpells[turn]))
                                enemyChoice -= 1
                                enemySpellChoice = enemySupportSpells[turn][enemyChoice]
                                enemyChoice = random.randint(0, len(enemyName)-1)
                                print(enemyName[enemyChoice] + " was imaginally healed by " + turn + "!")
                                turn = ""
                    else:
                        enemyChoice = random.randint(1, 5)
                        if (enemyChoice <= 2):
                            print(turn + " is trying to escape!")
                            turn = ""
                        else:
                            print(turn + " is defending!")
                            defend.append(turn)
                            turn = ""
                    time.sleep(1)
                    
                    enemiesRemoved = 0
                for check in range (len(enemyName)):
                    if (enemyCurrentHP[check-enemiesRemoved] <= 0):
                        print(enemyName[check-enemiesRemoved] + " has fallen!")
                        time.sleep(.5)
                        addXP +=int((.8*(enemyLevel[check-enemiesRemoved]/(sum(level)/len(level)))**3)+20)
                        #print("XP Added: " + str(int(.8*(enemyLevel[check-enemiesRemoved]/(sum(level)/len(level)))**3)+20))
                        turnOrder.remove(enemyName[check-enemiesRemoved])
                        enemyName.pop(check-enemiesRemoved)
                        enemyStrength.pop(check-enemiesRemoved)
                        enemyMagic.pop(check-enemiesRemoved)
                        enemyDefense.pop(check-enemiesRemoved)
                        enemyResistance.pop(check-enemiesRemoved)
                        enemySpeed.pop(check-enemiesRemoved)
                        enemyIntellect.pop(check-enemiesRemoved)
                        enemySkill.pop(check-enemiesRemoved)
                        enemyHP.pop(check-enemiesRemoved)
                        enemyCurrentHP.pop(check-enemiesRemoved)
                        enemyMP.pop(check-enemiesRemoved)
                        enemyCurrentMP.pop(check-enemiesRemoved)
                        enemyLevel.pop(check-enemiesRemoved)
                        numOfEnemies -= 1
                        enemiesRemoved += 1
                for check in range (players):
                    if (currentHP[check] <= 0 and name[check] in alive):
                        currentHP[check] = 0
                        print(name[check] + " has fallen!")
                        time.sleep(1.5)
                        alive.remove(name[check])
                if (alive == "[]"):
                    print("There are none left to fight!")
                    time.sleep(1)
                    print("Game Over")
                    sys.exit()

    removedstats = 0
    if (statcheck != []):
        print (statcheck)
        for statcheck in range (1, int(len(statChange[turn])/3) + 1):
            if (statChange[turn][(3*(statcheck - removedstats))-3] == "attack"):
                attack[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
            if (statChange[turn][(3*(statcheck - removedstats))-3] == "magic"):
                magic[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
            if (statChange[turn][(3*(statcheck - removedstats))-3] == "defense"):
                defense[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
            if (statChange[turn][(3*(statcheck - removedstats))-3] == "resistance"):
                resistance[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
            if (statChange[turn][(3*(statcheck - removedstats))-3] == "speed"):
                speed[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
            if (statChange[turn][(3*(statcheck - removedstats))-3] == "intellect"):
                intellect[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
            if (statChange[turn][(3*(statcheck - removedstats))-3] == "skill"):
                skill[name.index(turn)] -= statChange[turn][(3*(statcheck - removedstats))-2]
            
        for x in range (3):
            statChange[turn].pop((3*(statcheck-removedstats))-3)
        removedstats += 1
    print("XP earned: " + str(addXP))
    for gain in range (players):
        if (currentHP[gain] > 0):
            XP[gain] += addXP
    time.sleep(1)
    levelUP()

def enemies(number = 3):
    global enemyName
    global enemyStrength
    global enemyMagic
    global enemyDefense
    global enemyResistance
    global enemySpeed
    global enemyIntellect
    global enemySkill
    global enemyHP
    global enemyCurrentHP
    global enemyMP
    global enemyCurrentMP
    global enemyLevel
    global level
    global players
    global totalLevel
    global difficulty
    global enemySpells
    global enemySupportSpells
    totalLevel = 0
    enemyName = []
    enemyStrength = []
    enemyMagic = []
    enemyDefense = []
    enemyResistance = []
    enemySpeed = []
    enemyIntellect = []
    enemySkill = []
    enemyHP = []
    enemyMP = []
    enemyLevel = []
    enemySpells = {}
    enemySupportSpells = {}
    
    estats = open("Enemy Stats.txt", "r")
    enemyNames = estats.readline()
    enemyNames = enemyNames.split(", ")
    enemyStrengths = estats.readline()
    enemyStrengths = enemyStrengths.split(", ")
    enemyMagics = estats.readline()
    enemyMagics = enemyMagics.split(", ")
    enemyDefenses = estats.readline()
    enemyDefenses = enemyDefenses.split(", ")
    enemyResistances = estats.readline()
    enemyResistances = enemyResistances.split(", ")
    enemySpeeds = estats.readline()
    enemySpeeds= enemySpeeds.split(", ")
    enemyIntellects = estats.readline()
    enemyIntellects = enemyIntellects.split(", ")
    enemySkills = estats.readline()
    enemySkills = enemySkills.split(", ")
    enemyHPs = estats.readline()
    enemyHPs = enemyHPs.split(", ")
    enemyMPs = estats.readline()
    enemyMPs = enemyMPs.split(", ")
    estats.close()

    estats = open("Enemy Growth Rates.txt", "r")
    GenemyNames = estats.readline()
    GenemyNames = GenemyNames.split(", ")
    GenemyStrengths = estats.readline()
    GenemyStrengths = GenemyStrengths.split(", ")
    GenemyMagics = estats.readline()
    GenemyMagics = GenemyMagics.split(", ")
    GenemyDefenses = estats.readline()
    GenemyDefenses = GenemyDefenses.split(", ")
    GenemyResistances = estats.readline()
    GenemyResistances = GenemyResistances.split(", ")
    GenemySpeeds = estats.readline()
    GenemySpeeds= GenemySpeeds.split(", ")
    GenemyIntellects = estats.readline()
    GenemyIntellects = GenemyIntellects.split(", ")
    GenemySkills = estats.readline()
    GenemySkills = GenemySkills.split(", ")
    GenemyHPs = estats.readline()
    GenemyHPs = GenemyHPs.split(", ")
    GenemyMPs = estats.readline()
    GenemyMPs = GenemyMPs.split(", ")
    estats.close()

    for x in range (players):
        totalLevel += int(level[x])    
    totalLevel = round(totalLevel/players)
    if (difficulty == "easy"):
        totalLevel -= 2
        if (totalLevel < 1):
            totalLevel = 1
    elif (difficulty == "hard"):
        totalLevel += 2
    totalLevel -= 1
    for x in range (number):
        enemyChosen = random.randint(0, 4)
        if (enemyNames[enemyChosen] in enemyName):
            totnum = 2
            while (enemyNames[enemyChosen] + " " + str(totnum) in enemyName):
                totnum += 1
            enemyName.append(enemyNames[enemyChosen] + " " + str(totnum))
        else:
            enemyName.append(enemyNames[enemyChosen])
        enemyStrength.append(int(enemyStrengths[enemyChosen]) + round(int(GenemyStrengths[enemyChosen])/100*totalLevel))
        enemyMagic.append(int(enemyMagics[enemyChosen]) + round(int(GenemyMagics[enemyChosen])/100*totalLevel))
        enemyDefense.append(int(enemyDefenses[enemyChosen]) + round(int(GenemyDefenses[enemyChosen])/100*totalLevel))
        enemyResistance.append(int(enemyResistances[enemyChosen]) + round(int(GenemyResistances[enemyChosen])/100*totalLevel))
        enemySpeed.append(int(enemySpeeds[enemyChosen]) + round(int(GenemySpeeds[enemyChosen])/100*totalLevel))
        enemyIntellect.append(int(enemyIntellects[enemyChosen]) + round(int(GenemyIntellects[enemyChosen])/100*totalLevel))
        enemySkill.append(int(enemySkills[enemyChosen]) + round(int(GenemySkills[enemyChosen])/100*totalLevel))
        enemyHP.append(int(enemyHPs[enemyChosen]) + round(int(GenemyHPs[enemyChosen])/100*totalLevel))
        enemyMP.append(int(enemyMPs[enemyChosen]) + round(int(GenemyMPs[enemyChosen])/100*totalLevel))
        enemyLevel.append(totalLevel+1)
        enemySpells.update({enemyName[x] : []})
        enemySupportSpells.update({enemyName[x] : []})
        if (enemyChosen == 4):
            enemySpells[enemyName[x]].extend(["Ice", "Fire", "Wind"])
            enemySupportSpells[enemyName[x]].extend(["Heal", "DefUP"])
            if (enemyLevel[x] >= 3):
                enemySupportSpells[enemyName[x]].append("AtkUP")
            if (enemyLevel[x] >= 5):
                enemySpells[enemyName[x]].append("Lightning")
                enemySupportSpells[enemyName[x]].append("SpdUP")
        else:
            enemySpells[enemyName[x]].append("Ice")
            if (enemyLevel[x] >= 3):
                enemySpells[enemyName[x]].append("Fire")
                enemySupportSpells[enemyName[x]].append("Heal")
            if (enemyLevel[x] >= 4):
                enemySupportSpells[enemyName[x]].append("DefUP")
            if (enemyLevel[x] >= 5):
                enemySpells[enemyName[x]].append("Wind")
            if (enemyLevel[x] >= 6):
                enemySupportSpells[enemyName[x]].append("AtkUP")
            if (enemyLevel[x] >= 8):
                enemySupportSpells[enemyName[x]].append("SpdUP")
            if (enemyLevel[x] >= 10):
                enemySpells[enemyName[x]].append("Lightning")
                
            
    enemyCurrentHP = list(enemyHP)
    enemyCurrentMP = list(enemyMP)
    totalLevel += 1
    
def checkStats():
    global HP
    global currentHP
    global MP
    global currentMP
    for x in range (players):
        if (currentHP[x] > HP[x]):
            currentHP[x] = HP[x]
        if (currentMP[x] > MP[x]):
            currentMP[x] = MP[x]

def addInStats (numOfClass = 0):   
    importStats = open("Ally Stats.txt", "r")
    global strength
    global magic
    global defense
    global resistance
    global speed
    global intellect
    global skill
    global HP
    global MP
    addStats = importStats.readline()
    addStats = importStats.readline()
    addStats = addStats.split(", ")
    strength.append(int(addStats[numOfClass]))
    addStats = importStats.readline()
    addStats = addStats.split(", ")
    magic.append(int(addStats[numOfClass]))
    addStats = importStats.readline()
    addStats = addStats.split(", ")
    defense.append(int(addStats[numOfClass]))
    addStats = importStats.readline()
    addStats = addStats.split(", ")
    resistance.append(int(addStats[numOfClass]))
    addStats = importStats.readline()
    addStats = addStats.split(", ")
    speed.append(int(addStats[numOfClass]))
    addStats = importStats.readline()
    addStats = addStats.split(", ")
    intellect.append(int(addStats[numOfClass]))
    addStats = importStats.readline()
    addStats = addStats.split(", ")
    skill.append(int(addStats[numOfClass]))
    addStats = importStats.readline()
    addStats = addStats.split(", ")
    HP.append(int(addStats[numOfClass]))
    addStats = importStats.readline()
    addStats = addStats.split(", ")
    MP.append(int(addStats[numOfClass]))
    
def outputTheStats (numOfClass):
    global strength
    global magic
    global defense
    global resistance
    global speed
    global intellect
    global skill
    global HP
    global MP
    for x in range (2):
        if (x == 0):
            print("Starting Stats:")
            showStats = open("Ally Stats.txt", "r")
        if (x == 1):
            print("Growth Rates:")
            showStats = open("Ally Growth Rates.txt", "r")
        DisplayStats = showStats.readline()
        DisplayStats = showStats.readline()
        DisplayStats = DisplayStats.split(", ")
        print("\tStrength:\t\t" + str(DisplayStats[numOfClass]))
        DisplayStats = showStats.readline()
        DisplayStats = DisplayStats.split(", ")
        print("\tMagic:\t\t\t" + str(DisplayStats[numOfClass]))
        DisplayStats = showStats.readline()
        DisplayStats = DisplayStats.split(", ")
        print("\tDefense:\t\t" + str(DisplayStats[numOfClass]))
        DisplayStats = showStats.readline()
        DisplayStats = DisplayStats.split(", ")
        print("\tResistance:\t\t" + str(DisplayStats[numOfClass]))
        DisplayStats = showStats.readline()
        DisplayStats = DisplayStats.split(", ")
        print("\tSpeed:\t\t\t" + str(DisplayStats[numOfClass]))
        DisplayStats = showStats.readline()
        DisplayStats = DisplayStats.split(", ")
        print("\tIntellect:\t\t" + str(DisplayStats[numOfClass]))
        DisplayStats = showStats.readline()
        DisplayStats = DisplayStats.split(", ")
        print("\tSkill:\t\t\t" + str(DisplayStats[numOfClass]))
        DisplayStats = showStats.readline()
        DisplayStats = DisplayStats.split(", ")
        print("\tHP:\t\t\t" + str(DisplayStats[numOfClass]))
        DisplayStats = showStats.readline()
        DisplayStats = DisplayStats.split(", ")
        print("\tMP:\t\t\t" + str(DisplayStats[numOfClass]))
        showStats.close()
        print("")
    
def printHP(charNumber):
    remainder = 0
    print(str(name[charNumber]) + "| Level: " + str(level[charNumber]) + ", XP: " + str(XP[charNumber]))
    print("    HP: " + str(currentHP[charNumber]) + "/" + str(HP[charNumber]))
    print("        ", end = "")
    if (currentHP[charNumber]<= 0):
        for x in range (int(HP[charNumber]/5)):
            print(HPEmpty, end = "")
    elif (currentHP[charNumber] < 5):
        print(HPHalf, end = "")
        for x in range (math.ceil(HP[charNumber]/5-1)):
            print(HPEmpty, end = "")
    else:
        for x in range (int(math.floor(currentHP[charNumber]/5))):
            print (HPFull, end = "")
        if (currentHP[charNumber] %5 != 0):
            print(HPHalf, end = "")
            remainder = 1
        #print("number" + str(math.ceil(HP[charNumber]/5) - math.floor(currentHP[charNumber]/5)))
        for x in range ((math.ceil(HP[charNumber]/5) - math.floor(currentHP[charNumber]/5)) - remainder):
            print(HPEmpty, end = "")
    print("")
    remainder = 0
    print("    MP: " + str(currentMP[charNumber]) + "/" +str(MP[charNumber]))
    print("        ", end = "")
    if (currentMP[charNumber] <= 0):
        for x in range (int(MP[charNumber]/5)):
            print(MPEmpty, end = "")
    elif (currentMP[charNumber] < 5):
        print(MPFull, end = "")
        for x in range (math.ceil(MP[charNumber]/5-1)):
            print(MPEmpty, end = "")
    else:
        for x in range (int(math.floor(currentMP[charNumber]/5))):
            print (MPFull, end = "")
        for x in range (int(math.ceil((MP[charNumber]-currentMP[charNumber])/5))):
            print(MPEmpty, end = "")
    
    
    print("")
def save ():
    savesOpen = open("Saves.txt", "w")
    savesOpen.write(str(players) + "\n")
    for x in range (players):
        savesOpen.write(str(name[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(group[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(strength[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(magic[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(defense[x]) +  ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(resistance[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(speed[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(intellect[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(skill[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(HP[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(currentHP[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(MP[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(currentMP[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(level[x]) + ", ")
    savesOpen.write("\n")
    for x in range (players):
        savesOpen.write(str(XP[x]) + ", ")
    savesOpen.write("\n")
    savesOpen.write(str(spells))
    savesOpen.write("\n")
    savesOpen.write(str(supportSpells))
    savesOpen.write("\n")
    savesOpen.close()

def line (length = 10):
    for numOfLines in range (length):
        print ("-", end = "")
    print("")
def checkNum (thingToCheck):
    if (thingToCheck.isdigit() == True):
        return(True)
    else:
        return(False)
        
def menu ():
    global NG
    global LG
    global sett
    global ex
    NG = 10
    LG = 10
    sett = 10
    ex = 10
    
    savesOpen = open("Saves.txt", "r")
    savesLine = savesOpen.readline()
    menuNum = 0
    
    menuNum += 1
    print(str(menuNum) + ") New Game")
    NG = menuNum
    
    if (savesLine != ""):
        menuNum += 1
        print(str(menuNum) + ") Load Game")
        LG = menuNum
        
    menuNum += 1
    print(str(menuNum) + ") Settings")
    sett = menuNum
    
    menuNum += 1
    print(str(menuNum) + ") Exit")
    ex = menuNum

    global menuChoice
    menuChoice = input()
    
    if (menuChoice.isdigit() == True):
        menuChoice = int(menuChoice)
        if (menuChoice <=menuNum):
            if (menuChoice == NG):
                newGame()
                
            if (menuChoice == LG):
                menuChoice = LG
            if (menuChoice == sett):
                print("Settings")
                
            if (menuChoice == ex):
                sys.exit()
        else:
            menu()
    else:
        menu()
    savesOpen.close()
    
def newGame ():

    global name
    name = []
    global group
    group = []
    global strength
    strength = []
    global magic
    magic = []
    global defense
    defense = []
    global resistance
    resistance = []
    global speed
    speed = []
    global intellect
    intellect = []
    global skill
    skill = []
    global HP
    HP = []
    global currentHP
    currentHP = []
    global MP
    MP = []
    global currentMP
    currentMP = []
    global level
    level = []
    global XP
    XP = []
    global players
    
    players = 0
    while (players == 0):
        print("How many players?")
        players = input()
        if (players.isdigit() == True):
            players = int(players)
        else:
            players = 0
    for numPlayers in range (players):
        sure = "no"
        while (sure != "yes"):
            print("What is player " + str(numPlayers + 1) + "'s name?")
            plrName = input()
            plrName = plrName.capitalize()
            print("You have chosen " + str(plrName) + ". Are you sure?")
            sure = input()
            sure = sure.lower()
            if (sure == "yes"):
                name.append(plrName)
                
        sure = "no"
        while (sure != "yes"):
            print("What class do you want to be in?")
            print("Mercenary")
            print("Thief")
            print("Knight")
            print("Fighter")
            print("Soldier")
            print("Mage")
            plrClass = input()
            plrClass = plrClass.lower()
            if (plrClass == "mercenary"):
                sure = "check"
                while (sure == "check"):
                    print("Enter 'Check' to check this class's stats.")
                    print("Are you sure you want to use this class?")
                    sure = input()
                    sure = sure.lower()
                    if (sure == "yes"):
                        group.append("Mercenary")
                    if (sure == "check"):
                        outputTheStats(0)

            if (plrClass == "thief"):
                sure = "check"
                while (sure == "check"):
                    print("Enter 'Check' to check this class's stats.")
                    print("Are you sure you want to use this class?")
                    sure = input()
                    sure = sure.lower()
                    if (sure == "yes"):
                        group.append("Thief")
                    if (sure == "check"):
                        outputTheStats(1)

            if (plrClass == "knight"):
                sure = "check"
                while (sure == "check"):
                    print("Enter 'Check' to check this class's stats.")
                    print("Are you sure you want to use this class?")
                    sure = input()
                    sure = sure.lower()
                    if (sure == "yes"):
                        group.append("Knight")
                    if (sure == "check"):
                        outputTheStats(2)

            if (plrClass == "fighter"):
                sure = "check"
                while (sure == "check"):
                    print("Enter 'Check' to check this class's stats.")
                    print("Are you sure you want to use this class?")
                    sure = input()
                    sure = sure.lower()
                    if (sure == "yes"):
                        group.append("Fighter")
                    if (sure == "check"):
                        outputTheStats(3)

            if (plrClass == "soldier"):
                sure = "check"
                while (sure == "check"):
                    print("Enter 'Check' to check this class's stats.")
                    print("Are you sure you want to use this class?")
                    sure = input()
                    sure = sure.lower()
                    if (sure == "yes"):
                        group.append("Soldier")
                    if (sure == "check"):
                        outputTheStats(4)
            
            if (plrClass == "mage"):
                sure = "check"
                while (sure == "check"):
                    print("Enter 'Check' to check this class's stats.")
                    print("Are you sure you want to use this class?")
                    sure = input()
                    sure = sure.lower()
                    if (sure == "yes"):
                        group.append("Mage")
                    if (sure == "check"):
                        outputTheStats(5)
                        
        if (plrClass == "mercenary"):
            addInStats(0)
            
        elif (plrClass == "thief"):
            addInStats(1)

        elif (plrClass == "knight"):
            addInStats(2)

        elif (plrClass == "fighter"):
            addInStats(3)

        elif (plrClass == "soldier"):
            addInStats(4)

        elif (plrClass == "mage"):
            addInStats(5)
            
        level.append(1)
        XP.append(0)
    currentHP = list(HP)
    currentMP = list(MP)
def printStats (stat, tab = "\t\t\t"):
    for Print in range (players):
        thingToCheck = str(stat[Print])
        if (checkNum(thingToCheck) == False):
            if (len(stat[Print]) >= 16):
                tab = "\t"
            elif (len(stat[Print]) >= 8):
                tab = "\t\t"
            else:
                tab = "\t\t\t"
        print(stat[Print], end = tab)
        
menu()
if (menuChoice == LG):
    with open("Saves.txt", "r") as savesOpen:
        savesLine = savesOpen.readline()
        players = int(savesLine)
        savesLine = savesOpen.readline()
        name = savesLine
        name = name.split(", ")
        
        savesLine = savesOpen.readline()
        group = savesLine
        group = group.split(", ")
        
        savesLine = savesOpen.readline()
        strength = savesLine
        strength = strength.split(", ")
        for x in range (players):
            strength[x] = int(strength[x])
        strength.pop(len(strength)-1)

        savesLine = savesOpen.readline()
        magic = savesLine
        magic = magic.split(", ")
        for x in range (players):
            magic[x] = int(magic[x])
        magic.pop(len(magic)-1)
            
        savesLine = savesOpen.readline()
        defense = savesLine
        defense = defense.split(", ")
        for x in range (players):
            defense[x] = int(defense[x])
        defense.pop(len(defense)-1)
            
        savesLine = savesOpen.readline()
        resistance = savesLine
        resistance = resistance.split(", ")
        for x in range (players):
            resistance[x] = int(resistance[x])
        resistance.pop(len(resistance)-1)
            
        savesLine = savesOpen.readline()
        speed = savesLine
        speed = speed.split(", ")
        for x in range (players):
            speed[x] = int(speed[x])
        speed.pop(len(speed)-1)
            
        savesLine = savesOpen.readline()
        intellect = savesLine
        intellect = intellect.split(", ")
        for x in range (players):
            intellect[x] = int(intellect[x])
        intellect.pop(len(intellect)-1)

        savesLine = savesOpen.readline()
        skill = savesLine
        skill = skill.split(", ")
        for x in range (players):
            skill[x] = int(skill[x])
        skill.pop(len(skill)-1)

        savesLine = savesOpen.readline()
        HP = savesLine
        HP = HP.split(", ")
        for x in range (players):
            HP[x] = int(HP[x])
        HP.pop(len(HP)-1)

        savesLine = savesOpen.readline()
        currentHP = savesLine
        currentHP = currentHP.split(", ")
        for x in range (players):
            currentHP[x] = int(currentHP[x])
        currentHP.pop(len(currentHP)-1)

        savesLine = savesOpen.readline()
        MP = savesLine
        MP = MP.split(", ")
        for x in range (players):
            MP[x] = int(MP[x])
        MP.pop(len(MP)-1)

        savesLine = savesOpen.readline()
        currentMP = savesLine
        currentMP = currentMP.split(", ")
        for x in range (players):
            currentMP[x] = int(currentMP[x])
        currentMP.pop(len(currentMP)-1)
            
        savesLine = savesOpen.readline()
        level = savesLine
        level = level.split(", ")
        for x in range (players):
            level[x] = int(level[x])
        level.pop(len(level)-1)

        savesLine = savesOpen.readline()
        XP = savesLine
        XP = XP.split(", ")
        for x in range (players):
            XP[x] = int(XP[x])
        XP.pop(len(XP)-1)

        savesLine = savesOpen.readline()
        spells = literal_eval(savesLine)

        savesLine = savesOpen.readline()
        supportSpells = literal_eval(savesLine)

if (menuChoice == NG):
    for startingSpells in range (players):
        spells.update({name[startingSpells] + "Spells" : ["Ice"]})
        if (group[startingSpells] == "Mage"):
            spells[name[startingSpells] + "Spells"].extend(["Fire", "Wind"])

    for startingSupport in range (players):
        supportSpells.update({name[startingSupport] + "Support" : []})
        if (group[startingSupport] == "Mage"):
            supportSpells[name[startingSupport] + "Support"].extend(["Heal", "DefUP"])
      
#print(spells)
#print(supportSpells)
#print(menuChoice)

line(25)
print("Name: ", end = tab)
printStats(name)
print("")
print("Class: ", end = tab)
printStats(group)
print("")
print("Strength: ", end = "\t\t")
printStats(strength)
print("")
print("Magic: ", end = tab)
printStats(magic)
print("")
print("Defense: ", end = "\t\t")
printStats(defense)
print("")
print("Resistance: ", end = "\t\t")
printStats(resistance)
print("")
print("Speed: ", end = tab)
printStats(speed)
print("")
print("Intellect: ", end = "\t\t")
printStats(intellect)
print("")
print("Skill: ", end = tab)
printStats(skill)
print("")
print("HP: ", end = tab)
printStats(HP)
print("")
print("MP: ", end = tab)
printStats(MP)
print("")
print("Level: ", end = tab)
printStats(level)
print("")
print("XP: ", end = tab)
printStats(XP)
print("")
print("Press Enter when you have finished viewing your stats.")
input()
if (currentHP > HP):
    currentHP = list(HP)
    print("Higher HP")
if (currentMP > MP):
    currentMP = list(MP)
    print("Higher MP")

if (menuChoice == NG):
    choice = "sdf"
    while (choice != "yes" and choice != "no"):
        print("Would you like to save your progress?")
        choice = input()
        choice = choice.lower()
        if (choice == "yes"):
            save()
            print ("Saved!")
            time.sleep(1)
        elif (choice == "no"):
            choice = "no"

playing = True
while (playing == True):
    alive = []
    for character in range (players):
        if (currentHP[character] > 0):
            alive.append(name[character])
    print(newScreen)
    line(35)
    #print(alive)
    checkStats()
    for x in range(players):
        printHP(x)
              
    print ("What do you want to do?")
    time.sleep(.5)
    print ("--Fight")
    print ("--Sleep")
    print ("--Settings")
    print ("--Stop")
    choice = input("")
    choice = choice.lower()
    if (choice == "fight"):
        print("Fight")
        choice = "alsdf"
        difficulty = "Tax Extension"
        while (choice != "random" and choice != "custom" and choice != "boss" and choice != ""):
            print ("Random, custom, or boss fight? Leave blank to exit")
            choice = input()
            choice = choice.lower()
            if (choice == "random"):
                difficulty = random.randint(1,3)
                if (difficulty == 1):
                    difficulty = "easy"
                if (difficulty == 2):
                    difficulty = "normal"
                if (difficulty == 3):
                    difficulty = "hard"
            elif (choice == "custom"):
                while (difficulty != "easy" and difficulty != "normal" and difficulty != "hard"):
                    print("Easy, normal, or hard?")
                    difficulty = input()
                    difficulty.lower()
            elif (choice == "boss"):
                difficulty = "boss"
        if (choice != ""):
            if (players <= 2):
                numOfEnemies = random.randint(1, players+2)
                enemies(numOfEnemies)
            else:
                numOfEnemies = random.randint(players-2, players +2)
                enemies(numOfEnemies)
            battle()
        
    elif (choice == "sleep"):
        print("Sleeping", end = "")
        for x in range (3):
            time.sleep(.2)
            print(".", end = "")
        print()
        currentHP = list(HP)
        currentMP = list(MP)
        
    elif (choice == "settings"):
        print("Settings")
        
    elif (choice == "stop"):
        choice = "sdf"
        while (choice != "yes" and choice != "no"):
            print("Would you like to save your progress?")
            choice = input()
            choice = choice.lower()
            if (choice == "yes"):
                save()
                print ("Saved!")
                time.sleep(.1)
            elif (choice == "no"):
                choice = "no"
        
        print("Stopping", end = "")
        for x in range (3):
            time.sleep(.4)
            print(".", end = "")
        sys.exit()

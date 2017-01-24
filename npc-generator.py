# Module for the GM tools
import random
import sys
import namegen

races = {1: 'Human', 2: 'Hill Dwarf', 3: 'Mountain Dwarf', 4: 'Wood Elf',
            5: 'Half-Elf', 6: 'Half-Orc', 7: 'Dragonborn', 8: 'Tiefling',
            9:  'Forest Gnome', 10: 'Rock Gnome', 11: 'Stout Halfling',
            12: 'LightFoot Halfling', 13: 'Drow', 14: 'High Elf'}

alignments = {1: 'True Neutral', 2: 'Neutral Good', 3: 'Neutral Evil',
                4: 'Lawful Neutral', 5: 'Lawful Good', 6: 'Lawful Evil',
                7: 'Chaotic Neutral', 8: 'Chaotic Good', 9: 'Chaotic Evil'}

appearances = {1: 'Wears earrings', 2: 'Wears necklace', 3: 'Wears circlet',
                4: 'Wears bracelets', 5: 'Wears piercings',
                6: 'Wears Flamboyant clothes', 7: 'Wears an outlandish garb',
                8: 'Wears Formal, clean clothes',
                9: 'Wears Ragged, dirty clothes',
                10: 'Has a pronounced scar', 11: 'Has some missing teeth',
                12: 'Has a missing finger', 13: 'Has an unusual eye color',
                14: 'Has heterochromy', 15: 'Wears Tattoos',
                16: 'Has a Birthmark', 17: 'Has an unusual skin color',
                18: 'Is bald', 19: 'Is braided beard or hair',
                20: 'Has an unusual hair color', 21: 'Has a nervous eye twitch',
                22: 'Has a Distinctive nose',
                23: 'Has a distinctive posture (crooked or rigid)',
                24: 'Is exceptionally beautiful', 25: 'Is exceptionally ugly'}

talents = {1: 'Plays a musical instrument',
            2: 'Speaks several languages fluently',
            3: 'Unbelievably lucky', 4: 'Perfect memory',
            5: 'Great with animals', 6: 'Great with children',
            7: 'Great at solving puzzles', 8: 'Great at one game',
            9: 'Great at impersonations', 10: 'Draws beautifully',
            11: 'Paints beautifully', 12: 'Sings beautifully',
            13: 'Drinks everyone under the table', 14: 'Expert carpenter',
            15: 'Expert cook', 16: 'Expert dart thrower and rock skipper',
            17: 'Expert juggler', 18: 'Skilled actor and master of disguise',
            19: 'Skilled dancer', 20: 'Knows thieves\' cant'}

mannerisms = {1: 'Prone to singing, whistling, or humming quietly',
                2: 'Speaks in rhyme or some other peculiar way',
                3: 'Particularly low or high voice',
                4: 'Slurs words, lisps, or stutters',
                5: 'Enunciates overly clearly', 6: 'Speaks loudly',
                7: 'Whispers', 8: 'Uses flowery speech or long words',
                9: 'Frequently uses the wrong word',
                10: 'Uses colorful oaths and exclamations',
                11: 'Makes constant jokes or puns',
                12: 'Prone to predictions of doom', 13: 'Fidgets', 14: 'Squints',
                15: 'Stares into the distance', 16: 'Chews something',
                17: 'Paces', 18: 'Taps fingers', 19: 'Bites fingernails',
                20: 'Twirls hair or tugs beard'}

traits = {1: 'Argumentative',  7: 'Honest', 2: 'Arrogant', 8: 'Hot tempered',
            3: 'Blustering', 9: 'Irritable', 4: 'Rude', 10: 'Ponderous',
            5: 'Curious', 11: 'Quiet', 6: 'Friendly', 12: 'Suspicious'}

bonds = {1: 'Dedicated to fulfilling a personal life goal',
         2: 'Protective of close family members',
         3: 'Protective of colleagues or compatriots',
         4: 'Loyal to a benefactor, patron, or employer',
         5: 'Captivated by a romantic interest', 6: 'Drawn to a special place',
         7: 'Protective of a sentimental keepsake',
         8: 'Protective of a valuable possession', 9: 'Out for revenge'}

flaws = {1: 'Forbidden love or susceptibility to romance',
         2: 'Enjoys decadent pleasures', 3: 'Arrogance',
         4: 'Envies another creature\'s possessions or status',
         5: 'Overpowering greed', 6: 'Prone to rage', 7: 'Has a powerful enemy',
         8: 'Specific phobia', 9: 'Shameful or scandalous history',
         10: 'Secret crime or misdeed', 11: 'Possession of forbidden lore',
         12: 'Foolhardy bravery'}

class npc(object):
    def __init__(self):
        gender = ''
        name = ''
        race = ''
        alignment = ''
        trait = ''
        appearance = ''
        bond = ''
        flaw = ''
        epicLevel = "Commoner"
        adventurer = False
        skills = {'Str': 10, 'Dex': 10, 'Con': 10, 'Int': 10, 'Wis': 10,
                      'Cha': 10}


def generateNPC(npc):
    npc.gender = generateGender()
    npc.race = races[random.randint(1,14)]
    npc.alignment = alignments[random.randint(1, 9)]
    npc.trait = traits[random.randint(1, 12)]
    npc.appearance = appearances[random.randint(1, 25)]
    npc.bond = bonds[random.randint(1, 8)]
    npc.flaw = flaws[random.randint(1,12)]
    npc.name = generateName(npc.gender, npc.race)
    npc.epicLevel = "Commoner"
    npc.adventurer = False
    npc.skills = {'Str': 10, 'Dex': 10, 'Con': 10, 'Int': 10, 'Wis': 10,
                  'Cha': 10}
    generateSkills(npc)

def generateGender():
    y = random.randint(1, 2)
    if y == 1:
            return 'male'
    else:
            return 'female'

def generateName(gender, race):
    if gender == "male":
        return namegen.generateMaleName(race)
    else:
        return namegen.generateFemaleName(race)


def generateSkills(npc):
        high_bonus = random.randint(2,5)
        low_bonus = random.randint(1, 2)
        skill_list = ['Str', 'Dex', 'Con', 'Int', 'Wis',
                      'Cha']
        npc.skills[skill_list[random.randint(0,5)]] += high_bonus
        i = random.randint(1,5)
        for x in xrange(1, 6):
            if x == i:
                continue
        else:
            npc.skills[skill_list[random.randint(0,5)]] -= low_bonus

        if npc.race == 'Hill Dwarf':
            npc.skills['Con'] += 2
            npc.skills['Wis'] += 1
        elif npc.race == 'Mountain Dwarf':
            npc.skills['Con'] += 2
            npc.skills['Str'] += 2
        elif npc.race == 'High elf':
            npc.skills['Int'] += 1
            npc.skills['Dex'] += 2
        elif npc.race == 'Wood Elf':
            npc.skills['Dex'] += 2
            npc.skills['Wis'] += 1
        elif npc.race == 'Drow':
            npc.skills['Dex'] += 2
            npc.skills['Cha'] += 1
        elif npc.race == 'Half Elf':
            npc.skills['Cha'] += 2
            npc.skills[random.randint(1,6)] + 1
            npc.skills[random.randint(1,6)] + 1
        elif npc.race == 'Half Orc':
            npc.skills['Str'] += 2
            npc.skills['Con'] += 1
        elif npc.race == 'Dragonborn':
            npc.skills['Cha'] += 1
            npc.skills['Str'] += 2
        elif npc.race == 'Human':
            npc.skills['Str'] += 1
            npc.skills['Dex'] += 1
            npc.skills['Con'] += 1
            npc.skills['Int'] += 1
            npc.skills['Wis'] += 1
            npc.skills['Cha'] += 1
        elif npc.race == 'LightFoot Halfling':
            npc.skills['Dex'] += 2
            npc.skills['Cha'] += 1
        elif npc.race == 'Stout Dwarf':
            npc.skills['Con'] += 1
            npc.skills['Dex'] += 2
        elif npc.race == 'Forest Gnome':
            npc.skills['Int'] += 2
            npc.skills['Dex'] += 1
        elif npc.race == 'Forest Gnome':
            npc.skills['Int'] += 2
            npc.skills['Con'] += 1
        elif npc.race == 'Tiefling':
            npc.skills['Int'] += 1
            npc.skills['Cha'] += 2



def showNPC(npc):
    print "%s, %s %s " % (npc.name, npc.gender, npc.race)
    print npc.alignment
    print npc.skills
    print npc.trait
    print npc.appearance
    print npc.bond
    print npc.flaw

def run():
    new_npc = npc()
    generateNPC(new_npc)
    showNPC(new_npc)

try:
    while True:
                raw_input("> ")
                run()

except EOFError:
    print "KTHXBYE"

#TODO: correct out of range error in female Halfling and Dwarf namegen

import string
import random

dwarfMaleNames = ['Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor',
                  'Bruenor', 'Dain', 'Darrak', 'Delg', 'Eberk', 'Einkil',
                  'Fargrim', 'Flint', 'Gardain', 'Harbek', 'Kildrak', 'Morgran',
                  'Orsik', 'Oskar', 'Rangrim', 'Rurik', 'Taklinn', 'Thoradin',
                  'Thorin', 'Tordek', 'Traubon', 'Travok', 'Ulfgar', 'Veit',
                  'Vondal']

dwarfFemaleNames = ['Amber', 'Artin', 'Audhild', 'Bardryn',
                    'Dagnal', 'Diesa', 'Eldeth', 'Falkrunn', 'Finellen',
                    'Gunnloda', 'Gurdis', 'Helja', 'Hlin', 'Kathra', 'Kristryd',
                    'Ilde', 'Liftrasa', 'Mardred', 'Riswynn', 'Sannl',
                    'Torbera', 'Torgga', 'Wigga', 'Daghilde', 'Hilde',
                    'Jorunn', 'Porunn', 'Helga', 'Hilda', 'Lorna']

dwarfClanNames =  ['Balderk', 'Battlehammer', 'Brawnanvil', 'Dankil',
                    'Fireforge', 'Frostbeard', 'Gorunn', 'Holderhek',
                    'Ironfist', 'Loderr', 'Lutgehr', 'Rumnaheim', 'Strakeln',
                    'Torunn', 'Ungart']

elfMaleNames = ['Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Beiro',
                'Berrian', 'Carric', 'Enialis', 'Erdan', 'Erevan', 'Galinndan',
                'Hadarai', 'Heian', 'Himo', 'Immeral', 'Ivellios', 'Laucian',
                'Mindartis', 'Paelias', 'Peren', 'Quarion', 'Riardon', 'Rolen',
                'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis', 'Raoden']

elfFemaleNames = ['Adrie', 'Althaea', 'Anastrianna', 'Andraste', 'Antinua',
                  'Bethrynna', 'Birel', 'Caelynn', 'Drusilia', 'Enna',
                  'Felosial', 'Ielenia', 'Jelenneth', 'Keyleth', 'Leshanna',
                  'Lia', 'Meriele', 'Mialee', 'Naivara', 'Quelenna',
                  'Quillathe', 'Sariel', 'Shanairra', 'Shava', 'Silaqui',
                  'Theirastra', 'Thia', 'Vadania', 'Valanthe', 'Xanaphia']

elfFamilyNames = ['Amakiir (Gemflower)', 'Amastacia (Starflower)',
                  'Galanodel (Moonwhisper)', 'Holimion (Diamonddew)',
                  'Ilphelkiir (Gemblossom)', 'Liadon (Silverfrond)',
                  'Meliamne (Oakenheel)', 'Nai\'lo (Nightbreeze)',
                  'Siannodel (Moonbrook)', 'Xiloscient (Goldpetal)']

halflingMaleNames = ['Alton', 'Ander', 'Cade', 'Corrin', 'Eldon', 'Errich',
                     'Finnan', 'Garret', 'Lindal', 'Lyle', 'Merric', 'Milo',
                     'Osborn', 'Perrin', 'Reed', 'Roscoe', 'Wellby', 'Holgo',
                     'Philliam', 'Wyrrel']

halflingFemaleNames = ['Andry', 'Bree', 'Callie', 'Cora', 'Euphemia', 'Jillian',
                       'Kithri', 'Lavinia', 'Lidda', 'Merla', 'Nedda', 'Paela',
                       'Portia', 'Seraphina', 'Shaena', 'Trym', 'Vani', 'Verna',
                       'Lilina', 'Rose']

halflingFamilyNames = ['Brushgather', 'Goodbarrel', 'Greenbottle', 'High-hill',
                       'Hilltopple', 'Leagallow', 'Tealeaf', 'Thorngage',
                       'Tosscobble', 'Underbough']

humanMaleNames = ['Darvin', 'Dorn', 'Evendur', 'Gorstag', 'Grim', 'Helm',
                  'Malark', 'Morn', 'Randal', 'Stedd']

humanFemaleNames = ['Arveene', 'Esvele', 'Jhessail', 'Kerri', 'Lureene',
                     'Miri', 'Rowan', 'Shandri', 'Tessele', 'Juliana']

humanSurnames = ['Amblecrown', 'Buckman', 'Dundragon', 'Evenwood', 'Greycastle',
                 'Tallstag']

dragonbornMaleNames = ['Arjhan', 'Balasar', 'Bharash', 'Donaar', 'Ghesh',
                       'Heskan', 'Kriv', 'Medrash', 'Mehen', 'Nadarr',
                       'Pandjed', 'Patrin', 'Rhogar', 'Shamash', 'Shedinn',
                       'Tarhun', 'Torinn']

dragonbornFemaleNames = ['Akra', 'Biri', 'Daar', 'Farideh', 'Harann',
                         'Flavilar', 'Jheri', 'Kava', 'Korinn', 'Mishann',
                         'Nala', 'Perra', 'Raiann', 'Sora', 'Surina', 'Thava',
                         'Uadjit']

dragonbornClanNames = ['Clethtinthiallor', 'Daardendrian', 'Delmirev',
                         'Drachedandion', 'Fenkenkabradon', 'Kepeshkmolik',
                         'Kerrhylon', 'Kimbatuul', 'Linxakasendalor', 'Myastan',
                         'Nemmonis', 'Norixius', 'Ophinshtalajiir',
                         'Prexijandilin', 'Shestendeliath', 'Turnuroth',
                         'Verthisathurgiesh', 'Yarjerit']

gMaleNames = ['Alston', 'Alvyn', 'Boddynock', 'Brocc', 'Burgell', 'Dimble',
                  'Eldon', 'Erky', 'Fonkin', 'Frug', 'Gerbo', 'Gimble', 'Glim',
                  'Jebeddo', 'Kellen', 'Namfoodle', 'Orryn', 'Roondar', 'Seebo',
                  'Sindri', 'Warryn', 'Wrenn', 'Zook']

gFemaleNames = ['Bimpnottin', 'Breena', 'Caramip', 'Carlin', 'Donella',
                    'Duvamil', 'Ella', 'Ellyjobell', 'Ellywick', 'Lilli',
                    'Loopmottin', 'Lorilla', 'Mardnab', 'Nissa', 'Nyx', 'Oda',
                    'Orla', 'Roywyn', 'Shamil', 'Tana', 'Waywocket', 'Zanna',
                    'Tana']

gClanNames = ['Beren', 'Daergel', 'Folkor', 'Garrick', 'Nackle', 'Murnig',
                  'Ningel', 'Raulnor', 'Scheppen', 'Timbers', 'Turen']

gNickNames = ['Aleslosh', 'Ashhearth', 'Badger', 'Cloak', 'Doublelock',
                  'Filchbatter', 'Fnipper', 'Ku', 'Nim', 'Oneshoe', 'Pock',
                  'Sparklegem', 'Stumbleduck']

halfOrcMaleNames = ['Dench', 'Feng', 'Gell', 'Henk', 'Holg', 'Imsh', 'Keth',
                    'Krusk', 'Mhurren', 'Ront', 'Shump', 'Thokk', 'Grom']

halfOrcFemaleNames = ['Baggi', 'Emen', 'Engong', 'Kansif', 'Myev', 'Neega',
                      'Ovak', 'Ownka', 'Shautha', 'Sutha', 'Vola', 'Volen',
                      'Yevelda']

tieflingMaleNames = ['Akmenos', 'Amnon', 'Barakas', 'Damakos', 'Ekemon',
                     'Iados', 'Kairon', 'Leucis', 'Melech', 'Mordai', 'Morthos',
                     'Pelaios', 'Skamos', 'Therai']

tieflingFemaleNames = ['Akta', 'Anakis', 'Bryseis', 'Criella', 'Damaia', 'Ea',
                       'Kallista', 'Lerissa', 'Makaria', 'Nemeia', 'Orianna',
                       'Phelaia', 'Rieta', 'Ellaria']

tieflingVirtueNames = ['Art', 'Carrion', 'Chant', 'Creed', 'Despair',
                       'Excellence', 'Fear', 'Glory', 'Hope', 'Ideal', 'Music',
                       'Nowhere', 'Open', 'Poetry', 'Quest', 'Random',
                       'Reverence', 'Sorrow', 'Temerity', 'Torment', 'Weary']

def generateMaleName(race):
    name = ""
    if race == "Half-Elf":
        coin = random.randint(1,2)
        if coin == 1:
            return generateMaleName("High Elf")
        else:
            return generateMaleName("Human")
    elif "Human" in race:
        x = random.randint(0, 9)
        y = random.randint(0, 5)
        name = "%s %s" % (humanMaleNames[x], humanSurnames[y])

    elif "Dwarf" in race:
        x = random.randint(0, 29)
        y = random.randint(0, 14)
        name = "%s %s" % (dwarfMaleNames[x], dwarfClanNames[y])

    elif "Elf" in race:
        x = random.randint(0, 29)
        y = random.randint(0, 9)
        name = "%s %s" % (elfMaleNames[x], elfFamilyNames[y])

    elif "Drow" in race:
        x = random.randint(0, 29)
        y = random.randint(0, 9)
        name = "%s %s" % (elfMaleNames[x], elfFamilyNames[y])

    elif "Half-Orc" in race:
         name = "%s" % (halfOrcMaleNames[random.randint(0, 11)])

    elif "Dragonborn" in race:
        x = random.randint(0, 16)
        y = random.randint(0, 17)
        name = "%s %s" % (dragonbornMaleNames[x], dragonbornClanNames[y])
    elif "Tiefling" in race:
        x = random.randint(0, 13)
        y = random.randint(0, 14)
        name = "%s, the %s" % (tieflingMaleNames[x], tieflingVirtueNames[y])

    elif "Gnome" in race:
        x = random.randint(0, 22)
        y = random.randint(0, 10)
        z = random.randint(0, 12)
        name = "%s %s, a.k.a %s" % (gMaleNames[x], gClanNames[y], gNickNames[z])

    else:
        x = random.randint(0, 19)
        y = random.randint(0, 9)
        name = "%s %s" % (halflingMaleNames[x], halflingFamilyNames[y])

    return name


def generateFemaleName(race):
    name = ""
    if race == "Half-Elf":
        coin = random.randint(0,1)
        if coin == 0:
            return generateFemaleName("High Elf")
        else:
            return generateFemaleName("Human")
    elif "Human" in race:
        x = random.randint(0, 9)
        y = random.randint(0, 5)
        name = "%s %s" % (humanFemaleNames[x], humanSurnames[y])

    elif "Dwarf" in race:
        x = random.randint(0, 29)
        print x
        y = random.randint(0, 14)
        print y
        name = "%s %s" % (dwarfFemaleNames[x], dwarfClanNames[y])

    elif "Elf" in race:
        x = random.randint(0, 29)
        y = random.randint(0, 9)
        name = "%s %s" % (elfFemaleNames[x], elfFamilyNames[y])

    elif "Drow" in race:
        x = random.randint(0, 29)
        y = random.randint(0, 9)
        name = "%s %s" % (elfFemaleNames[x], elfFamilyNames[y])

    elif "Half-Orc" in race:
         name = "%s" % (halfOrcFemaleNames[random.randint(0, 11)])

    elif "Dragonborn" in race:
        x = random.randint(0, 16)
        y = random.randint(0, 17)
        name = "%s %s" % (dragonbornFemaleNames[x], dragonbornClanNames[y])
    elif "Tiefling" in race:
        x = random.randint(0, 13)
        y = random.randint(0, 14)
        name = "%s, the %s" % (tieflingFemaleNames[x], tieflingVirtueNames[y])

    elif "Gnome" in race:
        x = random.randint(0, 22)
        y = random.randint(0, 10)
        z = random.randint(0, 12)
        name = "%s %s, a.k.a %s" % (gFemaleNames[x], gClanNames[y], gNickNames[z])

    else:
        x = random.randint(0, 19)
        print x
        y = random.randint(0, 9)
        print y
        name = "%s %s" % (halflingFemaleNames[x], halflingFamilyNames[y])

    return name

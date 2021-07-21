# League Randomizer mit GUI

import tkinter as tk
from tkinter import *
import random
import sys
import os

# Listen der Champs, alle und nach Lane sortiert

listA = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie",
         "Aphelios", "Ashe", "Aurelion-Sol", "Azir", "Bard", "Blitzcrank", "Brand",
         "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius",
         "Diana", "Dr.Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal",
         "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar",
         "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia",
         "Ivern", "Janna", "JarvanIV", "Jax", "Jayce", "Jhin", "Jinx", "Kai'Sa",
         "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn",
         "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "LeBlanc", "Lee-Sin",
         "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite",
         "Malzahar", "Maokai", "Master-Yi", "Miss-Fortune", "Mordekaiser",
         "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nocturne",
         "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke",
         "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renekton", "Rengar",
         "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine",
         "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner",
         "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm-Kench", "Taliyah",
         "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere",
         "Twisted-Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar",
         "Vel'Koz", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick",
         "Wukong", "Xayah", "Xerath", "Xin-Zhao", "Yasuo", "Yone", "Yorick", "Yuumi",
         "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]

listTop = ["Aatrox", "Akali", "Camille", "Cho'Gath", "Darius", "Dr.Mundo", "Fiora", "Gangplank", "Garen", "Gnar",
           "Gwen", "Heimerdinger", "Illaoi", "Irelia", "Jax", "Jayce", "Kayle", "Kennen", "Kled", "Lee-Sin",
           "Malphite", "Mordekaiser", "Nasus", "Ornn", "Poppy", "Quinn", "Renekton", "Riven", "Sett", "Shen",
           "Singed", "Sion", "Sylas", "Tahm-Kench", "Teemo", "Tryndamere", "Urgot", "Volibear",
           "Wukong", "Yasuo", "Yone", "Yorick"]

listJungle = ["Amummu", "Diana", "Dr.Mundo", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Gragas", "Graves",
              "Heacrim", "Ivern", "Jarvan-IV", "Karthus", "Kayn", "Kha'Zix", "Kindred", "Lee-Sin", "Lillia",
              "Master-Yi", "Morgana", "Nidalee", "Nocturne", "Nunu", "Olaf", "Poppy", "Rammus",
              "Rek'Sai", "Rengar", "Rumble", "Sejuani", "Shaco", "Shyvana", "Skarner", "Taliyah", "Trundle",
              "Udyr", "Vi", "Viego", "Volibear", "Warwick", "Xin-Zhao", "Zac"]

listMid = ["Ahri", "Akali", "Anivia", "Annie", "Aurelion-Sol", "Azir", "Cassiopeia", "Corki", "Diana",
           "Ekko", "Fizz", "Galio", "Heimerdinger", "Irelia", "Kassadin", "Katarina", "LeBlanc", "Lissandra",
           "Lucian", "Lux", "Malzahar", "Neeko", "Orianna", "Pantheon", "Qiyana", "Ryze", "Sylas", "Syndra",
           "Talon", "Twisted-Fate", "Veigar", "Viego", "Victor", "Vladimir", "Xerath", "Yasuo", "Yone", "Zed",
           "Ziggs", "Zoe"]

listBottom = ["Aphelios", "Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Kog'Maw",
              "Lucian", "Miss-Fortune", "Samira", "Senna", "Sivir", "Tristana", "Twitch", "Varus", "Vayne",
              "Xayah", "Yasuo"]

listSupport = ["Alistar", "Bard", "Blitzcrank", "Brand", "Braum", "Galio", "Janna", "Karma", "Leona", "Lulu",
               "Lux", "Maokai", "Morgana", "Nami", "Nautilus", "Pantheon", "Pyke", "Rakan", "Rell", "Senna",
               "Seraphine", "Sett", "Sona", "Soraka", "Swain", "Taric", "Thresh",
               "Yuumi", "Zilean", "Zyra"]

listPrecision1 = ["Press-The-Attack", "Lethal-Tempo", "Fleet-Footwork", "Conqueror"]
listPrecision2 = ["Overheal", "Triumph", "Presence-Of-Mind"]
listPrecision3 = ["Legend_Alacrity", "Legend_Tenacity", "Legend_Bloodline"]
listPrecision4 = ["Coup-De-Grace", "Cut-Down", "Last-Stand"]
listPrecision5 = ["Domination", "Sorcery", "Resolve", "Inspiration"]

listDomination1 = ["Electrocute", "Predator", "Dark-Harvest", "Hail-Of-Blades"]
listDomination2 = ["Cheap-Shot", "Taste-Of-Blood", "Sudden-Impact"]
listDomination3 = ["Zombie-Ward", "Ghost-Poro", "Eyeball-Collection"]
listDomination4 = ["Ravenous-Hunter", "Ingenious-Hunter", "Relentless-Hunter", "Ultimate-Hunter"]
listDomination5 = ["Presicion", "Sorcery", "Resolve", "Inspiration"]

listSorcery1 = ["Summon-Aery", "Arcane-Comet", "Phase-Rush"]
listSorcery2 = ["Nullifying-Orb", "Manaflow-Band", "Nimbus-Cloak"]
listSorcery3 = ["Transcendence", "Celerity", "Absolute-Focus"]
listSorcery4 = ["Scorch", "Waterwalking", "Gathering-Storm"]
listSorcery5 = ["Presicion", "Domination", "Resolve", "Inspiration"]

listResolve1 = ["Grasp-Of-Undying", "Aftershock", "Guardian"]
listResolve2 = ["Demolish", "Font-Of-Life", "Shield-Bash"]
listResolve3 = ["Conditioning", "Second-Wind", "Bone-Plating"]
listResolve4 = ["Overgrowth", "Revitalize", "Unflinching"]
listResolve5 = ["Presicion", "Domination", "Sorcery", "Inspiration"]

listInspiration1 = ["Glacial-Gauntlet", "Unsealed-Spellbook", "Prototype_Omnistone"]
listInspiration2 = ["Hextech-Flashtraption", "Magical-Footwear", "Perfect-Timing"]
listInspiration3 = ["Future's-Market", "Minion-Dematerializer", "Biscuit-Delivery"]
listInspiration4 = ["Cosmic-insight", "Approach-Velocity", "Time-Warp-Tonic"]
listInspiration5 = ["Presicion", "Domination", "Sorcery", "Resolve"]

listOffense = ["Adaptive Force", "Attack Speed", "Ability Haste"]
listFlex = ["Adaptive Force", "Armor", "Magic Resist"]
listDefense = ["Health", "Armor", "Magic Resist"]

listFighter = ["Chempunk Chainsword", "Guinsoo's Rageblade", "Maw of  Malmortius",
               "Hullbreaker", "Guardian Angel", "Manamune", "Dead Man's Plate", "Silvermere Dawn",
               "Black Cleaver", "Sterak's Gage", "Death's Dance", "Wit's End", "Blade of the Ruined King",
               "Serylda's Grudge", "Ravenous Hydra", "Titanic Hydra"]
listMarksman = ["Rapid Firecannon", "Mortal Reminder", "Phantom Dancer", "Runaan's Hurricane",
                "Guinsoo's Rageblade", "Stormrazor", "Maw of Malmortius", "Essence Reaver",
                "Guardian Angel", "Manamune",
                "Lord Dominik's Regards", "Mercurial Scimitar", "The Collector", "Blade of the Ruined King",
                "Serylda's Grudge", "Infinity Edge", "Navori Quickblades", "Bloodthirster"]
listAssasin = ["Chempunk Chainsword", "Umbral Glaive", "Serpent's Fang", "Maw of Malmortius", "Guardian Angel",
               "Manamune", "Edge of Night", "Silvermere Dawn", "Youmuu's Ghostblade", "The Collector",
               "Black Cleaver", "Serylda's Grudge", "Ravenous Hydra"]
listMage = ["Mejai's Soulstealer", "Morellonomicon", "Zhonyas's Hourglass", "Banshee's Veil", "Void Staff",
            "Nashor's Tooth", "Rylai's Crystal Scepter", "Horizon Focus", "Cosmic Drive", "Demonic Embrace",
            "Lich Bane", "Archangel'S Staff", "Rabadon's Deathcap"]
listTank = ["Knight's Vow", "Zeke's Convergence", "Frozen Heart", "Anathema's Chains", "Randuin's Omen",
            "Thornmail", "Abyssal Mask", "Spirit Visage", "Dead Man's Plate", "Force of Nature", "Warmog's Armor",
            "Sterak's Gage", "Gargoyle Stoneplate", "Titanic Hydra"]
listSupportItems = ["Knight's Vow", "Chemtech Putrifier", "Staff of Flowing Water", "Mikael's Blessing",
                    "Redemption", "Ardent Censer", "Zeke's Convergence"]

root = tk.Tk()
root.title("League Of Legends Randomizer")
helpList = []


# Methoden für Buttons

def restartProgram():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def randomChamp():
    i = random.choice(listA)
    helpList.append(i)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=0, column=1)
        helpList.clear()


def randomTop():
    i = random.choice(listTop)
    helpList.append(i)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=1, column=1)
        helpList.clear()


def randomJungle():
    i = random.choice(listJungle)
    helpList.append(i)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=2, column=1)
        helpList.clear()


def randomMid():
    i = random.choice(listMid)
    helpList.append(i)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=3, column=1)
        helpList.clear()


def randomBottom():
    i = random.choice(listBottom)
    helpList.append(i)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=4, column=1)
        helpList.clear()


def randomSupport():
    i = random.choice(listSupport)
    helpList.append(i)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=5, column=1)
        helpList.clear()


def randomPresicion():
    a = random.choice(listPrecision1)
    label = tk.Label(text=a, height=2, width=18, bg="#FFFFFF")
    label.grid(row=7, column=1)
    b = random.choice(listPrecision2)
    label = tk.Label(text=b, height=2, width=18, bg="#FFFFFF")
    label.grid(row=8, column=1)
    c = random.choice(listPrecision3)
    label = tk.Label(text=c, height=2, width=18, bg="#FFFFFF")
    label.grid(row=9, column=1)
    d = random.choice(listPrecision4)
    label = tk.Label(text=d, height=2, width=18, bg="#FFFFFF")
    label.grid(row=10, column=1)

    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=10, column=2)
    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=9, column=2)
    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=8, column=2)

    listSecond = ["1", "2", "3"]

    ndPage1 = random.choice(listPrecision5)
    ndRow1 = random.choice(listSecond)
    listSecond.remove(ndRow1)
    ndRow2 = random.choice(listSecond)

    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listDomination2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listDomination3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listDomination2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listDomination4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listDomination3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listDomination4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listSorcery2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listSorcery3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listSorcery2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listSorcery4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listSorcery3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listSorcery4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listResolve2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listResolve3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listResolve2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listResolve4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listResolve3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listResolve4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listInspiration2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listInspiration3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listInspiration2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listInspiration4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listInspiration3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listInspiration4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

        label = tk.Label(text=random.choice(listOffense), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=3)
        label = tk.Label(text=random.choice(listFlex), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=3)
        label = tk.Label(text=random.choice(listDefense), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=3)

def randomDomination():
    a = random.choice(listDomination1)
    helpList.append(a)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=7, column=1)
        helpList.clear()
    b = random.choice(listDomination2)
    helpList.append(b)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=1)
        helpList.clear()
    c = random.choice(listDomination3)
    helpList.append(c)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=1)
        helpList.clear()
    d = random.choice(listDomination4)
    helpList.append(d)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=1)
        helpList.clear()

    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=10, column=2)
    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=9, column=2)
    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=8, column=2)

    listSecond = ["1", "2", "3"]

    ndPage1 = random.choice(listDomination5)
    ndRow1 = random.choice(listSecond)
    listSecond.remove(ndRow1)
    ndRow2 = random.choice(listSecond)

    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listPrecision2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listPrecision3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listPrecision2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listPrecision4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listPrecision3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listPrecision4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listSorcery2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listSorcery3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listSorcery2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listSorcery4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listSorcery3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listSorcery4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listResolve2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listResolve3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listResolve2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listResolve4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listResolve3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listResolve4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listInspiration2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listInspiration3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listInspiration2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listInspiration4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listInspiration3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listInspiration4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    label = tk.Label(text=random.choice(listOffense), height=2, width=18, bg="#FFFFFF")
    label.grid(row=8, column=3)
    label = tk.Label(text=random.choice(listFlex), height=2, width=18, bg="#FFFFFF")
    label.grid(row=9, column=3)
    label = tk.Label(text=random.choice(listDefense), height=2, width=18, bg="#FFFFFF")
    label.grid(row=10, column=3)


def randomSorcery():
    a = random.choice(listSorcery1)
    helpList.append(a)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=7, column=1)
        helpList.clear()
    b = random.choice(listSorcery2)
    helpList.append(b)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=1)
        helpList.clear()
    c = random.choice(listSorcery3)
    helpList.append(c)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=1)
        helpList.clear()
    d = random.choice(listSorcery4)
    helpList.append(d)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=1)
        helpList.clear()

    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=10, column=2)
    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=9, column=2)
    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=8, column=2)

    listSecond = ["1", "2", "3"]

    ndPage1 = random.choice(listSorcery5)
    ndRow1 = random.choice(listSecond)
    listSecond.remove(ndRow1)
    ndRow2 = random.choice(listSecond)

    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listPrecision2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listPrecision3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listPrecision2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listPrecision4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listPrecision3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listPrecision4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listDomination2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listDomination3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listDomination2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listDomination4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listDomination3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listDomination4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listResolve2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listResolve3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listResolve2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listResolve4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listResolve3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listResolve4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listInspiration2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listInspiration3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listInspiration2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listInspiration4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listInspiration3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listInspiration4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    label = tk.Label(text=random.choice(listOffense), height=2, width=18, bg="#FFFFFF")
    label.grid(row=8, column=3)
    label = tk.Label(text=random.choice(listFlex), height=2, width=18, bg="#FFFFFF")
    label.grid(row=9, column=3)
    label = tk.Label(text=random.choice(listDefense), height=2, width=18, bg="#FFFFFF")
    label.grid(row=10, column=3)


def randomResolve():
    a = random.choice(listResolve1)
    helpList.append(a)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=7, column=1)
        helpList.clear()
    b = random.choice(listResolve2)
    helpList.append(b)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=1)
        helpList.clear()
    c = random.choice(listResolve3)
    helpList.append(c)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=1)
        helpList.clear()
    d = random.choice(listResolve4)
    helpList.append(d)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=1)
        helpList.clear()

    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=10, column=2)
    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=9, column=2)
    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=8, column=2)

    listSecond = ["1", "2", "3"]

    ndPage1 = random.choice(listResolve5)
    ndRow1 = random.choice(listSecond)
    listSecond.remove(ndRow1)
    ndRow2 = random.choice(listSecond)

    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listPrecision2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listPrecision3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listPrecision2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listPrecision4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listPrecision3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listPrecision4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listDomination2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listDomination3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listDomination2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listDomination4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listDomination3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listDomination4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listSorcery2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listSorcery3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listSorcery2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listSorcery4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listSorcery3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listSorcery4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listInspiration2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listInspiration3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listInspiration2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listInspiration4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listInspiration3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listInspiration4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    label = tk.Label(text=random.choice(listOffense), height=2, width=18, bg="#FFFFFF")
    label.grid(row=8, column=3)
    label = tk.Label(text=random.choice(listFlex), height=2, width=18, bg="#FFFFFF")
    label.grid(row=9, column=3)
    label = tk.Label(text=random.choice(listDefense), height=2, width=18, bg="#FFFFFF")
    label.grid(row=10, column=3)


def randomInspiration():
    a = random.choice(listInspiration1)
    helpList.append(a)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=7, column=1)
        helpList.clear()
    b = random.choice(listInspiration2)
    helpList.append(b)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=1)
        helpList.clear()
    c = random.choice(listInspiration3)
    helpList.append(c)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=1)
        helpList.clear()
    d = random.choice(listInspiration4)
    helpList.append(d)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=1)
        helpList.clear()

    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=10, column=2)
    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=9, column=2)
    label = tk.Label(text=None, height=2, width=18, bg="#FFFFFF")
    label.grid(row=8, column=2)

    listSecond = ["1", "2", "3"]

    ndPage1 = random.choice(listInspiration5)
    ndRow1 = random.choice(listSecond)
    listSecond.remove(ndRow1)
    ndRow2 = random.choice(listSecond)

    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listPrecision2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listPrecision3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listPrecision2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listPrecision4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listPrecision3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listPrecision4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listDomination2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listDomination3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listDomination2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listDomination4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listDomination3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listDomination4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listResolve2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listResolve3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listResolve2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listResolve4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listResolve3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listResolve4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(text=random.choice(listSorcery2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listSorcery3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listSorcery2), height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=2)
        label = tk.Label(text=random.choice(listSorcery4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(text=random.choice(listSorcery3), height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=2)
        label = tk.Label(text=random.choice(listSorcery4), height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=2)

    label = tk.Label(text=random.choice(listOffense), height=2, width=18, bg="#FFFFFF")
    label.grid(row=8, column=3)
    label = tk.Label(text=random.choice(listFlex), height=2, width=18, bg="#FFFFFF")
    label.grid(row=9, column=3)
    label = tk.Label(text=random.choice(listDefense), height=2, width=18, bg="#FFFFFF")
    label.grid(row=10, column=3)


def randomRoles():
    rollen = ["Top", "Jungle", "Mid", "ADC", "Support"]
    role1 = random.choice(rollen)
    label = tk.Label(text="P1 -> " + role1, height=2, width=18, bg="#FFFFFF")
    label.grid(row=1, column=2)
    rollen.remove(role1)
    role2 = random.choice(rollen)
    label = tk.Label(text="P2 -> " + role2, height=2, width=18, bg="#FFFFFF")
    label.grid(row=2, column=2)
    rollen.remove(role2)
    role3 = random.choice(rollen)
    label = tk.Label(text="P3 -> " + role3, height=2, width=18, bg="#FFFFFF")
    label.grid(row=3, column=2)
    rollen.remove(role3)
    role4 = random.choice(rollen)
    label = tk.Label(text="P4 -> " + role4, height=2, width=18, bg="#FFFFFF")
    label.grid(row=4, column=2)
    rollen.remove(role4)
    role5 = random.choice(rollen)
    label = tk.Label(text="P5 -> " + role5, height=2, width=18, bg="#FFFFFF")
    label.grid(row=5, column=2)
    rollen.remove(role5)

def randomSkillOrder():
    listSKill = ["Q", "W", "E"]
    skill1 = random.choice(listSKill)
    label = tk.Label(text="1. "+skill1, height=2, width=18, bg="#FFFFFF")
    label.grid(row=1, column=3)
    listSKill.remove(skill1)
    skill2 = random.choice(listSKill)
    label = tk.Label(text="2. "+skill2, height=2, width=18, bg="#FFFFFF")
    label.grid(row=2, column=3)
    listSKill.remove(skill2)
    skill3 = random.choice(listSKill)
    label = tk.Label(text="3. "+skill3, height=2, width=18, bg="#FFFFFF")
    label.grid(row=3, column=3)
    listSKill.remove(skill3)


# GUI
randChamp = tk.Button(text="All Champions", padx=5, pady=5, fg="white", bg="#23272a",
                      command=randomChamp)
randChamp.grid(row=0, column=0, padx='5', pady='5', sticky='ew')

restart = tk.Button(text="Restart", padx=5, pady=5, fg="white", bg="#23272a",
                    command=restartProgram)
restart.grid(row=11, column=2, padx='5', pady='5', sticky='ew')

randTop = tk.Button(text="Toplaner", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomTop)
randTop.grid(row=1, column=0, padx='5', pady='5', sticky='ew')

randJgl = tk.Button(text="Jungler", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomJungle)
randJgl.grid(row=2, column=0, padx='5', pady='5', sticky='ew')

randMid = tk.Button(text="Midlaner", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomMid)
randMid.grid(row=3, column=0, padx='5', pady='5', sticky='ew')

randBot = tk.Button(text="ADC", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomBottom)
randBot.grid(row=4, column=0, padx='5', pady='5', sticky='ew')

randSup = tk.Button(text="Supporter", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomSupport)
randSup.grid(row=5, column=0, padx='5', pady='5', sticky='ew')

frame = tk.Frame(height=5, width=132, bg="#7289da")
frame.grid(row=6, column=0, sticky='nw')

frame2 = tk.Frame(height=5, width=132, bg="#7289da")
frame2.grid(row=6, column=1, sticky='n')

frame3 = tk.Frame(height=5, width=132, bg="#7289da")
frame3.grid(row=6, column=2, sticky='ne')

frame4 = tk.Frame(height=5, width=132, bg="#7289da")
frame4.grid(row=6, column=3, sticky='ne')


randPre = tk.Button(text="Precision Runes", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomPresicion)
randPre.grid(row=7, column=0, padx='5', pady='5', sticky='ew')

randDom = tk.Button(text="Domination Runes", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomDomination)
randDom.grid(row=8, column=0, padx='5', pady='5', sticky='ew')

randSor = tk.Button(text="Sorcery Runes", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomSorcery)
randSor.grid(row=9, column=0, padx='5', pady='5', sticky='ew')

randRes = tk.Button(text="Resolve Runes", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomResolve)
randRes.grid(row=10, column=0, padx='5', pady='5', sticky='ew')

randIns = tk.Button(text="Inspiration Runes", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomInspiration)
randIns.grid(row=11, column=0, padx='5', pady='5', sticky='ew')

randRoles = tk.Button(text="Roles", padx="5", pady="5", fg="white", bg="#23272a", command=randomRoles)
randRoles.grid(row=0, column=2, padx='5', pady='5', sticky='ew')

randSkillOrder = tk.Button(text="Skill Order", padx="5", pady="5", fg="white", bg="#23272a", command=randomSkillOrder)
randSkillOrder.grid(row=0, column=3, padx='5', pady='5', sticky='ew')

root.mainloop()

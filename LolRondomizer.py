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

listSupporter = ["Alistar", "Bard", "Blitzcrank", "Brand", "Braum", "Galio", "Janna", "Karma", "Leona", "Lulu",
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

listBoots = ["Berserker's Greaves", "Sorcerer's Shoes", "Plated Steelcaps", "Mercury's Treads", "Mobility Boots",
             "Ionian Boots of Lucidity", "Boots of Swiftness"]

root = tk.Tk()
root.title("League Of Legends Randomizer")
helpList = []


# Methoden für Buttons

def restartProgram():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def randomChamp():
    label = tk.Label(frame, text=random.choice(listA), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=0, column=1)


def randomTop():
    label = tk.Label(frame, text=random.choice(listTop), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=1, column=1)


def randomJungle():
    label = tk.Label(frame, text=random.choice(listJungle), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=2, column=1)


def randomMid():
    label = tk.Label(frame, text=random.choice(listMid), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=3, column=1)


def randomBottom():
    label = tk.Label(frame, text=random.choice(listBottom), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=4, column=1)


def randomSupporter():
    label = tk.Label(frame, text=random.choice(listSupporter), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=5, column=1)


def randomPresicion():
    label = tk.Label(frame, text=random.choice(listPrecision1), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=7, column=1)
    label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=1)
    label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=1)
    label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=1)

    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=2)
    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=2)
    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=2)

    listSecond = ["1", "2", "3"]

    ndPage1 = random.choice(listPrecision5)
    ndRow1 = random.choice(listSecond)
    listSecond.remove(ndRow1)
    ndRow2 = random.choice(listSecond)

    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    label = tk.Label(frame, text=random.choice(listOffense), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=3)
    label = tk.Label(frame, text=random.choice(listFlex), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=3)
    label = tk.Label(frame, text=random.choice(listDefense), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=3)


def randomDomination():
    label = tk.Label(frame, text=random.choice(listDomination1), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=7, column=1)
    label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=1)
    label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=1)
    label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=1)

    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=2)
    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=2)
    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=2)

    listSecond = ["1", "2", "3"]

    ndPage1 = random.choice(listDomination5)
    ndRow1 = random.choice(listSecond)
    listSecond.remove(ndRow1)
    ndRow2 = random.choice(listSecond)

    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    label = tk.Label(frame, text=random.choice(listOffense), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=3)
    label = tk.Label(frame, text=random.choice(listFlex), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=3)
    label = tk.Label(frame, text=random.choice(listDefense), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=3)


def randomSorcery():
    label = tk.Label(frame, text=random.choice(listSorcery1), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=7, column=1)
    label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=1)
    label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=1)
    label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=1)

    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=2)
    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=2)
    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=2)

    listSecond = ["1", "2", "3"]

    ndPage1 = random.choice(listSorcery5)
    ndRow1 = random.choice(listSecond)
    listSecond.remove(ndRow1)
    ndRow2 = random.choice(listSecond)

    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    label = tk.Label(frame, text=random.choice(listOffense), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=3)
    label = tk.Label(frame, text=random.choice(listFlex), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=3)
    label = tk.Label(frame, text=random.choice(listDefense), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=3)


def randomResolve():
    label = tk.Label(frame, text=random.choice(listResolve1), height=2, width=18, border=5, bg='#000000', fg='#FFFFFF')
    label.grid(row=7, column=1)
    label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=1)
    label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=1)
    label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=1)

    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=2)
    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=2)
    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=2)

    listSecond = ["1", "2", "3"]

    ndPage1 = random.choice(listResolve5)
    ndRow1 = random.choice(listSecond)
    listSecond.remove(ndRow1)
    ndRow2 = random.choice(listSecond)

    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Inspiration" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Inspiration" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    label = tk.Label(frame, text=random.choice(listOffense), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=3)
    label = tk.Label(frame, text=random.choice(listFlex), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=3)
    label = tk.Label(frame, text=random.choice(listDefense), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=3)


def randomInspiration():
    label = tk.Label(frame, text=random.choice(listInspiration1), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=7, column=1)
    label = tk.Label(frame, text=random.choice(listInspiration2), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=1)
    label = tk.Label(frame, text=random.choice(listInspiration3), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=1)
    label = tk.Label(frame, text=random.choice(listInspiration4), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=1)

    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=2)
    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=2)
    label = tk.Label(frame, text=None, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=2)

    listSecond = ["1", "2", "3"]

    ndPage1 = random.choice(listInspiration5)
    ndRow1 = random.choice(listSecond)
    listSecond.remove(ndRow1)
    ndRow2 = random.choice(listSecond)

    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Presicion" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listPrecision2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Presicion" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listPrecision3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listPrecision4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Domination" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Domination" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listDomination2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Domination" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listDomination3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listDomination4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Sorcery" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listSorcery2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Sorcery" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listSorcery3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listSorcery4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "1" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "3":
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    if ndPage1 == "Resolve" and ndRow1 == "2" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "3" and ndRow2 == "1":
        label = tk.Label(frame, text=random.choice(listResolve2), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=8, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)
    if ndPage1 == "Resolve" and ndRow1 == "3" and ndRow2 == "2":
        label = tk.Label(frame, text=random.choice(listResolve3), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=9, column=2)
        label = tk.Label(frame, text=random.choice(listResolve4), height=2, width=18, bg='#000000', fg='#FFFFFF')
        label.grid(row=10, column=2)

    label = tk.Label(frame, text=random.choice(listOffense), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=3)
    label = tk.Label(frame, text=random.choice(listFlex), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=3)
    label = tk.Label(frame, text=random.choice(listDefense), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=3)


def randomRoles():
    rollen = ["Top", "Jungle", "Mid", "ADC", "Support"]
    role1 = random.choice(rollen)
    label = tk.Label(frame, text="P1 -> " + role1, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=5)
    rollen.remove(role1)
    role2 = random.choice(rollen)
    label = tk.Label(frame, text="P2 -> " + role2, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=5)
    rollen.remove(role2)
    role3 = random.choice(rollen)
    label = tk.Label(frame, text="P3 -> " + role3, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=5)
    rollen.remove(role3)
    role4 = random.choice(rollen)
    label = tk.Label(frame, text="P4 -> " + role4, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=11, column=5)
    rollen.remove(role4)
    role5 = random.choice(rollen)
    label = tk.Label(frame, text="P5 -> " + role5, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=12, column=5)
    rollen.remove(role5)


def randomSkillOrder():
    listSKill = ["Q", "W", "E"]
    skill1 = random.choice(listSKill)
    label = tk.Label(frame, text="1. " + skill1, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=8, column=6)
    listSKill.remove(skill1)
    skill2 = random.choice(listSKill)
    label = tk.Label(frame, text="2. " + skill2, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=9, column=6)
    listSKill.remove(skill2)
    skill3 = random.choice(listSKill)
    label = tk.Label(frame, text="3. " + skill3, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=10, column=6)
    listSKill.remove(skill3)


def itemSupport():
    listSupport = ["Knight's Vow", "Chemtech Putrifier", "Staff of Flowing Water", "Mikael's Blessing",
                   "Redemption", "Ardent Censer", "Zeke's Convergence"]
    label = tk.Label(frame, text="Any Mythic", height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=5, column=4)
    label = tk.Label(frame, text=random.choice(listBoots), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=5, column=5)
    item1 = random.choice(listSupport)
    label = tk.Label(frame, text=item1, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=5, column=6)
    listSupport.remove(item1)
    item2 = random.choice(listSupport)
    label = tk.Label(frame, text=item2, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=5, column=7)
    listSupport.remove(item2)
    item3 = random.choice(listSupport)
    label = tk.Label(frame, text=item3, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=5, column=8)
    listSupport.remove(item3)
    item4 = random.choice(listSupport)
    label = tk.Label(frame, text=item4, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=5, column=9)
    listSupport.remove(item4)

    i = 6
    while i <= 9:
        line = tk.Frame(frame, height=5, width=138, bg='#7289da')
        line.grid(row=6, column=i, sticky='w')
        i += 1


def itemAssasin():
    listAssasin = ["Chempunk Chainsword", "Umbral Glaive", "Serpent's Fang", "Maw of Malmortius", "Guardian Angel",
                   "Manamune", "Edge of Night", "Silvermere Dawn", "Youmuu's Ghostblade", "The Collector",
                   "Black Cleaver", "Serylda's Grudge", "Ravenous Hydra"]
    label = tk.Label(frame, text="Any Mythic", height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=2, column=4)
    label = tk.Label(frame, text=random.choice(listBoots), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=2, column=5)
    item1 = random.choice(listAssasin)
    label = tk.Label(frame, text=item1, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=2, column=6)
    listAssasin.remove(item1)
    item2 = random.choice(listAssasin)
    label = tk.Label(frame, text=item2, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=2, column=7)
    listAssasin.remove(item2)
    item3 = random.choice(listAssasin)
    label = tk.Label(frame, text=item3, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=2, column=8)
    listAssasin.remove(item3)
    item4 = random.choice(listAssasin)
    label = tk.Label(frame, text=item4, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=2, column=9)
    listAssasin.remove(item4)

    i = 6
    while i <= 9:
        line = tk.Frame(frame, height=5, width=138, bg='#7289da')
        line.grid(row=6, column=i, sticky='w')
        i += 1


def itemFighter():
    listFighter = ["Chempunk Chainsword", "Guinsoo's Rageblade", "Maw of  Malmortius",
                   "Hullbreaker", "Guardian Angel", "Manamune", "Dead Man's Plate", "Silvermere Dawn",
                   "Black Cleaver", "Sterak's Gage", "Death's Dance", "Wit's End", "Blade of the Ruined King",
                   "Serylda's Grudge", "Ravenous Hydra", "Titanic Hydra"]
    label = tk.Label(frame, text="Any Mythic", height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=0, column=4)
    label = tk.Label(frame, text=random.choice(listBoots), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=0, column=5)
    item1 = random.choice(listFighter)
    label = tk.Label(frame, text=item1, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=0, column=6)
    listFighter.remove(item1)
    item2 = random.choice(listFighter)
    label = tk.Label(frame, text=item2, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=0, column=7)
    listFighter.remove(item2)
    item3 = random.choice(listFighter)
    label = tk.Label(frame, text=item3, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=0, column=8)
    listFighter.remove(item3)
    item4 = random.choice(listFighter)
    label = tk.Label(frame, text=item4, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=0, column=9)
    listFighter.remove(item4)

    i = 6
    while i <= 9:
        line = tk.Frame(frame, height=5, width=138, bg='#7289da')
        line.grid(row=6, column=i, sticky='w')
        i += 1


def itemMarksman():
    listMarksman = ["Rapid Firecannon", "Mortal Reminder", "Phantom Dancer", "Runaan's Hurricane",
                    "Guinsoo's Rageblade", "Stormrazor", "Maw of Malmortius", "Essence Reaver",
                    "Guardian Angel", "Manamune",
                    "Lord Dominik's Regards", "Mercurial Scimitar", "The Collector", "Blade of the Ruined King",
                    "Serylda's Grudge", "Infinity Edge", "Navori Quickblades", "Bloodthirster"]
    label = tk.Label(frame, text="Any Mythic", height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=4, column=4)
    label = tk.Label(frame, text=random.choice(listBoots), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=4, column=5)
    item1 = random.choice(listMarksman)
    label = tk.Label(frame, text=item1, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=4, column=6)
    listMarksman.remove(item1)
    item2 = random.choice(listMarksman)
    label = tk.Label(frame, text=item2, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=4, column=7)
    listMarksman.remove(item2)
    item3 = random.choice(listMarksman)
    label = tk.Label(frame, text=item3, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=4, column=8)
    listMarksman.remove(item3)
    item4 = random.choice(listMarksman)
    label = tk.Label(frame, text=item4, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=4, column=9)
    listMarksman.remove(item4)

    i = 6
    while i <= 9:
        line = tk.Frame(frame, height=5, width=138, bg='#7289da')
        line.grid(row=6, column=i, sticky='w')
        i += 1


def itemTank():
    listTank = ["Knight's Vow", "Zeke's Convergence", "Frozen Heart", "Anathema's Chains", "Randuin's Omen",
                "Thornmail", "Abyssal Mask", "Spirit Visage", "Dead Man's Plate", "Force of Nature", "Warmog's Armor",
                "Sterak's Gage", "Gargoyle Stoneplate", "Titanic Hydra"]
    label = tk.Label(frame, text="Any Mythic", height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=1, column=4)
    label = tk.Label(frame, text=random.choice(listBoots), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=1, column=5)
    item1 = random.choice(listTank)
    label = tk.Label(frame, text=item1, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=1, column=6)
    listTank.remove(item1)
    item2 = random.choice(listTank)
    label = tk.Label(frame, text=item2, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=1, column=7)
    listTank.remove(item2)
    item3 = random.choice(listTank)
    label = tk.Label(frame, text=item3, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=1, column=8)
    listTank.remove(item3)
    item4 = random.choice(listTank)
    label = tk.Label(frame, text=item4, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=1, column=9)
    listTank.remove(item4)

    i = 6
    while i <= 9:
        line = tk.Frame(frame, height=5, width=138, bg='#7289da')
        line.grid(row=6, column=i, sticky='w')
        i += 1


def itemMage():
    listMage = ["Mejai's Soulstealer", "Morellonomicon", "Zhonyas's Hourglass", "Banshee's Veil", "Void Staff",
                "Nashor's Tooth", "Rylai's Crystal Scepter", "Horizon Focus", "Cosmic Drive", "Demonic Embrace",
                "Lich Bane", "Archangel'S Staff", "Rabadon's Deathcap"]
    label = tk.Label(frame, text="Any Mythic", height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=3, column=4)
    label = tk.Label(frame, text=random.choice(listBoots), height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=3, column=5)
    item1 = random.choice(listMage)
    label = tk.Label(frame, text=item1, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=3, column=6)
    listMage.remove(item1)
    item2 = random.choice(listMage)
    label = tk.Label(frame, text=item2, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=3, column=7)
    listMage.remove(item2)
    item3 = random.choice(listMage)
    label = tk.Label(frame, text=item3, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=3, column=8)
    listMage.remove(item3)
    item4 = random.choice(listMage)
    label = tk.Label(frame, text=item4, height=2, width=18, bg='#000000', fg='#FFFFFF')
    label.grid(row=3, column=9)
    listMage.remove(item4)

    i = 6
    while i <= 9:
        line = tk.Frame(frame, height=5, width=138, bg='#7289da')
        line.grid(row=6, column=i, sticky='w')
        i += 1


# GUI
frame = tk.Frame(bg='#23272a')
frame.grid()
randChamp = tk.Button(frame, text="All Champions", padx=5, pady=5, fg="white", bg='#2c2f33', command=randomChamp)
randChamp.grid(row=0, column=0, padx='5', pady='5', sticky='ew')

restart = tk.Button(frame, text="Restart", padx=5, pady=5, fg="white", bg='#2c2f33', command=restartProgram)
restart.grid(row=12, column=0, padx='5', pady='5', sticky='ew')

randTop = tk.Button(frame, text="Toplaner", padx=5, pady=5, fg="white", bg='#2c2f33', command=randomTop)
randTop.grid(row=1, column=0, padx='5', pady='5', sticky='ew')

randJgl = tk.Button(frame, text="Jungler", padx=5, pady=5, fg="white", bg='#2c2f33', command=randomJungle)
randJgl.grid(row=2, column=0, padx='5', pady='5', sticky='ew')

randMid = tk.Button(frame, text="Midlaner", padx=5, pady=5, fg="white", bg='#2c2f33', command=randomMid)
randMid.grid(row=3, column=0, padx='5', pady='5', sticky='ew')

randBot = tk.Button(frame, text="ADC", padx=5, pady=5, fg="white", bg='#2c2f33', command=randomBottom)
randBot.grid(row=4, column=0, padx='5', pady='5', sticky='ew')

randSup = tk.Button(frame, text="Supporter", padx=5, pady=5, fg="white", bg='#2c2f33', command=randomSupporter)
randSup.grid(row=5, column=0, padx='5', pady='5', sticky='ew')

randPre = tk.Button(frame, text="Precision Runes", padx=5, pady=5, fg="white", bg='#2c2f33', command=randomPresicion)
randPre.grid(row=7, column=0, padx='5', pady='5', sticky='ew')

randDom = tk.Button(frame, text="Domination Runes", padx=5, pady=5, fg="white", bg='#2c2f33', command=randomDomination)
randDom.grid(row=8, column=0, padx='5', pady='5', sticky='ew')

randSor = tk.Button(frame, text="Sorcery Runes", padx=5, pady=5, fg="white", bg='#2c2f33', command=randomSorcery)
randSor.grid(row=9, column=0, padx='5', pady='5', sticky='ew')

randRes = tk.Button(frame, text="Resolve Runes", padx=5, pady=5, fg="white", bg='#2c2f33', command=randomResolve)
randRes.grid(row=10, column=0, padx='5', pady='5', sticky='ew')

randIns = tk.Button(frame, text="Inspiration Runes", padx=5, pady=5, fg="white", bg='#2c2f33',
                    command=randomInspiration)
randIns.grid(row=11, column=0, padx='5', pady='5', sticky='ew')

randRoles = tk.Button(frame, text="Roles", padx="5", pady="5", fg="white", bg='#2c2f33', command=randomRoles)
randRoles.grid(row=7, column=5, padx='5', pady='5', sticky='ew')

randSkillOrder = tk.Button(frame, text="Skill Order", padx="5", pady="5", fg="white", bg='#2c2f33',
                           command=randomSkillOrder)
randSkillOrder.grid(row=7, column=6, padx='5', pady='5', sticky='ew')

randSupport = tk.Button(frame, text="Support", padx="5", pady="5", fg="white", bg='#2c2f33', command=itemSupport)
randSupport.grid(row=5, column=3, padx='5', pady='5', sticky='ew')

randAssasin = tk.Button(frame, text="Assasin", padx="5", pady="5", fg="white", bg='#2c2f33', command=itemAssasin)
randAssasin.grid(row=2, column=3, padx='5', pady='5', sticky='ew')

randFighter = tk.Button(frame, text="Fighter", padx="5", pady="5", fg="white", bg='#2c2f33', command=itemFighter)
randFighter.grid(row=0, column=3, padx='5', pady='5', sticky='ew')

randMarksman = tk.Button(frame, text="Marksman", padx="5", pady="5", fg="white", bg='#2c2f33', command=itemMarksman)
randMarksman.grid(row=4, column=3, padx='5', pady='5', sticky='ew')

randTank = tk.Button(frame, text="Tank", padx="5", pady="5", fg="white", bg='#2c2f33', command=itemTank)
randTank.grid(row=1, column=3, padx='5', pady='5', sticky='ew')

randMage = tk.Button(frame, text="Mage", padx="5", pady="5", fg="white", bg='#2c2f33', command=itemMage)
randMage.grid(row=3, column=3, padx='5', pady='5', sticky='ew')

i = 0
while i <= 6:
    line = tk.Frame(frame, height=5, width=138, bg='#7289da')
    line.grid(row=6, column=i, sticky='w')
    i += 1

j = 0
while j <= 5:
    line = tk.Frame(frame, height=44, width=5, bg='#7289da')
    line.grid(row=j, column=2, sticky='n')
    j += 1

k = 7
while k <= 12:
    line = tk.Frame(frame, height=44, width=5, bg='#7289da')
    line.grid(row=k, column=4, sticky='n')
    k += 1

root.mainloop()

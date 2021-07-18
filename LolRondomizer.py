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
               "Seraphine", "Sett", "Shaco", "Sona", "Soraka", "Swain", "Taric", "Thresh", "Vel'Koz", "Xerath",
               "Yuumi", "Zilean", "Zyra"]

listPrecision1 = ["Press-The-Attack", "Lethal-Tempo", "Fleet-Footwork", "Conqueror"]
listPrecision2 = ["Overheal", "Triumph", "Presence-Of-Mind"]
listPrecision3 = ["Legend_Alacrity", "Legend_Tenacity", "Legend_Bloodline"]
listPrecision4 = ["Coup-De-Grace", "Cut-Down", "Last-Stand"]

listDomination1 = ["Electrocute", "Predator", "Dark-Harvest", "Hail-Of-Blades"]
listDomination2 = ["Cheap-Shot", "Taste-Of-Blood", "Sudden-Impact"]
listDomination3 = ["Zombie-Ward", "Ghost-Poro", "Eyeball-Collection"]
listDomination4 = ["Ravenous-Hunter", "Ingenious-Hunter", "Relentless-Hunter", "Ultimate-Hunter"]

listSorcery1 = ["Summon-Aery", "Arcane-Comet", "Phase-Rush"]
listSorcery2 = ["Nullifying-Orb", "Manaflow-Band", "Nimbus-Cloak"]
listSorcery3 = ["Transcendence", "Celerity", "Absolute-Focus"]
listSorcery4 = ["Scorch", "Waterwalking", "Gathering-Storm"]

listResolve1 = ["Grasp-Of-Undying", "Aftershock", "Guardian"]
listResolve2 = ["Demolish", "Font-Of-Life", "Shield-Bash"]
listResolve3 = ["Conditioning", "Second-Wind", "Bone-Plating"]
listResolve4 = ["Overgrowth", "Revitalize", "Unflinching"]

listInspiration1 = ["Glacial-Gauntlet", "Unsealed-Spellbook", "Prototype_Omnistone"]
listInspiration2 = ["Hextech-Flashtraption", "Magical-Footwear", "Perfect-Timing"]
listInspiration3 = ["Future's-Market", "Minion-Dematerializer", "Biscuit-Delivery"]
listInspiration4 = ["Cosmic-insight", "Approach-Velocity", "Time-Warp-Tonic"]

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
    helpList.append(a)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=7, column=1)
        helpList.clear()
    b = random.choice(listPrecision2)
    helpList.append(b)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=8, column=1)
        helpList.clear()
    c = random.choice(listPrecision3)
    helpList.append(c)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=9, column=1)
        helpList.clear()
    d = random.choice(listPrecision4)
    helpList.append(d)
    for helpVar in helpList:
        label = tk.Label(text=helpList, height=2, width=18, bg="#FFFFFF")
        label.grid(row=10, column=1)
        helpList.clear()


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


# GUI
randChamp = tk.Button(text="All Champions", padx=5, pady=5, fg="white", bg="#23272a",
                      command=randomChamp)
randChamp.grid(row=0, column=0, padx='5', pady='5', sticky='ew')

restart = tk.Button(text="Restart", padx=5, pady=5, fg="white", bg="#23272a",
                    command=restartProgram)
restart.grid(row=0, column=2, padx='5', pady='5', sticky='ew')

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

root.mainloop()

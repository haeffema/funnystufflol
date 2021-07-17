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
              "Heacrim", "Ivern", "Jarvan IV", "Karthus", "Kayn", "Kha'Zix", "Kindred", "Lee-Sin", "Lillia",
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

root = tk.Tk()
root.title("League Of Legends Randomizer")
champs = []


# Methoden für Buttons

def restartProgram():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def randomChamp():
    i = random.choice(listA)
    champs.append(i)
    for champ in champs:
        label = tk.Label(text=champs, height=2, width=12, bg="#FFFFFF")
        label.grid(row=1, column=2)
        champs.clear()


def randomTop():
    i = random.choice(listTop)
    champs.append(i)
    for champ in champs:
        label = tk.Label(text=champs, height=2, width=12, bg="#FFFFFF")
        label.grid(row=0, column=1)
        champs.clear()


def randomJungle():
    i = random.choice(listJungle)
    champs.append(i)
    for champ in champs:
        label = tk.Label(text=champs, height=2, width=12, bg="#FFFFFF")
        label.grid(row=1, column=1)
        champs.clear()


def randomMid():
    i = random.choice(listMid)
    champs.append(i)
    for champ in champs:
        label = tk.Label(text=champs, height=2, width=12, bg="#FFFFFF")
        label.grid(row=2, column=1)
        champs.clear()


def randomBottom():
    i = random.choice(listBottom)
    champs.append(i)
    for champ in champs:
        label = tk.Label(text=champs, height=2, width=12, bg="#FFFFFF")
        label.grid(row=3, column=1)
        champs.clear()


def randomSupport():
    i = random.choice(listSupport)
    champs.append(i)
    for champ in champs:
        label = tk.Label(text=champs, height=2, width=12, bg="#FFFFFF")
        label.grid(row=4, column=1)
        champs.clear()


# GUI

# canvas = tk.Canvas(root, height=500, width=500, bg="#7289da")
# canvas.grid()
# canvas.pack()

# frame = tk.Frame(root, bg="#2C2F33")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
# frame.grid(row=0, column=0, padx='5', pady='5', sticky='ew')

randTop = tk.Button(text="Random Toplaner", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomTop)
randTop.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
# randTop.pack()

randJgl = tk.Button(text="Random Jungler", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomJungle)
randJgl.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
# randJgl.pack()

randMid = tk.Button(text="Random Midlaner", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomMid)
randMid.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
# randMid.pack()

randBot = tk.Button(text="Random ADC", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomBottom)
randBot.grid(row=3, column=0, padx='5', pady='5', sticky='ew')
# randBot.pack()

randSup = tk.Button(text="Random Supporter", padx=5, pady=5, fg="white", bg="#23272a",
                    command=randomSupport)
randSup.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
# randSup.pack()

randChamp = tk.Button(text="Random Champion", padx=5, pady=5, fg="white", bg="#23272a",
                      command=randomChamp)
randChamp.grid(row=0, column=2, padx='5', pady='5', sticky='ew')
# randChamp.pack()

restart = tk.Button(text="Restart", padx=5, pady=5, fg="white", bg="#23272a",
                    command=restartProgram)
restart.grid(row=2, column=2, padx='5', pady='5', sticky='ew')
# restart.pack()

root.mainloop()

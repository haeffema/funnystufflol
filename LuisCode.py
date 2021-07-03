import tkinter as tk
from tkinter import Text
import random
import sys
import os

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
         "Nunu_and_Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke",
         "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renekton", "Rengar",
         "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine",
         "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner",
         "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm-Kench", "Taliyah",
         "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere",
         "Twisted-Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar",
         "Vel'Koz", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick",
         "Wukong", "Xayah", "Xerath", "Xin-Zhao", "Yasuo", "Yone", "Yorick", "Yuumi",
         "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]

root = tk.Tk()
champs = []


def restartProgram():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def randomChamp():
    i = random.choice(listA)
    champs.append(i)
    for champ in champs:
        label = tk.Label(frame, text=champs, bg="#FFFFFF")
        label.pack()
        champs.clear()


canvas = tk.Canvas(root, height=700, width=700, bg="#7289da")
canvas.pack()

frame = tk.Frame(root, bg="#2c2f33")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

randomize = tk.Button(root, text="Random Champ", padx=10, pady=5, fg="white", bg="#23272a",
                      command=randomChamp)
randomize.pack()

restart = tk.Button(root, text="Restart", padx=10, pady=5, fg="white", bg="#23272a",
                    command=restartProgram)

restart.pack()

root.mainloop()

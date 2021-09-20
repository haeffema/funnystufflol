datei = open('pokemon.txt', 'r', encoding='UTF-8')
Text = ""
for zeile in datei:
    Text += datei.read()
Text = Text.replace("},", "")
datei.close()
xd = open('pokemon.txt', 'a', encoding='UTF-8')
xd.write(Text)
xd.close()

datei = open('pokemon.txt', 'r', encoding='UTF-8')
Text = ""
for zeile in datei:
    Text += zeile
datei.close()
Text.replace(" at:", "")
print(Text)
open('pokemon.txt', 'w', encoding='UTF-8').close()
test = open('pokemon.txt', 'w', encoding='UTF-8')
test.write(Text)
test.close()

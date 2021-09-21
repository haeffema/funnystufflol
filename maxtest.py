datei = open('pokemon.txt', 'r', encoding='UTF-8')
Text = ""
counter = 0
for zeile in datei:
    if counter == 3:
        zeile = zeile.replace("\n", "")
        counter == 0
    counter += 1
    Text += zeile
datei.close()
print(Text)
open('pokemon.txt', 'w', encoding='UTF-8').close()
test = open('pokemon.txt', 'w', encoding='UTF-8')
test.write(Text)
test.close()

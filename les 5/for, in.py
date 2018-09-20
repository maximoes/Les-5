teRadenWoord = "Hogeschool"
weerTeGevenWoord = ""

for letter in teRadenWoord:
    if letter in ['a', 'e', 'o', 'u']:
        weerTeGevenWoord += '*'
    else:
        weerTeGevenWoord += '-'

print(weerTeGevenWoord)




eenWoord="Hogeschool"
weerTeGevenWoord = ""
for letterPositie in range(4, len(eenWoord)-1):
    weerTeGevenWoord+= eenWoord[letterPositie]

print(weerTeGevenWoord)


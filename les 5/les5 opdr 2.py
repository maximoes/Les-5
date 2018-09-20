leeftijd = int(input(' wat is je leeftijd? '))

paspoort = str(input(' ben je in het bezit van een Nederlands Paspoort? '))

if leeftijd > 17 and paspoort == 'Ja':
    print('Gefeliciteerd, je mag stemmen!')

else:
    print('over een paar jaar pas snottebel')

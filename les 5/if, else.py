lijst = input('is your ticket the same as on the list?  ')

if lijst == 'Ja' or 'ja':

    print('you won!')

else:

    print('shame, you lose..')




hits = int(input('hoeveel dmg kreeg je? '))
shield = 0
dead = hits > 10 and shield == 0
if dead:
    print('youre dead')

else:
    print('mooizo')

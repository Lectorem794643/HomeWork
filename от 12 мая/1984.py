questionNUMBER = int(input())
war, world, question = 'Евразия', 'Остазия', str(input('что хотите знать?  '))
while questionNUMBER != 0:
    if question == 'С кем война?':
        print(war)
    if question == 'С кем мир?':
        print(world)
    if question == 'Mеняем':
        war = world
        if war == 'Евразия':
            world = 'Остазия'
        if war :
            world = 'Евразия'
    else:
        print('Не знаю таких команд')
    question = str(input('что хотите знать?  '))
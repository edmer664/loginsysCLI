def x():
    users = ['prettyME;1234;Rhea;Tortor;12/25/1990\n',
             'cuteME;1234;Iya;Tortor;12/25/1991\n',
             'coolGuy;1234;Ruru;Sebastian;05/26/1990\n',
             'amazingMan;5678;Roxy;Bailon;11/01/1995\n',
             'itSme;3452;Andrea;Alcaide;01/28/1990']
    f = open('userCredentials.txt', 'w')
    for i in users:
        f.write(i)
    f.close()

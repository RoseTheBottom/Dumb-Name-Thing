import time

name = input('What is your name?\n')
stupid = ["egg", "james", "jeff","keith","arron","Egg", "James", "Jeff","Keith","Arron"]
doubleA = ["Aaron","Aaliyah","aaron","aaliyah"]
if name in stupid:
    print(name, ', thats a stupid name')
elif name in doubleA:
    print("Having double letters in your name doesn't make you special.\n")
    time.sleep(3)
    print("You're just stupid \n")
    time.sleep(5)
    print("Go fuck yourself.")
    time.sleep(4.5)
    exit
else:
    print('Hi, %s.' % name)

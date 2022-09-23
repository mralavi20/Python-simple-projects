import random
name = input ("What is your name? \n")
print ("Hello welcome " + name + "\n")
words = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]

def main ():
    global chosenword
    global length
    global count
    global limit
    global display
    chosenword = random.choice(words)
    length = len (chosenword)
    limit = 5
    display = "_" * length
    print ("the word is" + display)
    game ()


def game ():
    global guess
    guess = input ("Enter a letter: \n")
    if (len (guess.strip()) == 0 or len (guess.strip()) > 1):
        a = 1
    else:
        a = 2
    if (a == 1):
        print ("invalid")
        game ()
    check ()


def check ():
    global limit
    global display
    n = 0
    t = 0
    for char in chosenword:
        if (char == guess):
            word = list (display)
            word[n] = char
            display = ""
            for i in word:
                display = display + i
            t = 1
        n = n + 1
    if (t == 1):
        print ("Right \n")
        print ("the word is:" + display)
    else:
        print ("Wrong")
        print ("the word is:" + display)
        limit = limit - 1
        print (limit)
    chance ()

def chance ():
    global limit
    global display
    global chosenword
    if (limit == 0):
        print ("you lose")
        print ("the word is " + chosenword)
        play ()
    else:
        if (display == chosenword):
            print ("you win")
            print ("the word is " + chosenword)
            play ()
        else:
            game ()


def play ():
    a = input ("play again? (y or n) \n")
    if (a == "y"):
        main ()
    elif (a == "n"):
        print ("bye \n")
        exit ()
    else:
        print ("invalid \n")
        play ()

main ()

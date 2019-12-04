import sys
import mmap
import time
players = 2
curword = ""
dictfile = sys.argv[1]

def checkDict(word):
    try:
        with open(dictfile) as search:
            for line in search:
                line = line.rstrip()  # remove '\n' at end of line
                if word == line:
                    print(line)
                    return True
            return False
    except:
        print("Dictionary File could not be opened... Assuming %s is correct" %word)
        return True

while True:
    strplayers = input("How many players: ")
    if strplayers.isdigit():
        players = int(strplayers)
        if 5 > players > 1:
            break
    else:
        print("That is not a number")

loser = None
while True:
    for player in range(1,players+1):
        wordcorrect = False
        while not wordcorrect:
            pinput = input("Input letter for player %d: " %player)
            if (len(pinput) is 1):
                curword += pinput
                wordcorrect = True
            elif pinput == "challenge":
                break
            else: print("That is not a letter. Try Again")
        if pinput == "challenge":
            if not checkDict(curword):
                print("Player %d Challenged player %d for his word in mind" %(player, prevplayer))
                wordguess = input("Player %d what is your word you had in mind?: " %prevplayer)
                if checkDict(wordguess):
                    if(curword in wordguess):
                        print(wordguess + " is a valid word!")
                        loser = player
                        break
                    else:
                        print(wordguess + " is a word but couldn't be what you were thinking!")
                        loser = prevplayer
                        break
                else:
                    print(wordguess + " is not a word or is less then 2 characters!")
                    loser = prevplayer
                    break;
            else:
                print("Player %d Challenged because there is a word" % player)
                loser = prevplayer
                break
        print("Word is " + curword)
        prevplayer = player

    if loser != None:
        break


loserstr = "-----------------\nPlayer %d Lost!\n------------------\n" % loser
for i in loserstr:
    print(i, end='')
    time.sleep(.05)

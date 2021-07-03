import random
def hangman():
    word =random.choice(["pugger","superman","tiger","lion","pokemon","gamer","ice-breaker"])
    #print(word)
    validletters = "abcdefghijklmnopqrstuvwxyz"
    turn = 10
    guessmade = ""

    while len(word) > 0:
        main  = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main +=letter
            else:
                main += "_" +" "  
        if  main == word:
            print(main)
            print("you win")
            break
        print("Guess word ", main)
        guess = input()         

        if  guess in validletters:
            guessmade += guess
        else:
            print("invalid character")  
        if guess not in word:
            turn = turn -1
            if turn == 9:
                print("9 turns left")
                print("-------------")
            if turn == 8:
                print("8 turns left")
                print("-------------")
                print("      0      ")
            if turn == 7:
                print("7 turns left")
                print("-------------")
                print("      0      ")
                print("      |      ")    
            if turn == 6:
                print("6 turns left")
                print("-------------")
                print("      0      ")
                print("      |      ")    
                print("     /       ")                            
            if turn == 5:
                print("5 turns left")
                print("-------------")
                print("      0      ")
                print("      |      ")    
                print("     / \     ")
            if turn == 4:
                print("5 turns left")
                print("-------------")
                print("    \ 0      ")
                print("      |      ")    
                print("     / \     ")
            if turn == 3:
                print("3 turns left")
                print("-------------")
                print("    \ 0 /    ")
                print("      |      ")    
                print("     / \     ")
            if turn == 2:
                print("2 turns left")
                print("-------------")
                print("    \ 0 /|   ")
                print("      |      ")    
                print("     / \     ")
            if turn == 1:
                print("1 turns left")
                print("-------------")
                print("    \ 0_|/   ")
                print("      |      ")    
                print("     / \     ")  
            if turn == 0:
                print("game over he died beacuse of u")
                print("-------------")
                print("      0_|    ")
                print("     /|\     ")    
                print("     / \     ")  


name  = input("Enter your name : ")
print("Welcome ",name)
print("-------------------------")
print("Try to guess the word in less than 10 try")
print()
hangman()
def hangman(word):
    # keep track of how many incorrect answers
    wrong = 0
    # strings used to draw hangman
    stages = ["",
              "--------       ",
              "|       |      ",
              "|       |      ",
              "|       O      ",
              "|      /|\     ",
              "|      / \     ",
              "|              ",
              "|              "
              ]
    # list containing each character in the variable word that keeps track of what letters are left
    rletters = list(word)
    # list that keeps track of hints you display
    board = ["__"] * len(word)
    # start at false to keep track if you have won the game
    win = False
    print("Welcome to Hangman")
    # continue as long as wrong is less than stages - 1 
    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        # if guess is in rletters (rletters keep track of letters that hasn been guessed)
        if char in rletters:
            cind = rletters \
                   .index(char)
            # if correct updated board which will be used later in the game to display letters remaining
            board[cind] = char
            # replace dollar sign for guessed letter // more than one character will not work
            rletters[cind] = '$'
        else:
            wrong += 1
        # print scoreboard and hangman
        print((" ".join(board)))
        e = wrong +1
        # create entire hangman, add new line to each string in the stages // start at 0 and slice stages list
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    # prints full hangman     
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        # prints the word
        print("You lose! It was {}."
              .format(word))
hangman("cat")

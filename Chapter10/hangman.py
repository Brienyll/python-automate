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
    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong +1
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lose! It was {}."
              .format(word))
hangman("cat")

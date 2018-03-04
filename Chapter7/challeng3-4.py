tvshows =  ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for i,show in enumerate(tvshows):
    print(i,show)
    


nums = [5, 15, 29]

while True:
    answer = input("Guess a number or type q to quit?")
    if answer == 'q':
        break
    try:
        answer = int(answer)
    except ValueErrror:
        print("please type a number or q to quit.")
    if answer in nums:
        print("You guessed the correct number!")
    else:
        print("You guessed the wrong number!")

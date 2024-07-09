import random

words = ["words", "fruit", "gold"]
for a in range(len(words)):

    chosen_word = random.choice(words)
    print(chosen_word)
    display = []
    lenght_of_word = len(chosen_word)
    lives = 6
    blanks = "_"*lenght_of_word
    for j in blanks:
        display.append(j)
    # print(display)
    end_of_game = False
    while end_of_game == False:
        guess = input("Enter a letter: ").lower()
        if guess in display:
            print("You have guessed this letter before ")
        for i in range(lenght_of_word):
            if guess == chosen_word[i]:
                display[i] = guess
            
                
        if guess not in chosen_word:
            
            lives -= 1
            print(lives)
            if lives == 0:
                end_of_game = True
                print("You Lose")
        print("".join(display))
        if "_" not in display:
            end_of_game = True
            print("You Win")
            words.remove(chosen_word)

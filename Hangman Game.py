#download the hangman_art.py and hangman_words.py file to run this Game
import random
import hangman_art
import hangman_words

wordf = random.choice(hangman_words.word_list)
word_length = len(wordf)
print(hangman_art.logo)

display = []
end = False
chance = 6

print(f"It is a {word_length} letter word.")

for _ in range(word_length):
    display += '_'
    
while end is False:
    guess = input("Guess a letter: ")
          
    for j in range(word_length):
        letter = wordf[j]
        if letter == guess:
            display[j] = letter

    if guess not in wordf:
        chance -= 1
        print(f"'{guess}' is not in the word. {chance} chances left.")
        if chance == 0:
            end = True

            print("You lose.")
            print(f"The Word is '{wordf}'.")
            
    print(f"{' '.join(display)}")

    if "_" not in display:
        end is True
        print("You win.")
        exit()

    print(hangman_art.stages[chance])

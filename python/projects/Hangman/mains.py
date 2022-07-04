import random

words = ["nobita", "doraemon", "sizuka"]

quiz_word = random.choice(words)
word_length = len(quiz_word)

print(f"Welcome to the Hangman game::")
display = []

for _ in range(word_length):
    display += "_"
life = 6
end_of_game= False
while not end_of_game:
    guess = input("Guess the alphabet ???").lower()

    if guess in display:
        print(f"you already guess the letter")

    for position in range(word_length):
        if guess == quiz_word[position]:
            display[position] = guess

    if guess not in quiz_word:
        print(f"You guess wrong,{life} life remain!!!")
        life -= 1


        if '_' not in display:
            end_of_game = True
            print('you win.')
    if life == 0:
        print('You Loss!!!')
        break
    print(display)

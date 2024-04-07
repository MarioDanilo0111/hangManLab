import random

correct_guesses_emoji = ' '
emoji_to_add = '👍'

words = [
    "mystery", "python", "galaxy", "dinosaur", "puzzle",
    "astronaut", "champion", "keyboard", "jazz", "zigzag",
    "buzzard", "jockey", "quiz", "whiskey", "zephyr",
    "vortex", "jackpot", "quartz", "hyphen", "oxygen",
    "kayak", "zebra", "labyrinth", "yacht", "vampire",
    "wizard", "gypsy", "jungle", "hazard", "quiver"
]
# for choosing a random word
secret_word = random.choice(words)
# creating the Chain
chain = '-' * len(secret_word)
print('Welcome to Hangman!')
attempts = 0
printword = secret_word.upper()

while True:
    print(chain)

    guessLetter = input('Guess a letter: ')
    if guessLetter in secret_word:
        correct_guesses_found = False
        for i in range(len(secret_word)):
            if secret_word[i] == guessLetter and chain[i] == '-':
                chain = chain[:i] + guessLetter + chain[i + 1:] 
                correct_guesses_found = True
        if correct_guesses_found:
              correct_guesses_emoji += emoji_to_add
    else:
        print('Wrong guess, try again!')
        attempts += 1

    if correct_guesses_emoji.strip():
        print('Correct guesses: ' + correct_guesses_emoji)
        
   
    if attempts == 0:
            print('|')
            print('| ')
            print('| ')
            print('| ')
            print('| ')
            print('⎺⎺⎺⎺⎺⎺')
    elif attempts == 1:            
            print('|⎺⎺0')
            print('| ')
            print('| ')
            print('| ')
            print('| ')
            print('⎺⎺⎺⎺⎺⎺')
    elif attempts == 2:
            print('|⎺⎺0')
            print('| /')
            print('| ')
            print('|  ')
            print('| ')
            print('|  ')
            print('⎺⎺⎺⎺⎺⎺')
    elif attempts == 3:
            print('|⎺⎺0')
            print('| /|')
            print('| ')
            print('|  ')
            print('| ')
            print('|  ')
            print('⎺⎺⎺⎺⎺⎺')
    elif attempts == 4:
            print('|⎺⎺0')
            print('| /|\\')            
            print('|  ')
            print('| ')
            print('|  ')
            print('⎺⎺⎺⎺⎺⎺')
    elif attempts == 5:
            print('Last try 💀!!!')
            print('|⎺⎺0')
            print('| /|\\')
            print('|  |')
            print('| / \\')
            print('|⏠  ') 
            print('⎺⎺⎺⎺⎺⎺')

    if attempts == 6:
            print('|⎺⎺0')
            print('| /|\\')
            print('|  |')
            print('| / \\')
            print('|⏠   ⏠')
            print('⎺⎺⎺⎺⎺⎺')
            print(f'GAME OVER 😾! The secret word was, {printword}')
            break
        
    if chain == secret_word: 
        print(f'YOU WIN! The secret word was,{printword}')
        break
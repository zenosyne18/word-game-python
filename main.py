import random


def winner_congratulations():
    print('+---------------------------------------------------+')
    print('|                   *                ^              |')
    print('|      *        >>   YOU WIN !   <<           *     |')
    print('|                   .                .              |')
    print('|        .        Congratulations!                  |')
    print('|          You guessed the word correctly.          |')
    print('|                    *              .               |')
    print('|  *                       .              *         |')
    print('+---------------------------------------------------+')


def game_over(chosen_word):
    print('      GAME OVER')
    print('')
    print('      ( ͡° ͜ʖ ͡°)')
    print('')
    print('You have run out of lives')
    print('The correct answer was: ', chosen_word)


def display_word(temp_answer, display_life):
    print('')
    print('================================================')
    print('You have ' + str(display_life) + ' life')
    print('')
    print('               ' + ' '.join(temp_answer))
    print('')
    print('================================================')


def start_game():
    print('+-------------------------------------------+')
    print('|       ====== GUESS THE WORD ======        |')
    print('|     Welcome to the word guessing game     |')
    print('|              .                .           |')
    print('|      You need to find the right word!     |')
    print('|                *         .                |')
    print('|                  START                    |')
    print('+-------------------------------------------+')
    print('')


# Dictionary
listEnglishWordEasy = ['bird', 'fish', 'tree', 'book', 'ball',
                       'milk', 'hand', 'door', 'time', 'desk']

listEnglishWordMedium = ['world', 'steam', 'habit', 'apple', 'chair',
                         'break', 'table', 'plant', 'queen', 'smile']

listEnglishWordHard = ['banana', 'orange', 'potato', 'rocket', 'turtle'
                       'doctor', 'school', 'flower', 'window', 'hammer']

listIndonesianWordEasy = ['baju', 'kaki', 'tali', 'roda', 'buku',
                          'daun', 'kera', 'basi', 'lari', 'mata']

listIndonesianWordMedium = ['kursi', 'hewan', 'rumah', 'dapur', 'bulan',
                            'bunga', 'mobil', 'kecil', 'surat', 'kamar']

listIndonesianWordHard = ['rambut', 'kucing', 'burung', 'belati', 'kereta',
                          'pintar', 'kapten', 'melati', 'kerbau', 'gelang']

# Start game
start_game()

# Setting
print('Choose a language')
print('1. English')
print('2. Bahasa')
language = str(input('Your answer : '))

print('')
print('Choose a difficulty level')
print('1. Easy (4 word)')
print('2. Medium (5 word)')
print('3. Hard (6 word)')
difficulty = str(input('Your answer : '))

if language == '1':
    chosenLanguage = 'English'
    word_lists = [listEnglishWordEasy, listEnglishWordMedium, listEnglishWordHard]
else:
    chosenLanguage = 'Indonesian'
    word_lists = [listIndonesianWordEasy, listIndonesianWordMedium, listIndonesianWordHard]

if difficulty in ['1', '2', '3']:
    chosenDifficulty = ['Easy', 'Medium', 'Hard'][int(difficulty) - 1]
    chosenWord = random.choice(word_lists[int(difficulty) - 1])
else:
    chosenDifficulty = 'Medium'
    chosenWord = random.choice(word_lists[1])

chosenWord = chosenWord.upper()

# Cheating
print('the chosen word is : ' + chosenWord + '\n')

# Game Start
print('  Game starting!, you choose ' + chosenDifficulty + ' in ' + chosenLanguage)
answer = False
life = 5
tempAnswer = ['_'] * len(chosenWord)

while not answer:
    display_word(tempAnswer, life)
    guess = input('Guess the word : ').upper()
    print('')

    if len(guess) != len(chosenWord):
        print('            Word must be ' + str(len(chosenWord)) + ' letters!')
    else:
        if guess == chosenWord:
            winner_congratulations()
            answer = True
        else:
            for i in range(len(chosenWord)):
                if guess[i] == chosenWord[i]:
                    tempAnswer[i] = guess[i]

            life -= 1
            print('Wrong guess! Try again.\n')

    if life <= 0:
        game_over(chosenWord)
        answer = True

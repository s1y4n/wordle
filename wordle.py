import random
from wordlist import words

def right_both():
    return "🟩"

def right_letter():
    return "🟨"

def wrong():
    return "⬛"

word = random.choice(words)
count = 0
result = []
End = False
while count < 6 and not End:
    corret = False
    while not corret:
        global guess
        guess = input("\nEnter a 5 letter word: ")
        guess = guess.lower()
        if len(guess) != 5 or guess not in words:
            print("Not in wordlist")
        else:
            corret = True
    for i in range(5):
        if guess[i] == word[i]:
            result.append(right_both())
        elif guess[i] in word:
            result.append(right_letter())
        else:
            result.append(wrong())
    result.append("\n") 
    for r in result:                                                                                                                                                                                          
        print(r, end=" ")
    if guess == word:
        print("\nWin")
        End = True
    count += 1
else:
    if not End:
        print("\nNo more guesses")
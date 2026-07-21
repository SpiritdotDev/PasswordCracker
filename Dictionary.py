import time

wordlist_path = "rockyou.txt"

def Dictionary(target):

    found = False
    counter = 0
    startTime = time.time()
    while found == False:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for word in file:
                counter += 1
                word = word.strip()
                if word == target:
                    end = time.time()
                    timetaken = end - startTime
                    attemptsPerSecond = counter / timetaken
                    print(f"Your password was: {word}. It was found in {timetaken} seconds, {counter} attempts, at a rate of {attemptsPerSecond} attempts per second.")
                    found = True
                    return

    
import itertools
import time
MAXLENGTH = 25

def BruteForce(password):

    Alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+{}:"|<>?-=[]\;,./'
    startTime = time.time()
    CharLength = 1
    found = False
    counter = 1

    while CharLength <= MAXLENGTH and found == False:
        attempts = itertools.product(Alphabet,repeat=CharLength)
        for attempt in attempts:
            attempt = str(attempt)
            attempt = attempt.replace(" ","")
            attempt = attempt.replace("(","")
            attempt = attempt.replace(")","")
            attempt = attempt.replace(",","")
            attempt = attempt.replace("'","")
            counter += 1
            if attempt == password:
                end = time.time()
                timetaken = end - startTime
                attemptsPerSecond = counter / timetaken
                print(f"Your password was: {attempt}. It was found in {timetaken} seconds, {counter} attempts, at a rate of {attemptsPerSecond} attempts per second.")
                found = True
                return

        CharLength += 1
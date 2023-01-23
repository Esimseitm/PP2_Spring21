import random
dd = 0
def guess_the_number(dd):
    number = random.randint(1, 20)
    print("Hello! What is your name?")

    name = input()
    print()
    print("Well , " + name + ", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    nm1 = int(input())
    print()
    count = 1
    while nm1 != number:
        if nm1 < number:
            print("Your guess is too low.")
            print("Take a guess.")
        if nm1 > number:
            print("Your guess is too high.")
            print("Take a guess.")
        nm1 = int(input())
        print()
        count += 1
    print(f'Good job, {name}! You guessed my number in {count} guesses!')

guess_the_number(dd)

    
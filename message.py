import random

with open('quotes.txt', 'r') as f:
    quotes = f.readlines()


def print_message():
    random_number = random.randrange(len(quotes))

    if not quotes[random_number]:
        print("I am speechless")
    else:
        return quotes[random_number]

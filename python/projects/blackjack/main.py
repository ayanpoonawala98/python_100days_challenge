import random
from card import Card


def rand_card():
    pick = random.choice(Card)
    return pick


user_card = []
computer_card = []

for _ in range(2):
    user_card.append(rand_card())
    computer_card.append(rand_card())
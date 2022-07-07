from turtle import clear

import art, random


from gameData import data

def question():
    return random.choice(data)

def display(first_question,second_question):
    print(art.logo)

    print(f'Compare A: {first_question.get("name")}, a {first_question.get("description")}, from {first_question.get("country")}')
    print(art.vs)
    print(f'Against B: {second_question.get("name")}, a {second_question.get("description")}, from {second_question.get("country")}')


def compare(first_question,second_question,ans):
    if(first_question.get('follower_count') > second_question.get("follower_count")):
        return ans == 'A'
    if(first_question.get('follower_count') < second_question.get("follower_count")):
        return  ans == 'B'

    return False;

def game():
    count=0
    second_question = question()

    game_on = True

    while(game_on):
        first_question = second_question
        second_question = question()
        display(first_question,second_question)
        ans = input(f'Who has more followers? Type \'A\' or \'B\':')

        result = compare(first_question,second_question,ans)

        if(result):
            count+=1
            print(f'Right answer,your score is {count}')
        else:
            game_on = False
            print(f'Sorry,that\'s wrong answer. Final score is {count}')

        clear()

game()
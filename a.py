def get_choices():
    player_choice = input("Enter a season (summer or winter): ")
    computer_choice = 'bad'
    season_to_fruit = {'summer': 'mango', 'winter': 'orange'}

    chosen_fruit = season_to_fruit.get(player_choice.lower())

    choices = {"player": player_choice, "computer": computer_choice}

    return  chosen_fruit


fruit = get_choices()
# print(f"Choices: {choices}")
print(f"Fruit: {fruit}")


def MyName (name , age):
    return [name , age]


print(MyName("ali" , 23))



def mymy(player, computer):

    print(f"this is computer {computer} , this is player {player}")
    if player == computer:
        return "this is tie"
    elif player == 'rock' and computer == 'paper':
        return "computer won"
    elif player == 'paper' and computer == 'rock':
        return "player won"
    elif player == 'scissors' and computer == 'rock':
        return "computer won"
    elif player == 'rock' and computer == 'scissors':
        return "player won"
    elif player == 'paper' and computer == 'scissors':
        return "computer won"
    elif player == 'scissors' and computer == 'paper':
        return "player won"

print(mymy('rock', "paper"))
print(mymy('rock', "scissors"))
print(mymy('rock', "rock"))
print(mymy('paper', 'scissors'))
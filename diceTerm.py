import random 


from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.history import InMemoryHistory



def roll_dice(command, params):
    if len(params) == 1:
        print(random.randint(1, int(params[0])))
    else:
        result = []
        for i in range(int(params[0])):
            result.append(random.randint(1,int(params[1])))

        print(f"result of {command} : {result}")
        print(f"Total : {sum(result)}")


quotes = [
        "Courage is found in unlikely places. - The Return of The King",
        "There is one rule, above all others, for being a man. Whatever comes, face it on your feet. - The Great Hunt (The Wheel of Time)", 
        "The most important step a man can take. It’s not the first one, is it? It’s the next one. Always the next step. - Oathbringer (The Stormlight Archive)",
        ]



style = Style.from_dict({
    'rprompt': 'bg:#ff0066 #ffffff'
})

history = InMemoryHistory()

run = True

while run:
    user_input = prompt('> ', style=style, history=history)

    if user_input == "exit":
        run = False
        break

    processesd = user_input.split("d")

    if processesd[0] == "":
        processesd.remove("")

    roll_dice(user_input, processesd)


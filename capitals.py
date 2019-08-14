# an array of state dictionaries
import random
from random import shuffle

states = [
    {
        "name": "Alabama",
        "capital": "Montgomery"
    }, {
        "name": "Alaska",
        "capital": "Juneau"
    }, {
        "name": "Arizona",
        "capital": "Phoenix"
    }, {
        "name": "Arkansas",
        "capital": "Little Rock"
    }, {
        "name": "California",
        "capital": "Sacramento"
    }, {
        "name": "Colorado",
        "capital": "Denver"
    }, {
        "name": "Connecticut",
        "capital": "Hartford"
    }, {
        "name": "Delaware",
        "capital": "Dover"
    }, {
        "name": "Florida",
        "capital": "Tallahassee"
    }, {
        "name": "Georgia",
        "capital": "Atlanta"
    }, {
        "name": "Hawaii",
        "capital": "Honolulu"
    }, {
        "name": "Idaho",
        "capital": "Boise"
    }, {
        "name": "Illinois",
        "capital": "Springfield"
    }, {
        "name": "Indiana",
        "capital": "Indianapolis"
    }, {
        "name": "Iowa",
        "capital": "Des Moines"
    }, {
        "name": "Kansas",
        "capital": "Topeka"
    }, {
        "name": "Kentucky",
        "capital": "Frankfort"
    }, {
        "name": "Louisiana",
        "capital": "Baton Rouge"
    }, {
        "name": "Maine",
        "capital": "Augusta"
    }, {
        "name": "Maryland",
        "capital": "Annapolis"
    }, {
        "name": "Massachusetts",
        "capital": "Boston"
    }, {
        "name": "Michigan",
        "capital": "Lansing"
    }, {
        "name": "Minnesota",
        "capital": "St. Paul"
    }, {
        "name": "Mississippi",
        "capital": "Jackson"
    }, {
        "name": "Missouri",
        "capital": "Jefferson City"
    }, {
        "name": "Montana",
        "capital": "Helena"
    }, {
        "name": "Nebraska",
        "capital": "Lincoln"
    }, {
        "name": "Nevada",
        "capital": "Carson City"
    }, {
        "name": "New Hampshire",
        "capital": "Concord"
    }, {
        "name": "New Jersey",
        "capital": "Trenton"
    }, {
        "name": "New Mexico",
        "capital": "Santa Fe"
    }, {
        "name": "New York",
        "capital": "Albany"
    }, {
        "name": "North Carolina",
        "capital": "Raleigh"
    }, {
        "name": "North Dakota",
        "capital": "Bismarck"
    }, {
        "name": "Ohio",
        "capital": "Columbus"
    }, {
        "name": "Oklahoma",
        "capital": "Oklahoma City"
    }, {
        "name": "Oregon",
        "capital": "Salem"
    }, {
        "name": "Pennsylvania",
        "capital": "Harrisburg"
    }, {
        "name": "Rhode Island",
        "capital": "Providence"
    }, {
        "name": "South Carolina",
        "capital": "Columbia"
    }, {
        "name": "South Dakota",
        "capital": "Pierre"
    }, {
        "name": "Tennessee",
        "capital": "Nashville"
    }, {
        "name": "Texas",
        "capital": "Austin"
    }, {
        "name": "Utah",
        "capital": "Salt Lake City"
    }, {
        "name": "Vermont",
        "capital": "Montpelier"
    }, {
        "name": "Virginia",
        "capital": "Richmond"
    }, {
        "name": "Washington",
        "capital": "Olympia"
    }, {
        "name": "West Virginia",
        "capital": "Charleston"
    }, {
        "name": "Wisconsin",
        "capital": "Madison"
    }, {
        "name": "Wyoming",
        "capital": "Cheyenne"
    }]

test = [
    {
        "name": "Alabama",
        "capital": "Montgomery"
    }, {
        "name": "Alaska",
        "capital": "Juneau"
    }, {
        "name": "Arizona",
        "capital": "Phoenix"
    }
]

score = {
    'correct': 0,
    'wrong': 0
}


# print(test[3]) <- returns 2nd object
# print(test[0]['capital'][0]) <- returns first letter of capital


def states_game():
    random.shuffle(test)

    def check_answer():
        if response_lower_case == answer_lower_case:
            score['correct'] += 1
            print('correct! nice job!')
        else:
            score['wrong'] += 1
            print('NOPE')

    for i in test:
        hint = input('type "hint" to get a hint ')
        hint_response = (hint).lower()
        if hint_response == 'hint':
            print(i['capital'][0])

        question = input('what is the capital of ' +
                         i['name'] + ' ')

        response_lower_case = (question).lower()
        answer_lower_case = (i['capital']).lower()

        check_answer()
    print("{} {}".format(
        "Here is how many you got correct! : ", score['correct']))


start_game = input('ready to play? yes/no ')

if start_game == 'yes':
    states_game()
elif start_game == 'no':
    print('too bad!')
    states_game()

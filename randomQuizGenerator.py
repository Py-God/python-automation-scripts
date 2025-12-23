#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quiz files
for quizNum in range(35):
    # create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')      # %s would be filled with whatever is in (quizNum + 1) using the % operator
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')     # once the program gets here it executes this and does'nt overwrite it on another write call
    quizFile.write((' ' * 20) + 'State Capitals Quiz (form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    # cuz you have called 'w' and haven't closed the file, you can write in it.
    # i guess to make the code a lot easier, it is written in different lines. i guess cuz you can actually

    # shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)              # the order generated is the order the questions will come out
    # everything here written in the forloop to generate for all the 35 files

    # Loop through all 50 states, making a question for each. forloop to generate questions
    for questionNum in range(50):

        # get right and wrong answers
        correctAnswer = capitals[states[questionNum]]   # fetching the actual capital answer to the particular question
        wrongAnswers = list(capitals.values())          # all the capitals
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # deleting the actual answer from the list to prepare generating the random 3 wrong answers for a question
        wrongAnswers = random.sample(wrongAnswers, 3)   # generating 3 random wrong answers using this piece of code - random.sample()
        answerOptions = wrongAnswers + [correctAnswer]  # creating a list of the answer options
        random.shuffle(answerOptions)                   # shuffling it for so the answer does'nt always come at the end like the code above says

        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))

        # forloop to display answers
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')
            # Write the answer key to a file.
            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
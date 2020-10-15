# Goals for project
# 1. Creates 35 different quizzes
# 2. Creates 50 multiple-choice questions for each quiz, in random order
# 3. Provide the correct answer and three random wrong answers for each question, in random order
# 4. Writes the quizzes to 35 text files
# 5. Writes the answer keys to 35 text files

import random

quizInformation = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# Declare Two list from the quiz dictionary
stateList = list(quizInformation.keys())
capitalList = list(quizInformation.values())

# Dictionary for checking letter value of correct answer
test_keys = {0:'A',1:'B',2:'C',3:'D'}

# First loop for number of students
for j in range(1,36):
    #List of states will be randomized as requested
    random.shuffle(stateList)
    #Header information for students
    with open('capitalsquiz'+str(j)+'.txt','a') as fh:
        fh.write("Name: \n"+"\n"+"Date:\n"+"\n"+"Period: \n"+"\n")
        fh.write("      State Capitals Quiz (Form "+str(j)+")      \n"+"\n")
    #Second loop for number of quiz questions
    for i in range(len(stateList)):
      correctAnswer = quizInformation[stateList[i]]
      # Create a list for three incorrect capitals
      list_of_capitals = list(capitalList)
      # Randomly select three capitals after the correct answer has been removed
      list_of_capitals.remove(correctAnswer)
      list_of_capitals = random.sample(list_of_capitals, 3)
      # Return correct answer and shuffle
      list_of_capitals.append(correctAnswer)
      random.shuffle(list_of_capitals)
      #locate the correct answers letter value for answer key file
      answerIndex = list_of_capitals.index(correctAnswer)
      letter = test_keys[answerIndex]
      # After all information has been properly sorted write to test files
      with open('capitalsquiz'+str(j)+'.txt','a') as fh:
        fh.write(str(i + 1)+"."+" What is the capital of {}?\n".format(stateList[i])+"\n")
        for s in range(len(list_of_capitals)):
           fh.write(" "+test_keys[s]+". "+list_of_capitals[s]+' \n'+"\n")
      # Write the answers to the answer file
      with open('capitalsquiz_answers'+str(j)+'.txt','a') as fh:
        fh.write(str(i + 1)+". "+letter+"\n")
        fh.write(' ')
       
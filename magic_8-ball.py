import random

name = 'Troy'
question = 'Am I awesome?'
answer = ''
random_number = random.randint(1, 10)
# print(random_number)

# Assigning the answer based on random_number
if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
elif random_number == 10:
  answer = "I'd rather not say"
else:
  answer = 'Error'

# Printing the result
if question == '':
  if name == '':
    print('I need a question!')
  else:
    print('I need a question, ' + name + '!')
else:
  if name == '':
    print('Question:', question)
  else:
    print(name, 'asks:', question)
  print("Magic 8-Ball's answer:", answer)

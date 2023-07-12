print("Welcome to my Quiz :]")

playing = input('Would you like to have some fun? ')

if playing.lower() != "yes":
    quit()

print("let's get started!")
score = 0

answer = input('What is the capitol of Connecticut? ')
if answer.lower() == 'hartford':
    score += 1 
    print('Correct')
else: 
    print('better luck next time')

answer = input('What brand does Travis Scott have a sneaker with? ')
if answer.lower() == 'nike':
    score += 1 
    print('Correct')
else: 
    print('better luck next time')

answer = input('What is the first pokemon in the pokedex? ')
if answer.lower() == 'charmander':
    score += 1 
    print('Correct')
else: 
    print('better luck next time')

answer = input("Which consle has the spiderman exclusive game? ")
if answer.lower() =='playstation' :
    score += 1 
    print('Correct')
else: 
    print('better luck next time')

answer = input('Who is the current president of the USA? ')
if answer.lower() == 'joe biden':
    score += 1 
    print('Correct')
else: 
    print('better luck next time')

print(("You scored " + str(score) + ' out of 5')




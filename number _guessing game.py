import random
print( 'welcome to number guessing game')
name = input(' enter your name:')

print(' Choose your difficulty level:' )
print('1.Easy mode')
print('2. Moderate mode')
print('3. Difficult mode')
choice = input('enter your choice (1,2 or 3):')

if choice == '1':
    max_range = 10
    print('You selected easy mode , guess a number between 1 to 10')
elif choice =='2':
    max_range = 50
    print('You selected moderate mode, guess a number between 1 to 50')
else:
    max_range = 100
    print('You selected diffcult mode, guess a  number between 1 to 100')

n = random.randint(1, max_range)
attempts = 0
while True:
    guess = int(input(' Enter your guess number:'))
    attempts +=1

    if guess > n :
        print('guess is too high !! try again!!')
    elif guess < n:
        print(' Too low !!, Try again!!')
    else:
        print('yeahh you guessed it right! in',attempts,'attempts')
        print(name, 'wins the game!!')

        
        break

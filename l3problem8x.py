# Prints the welcome message
print ('Please think of a number between 0 and 100!')

# low/mininum
low = 0
# high/maximum
high = 100
# the guess
guess = (high+low)/2

while True:
    print ('Is your secret number ' + str(guess) + '?')
    # It receives the string with the answer
    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    # if h -> high
    if ans == 'h':
        high = guess
    # elif l -> low
    elif ans == 'l':
        low = guess
    # elif c -> correct
    elif ans == 'c':
        print ('Game over. ' + 'Your secret number was: ' + str(guess))
        break
    # error message
    else:
        print('Sorry I did not understand your input.')
    guess = (high+low)/2
    # some kind of system log for low and high variable on each stage
    print("low: " + str(low))
    print("high: " + str(high))

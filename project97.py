print("Number Guessing Game")
print("guess a number between 1-9")

number = int(input("enter your guess: "))
if(number<2):
    print("your guess was too low")
elif(number>2):
    print("your guess was too high")
else:
    print("CONGRATULATIONS YOU WON!!!")
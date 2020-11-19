import random

number = random.randint(1, 20)
counter = 0

for i in range( 6 ):
    
    your_number = int(input("Make a guess : ") )
    counter = counter + 1
    
    if (your_number == number):
        print("Congratulations!")
        print("You took " + str(counter) + " times")
        break;
    else:
        if your_number > number:
            print("Your number is higher")
        else:
            print("Your number is lower")
#Guessing the number game
import random
class NumberGuess():
    user_number=''
    def numberGuess(self):
        global user_number, user_count
        rand_number = random.randint(1,5)
        user_number = int(input("Enter a guess number between 1-10"))
        if user_number>10:
            print("Please enter number bewteen 1-10")
        user_count=3
        if rand_number==user_number:
            print("Congrats, you choose a correct number")
            exit()
        else:
            user_count=user_count-1
            self.compares(rand_number, user_count)

    def compares(self,rand_number, user_count):
        if rand_number>5:
            print("clue 1 - Number is greater than 5")
        elif rand_number<5:
                print("clue 1 - Number is lesser than 5")
        else:
            print("clue 1 - Number is multiple of 5")
        user_number = int(input("Enter a number"))
        if rand_number == user_number:
            print("Congrats, you choose a correct number")
            exit()
        else:
            user_count = self.user_count_minus(user_count, rand_number)
        print("clue 2 - Number mod 5 equals to {}".format(rand_number%5))
        user_number = int(input("Enter a number"))
        if rand_number == user_number:
            print("Congrats, you choose a correct number")
            exit()
        else:
            user_count = self.user_count_minus(user_count, rand_number)
        print("clue 3 - Number mod 10 equals to {}".format(rand_number%10))
        user_number = int(input("Enter a number"))
        if rand_number == user_number:
            print("Congrats, you choose a correct number")
            exit()
        else:
            self.user_count_minus(user_count, rand_number)

    def user_count_minus(self,user_count, rand_number):
        if user_count == 0:
            print("you exhausted all limits, number is {}".format(rand_number))
            exit()
        else:
            user_count = user_count - 1
        return user_count

num=NumberGuess()
num.numberGuess()
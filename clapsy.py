from tooling import *

print("---CLAPSY---")
print("********--********")
print("Welcome to my first game!")

name = input("What is your name? ")
try:
    age = int(input("What is your age? "))

except:
    raise ValueError("You forgot how to write a number or what! ")

print("SO, {} you born in {}".format(name, year_you_born(age)))
player = Player(name, age)

if player.is_older:
    player.start_game()

elif player.age >= 14:
    print("You can play! but sorry BUT WITH SUPERVISION :D")
else:
    print("Sorry! you still a kid! Yes sorry to hear that \:/ ")
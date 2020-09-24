import datetime


class Player():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_older = (age >= 18)
    def start_game(self):
        print("You are old enough!")
        want_to_play = input("want to Start ? ").upper()
        if want_to_play == "YES":
            print("YOHOOO, Start")
            print("YOHIII, End")
        elif want_to_play == "NO":
            print("Maybe another time!")
        else:
            print("We dont want to play with someone like you /_/")


def year_you_born(age):
    now = datetime.datetime.now().year
    return now - age

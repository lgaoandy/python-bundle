# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ____"

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Another Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}.\
    Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)

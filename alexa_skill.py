from flask import Flask
from flask_ask import Ask, statement, question, session
import numpy as np
import os


app = Flask(__name__)
ask = Ask(app, "/github_contribs")


def add_contributions(number):
    # do a thing here
    for ii in range(0,number):
        os.system("firstfile.sh")
    print("done")

@app.route("/")
def homepage():
    return "assuh, dude"

@ask.launch
def start_skill():
    welcome_message = "Do you love Github contributions, but hate to actually code?"
    return question(welcome_message)

@ask.intent("YesIntent")
def yes_intent():
    return question("how many contributions would you like?")

@ask.intent("NoIntent")
def no_intent():
    # do a thing here
    message = "You fucking snake... go crawl back into your hole and die"
    return statement(message)

@ask.intent("HowManyIntent", convert={"Amount": int}, default={"Amount" : "1"})
def how_many_intent(Amount):
    print(Amount)
    add_contributions(Amount)

    return statement("I just added {} contributions... you lazy piece of shit".format(Amount))

@ask.intent("SurpriseMeIntent")
def surprise_me_intent():
    number = int(np.random.rand()*10)
    add_contributions(number)

    return statement("I just added {} contributions... you lazy piece of shit".format(number))


if __name__ == "__main__":
    app.run(debug=True)
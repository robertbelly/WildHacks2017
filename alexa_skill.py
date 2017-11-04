from flask import Flask
from flask_ask import Ask, statement, question, session


app = Flask(__name__)
ask = Ask(app, "/github_contribs")

def get_headline():
    pass

@app.route("/")
def homepage():
    return "assuh, dude"


@ask.launch
def start_skill():
    welcome_message = "hello there, isn't Github neat?"
    return question(welcome_message)

@ask.intent("YesIntent")
def add_contributions():
    # do a thing here
    message = "I am about to add a ton of contributions"
    return statement(message)

@ask.intent("NoIntent")
def no_intent():
    # do a thing here
    message = "You fucking snake... don't talk to me or my son ever again."
    return statement(message)

if __name__ == "__main__":
    app.run(debug=True)
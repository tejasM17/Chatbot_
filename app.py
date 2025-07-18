from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


app = Flask(__name__)

# initialinsing chatbot

bot = ChatBot(
    "MyChatbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.BestMatch",
    ],
    database_uri="sqlite:///database.sqlite3",
)


# set up the trainers

list_traners = ListTrainer(bot)
corpus_trainer = ChatterBotCorpusTrainer(bot)

# training using English Corpus

corpus_trainer.train("chatterbot.corpus.english")


# define routes


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get", methods=["GET", "POST"])
def get_bot_response():
    userText = request.args.get("msg")  # Get message from user
    return str(bot.get_response(userText))  # Return bot response


if __name__ == "__main__":
    app.run(debug=True)

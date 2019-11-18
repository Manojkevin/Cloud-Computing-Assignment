# from flask import Flask, render_template, request
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer
#
#
# app = Flask(__name__)
#
# bot = ChatBot("Crazy Becksy")
# # bot.set_trainer(ListTrainer)
# # bot.set_trainer(ChatterBotCorpusTrainer)
# # bot.train("chatterbot.corpus.english")
#
# trainer = ChatterBotCorpusTrainer(ChatBot)
# trainer.train("chatterbot.corpus.english")
#
#
#
# @app.route("/")
# def home():
#     return render_template("home.html")
# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(bot.get_response(userText))
# if __name__ == "__main__":
#     app.run()

#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
app = Flask(__name__)
#create chatbot
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english
#define app routes
@app.route("/")
def index():
    return render_template("home.html")
@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))
if __name__ == "__main__":
    app.run()
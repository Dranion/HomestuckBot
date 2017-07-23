from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
logging.basicConfig(level=logging.INFO)
print("start")
bot = ChatBot("Homestuck Bot",
              input_adapter='chatterbot.input.TerminalAdapter',
              output_adapter='chatterbot.output.TerminalAdapter',
              logic_adapters=["chatterbot.logic.BestMatch",
                              "chatterbot.logic.multi_adapter.MultiLogicAdapter"],)
lines = open('chat.txt').read().splitlines()
bot.set_trainer(ListTrainer)
bot.train(
    "chatterbot.corpus.english"
)
bot.train(lines)
bot.train(lines)
bot.train(lines)
print("Welcome to the Homestuck Bot! <3")
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

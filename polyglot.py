from chatterbot import ChatBot, response_selection
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging


'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

bot = ChatBot('Polyglot Bot')

# Start by training our bot with the ChatterBot corpus data
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(

    "C:/Users/Hiroaki/Desktop/Github/polyglot-chatbot/venv/Lib/site-packages/chatterbot_corpus/data/portuguese"

)


def get_feedback():

    text = input('\nVocê: ')

    if 'sim' in text.lower():
        return False
    elif 'não' in text.lower():
        return True
    else:
        print('Por favor responda "Sim" ou "Não"')
        return get_feedback()


# The following loop will execute each time the user enters input
while True:
    try:
        print("\nPoliglota: Digite aqui sua pergunta que gostaria de fazer para mim")
        pergunta = input("Você: ")
        input_statement = bot.input.process_input_statement(pergunta)

        response_list = bot.storage.filter()
        response = response_selection.get_most_frequent_response(input_statement, response_list)
        bot.output.process_response(response)

        print('\nPoliglota: "{}" é uma resposta coerente para "{}"? \n'.format(response, input_statement))

        if get_feedback()==True:
            print("Poliglota: Por favor insira qual seria a resposta correta")
            response1 = input("Você: ")
            response1_statement = bot.input.process_input_statement(response1)
            bot.learn_response(response1_statement, input_statement)
            print("Poliglota: Resposta adicionada!")

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

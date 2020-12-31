# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot('Dimi',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'אני מצטער אבל אני לא מבין שאילה?',
            'maximum_similarity_threshold': 0.4
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'help_me!',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        },
        'chatterbot.logic.MathematicalEvaluation' ,
        {
            'import_path': 'test_adapter.MyLogicAdapter'
        }
  #          'chatterbot.logic.TimeLogicAdapter',



    ],
    database_uri='sqlite:///database.sqlite3'
)


# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(chatbot)

#trainer.train('chatterbot.corpus.english')
trainer.train('chatterbot.corpus.hebrew')
trainer.train('chatterbot.corpus.english')

# Now we can export the data to a file
#trainer.export_for_training('./my_export.json')


conversation = [
    "שלום",
    "ברוך הבאה לבוט",
    "מה נשמע?",
    "הכול טוב.",
    "טוב לדעת",
    "תודה",
    "האונג כולו שלי"
]


trainer = ListTrainer(chatbot)

trainer.train(conversation)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        try:
            insent=input()
            print(insent ,type(insent))
            bot_input = chatbot.get_response(insent)
            print(bot_input)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

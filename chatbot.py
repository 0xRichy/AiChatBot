from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot(
    'My ChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
)

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.emotion",
    "chatterbot.corpus.english.food",
    "chatterbot.corpus.english.gossip",
    "chatterbot.corpus.english.humor",
)

# Get a response
response = chatbot.get_response("Tell me a joke")
print(response)

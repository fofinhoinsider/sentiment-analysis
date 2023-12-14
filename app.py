from flask import Flask
from sentiment import analyze_entity_sentiment

from translate import translate_text

app = Flask(__name__)

COMMENTS = ["Satisfeito com o produto!", "Muito bom", "Excelente", "Dinheiro jogado fora", "Até o momento não senti diferença nenhuma"]

@app.route('/')
def hello_world():

    analysis = []

    for comment in COMMENTS:
        translated_text = translate_text("en", comment)['translatedText']
        print(translated_text)

        analysis += analyze_entity_sentiment(translated_text)

        # Send a request to the API
        

    print(analysis)
    return analysis
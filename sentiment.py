from google.cloud import language

from translate import translate_text

def map_function(item):
    entity, index = item
    return {
        "sentiment": {
            "magnitude": entity.sentiment.magnitude,
            "score": entity.sentiment.score
        } ,
        "salience": entity.salience,
    }

def analyze_entity_sentiment(text):
    # Create a client
    client = language.LanguageServiceClient()

    # Initialize request argument(s)
    document = language.Document(
        content=text,
        type_=language.Document.Type.PLAIN_TEXT,
    )

    request = language.AnalyzeEntitySentimentRequest(
        document=document,
    )

    response = client.analyze_entity_sentiment(request=request)

    entity_names = list(map(lambda entity : entity.name, response.entities))

    if len(entity_names) == 0:

        print("A")
        sentiment_request = language.AnalyzeSentimentRequest(
            document=document,
        )
        
        print("B")

        sentiment_response = client.analyze_sentiment(sentiment_request)
        document_sentiment = sentiment_response.document_sentiment
        return [{

            "name": "Product",
            "sentiment": {
                "magnitude": document_sentiment.magnitude,
                "score": document_sentiment.score
            },
            # "salience": 1,
        }]
        
    else:
        pt_translated_entities = translate_text("pt", entity_names)

        print('== == == translated: ')
        print(pt_translated_entities)

        return list(map(lambda entity_index_tuple: {
            "name": pt_translated_entities[entity_index_tuple[0]]['translatedText'],
            "sentiment": {
                "magnitude": entity_index_tuple[1].sentiment.magnitude,
                "score": entity_index_tuple[1].sentiment.score
            },
            # "salience": entity_index_tuple[1].salience,
        }, enumerate(response.entities)))
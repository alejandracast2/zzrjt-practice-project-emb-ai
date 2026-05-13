'''Module for sentiment analysis using Watson NLP API.'''
import json

import requests


def sentiment_analyzer(text_to_analyze):
    '''Analyze sentiment of a given text.'''

    # Define the URL for the sentiment analysis API
    url = (
        "https://sn-watson-sentiment-bert.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )

    # Create the payload with the text to be analyzed
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Set the headers with the required model ID
    header = {
        "grpc-metadata-mm-model-id":
        "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    # Make a POST request to the API
    response = requests.post(
        url,
        json=myobj,
        headers=header,
        timeout=10
    )

    # If the response status code is 200
    if response.status_code == 200:

        # Parse the response from the API
        formatted_response = json.loads(response.text)

        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    # If the response status code is 500
    elif response.status_code == 500:

        label = None
        score = None

    # For any other unexpected status codes
    else:

        label = None
        score = None

    # Return the label and score
    return {
        'label': label,
        'score': score
    }
    
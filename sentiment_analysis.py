import requests 
# Importar la biblioteca requests para manejar solicitudes HTTP

def sentiment_analyzer(text_to_analyse): 
    # Definir una función llamada sentiment_analyzer que toma una entrada de tipo cadena (text_to_analyse)
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' 
    # URL del servicio de análisis de sentimientos 
    myobj = { "raw_document": { "text": text_to_analyse } } 
    # Crear un diccionario con el texto a analizar 
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} 
    # Establecer las cabeceras requeridas para la solicitud API 
    response = requests.post(url, json = myobj, headers=header)
    return response.text

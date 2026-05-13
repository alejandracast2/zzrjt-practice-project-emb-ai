
''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request 
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Recuperar el texto a analizar de los argumentos de la solicitud 
    text_to_analyze = request.args.get('textToAnalyze')
    # Pasar el texto a la función sentiment_analyzer y almacenar la respuesta 
    response = sentiment_analyzer(text_to_analyze)
    # Extraer la etiqueta y el puntaje de la respuesta 
    label = response['label'] score = response['score']
    # Devolver una cadena formateada con la etiqueta de sentimiento y el puntaje 
    return "El texto proporcionado ha sido identificado como {} con un puntaje de {}.".format(label.split('_')[1], score)
    
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
    #TODO

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO

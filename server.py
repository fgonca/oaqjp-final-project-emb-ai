"""
This web application makes emotion analysis of input texts
and returns the emotions scores and the dominant emotion's name
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_dect():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions scores and 
        and the dominant emotion's name.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"

    anger = f"'anger': {response['anger']}, "
    disgust = f"'disgust': {response['disgust']}, "
    fear = f"'fear': {response['fear']}, "
    joy = f"'joy': {response['joy']}, "
    sadness = f"and 'sadness': {response['sadness']}. "
    dominant = f"'The dominant emotion is <b>{response['dominant_emotion']}</b>."
    statement = "For the given statement, the system response is "

    return statement + anger + disgust + fear + joy + sadness + dominant


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
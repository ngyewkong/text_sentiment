from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get('text')
        textbox = request.form.get('textbox')
        print(text)
        print(textbox)

        text_sentiment = TextBlob(text).sentiment
        textbox_sentiment = TextBlob(textbox).sentiment

        print(text_sentiment)
        print(textbox_sentiment)

        return (render_template("index.html", result1=text_sentiment, result2=textbox_sentiment))
    else:
        return (render_template("index.html", result1='No Text Submitted', result2='No Text Submitted'))


if __name__ == "__main__":
    app.run()

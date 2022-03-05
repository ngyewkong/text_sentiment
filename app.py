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

        print(text_sentiment.polarity)
        print(textbox_sentiment.polarity)
        print(text_sentiment.subjectivity)
        print(textbox_sentiment.subjectivity)

        titletext = ("The polarity of the title text is " + str(text_sentiment.polarity) +
                     " and the subjectivity is " + str(text_sentiment.subjectivity) + ". \n")
        maintext = ("The polarity of the body text is " + str(textbox_sentiment.polarity) +
                    " and the subjectivity is " + str(textbox_sentiment.subjectivity) + ". \n")

        return (render_template("index.html", result1=titletext, result2=maintext))
    else:
        return (render_template("index.html", result1='No Text Submitted', result2='No Text Submitted'))


if __name__ == "__main__":
    app.run()

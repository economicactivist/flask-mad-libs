from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)

app.config['SECRET_KEY'] = "secretkey"
debug = DebugToolbarExtension(app)

parts_of_speech = ["place", "noun", "verb", "adjective", "plural_noun"]


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', parts_of_speech=parts_of_speech)


@app.route('/story', methods=['GET', 'POST'])
def make_story():
    text = """Once upon a time, long-ago in a {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    s = Story(parts_of_speech, text)
    ans = request.form
    return render_template('story.html', story=s.generate(ans))

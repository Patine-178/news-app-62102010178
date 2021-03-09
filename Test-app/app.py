from flask import Flask, render_template
import feedparser

app = Flask(__name__)

COMING_SOON = "https://rss.itunes.apple.com/api/v1/us/apple-music/coming-soon/all/10/explicit.rss"

@app.route("/")
def coming_soon():
    feed = feedparser.parse(COMING_SOON)
    print(feed)
    return render_template("index.html", feed=feed)
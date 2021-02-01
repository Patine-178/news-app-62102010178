import feedparser
from flask import Flask

app = Flask(__name__)

ITUNE_FEED = "https://rss.itunes.apple.com/api/v1/us/apple-music/new-releases/all/10/explicit.rss"


@app.route("/")
def get_new_release():
    feed = feedparser.parse(ITUNE_FEED)
    first_item = feed['entries'][0]
    return """<html>
       <body>
           <h1>iTune New Release</h1>
           <b>{0}</b> <br/>
           <i>{1}</i> <br/>
           <a href="{2}">{2}</a> <br/>
       </body>
   </html>""".format(first_item.get("title"), first_item.
                     get("description"), first_item.get("link"))

app.env="development"
app.run(debug=True)
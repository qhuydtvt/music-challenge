from flask import *
from mlab import *
from mongoengine import *

app = Flask(__name__)

songs = [
    {
      "title": "Hello Hello",
      "artist": "FT Island",
      "genre": "Hàn Quốc, Pop / Ballad",
      "source": "http://api.mp3.zing.vn/api/mobile/source/song/LGJGTLGNVEDLVAGTLDJTDGLG"
    },
    {
      "title": "Faded",
      "artist": "Alan Walker",
      "genre": "Âu Mỹ, Electronic / Dance",
      "source": "http://api.mp3.zing.vn/api/mobile/source/song/LGJGTLGNQAQJNLVTLDJTDGLG"
    },
    {
      "title": "Heathens",
      "artist": "Twenty One Pilots",
      "genre": "Âu Mỹ, Pop, Nhạc Phim",
      "source": "http://api.mp3.zing.vn/api/mobile/source/song/LGJGTLGNQQVNLNJTLDJTDGLG"
    },
    {
      "title": "Clap Hands",
      "artist": "Tom Waits",
      "genre": "Âu Mỹ, Rock",
      "source": "http://api.mp3.zing.vn/api/mobile/source/song/LGJGTLGNVNXQEQJTLDJTDGLG"
    },
    {
      "title": "Everybody Knows",
      "artist": "Ride",
      "genre": "Âu Mỹ, Rock",
      "source": "http://api.mp3.zing.vn/api/mobile/source/song/LGJGTLGNAAQEEGDTLDJTDGLG"
    }
]


@app.route("/api/songs")
@app.route("/api/songs/")
def api_songs():
    return jsonify(songs)

if __name__ == '__main__':
    app.run()
